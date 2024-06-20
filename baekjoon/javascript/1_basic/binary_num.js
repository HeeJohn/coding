// 문제

// 양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 
// 최하위 비트(least significant bit, lsb)의 위치는 0이다.

// 입력
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)

// 출력
// 각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.


// input : 1    output : 0 2 3
//         13        

// 13 = 1101
// 1의 위치 : 0 2 3


// 출력과 계산 분리하기

// 계산 : 13을 2로 나누고 나머지를 저장하고, 몫은 2로 나눌 수 없을 때까지 반복.

// 출력 : 한자리씩 읽어가면서 1일 때 그 위치를 출력

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];
let count;

rl.on('line', (line) => {
    if (count === undefined) {
        count = parseInt(line);
    } else {
        input.push(parseInt(line));
        if (input.length === count) {
            rl.close();
        }
    }
});

rl.on('close', () => {
    const result = solve(count, input);
    result.forEach(positions => {
        console.log(positions.join(' '));
    });
});

function solve(count, input) {
    let result = [];
    for (let i = 0; i < count; i++) {
        let num = input[i];

        let positions = [];
        let position = 0;
        
        while (num > 0) {
            if (num % 2 === 1) {
                positions.push(position);
            }
            num = Math.floor(num / 2);
            position++;
        }
        result.push(positions);
    }
    return result;
}
