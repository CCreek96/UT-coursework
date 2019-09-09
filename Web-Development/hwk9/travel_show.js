
var idx = 0;
var img_src = new Array ("agra", "ajanta", "akshardham", "gateway", "hawa", "mehrangarh", "mysore", "qutub", "sun", "taj", "victoria");

function startSlideShow() {

	var interval = setInterval(changeImg, 3000);
}

function get_img () {
	if (idx == img_src.length - 1) {
		idx = 0;
		return img_src[idx];
	} else {
		idx += 1
		return img_src[idx];
	}
}

function changeImg() {
        var rnd_idx = get_img();
        var newImg = img_src[rnd_idx];
        var figCap = document.getElementById("figCap").innerHTML = img_cap[rnd_idx];
        var domTop = document.getElementById(topImg).className = "img1";
        var domNew = document.getElementById(newImg).className = "img2";
        topImg = newImg;
}

function exitSlideShow() {
	clearInterval(interval);
}
