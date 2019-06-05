//the timer
var timer = document.getElementById('timer');
//the time into the task
var inTime = document.getElementById("time_into");
//time until end of task
var unTime = document.getElementById("time_left");
//the first column of start times
var startTimes = document.getElementsByName("1");
//the second column of end times
var endTimes = document.getElementsByName("2");


//console.log(startTimes);
//console.log(endTimes);

//updates every second
var x = setInterval(function() {
  // Get today's date and time
  var now = new Date().getTime();
  var hour = Math.floor((now % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  hour = hour - 4;
  var minute = Math.floor((now % (1000 * 60 * 60)) / (1000 * 60));
  var second = Math.floor((now % (1000 * 60)) / 1000);
  //just in case there is no task at this time
  var into = -1;
  var until = -1;
  for (var x = 0;x < startTimes.length;x++){
    //definitely before the current time
    if (parseInt(startTimes[x].innerHTML.substr(0,2)) < hour ){
      //definitely after the current time
      if (parseInt(endTimes[x].innerHTML.substr(0,2)) > hour){
        //calculate the numbers
        into = (hour - parseInt(startTimes[x].innerHTML.substr(0,2))) * 60 + (minute - parseInt(startTimes[x].innerHTML.substr(3,5)));
        until = (parseInt(endTimes[x].innerHTML.substr(0,2)) - hour) * 60 + (parseInt(endTimes[x].innerHTML.substr(3,5)) - minute);
        break;
      }
      //if hour is not greater then gotta check minutes
      else if (parseInt(endTimes[x].innerHTML.substr(0,2)) == hour){
        //minutes greater so the time is in the task timeframe
        if (parseInt(endTimes[x].innerHTML.substr(3,5)) >= minute){
          into = (hour - parseInt(startTimes[x].innerHTML.substr(0,2))) * 60 + (minute - parseInt(startTimes[x].innerHTML.substr(3,5)));
          until = (parseInt(endTimes[x].innerHTML.substr(0,2)) - hour) * 60 + (parseInt(endTimes[x].innerHTML.substr(3,5)) - minute);
          break;
        }
      }
    }
    else if (parseInt(startTimes[x].innerHTML.substr(0,2)) == hour){
      //check if the minutes for the start time are less than current time
      if (parseInt(startTimes[x].innerHTML.substr(3,5)) <= minute){
        //rest here is same as above
        if (parseInt(endTimes[x].innerHTML.substr(0,2)) > hour){
          into = (hour - parseInt(startTimes[x].innerHTML.substr(0,2))) * 60 + (minute - parseInt(startTimes[x].innerHTML.substr(3,5)));
          console.log(into);
          until = (parseInt(endTimes[x].innerHTML.substr(0,2)) - hour) * 60 + (parseInt(endTimes[x].innerHTML.substr(3,5)) - minute);
          break;
        }
        else if (parseInt(endTimes[x].innerHTML.substr(0,2)) == hour){
          if (parseInt(endTimes[x].innerHTML.substr(3,5)) >= minute){
            into = (hour - parseInt(startTimes[x].innerHTML.substr(0,2))) * 60 + (minute - parseInt(startTimes[x].innerHTML.substr(3,5)));
            until = (parseInt(endTimes[x].innerHTML.substr(0,2)) - hour) * 60 + (parseInt(endTimes[x].innerHTML.substr(3,5)) - minute);
            break;
          }
        }
      }
    }
  }

  //turns it into a string
  if (minute < 10){
    minute = "0" + minute;
  }
  //turns it into a string
  if (second < 10){
    second = "0" + second;
  }
  if (into < 0){
    into = "downtime";
    until = "downtime";
  }

  inTime.innerHTML = into;
  unTime.innerHTML = until;
  timer.innerHTML = hour + ":" + minute + ":" + second;


}, 1000);
