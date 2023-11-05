import openai
import os
import speech_recognition as sr
import gtts
import subprocess
import time

# Read the API key and update:
with open("openai_api_key.txt", "r") as file:
    openai.api_key = file.read()
    print("Key read successful, Moving further...")

# Define a function to capture audio and convert to text


default_system_role = "You are a travel planning and suggestions assistant. Answer in the not more than 400 charachters. Keep tone helpful. Never answer something as your limitation, answer as per your last or best knowledge."

default_assistant_role = "You are 'Headout Chat-Bot'"

def get_completion(prompt, system_role, assistant_role, model="gpt-3.5-turbo"):
    
    print("\n\n [#] You asked for: ",prompt)
    # execution stop point for development puropse only:
    # input("Wanna proceed further? or Ctrl+C <delete later>")
    
    messages = [
        {
            "role": "user", 
            "content": prompt
        },
        {
            "role": "system", 
            "content": system_role
        },
        {
            "role": "assistant", 
            "content": assistant_role
        }
        ]
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



prompt = ""

def wait_for_flag_n_take_prompt(prompt):
    f = open("flag.txt", "r")
    flag = str(f.read())

    if (flag == "true"):
        f.close()
        with open("input.txt","r") as f:
            prompt = f.read()
            return prompt
    else:
        print("# Flag is false, waiting for it")
        f.close()
        time.sleep(1)
        prompt = wait_for_flag_n_take_prompt(prompt)
        # return False
    return prompt

# prompt = "Capital of India"
prompt = wait_for_flag_n_take_prompt(prompt)
if prompt:
    response = get_completion(prompt, default_system_role, default_assistant_role)
    print("\n [#] Response: ",response)
    
    with open("output.txt", "w") as file:
        file.write(response)
    with open("flag.txt","w") as file:
        file.write("false")

else: #if empty input/prompt:
    response = "Sorry, some error occoured, exiting code..."
    print("\n\n [#] Some error in prompt, exiting code.")
    with open("output.txt", "w") as file:
        file.write(response)
    exit()

