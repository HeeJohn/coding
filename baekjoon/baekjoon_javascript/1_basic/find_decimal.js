const readline = require("readline");
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
        input = line.split(" ").map(Number);
        rl.close();
    }
});

rl.on('close', () => {
    console.log(size - solve(input));
    process.exit();
});

function solve(input) {
    let counter = 0;
    
    input.forEach((num) => {
        if (num === 1) { // 1 예외
            counter++;
            return;
        }
        
        // 2부터 루트크기까지만 확인하면 됨. (나눠지는 수 없어야 됨.)
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i !== 0) continue;
            counter++;
            return;
        }
 
    });
    return counter;
}