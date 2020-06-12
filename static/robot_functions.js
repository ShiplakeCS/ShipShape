var ongoingTouches = [];
var mostRecentDirection = "";

function move(direction) {

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/robot/go/" + direction, true);
    xhttp.send();

}

function log(msg) {
	var p = document.getElementById('log');
	p.innerHTML = msg + "\n" + p.innerHTML;
}

function DetermineDirection(xStart,yStart,xEnd,yEnd){

	var xDifferent, yDifferent, direction = "";
	xDifferent = Math.abs(xEnd - xStart);
	yDifferent = Math.abs(yEnd - yStart);
	
	if (xDifferent > yDifferent) {
	
		if (xEnd < xStart){
			direction = "right";
		}
		else {
			direction = "left";
		}
	}
	else if (yDifferent > xDifferent) {
	
		if (yEnd > yStart){
			direction = "forward";
		}
		
		else {
			direction = "backwards";
		}
	}
	
	log("Direction: " + direction);
	
	return direction;
	
}


function copyTouch({ identifier, pageX, pageY }) {
	return { identifier, pageX, pageY };
}

function ongoingTouchIndexById(idToFind) {
  for (var i = 0; i < ongoingTouches.length; i++) {
	var id = ongoingTouches[i].identifier;
	
	if (id == idToFind) {
	  return i;
	}
  }
  return -1;    // not found
}

function handleStart(evt) {
  evt.preventDefault();
  var touches = evt.changedTouches;
  for (var i = 0; i < touches.length; i++) {
	ongoingTouches.push(copyTouch(touches[i]));
	log("Touch start x: " + touches[i].pageX + ", y: " + touches[i].pageY);
  }
}		

function handleMove(evt) {
  
  evt.preventDefault();
  
  var d;
  var touches = evt.changedTouches;
  var idx = ongoingTouchIndexById(touches[0].identifier);

  if (idx >= 0) {

    log("Movement - START: (" + touches[0].pageX + ", " + touches[0].pageY + "), MOVED TO: (" + ongoingTouches[idx].pageX + ", " + ongoingTouches[idx].pageY + ")");

    d = DetermineDirection(touches[0].pageX, touches[0].pageY, ongoingTouches[idx].pageX, ongoingTouches[idx].pageY);
    
    if (d != mostRecentDirection) {
    
      mostRecentDirection = d;
      move(mostRecentDirection);
      
    }

    ongoingTouches.splice(idx, 1, copyTouch(touches[0]));  // swap in the new touch record
    
  } 
}

function handleEnd(evt) {
  evt.preventDefault();
  log("touchend");

  var touches = evt.changedTouches;

  for (var i = 0; i < touches.length; i++) {

	var idx = ongoingTouchIndexById(touches[i].identifier);

	if (idx >= 0) {
	  ongoingTouches.splice(idx, 1);  // remove it; we're done
	} else {
	  console.log("can't figure out which touch to end");
	}
  }
  
  mostRecentDirection = "stop";
  move(mostRecentDirection);
  
}

function handleCancel(evt) {
  evt.preventDefault();
  console.log("touchcancel.");
  var touches = evt.changedTouches;
  
  for (var i = 0; i < touches.length; i++) {
	var idx = ongoingTouchIndexById(touches[i].identifier);
	ongoingTouches.splice(idx, 1);  // remove it; we're done
  }
}

function startup() {
  var el = document.getElementById("canvas");
  el.addEventListener("touchstart", handleStart, false);
  el.addEventListener("touchend", handleEnd, false);
  el.addEventListener("touchcancel", handleCancel, false);
  el.addEventListener("touchmove", handleMove, false);
  log("startup() function completed - v2");
}

document.addEventListener("DOMContentLoaded", startup);
