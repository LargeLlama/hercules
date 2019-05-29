var timer = document.getElementById('timer')

var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
  var hour = Math.floor((now % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minute = Math.floor((now % (1000 * 60 * 60)) / (1000 * 60));
  var second = Math.floor((now % (1000 * 60)) / 1000);
  if (minute < 10){
    minute = "0" + minute;
  }
  if (second < 10){
    second = "0" + second;
  }
  hour = hour - 4;
  timer.innerHTML = hour + ":" + minute + ":" + second;


}, 1000);
