
//최대, 최소 공약수 구하기

const readline = require('readline');


const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
});


let input =[];

rl.on('line',(line) => {
    input = line.split(" ").map(Number)
    rl.close();
});

rl.on('close', () => {
    let result = solution(input);
    result.forEach(function(number){
        console.log(number);
    });
});

// ----> 요구사항
// #. 두 수를 입력받아 최대공약수와 최소공배수를 구한다.

// ----> 분석
// # 최대공약수는 두 수가 서로 공통으로 가지고 있는 약수 중 가장 큰 수
// # 최소공배수는 두 수의 곱을 최대공약수로 나눈 수
// # 두 수를 입력받아 나눌 수 있는 제수를 찾아야 함.

// ----> 예시
//      24 18
// 2    12 9
// 3    4 3

// 최대공약수 = 2*3 = 6
// 최소공배수 = (24*18) / 6 = 72
// 24 18 => 6 72


// ----> 설계
// 1. 두 수를 입력받는다.
// 2. 두 수를 나눌 수 있는 제수를 찾는다.
// 3. 제수를 모두 찾아서 최대공약수를 구한다.
// 4. 최대공약수로 최소공배수를 구한다.


// ----> 구현
function solution(input){
    let max_common = 1;
    let [a, b] = [input[0], input[1]];
    
    let i =2;
    // 제수의 가장 큰 수는 두 수 중 작은 수보다 작거나 같음. (더 커지면 나눌 수가 없음.)
    while(i<= Math.min(a,b)){
        if(a%i===0 && b%i===0){
            max_common*=i;
            a = a/i;
            b = b/i;
            i = 2;
        }else{
            i++;
        }
    }
   
    return [max_common, a*b*max_common];
}


