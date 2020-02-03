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

// Complete the miniMaxSum function below.
function miniMaxSum(arr) {
    let newArr = []
    for(let i = 0; i < arr.length; i++){
        let sum = 0
        for(let j = 0; j < arr.length; j++){
            if(j != i){
                sum += arr[j]
            }
        }
        newArr.push(sum)
    }
    console.log(Math.min.apply(null, newArr), Math.max.apply(null, newArr))    
}

function main() {
    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    miniMaxSum(arr);
}
