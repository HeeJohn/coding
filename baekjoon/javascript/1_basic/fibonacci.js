const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let count = 0;

rl.on('line', (line) => {
    count = parseInt(line);
    rl.close();
});

rl.on('close', () => {
    let result = 0;
    switch (count) {
        case 0: break;
        case 1: result = 1; break;
        default: result = solve(0, 1, count - 2);
    }
    console.log(result);
});

function solve(a1, a2, count) {
    if (count === 0) return a1 + a2;
    return solve(a2, a1 + a2, --count);
}
