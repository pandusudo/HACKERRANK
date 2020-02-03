'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the plusMinus function below.
function plusMinus(arr) {
    let sum = arr.length
    let sumPos = 0
    let sumNeg = 0
    let sumZero = 0
    for(let i = 0; i < sum; i++){
        if(arr[i] > 0){
            sumPos += 1
        } else if (arr[i] < 0){
            sumNeg += 1
        } else {
            sumZero += 1
        }
    }

    console.log((sumPos / sum).toFixed(6) + '\n' + (sumNeg / sum).toFixed(6) + '\n' + (sumZero / sum).toFixed(6))

}

function main() {
    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
