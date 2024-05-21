// jshint esversion: 6

// Define the onclick handlers

function btn1Handler() {
  document.getElementById("outBox").value += "Ahoy! ";
  playAudio('ahoy.mp3');
}

function btn2Handler() {
  document.querySelector("textarea").value += "Avast! ";
  playAudio('avast.mp3');
}

function btn3Handler(){
  document.getElementById("outBox").value += "Arrr! ";
  playAudio('yarrgh.mp3');
}

function btn4Handler(){
  document.getElementById("outBox").value += "Show a Leg! ";
  playAudio('showaleg.mp3');
}

function btn5Handler(){
  document.getElementById("outBox").value += "Matey! ";
  playAudio('matey.mp3');
}

function btn6Handler(){
  document.getElementById("outBox").value += "Proud Beauty! ";
  playAudio('proudbeauty.mp3');
}

function btn7Handler(){
  document.getElementById("outBox").value += "Foul Blaggart! ";
  playAudio('foulblaggart.mp3');
}

function btn8Handler(){
  document.getElementById("outBox").value += "Me! ";
  playAudio('me.mp3');
}

// Function to play audio
function playAudio(audioPath) {
  const audio = new Audio(audioPath);
  audio.play();
}

// Register the onclick handlers after the page loads and the DOM is complete
window.onload = function() {
  document.getElementById("b1").addEventListener("click", btn1Handler);
  document.getElementById("b2").addEventListener("click", btn2Handler);
  document.getElementById("b3").addEventListener("click", btn3Handler);
  document.getElementById("b4").addEventListener("click", btn4Handler);
  document.getElementById("b5").addEventListener("click", btn5Handler);
  document.getElementById("b6").addEventListener("click", btn6Handler);
  document.getElementById("b7").addEventListener("click", btn7Handler);
  document.getElementById("b8").addEventListener("click", btn8Handler);
};
