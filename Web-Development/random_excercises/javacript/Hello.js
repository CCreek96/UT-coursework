function addTwo(x, y) {
	var z = x + y;
	return z;
}

function fib(n) {
	if ((n==0) || (n==1)) {
		return n;
	}
	else {
		return fib(n-1) + fib(n-2);
	}
}



function main() {
	console.log("Hello World!");
	var a = 2;
        var b = 3;
        var c = addTwo(a, b);
        console.log(c);
	console.log(fib(5));
	for (var i = 0; i < 10; i++) {
		console.log(i + i);
	}

}
main();
