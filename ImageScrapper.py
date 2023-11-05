import requests
from bs4 import BeautifulSoup
import subprocess
from PIL import Image
from io import BytesIO

# Set the URL of the website you want to scrape
# user_place_name = "Vellore Institue of Technology".replace(" ", "_") 
user_place_name = input("Place name pls: ").title().replace(" ", "_")

url = "https://en.wikipedia.org/wiki/" + user_place_name
print("Searching for: ",url)
# Get the HTML of the website

    
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(response.text, "html.parser")
soup = soup.encode("utf-8")
print("Found, please wait for process...\n\n")


s = str(soup)
# Get entire scrapped website in txt
# with open("out.txt","w") as f:
#     f.write(s)

ind = s.find("upload.wikimedia.org/")

lst = []
while (ind != -1):
        ind = s.find("upload.wikimedia.org/")
        # print(ind)
        i = ind + 1
        c = s[i]

        while(c != '"'):
            c = s[i]
            i += 1
            # print(i)
            end_ind = i
        # print("\n",s[ind:end_ind+1])
        lst.append(s[ind:end_ind+1])
        s=s[i:]

lst.pop()
lst2 = []

rm = ["upload.wikimedia.org/wikipedia/commons/9/94/The_Golden_Temple_of_Amrithsar_7.jpg".lower(),
        "upload.wikimedia.org/wikipedia/commons/0/0c/Red_pog.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/f/fa/Wikiquote-logo.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/4/41/Global_thinking.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/0/0c/Red_pog.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/0/0c/Red_pog.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/f/fa/Wikiquote-logo.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg".lower(),
        "upload.wikimedia.org/wikipedia/commons/4/41/Global_thinking.svg".lower(),
        "upload.wikimedia.org/wikipedia/en/9/96/Symbol_category_class.svg".lower()]

for i in range (0,len(lst)):
    lst[i] = lst[i].replace('/thumb/',"/")

    if lst[i].find("jpg") != -1:
        lst[i] = lst[i].split('.jpg')[0] + ".jpg"
        if ((lst[i] not in lst2) and (lst[i].lower() not in rm)):
            lst2.append(lst[i])
    if lst[i].find("JPG") != -1:
        lst[i] = lst[i].split('.JPG')[0] + ".JPG"
        if ((lst[i] not in lst2) and (lst[i].lower() not in rm)):
            lst2.append(lst[i])
    # if lst[i].find("svg") != -1:
    #     lst[i] = lst[i].split('.svg')[0] + ".svg"
    #     if ((lst[i] not in lst2) and (lst[i].lower() not in rm)):
    #         lst2.append(lst[i])

for i in range(0,len(lst2)):
    lst2[i] = "http://" + lst2[i]

print(*lst2, sep="\n")    

def get_image_width_from_url(image_url):
    try:
        # Send an HTTP GET request to the image URL
        response = requests.get(image_url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Read the image content into a BytesIO object
            image_data = BytesIO(response.content)

            # Open the image using PIL (Pillow) and get its width
            img = Image.open(image_data)
            width, height = img.size

            return width
    except Exception as e:
        # If there's an error, simply return None
        return None

def get_max_width_images(image_urls):
    # Create a list to store the image widths and URLs
    image_info = []

    # Iterate through the list of image URLs and retrieve their widths
    for url in image_urls:
        width = get_image_width_from_url(url)
        if width is not None:
            image_info.append((url, width))

    # Sort the list by image width in descending order
    image_info.sort(key=lambda x: x[1], reverse=True)

    l = len(image_urls)
    if not image_info:
        # image res fetch failed and not a single image found:
        print("Forcing first 5 images")
        if (l>=5):
            image_info = [[image_urls[i], 111] for i in range(0,5)]
        else:
            image_info = [[image_urls[i], 111] for i in range(0,l)]
        # image width is dummy as image dim fetch failed and hence list was empty
        print(image_info)
    
    li = len(image_info)
    if li<=2:
        print("Forcing some more images")
        if (l>=5-li):
            i=li
            image_info = [[image_urls[i], 111] for i in range(i,li)]
        else:
            i=li
            image_info = [[image_urls[i], 111] for i in range(0,l)]
        # image width is dummy as image dim fetch failed and hence list was empty
        print(image_info)

    # Return a list with a maximum of 5 images (or fewer if there are fewer than 5 images in the list)
    return image_info[:5]

max_width_images = get_max_width_images(lst2)

f = open("out2.sh","w")
for url, width in max_width_images:
    print(f"Image URL: {url}\nImage Width: {width} pixels\n")
    f.write("start \"Chrome\" " + url + "\n")
f.close()
subprocess.run(["bash","out2.sh"])




# https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/38px-Wikispecies-logo.svg.png

# https://upload.wikimedia.org/wikipedia/commons/d/df/Wikispecies-logo.svg
# .svg/38px-Wikispecies-logo.svg.png