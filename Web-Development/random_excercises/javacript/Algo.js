function shuffle(arr) {
 	var num = 0;
	var idx = 0;
	for (var i=0; i < arr.length; i++) {
                idx = Math.floor(Math.random() * arr.length);
                num = arr[idx];
                arr[idx] = arr[i];
                arr[i] = num;
        }
	return arr;
}

function main() {

	var a = new Array (1,2,3,4,5,6,7,8,9,10);

	console.log(a.toString());
	var b = shuffle(a);
	console.log(b.toString());

	var today = new Date();
	console.log(today);

	var hours = today.getHours();
	console.log(hours);
}

main();
