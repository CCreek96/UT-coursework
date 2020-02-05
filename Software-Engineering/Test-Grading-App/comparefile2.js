
var Answers = [{1: 'A'}, {2: 'B'}, {3: 'C'}];
var Student = [{1: 'B'}, {2: 'B'}, {3: 'C'}];

function compare(A, B) {
    "use strict"

    var correct = 0,
        keysA = [],
        keysB = [];

    for (var i=0, i<A.length, i++) {
        keysA= keysA.push(Object.keys(A[i]))
    }

    for (var i=0, i<B.length, i++) {
        keysB= keysB.push(Object.keys(B[i]))
    }

   // for (i=0; Object.keys(A)-1;i++) {
    for (var i=0; i<A.length; i++) {  
        if (A[i[keysA[i]]] == B[i[keysB[i]]]) {
            correct += 1
        } else {
            console.log("Input is the incorrectly formated")
        }
    }
    
    var score = correct/Object.keys(A).length();
    return(score)
}

compare(Answers,Student)

