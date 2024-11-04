const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let size;

rl.on('line', (line) => {
    if (size === undefined) {
        size = parseInt(line);
    } else {
        input.push(line.split(" ").map(Number));
    }
    if (input.length === size) {
        rl.close();
    }
});

rl.on('close', () => {
    let result = solve(input);
    result.forEach(function(max) {
        console.log(max);
    });
});

function solve(input) {
    let output = [];
    
    for (let i = 0; i < size; i++) {
        // 내림차순 정렬 후 세 번째로 큰 값 추출
        output.push(input[i].sort((a, b) => b - a)[2]);
    }
    
    return output;
}
