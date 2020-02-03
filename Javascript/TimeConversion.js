'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the timeConversion function below.
 */
function timeConversion(s) {
    /*
     * Write your code here.
     */

    let ampm = s.substr(8,9)
    let hour = s.substr(0,2)
    let newHour = 0
    if(ampm == 'PM'){
        if(hour == 12){
            newHour = '12'
        } else {
            newHour = 12 + parseInt(hour)
        }
    } else {
        if(hour == 12){
            newHour = '00'
        } else {
            newHour = hour
        }
    }
    return newHour + s.substr(2,6)
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    let result = timeConversion(s);

    ws.write(result + "\n");

    ws.end();
}
