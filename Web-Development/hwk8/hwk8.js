var topImg = "m51";
var img_src = new Array ("cluster", "interacting", "m104", "m51", "ngc1300", "ngc6217");
var img_cap = new Array ("Galaxy Cluster", "Interacting Galaxies", "M 104 Galaxy", "M 51 Galaxy", "NGC 1300 Galaxy", "NGC 6217 Galaxy");


function get_img () {
	var rnd_idx = Math.floor(Math.random() * img_src.length);
	if (rnd_idx == img_src.length) {
		rnd_idx = 0;
	}
	return rnd_idx;
}

function changeImg() {
	var rnd_idx = get_img();
	var newImg = img_src[rnd_idx];
	var figCap = document.getElementById("figCap").innerHTML = img_cap[rnd_idx];
	var domTop = document.getElementById(topImg).className = "img1";
	var domNew = document.getElementById(newImg).className = "img2";
	topImg = newImg;
}
