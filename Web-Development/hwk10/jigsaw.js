function shuffle(srcArray) {
	var i, j, k;
	for (i = srcArray.length - 1; i > 0; i--) {
		j = Math.floor(Math.random() * (i + 1));
		k = srcArray[i];
		srcArray[i] = srcArray[j];
		srcArray[j] = k;
	}
	return srcArray;
}

function getImages() {
	var rndSrc = Math.floor(Math.random() * 3) + 1;

	var pic1 = document.getElementById("img1");
    	var pic2 = document.getElementById("img2");
    	var pic3 = document.getElementById("img3");
    	var pic4 = document.getElementById("img4");
	var pic5 = document.getElementById("img5");
    	var pic6 = document.getElementById("img6");
    	var pic7 = document.getElementById("img7");
    	var pic8 = document.getElementById("img8");
    	var pic9 = document.getElementById("img9");
    	var pic10 = document.getElementById("img10");
    	var pic11 = document.getElementById("img11");
    	var pic12 = document.getElementById("img12");
	
	var imgArray = new Array(pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9, pic10, pic11, pic12);
	imgArray = shuffle(imgArray)

	for (var i=0; i < imgArray.length; i++) {
		imgArray[i].src = "./images"+String(rndSrc)+"/img"+String(rndSrc)+"-"+String(i+1)+".jpg";
	
	}
}

//Stopwatch

var seconds = 0; 
var minutes = 0; 
var hours = 0;
var t;

function add() {
	seconds++;
	if (seconds >= 60) {
        	seconds = 0;
        	minutes++;
        	if (minutes >= 60) {
           		minutes = 0;
            		hours++;
        	}
    	}
    
	document.getElementById("time").value = (hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds);

	timer();
}
function timer() {
    	t = setTimeout(add, 1000);
}
timer();

function stopTimer() {
	clearTimeout(t);
}

	
/*
 Define variables for the values computed by the grabber event 
 handler but needed by mover event handler
*/
var diffX, diffY, theElement;


// The event handler function for grabbing the word
function grabber(event) {

// Set the global variable for the element to be moved

	theElement = event.currentTarget;

// Determine the position of the word to be grabbed,
//  first removing the units from left and top

	var posX = parseInt(theElement.style.left);
	var posY = parseInt(theElement.style.top);

// Compute the difference between where it is and
// where the mouse click occurred

	diffX = event.clientX - posX;
	diffY = event.clientY - posY;

// Now register the event handlers for moving and
// dropping the word

	document.addEventListener("mousemove", mover, true);
	document.addEventListener("mouseup", dropper, true);

// Stop propagation of the event and stop any default
// browser action

	event.stopPropagation();
	event.preventDefault();

}  //** end of grabber

// *******************************************************

// The event handler function for moving the word

function mover(event) {
// Compute the new position, add the units, and move the word

	theElement.style.left = (event.clientX - diffX) + "px";
	theElement.style.top = (event.clientY - diffY) + "px";

// Prevent propagation of the event

	event.stopPropagation();
}  //** end of mover

// *********************************************************
// The event handler function for dropping the word

function dropper(event) {

// Unregister the event handlers for mouseup and mousemove

	document.removeEventListener("mouseup", dropper, true);
	document.removeEventListener("mousemove", mover, true); 
 
// Prevent propagation of the event

	event.stopPropagation();
}  //** end of dropper

