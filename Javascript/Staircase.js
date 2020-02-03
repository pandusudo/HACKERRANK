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

// Complete the staircase function below.
function staircase(n) {
    let result = ''
    for(let i = 0; i < n; i++){
        for(let j = n - i; j > 1; j--){
            result += ' '
        }
        for(let j = i; j >= 0; j--){
            result += '#'
        }
        if (i < n){
            result += '\n'
        }
    }
    console.log(result)
}

function main() {
    const n = parseInt(readLine(), 10);

    staircase(n);
}
