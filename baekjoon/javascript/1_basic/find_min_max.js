
const readline = require('readline');

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});

let input = [];
let inputCount;

rl.on('line', (line) => {
    if (inputCount === undefined) {
        inputCount = parseInt(line);
    } else {
        input = line.split(" ").map(Number);
    }
    if (input.length >= inputCount) {
        rl.close();
    }
});

rl.on('close', () => {
    let result = solve(inputCount, input);
    console.log(`${result[0]} ${result[1]}`);
});

function solve(inputCount, input) {
    let min = input[0];
    let max = input[0];
    
    for (let i = 1; i < inputCount; i++) {
        if (input[i] < min) min = input[i];
        if (input[i] > max) max = input[i];
    }
    
    return [min, max];
}
