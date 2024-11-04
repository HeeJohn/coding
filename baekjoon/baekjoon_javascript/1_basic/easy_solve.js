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

// counter >= high 이면 끝
// 대신, ( counter - high )   *i; 를 빼준다. 


// 3 ~ 7 구간이라고 한다면,
// 1 ~ 2 구간을 구한다. -> 따로 저장 (jonk1)
// 3 ~ 7 구간을 구한다. -> 이어서 저장 (junk2)

// 1 ~ 7 까지의 합에서 1 ~2를 빼면, 3 ~ 7까지의 합이 나온다.



function solve(input){
    let low = input[0] -1;
    let high = input[1];

    let sum = 0;
    let counter =0;
    let i =1;

    while(counter < high){
        sum+= (i*i); // 1, 5, 14, 30, 55, 91
        counter += i; // 1, 3, 6, 10, 15, 21    

        if(counter >= low && counter -i < low){
            sum = (counter - low) * i;
        }
    
       i++;
    }

    sum -= (counter - high) * (i-1);
    return  sum ;
}


