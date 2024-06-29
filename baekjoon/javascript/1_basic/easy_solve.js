const readline = require('readline');


const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});

let input;

rl.on('line', (line)=>{
    input = line.split(" ").map(Number);
    rl.close();

    console.log(solve(input));
});

// 입력 : A, B(1 ≤ A ≤ B ≤ 1,000)

    // 과정              // i        // counter      //each sum         // total sum
    // 1                // 1        // 1            // 1                // 1
    // 2 2              // 2        // 3            // 4                // 5
    // 3 3 3            // 3        // 6            // 9                // 14
    // 4 4 4 4          // 4        // 10           //16                // 30

// 3 ~ 7
// 

// 1 ~ 7 까지의 합에서 1 ~2를 빼면, 3 ~ 7까지의 합이 나온다.


function sumEach(i){
    return i*i;
}

function sumTotal(sum, currentSum){
    return sum+=currentSum;
}

function trackCounter(tracker, i){
    return tracker +=i;
}

function solve(input){
    let low = input[0];
    let high = input[1];

    let tracker = 0;
    let i =1;
    
    while(tracker <= high-1){
        
    }

    let counter = 0;
    let currentSum = 0;

    for(let i = 1 ;i<=high; i++){
        currentSum = sumEach(i);
        sum = sumTotal(sum, currentSum);
        console.log(sum);
    }
}


