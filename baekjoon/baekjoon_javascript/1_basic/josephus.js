// const readline = require('readline');
// const rl = readline.createInterface({
// 		input : process.stdin,
// 		output : process.stdout,
// });

// /*
// 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
// 이제 순서대로 K번째 사람을 제거한다. 
// 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
// 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
// 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
// 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

// N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
// */

// // 요구사항 
// // 1. N명의 사람이 원으로 앉음 
// // 2. 양의 정수 K(<=N)
// // 3. 순서대로 K번째 제거
// // 4. 반복
// // 5. 사람이 제거되지 않을 때 종료

// // 분석
// // 1. N명을 원으로 만들어야 됨. 원형 링크드 리스트 구현. or 마킹으로도 가능할 듯(크기가 줄어드는게 아니기 때문에 성능은 떨어짐)
// // 2. 원래있던 위치 - 1에서 K만큼 더해야 다음 제거 대상이 나옴.
// // 4. 순서대로 K번째를 제거하되, 기록을 유지해야됨. 
// // 5. 종료 : 모두 제거할 때까지


// // 예시 : 입력 (7, 3)
// // 출력  : <3, 6, 2, 7, 5, 1, 4>
// //  1, 2, 3, 4, 5, 6, 7
// //  <3>
// //  1, 2, 4, 5, 6, 7 
// //  <3, 6>
// //  1, 2, 4, 5, 7
// //  <3, 6, 2>
// //  1, 4, 5, 7
// //  <3, 6, 2, 7>

// // 고민 :
// // 근데 그냥 배열로도 링크드 리스트는 구현할 수 있으니깐 배열로 해야겠다. (노드 만들기 귀찮.)

// // 설계
// // 1. 배열로 링크드 리스트 만들기. (단방향)
// // 2. index : [0][1][2][3][4][5][6]
// // 3. value : [1][2][3][4][5][6][0] <- 이렇게
// // 4. 그럼 라운드 큐가 됨. (이전 값을 잘 유지해야 됨. 그래야 이어 줄 수 있음)

// input = [];

// rl.on('line', (line) => { 
// 		input = line.split(" ").map(Number);
// 		rl.close();
		
// 		let result = solution(input);
// 		console.log(`<${result.join(', ')}>`);
// });

// function init_array(n){
// 	let array = [];
// 	for(let i = 0 ; i < n-1 ; i++){
// 		array[i] = i;
// 	}
// 	array[n-1] = 0; 
// 	return array;
// }


// function solution(input){
// 		let [n, k] = [input[0], input[1]];
// 		let pre_i = 0; 
// 		let curr_i = 0;
// 		let result = [];
// 		let people = init_array(n);
	
// 		while(result.length < n){
// 				for (let c = 0; c < k-1; c++){ // 3번째의 값은 배열의 2번째 위치에 있음.
// 						pre_i = curr_i; 
// 						curr_i = people[curr_i];
// 				}
				
// 				// 현재 인덱스에 해당하는 사람을 제거하고 결과에 추가
//         result.push(curr_i + 1);
//         // 이전 사람의 다음 사람을 현재 사람의 다음 사람으로 설정
//         people[pre_i] = people[curr_i];
//         curr_i = people[curr_i];
		
// 		}
		 
// 		return result;
// }



////// 틀림 -> 어디가 틀렸는지 찾아보자. ---> 처음 배열 초기화를 잘못함. 실수로 +1을 빼먹음. -> 다음 위치를 가르켜야 해서 중요.


const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on('line', (line) => {
    input = line.split(" ").map(Number);
    rl.close();

    let result = solution(input);
    console.log(`<${result.join(', ')}>`);
});

function init_array(n) {
    let array = [];
    for (let i = 0; i < n - 1; i++) {
        array[i] = i + 1;
    }
    array[n - 1] = 0;
    return array;
}

function solution(input) {
    let [n, k] = [input[0], input[1]];
    let pre_i = 0; 
    let curr_i = 0;
    let result = [];
    let people = init_array(n);

    while (result.length < n) {
        for (let c = 0; c < k - 1; c++) {
            pre_i = curr_i;
            curr_i = people[curr_i];
        }

        result.push(curr_i + 1);
        people[pre_i] = people[curr_i];
        curr_i = people[curr_i];
    }

    return result;
}
