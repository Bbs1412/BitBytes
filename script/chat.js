// initialize by constructing a named function..chat-bubble.
// .and add text processing plugin:
var chatWindow = new Bubbles(document.getElementById("chat"), "chatWindow", {
  // the one that we care about is inputCallbackFn()
  // this function returns an object with some data that we can process from user input
  // and understand the context of it

  // this is an example function that matches the text user typed to one of the answer bubbles
  // this function does no natural language processing
  // this is where you may want to connect this script to NLC backend.
  inputCallbackFn: function(o) {
    // add error conversation block & recall it if no answer matched
    var miss = function() {
      chatWindow.talk(
        {
          "i-dont-get-it": {
            says: [
              "Sorry, I don't get it 😕. Pls repeat? Or you can just click below 👇"
            ],
            reply: o.convo[o.standingAnswer].reply
          }
        },
        "i-dont-get-it"
      )
    }

    // do this if answer found
    var match = function(key) {
      setTimeout(function() {
        chatWindow.talk(convo, key) // restart current convo from point found in the answer
      }, 600)
    }

    // sanitize text for search function
    var strip = function(text) {
      return text.toLowerCase().replace(/[\s.,\/#!$%\^&\*;:{}=\-_'"`~()]/g, "")
    }
    console.log(strip.text())
    // search function
    var found = false
    o.convo[o.standingAnswer].reply.forEach(function(e, i) {
      strip(e.question).includes(strip(o.input)) && o.input.length > 0
        ? (found = e.answer)
        : found ? null : (found = false)
    })
    found ? match(found) : miss()
  }
}) // done setting up chat-bubble

// conversation object defined separately, but just the same as in the
// "Basic chat-bubble Example" (1-basics.html)
var convo = {
  "ice": {
    says: ["Hey there, Planned anything?"],
    reply: [
      // {
      //   question: "Mountains",
      //   answer: "Mountains"
      // },
      // {
      //   question: "Beach",
      //   answer: "Beach"
      // },
      // {
      //   question: "Religious places",
      //   answer: "Religious places"
      // },
      {
        question: "yes",
        answer: "yes"
      },
      {
        question: "Not Yet",
        answer: "Not Yet"
      }
      // {
      //   question: "",
      //   answer: "biology"
      // }
    ]
  },
  "yes": {
    says: ["where do you want to go?"],
    // reply: [
    //   {
    //     question: "Start Over",
    //     answer: "ice"
    //   },
    //   {
    //     question: "Start Over",
    //     answer: "ice"
    //   },
      
    // ]
  },
  "Not Yet": {
    says: ["shall we plan for you?"],
    reply: [
      {
        question: "okay",
        answer: "okay"
      },
      {
        question: "no",
        answer: "no"
      }
    ]
  },
  "no": {
    says: ["ok"],
    // reply: [
    //   {
    //     question: "Start Over",
    //     answer: "ice"
    //   }
    // ]
  },
  "okay": {
    says: ["when are you planning for tour?"],
    reply: [
      {
        question: "Summer",
        answer: "Summer"
      },
      {
        question: "Winter",
        answer: "Winter"
      },
      {
        question: "Monsoon",
        answer: "Monsoon"
      },
    ]
  },
  "Summer": {
    says: ["you are planning for: "],
    reply: [
      {
        question: "Adventurous trip",
        answer: "Adventurous trip"
      },
      {
        question: "Educational trip",
        answer: "Educational trip"
      },
      {
        question: "casual trip",
        answer: "casual trip"
      },
    ]
  },
  "casual trip": {
    says: ["what kind of trip do you want?"],
    reply: [
      {
        question: "affodable",
        answer: "affodable"
      },
      {
        question: "luxurious",
        answer: "luxurious"
      },
    ]
  },
  "affodable": {
    says: ["how long do you wanna plan your trip?"],
    reply: [
      {
        answer: "final"
      }
    ]
  },
  "luxurious": {
    says: ["how long do you wanna plan your trip?"],
    reply: [
      {
        answer: "final"
      }
    ]
  },
  "final": {
    says: ["we are making packages for you."]
  },
}





// pass JSON to your function and you're done!
chatWindow.talk(convo);