const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const operators = [];
let count = 0;
let nums = [];

rl.on('line', line => {
    if (count === 0) {
        count = parseInt(line);
    } else if (nums.length === 0) {
        nums = line.split(" ").map(Number);
    } else {
        operators.push(...line.split(" ").map(Number));
        rl.close();
        const result = solution(count, nums, operators);
        console.log(result[0]);
        console.log(result[1]);
    }
});

function solution(count, nums, operators) {
    let max = -Infinity;
    let min = Infinity;

    function dfs(i, result, plus, minus, mul, div) {
        if (i === count) {
            max = Math.max(max, result);
            min = Math.min(min, result);
            return;
        }

        if (plus > 0) {
            dfs(i + 1, result + nums[i], plus - 1, minus, mul, div);
        }
        if (minus > 0) {
            dfs(i + 1, result - nums[i], plus, minus - 1, mul, div);
        }
        if (mul > 0) {
            dfs(i + 1, result * nums[i], plus, minus, mul - 1, div);
        }
        if (div > 0) {
            dfs(i + 1, parseInt(result / nums[i]), plus, minus, mul, div - 1);
        }
    }

    dfs(1, nums[0], operators[0], operators[1], operators[2], operators[3]);
    return [max, min];
}
