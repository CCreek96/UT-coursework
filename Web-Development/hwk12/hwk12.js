var imgArray = [
	"./images/crab_nebula.jpg",
	"./images/galaxy_1.jpg",
	"./images/galaxy_2.jpg",
	"./images/galaxy_cluster.jpg",
	"./images/jupiter.jpg",
	"./images/m31.jpg",
	"./images/nebula_1.jpg",
	"./images/saturn.jpg"
];
var tileArray = imgArray.concat(imgArray);
var matches = {
	match00: false, 
	match01: false,
	match02: false,
	match03: false,
	match10: false,
        match11: false,
        match12: false,
        match13: false,
        match20: false,
        match21: false,
        match22: false,
        match23: false,
        match30: false,
        match31: false,
        match32: false,
        match33: false
};

var numTries = 0;
var numCorrect = 0;
var firstGuess = "";
var secondGuess = "";
var isMatch = false;
var idx1 = -1;
var idx2 = -1;
var delay = 3000;

$.fn.shuffleArray = function() {
	var i, j, k;
	for (i = tileArray.length - 1; i > 0; i--) {
		j = Math.floor(Math.random() * (i + 1));
		k = tileArray[i];
		tileArray[i] = tileArray[j];
		tileArray[j] = k;
	}
	return tileArray;
}

$.fn.checkMatch = function() {
	var first = $(firstGuess).attr('src');
	var second = $(secondGuess).attr('src');
  	if (first == second) {
		isMatch = true;
	}
}

$.fn.fadeFunction = function(imgTag){ 
	$(imgTag).fadeOut(3000, function() {
		numTries++;
      		var tries = numTries.toString();
      		$("#triesCount").val(tries);
      		$.fn.checkMatch();      
      		if (isMatch == false) {
        		$(imgTag).attr('src', '');
        		if (secondGuess == '') {
          			firstGuess = '';
          			idx1 = -1;
        		} else {
      	    			$(secondGuess).attr('src', '');
            			firstGuess = '';
            			secondGuess = '';
            			idx2 = -1; 
        		} 
      		} else {
        		$(firstGuess).fadeIn(1, function(){
       				$(firstGuess).attr('src', tileArray[idx1]);
    			});
        		$(secondGuess).stop();
    			$(secondGuess).fadeIn(1, function(){
      	  			$(secondGuess).attr('src', tileArray[idx2]);
    			});
        
        		if (firstGuess == "#img00") {
          			matches.match00 = true;
        		} else if (firstGuess == "#img01") {
          			matches.match01 = true;
        		} else if (firstGuess == "#img02") {
          			matches.match02 = true;
        		} else if (firstGuess == "#img03") {
          			matches.match03 = true;
        		} else if (firstGuess == "#img10") {
          			matches.match10 = true;
        		} else if (firstGuess == "#img11") {
          			matches.match11 = true;
        		} else if (firstGuess == "#img12") {
          			matches.match12 = true;
        		} else if (firstGuess == "#img13") {
          			matches.match13 = true;
        		} else if (firstGuess == "#img20") {
          			matches.match20 = true;
        		} else if (firstGuess == "#img21") {
          			matches.match21 = true;
        		} else if (firstGuess == "#img22") {
          			matches.match22 = true;
        		} else if (firstGuess == "#img23") {
         	 		matches.match23 = true;
        		} else if (firstGuess == "#img30") {
          			matches.match30 = true;
        		} else if (firstGuess == "#img31") {
          			matches.match31 = true;
        		} else if (firstGuess == "#img32") {
          			matches.match32 = true;
        		} else if (firstGuess == "#img33") {
          			matches.match33 = true;
        		}
        		if (secondGuess == "#img00") {
          			matches.match00 = true;
        		} else if (secondGuess == "#img01") {
          			matches.match01 = true;
        		} else if (secondGuess == "#img02") {
          			matches.match02 = true;
        		} else if (secondGuess == "#img03") {
          			matches.match03 = true;
        		} else if (secondGuess == "#img10") {
          			matches.match10 = true;
        		} else if (secondGuess == "#img11") {
          			matches.match11 = true;
        		} else if (secondGuess == "#img12") {
          			matches.match12 = true;
        		} else if (secondGuess == "#img13") {
          			matches.match13 = true;
        		} else if (secondGuess == "#img20") {
          			matches.match20 = true;
        		} else if (secondGuess == "#img21") {
          			matches.match21 = true;
        		} else if (secondGuess == "#img22") {
          			matches.match22 = true;
        		} else if (secondGuess == "#img23") {
          			matches.match23 = true;
        		} else if (secondGuess == "#img30") {
          			matches.match30 = true;
        		} else if (secondGuess == "#img31") {
          			matches.match31 = true;
        		} else if (secondGuess == "#img32") {
          			matches.match32 = true;
        		} else if (secondGuess == "#img33") {
          			matches.match33 = true;
        		}

        		firstGuess = '';
        		secondGuess = '';
        		idx1 = -1;
        		idx2 = -1;
        		isMatch = false;
        		numCorrect++;
        		if(numCorrect === 8) {
          			alert('You took ' + numTries.toString() + ' tries!');
        		}
		}
	});
}

$.fn.assignTile = function(imgTag, idx, matchij){ 
	if (matchij == false) {
		if (firstGuess == "") {
			firstGuess = imgTag;
			idx1 = idx;
			$(imgTag).fadeIn(1, function(){
        			$(imgTag).attr('src', tileArray[idx]);
      			});
      			$.fn.fadeFunction(imgTag);
    		} else if (secondGuess == '' && firstGuess != imgTag) {
      			secondGuess = imgTag;
      			idx2 = idx;
      			$(imgTag).fadeIn(1, function(){
        			$(imgTag).attr('src', tileArray[idx]);
      			});     
      			$(imgTag).fadeOut(3000, function(){
      			}); 
    		}
	}
}

$(document).ready(function() {
	$.fn.shuffleArray();
	$(".b00").click(function(){ 
		$.fn.assignTile("#img00", 0, matches.match00);
	});
	$(".b01").click(function(){
                $.fn.assignTile("#img01", 1, matches.match01);
        });
	$(".b02").click(function(){
                $.fn.assignTile("#img02", 2, matches.match02);
        });
	$(".b03").click(function(){
                $.fn.assignTile("#img03", 3, matches.match03);
        });
	$(".b10").click(function(){
                $.fn.assignTile("#img10", 4, matches.match10);
        });
        $(".b11").click(function(){
                $.fn.assignTile("#img11", 5, matches.match11);
        });
        $(".b12").click(function(){
                $.fn.assignTile("#img12", 6, matches.match12);
        });
        $(".b13").click(function(){
                $.fn.assignTile("#img13", 7, matches.match13);
        });
	$(".b20").click(function(){
                $.fn.assignTile("#img20", 8, matches.match20);
        });
        $(".b21").click(function(){
                $.fn.assignTile("#img21", 9, matches.match21);
        });
        $(".b22").click(function(){
                $.fn.assignTile("#img22", 10, matches.match22);
        });
        $(".b23").click(function(){
                $.fn.assignTile("#img23", 11, matches.match23);
        });
	$(".b30").click(function(){
                $.fn.assignTile("#img30", 12, matches.match30);
        });
        $(".b31").click(function(){
                $.fn.assignTile("#img31", 13, matches.match31);
        });
        $(".b32").click(function(){
                $.fn.assignTile("#img32", 14, matches.match32);
        });
        $(".b33").click(function(){
                $.fn.assignTile("#img33", 15, matches.match33);
        });
});
