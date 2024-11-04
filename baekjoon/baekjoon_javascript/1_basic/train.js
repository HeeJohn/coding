const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});

let max = 0;
let current = 0;

rl.on("line", (line) => {
    let [off, on] = line.split(" ").map(Number);
    let diff = on - off;
    solve(diff);
});


rl.on("close", ()=>{
    console.log(max);
});

function solve(diff){
    current += diff;
    if(max < current) max = current;
}