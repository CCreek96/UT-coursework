
var Answers = {1: 'A', 2: 'B', 3: 'C'};
var Student = {1: 'B', 2: 'B', 3: 'C'};

function compare(A, B) {
    "use strict"
    var correct = 0,
        keysA = Object.keys(A),
        keysB = Object.keys(B);
    
   // for (i=0; Object.keys(A)-1;i++) {
    for (var i=0; keysA.length; i++) {  
        if (A[keysA[i]] == B[keysB[i]]) {
            correct += 1
        }
    }
    
    var score = correct/Object.keys(A).length();
    return(score)
}

compare(Answers,Student)

