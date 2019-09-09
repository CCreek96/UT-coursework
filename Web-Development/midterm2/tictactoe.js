var xImage = "./ticTacX.png";
var oImage = "./ticTacO.png";
var currentLetter = 'X';
var winner = "";
var gameOver = false;
var winsX = 0;
var winsO = 0;

$.fn.checkWinner = function() {
  if($("#img00").attr("src") != "" && $("#img00").attr("src") == $("#img01").attr("src") && $("#img01").attr("src") == $("#img02").attr("src")) {
    winner = $("#img00").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img10").attr("src") != "" && $("#img10").attr("src") == $("#img11").attr("src") && $("#img11").attr("src") == $("#img12").attr("src")) {
    winner = $("#img10").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img20").attr("src") != "" && $("#img20").attr("src") == $("#img21").attr("src") && $("#img21").attr("src") == $("#img22").attr("src")) {
    winner = $("#img20").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img00").attr("src") != "" && $("#img00").attr("src") == $("#img10").attr("src") && $("#img10").attr("src") == $("#img20").attr("src")) {
    winner = $("#img00").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img01").attr("src") != "" && $("#img01").attr("src") == $("#img11").attr("src") && $("#img11").attr("src") == $("#img21").attr("src")) {
    winner = $("#img01").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img02").attr("src") != "" && $("#img02").attr("src") == $("#img12").attr("src") && $("#img12").attr("src") == $("#img22").attr("src")) {
    winner = $("#img02").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img00").attr("src") != "" && $("#img00").attr("src") == $("#img11").attr("src") && $("#img11").attr("src") == $("#img22").attr("src")) {
    winner = $("#img00").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
  } else if ($("#img02").attr("src") != "" && $("#img02").attr("src") == $("#img11").attr("src") && $("#img11").attr("src") == $("#img20").attr("src")) {
    winner = $("#img02").attr("src")=="./ticTacX.png" ? "X" : "O";
    return true;
	} else {
    return false;
  }
}

$.fn.announceWinner = function() {
  gameOver = true;
  alert(winner + " has won!");
  if(winner == "X") {
    winsX++;
  } else if (winner == "O") {
    winsO++;
  }
  var winsXString = winsX.toString();
  $("#winsX").val(winsXString);
  var winsOString = winsO.toString();
  $("#winsO").val(winsOString);
}

$.fn.resetBoard = function() {
  winner = "";
  currentLetter = "X";
  gameOver = false;
  $("#img00").attr("src", "");
  $("#img01").attr("src", "");
  $("#img02").attr("src", "");
  $("#img10").attr("src", "");
  $("#img11").attr("src", "");
  $("#img12").attr("src", "");
  $("#img20").attr("src", "");
  $("#img21").attr("src", "");
  $("#img22").attr("src", "");
}

$.fn.assignTile = function(imgTag) {
  if (gameOver == true) {
    return;
  } else if (currentLetter == "O" && $(imgTag).attr("src") == "") {
    $(imgTag).attr("src", xImage);
    currentLetter = "X";
    if ($.fn.checkWinner()) {
      $.fn.announceWinner();
    }
  } else if (currentLetter == "X" && $(imgTag).attr("src") == ""){
    $(imgTag).attr("src", oImage);
    currentLetter = "O";
    if ($.fn.checkWinner()) {
      $.fn.announceWinner();
    }
  } else if ($(imgTag).attr("src") != ""){
    return;
  }
}

$(document).ready(function() {
	$(".b00").click(function(){
		$.fn.assignTile("#img00");
	});
	$(".b01").click(function(){
    $.fn.assignTile("#img01");
  });
	$(".b02").click(function(){
    $.fn.assignTile("#img02");
  });
	$(".b10").click(function(){
    $.fn.assignTile("#img10");
  });
  $(".b11").click(function(){
    $.fn.assignTile("#img11");
  });
  $(".b12").click(function(){
    $.fn.assignTile("#img12");
  });
	$(".b20").click(function(){
    $.fn.assignTile("#img20");
  });
  $(".b21").click(function(){
    $.fn.assignTile("#img21");
  });
  $(".b22").click(function(){
    $.fn.assignTile("#img22");
  });
  $(".resetBtn").click(function() {
    $.fn.resetBoard();
  });
});
