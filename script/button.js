// var p=["o"];
// function start_the_service() {
//   if (p[0] ==="o") {
//     var t  = document.createElement("div");
//     var t2  = document.createElement("script");
//     t.id = "chat";
//     if (window.innerWidth > window.innerHeight) {
//       t.style.width="29.6%";
//       t.style.left="68%";
//       t.style.top="10%";
//     } else {
//       t.style.width = "92.8%";
//     }
//     t2.src="script/chat.js";
//     document.body.appendChild(t);
//     p[0] = "c";
//     document.body.appendChild(t2);
//     document.getElementById("mn-btn").style.borderRadius = "0px 0px 20px 20px";
//   } else {
//     document.getElementById('chat').remove();
//     p[0] ="o";
//     document.getElementById("mn-btn").style.borderRadius = "20px 20px 0px 0px";
//   }
// }
// document.body.onload = function () {
// if (window.innerWidth < window.innerHeight) {
//   var t = document.getElementById("mn-btn");
//   t.style.width="94%";
//   t.style.left="23%";
//   t.style.top="75%";
// }
// console.log("loaded");
// }

// var p = ["o"];

// function adjustTabsWidth() {
//   var chatTab = document.getElementById("chat");
//   var mnBtnTab = document.getElementById("mn-btn");
  
//   if (window.innerWidth < window.innerHeight) {
//     // Adjust tab widths and positions when the condition is met
//     chatTab.style.width = "100%";
//     chatTab.style.left = "0";
//     mnBtnTab.style.width = "100%";
//     mnBtnTab.style.left = "0";
//   } else {
//     // Reset tab styles when the condition is not met
//     chatTab.style.width = "92.8%";
//     chatTab.style.left = "2vh";
//     mnBtnTab.style.width = "55%";
//     mnBtnTab.style.left = "23%";
//   }
// }

// function start_the_service() {
//   if (p[0] === "o") {
//     var t = document.createElement("div");
//     var t2 = document.createElement("script");
//     t.id = "chat";
//     t.style.position = "absolute";
//     t.style.top = "15vh";
//     t.style.left = "2vh";
//     t.style.border = "solid";
//     t.style.borderRadius = "20px";
//     t.style.height = "65vh";
//     t2.src = "script/chat.js";
//     document.body.appendChild(t);
//     p[0] = "c";
//     document.body.appendChild(t2);
//     document.getElementById("mn-btn").style.borderRadius = "20px";
//   } else {
//     document.getElementById('chat').remove();
//     p[0] = "o";
//     document.getElementById("mn-btn").style.borderRadius = "20px";
//   }
// }

// window.onload = function () {
//   adjustTabsWidth(); // Adjust tab widths on page load
//   console.log("loaded");
// }

// window.onresize = function () {
//   adjustTabsWidth(); // Adjust tab widths when the window is resized
// }


var p = ["o"];

function adjustTabsWidth() {
  var chatTab = document.getElementById("chat");
  var mnBtnTab = document.getElementById("mn-btn");
  
  if (window.innerWidth < window.innerHeight) {
    // Adjust tab widths and positions when the condition is met
    chatTab.style.width = "100%";
    chatTab.style.left = "0";
    mnBtnTab.style.width = "100%";
    mnBtnTab.style.left = "0";
  } else {
    // Reset tab styles when the condition is not met
    chatTab.style.width = "92.8%";
    chatTab.style.left = "2vh";
    mnBtnTab.style.width = "55%";
    mnBtnTab.style.left = "23%";
  }
}
/*
function toggleHeaderAndService() {
  const headerContainer = document.getElementById('header-container');
  headerContainer.style.display = 'none'; // Hide the header

  // Start your service here
  start_the_service();
}*/


function start_the_service() {
  if (p[0] === "o") {
    var t = document.createElement("div");
    var t2 = document.createElement("script");
    t.id = "chat";
    t.style.position = "absolute";
    t.style.top = "15vh";
    t.style.left = "2vh";
    t.style.border = "solid";
    t.style.borderRadius = "20px";
    t.style.height = "65vh";
    t2.src = "script/chat.js";
    document.body.appendChild(t);
    p[0] = "c";
    document.body.appendChild(t2);
    document.getElementById("mn-btn").style.borderRadius = "20px";
  } else {
    document.getElementById('chat').remove();
    p[0] = "o";
    document.getElementById("mn-btn").style.borderRadius = "20px";
  }
}

window.onload = function () {
  adjustTabsWidth(); // Adjust tab widths on page load
  console.log("loaded");
}

window.onresize = function () {
  adjustTabsWidth(); // Adjust tab widths when the window is resized
}
