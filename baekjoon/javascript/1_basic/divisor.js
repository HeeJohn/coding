
// input 1 : 6 3 | output 1 : 3
// input 2 : 25 4 | output 2 : 0
// input 3 : 2735 1 | output 3 : 1





// 모든 약수를 구하기보다는 K번째 약수까지 구하기
// p를 q로 나누었을 때 나머지가 0이고, 몫이 r이면 r도 약수에 포함됨. (이 값을 저장하면 계산을 줄일 수 있음)

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout  
});

let input;

rl.on('line', (line) => {
    input = line.split(" ").map(Number);
});

rl.on('close', () => {  
    const result = solve(input); 
    console.log(result);
});

function solve(input) {
    let low = [];
    let high = [];
    
    let n = input[0];
    let k = input[1];
    
    for (let i = 1; i <= Math.sqrt(n); i++) { // n^1/2 까지만
		    if (low.length === k ) return low[low.length-1]; // 약수를 모으는 과정에서 만족하면 바로 종료.
		    
        if (n % i === 0) {
            low.push(i); // 작은 쪽 (제수)
            if (i !== n / i) {
                high.push(n / i); // 큰 쪽 (몫)
            }
        }
    }
    
    let candidates = [...low, ...high.reverse()]; // high 배열을 뒤집어 결합.
    if (candidates.length < k) {
        return 0;
    } else {
        return candidates[k - 1];
    }
}