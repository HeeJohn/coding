// 입력을 받기 위한 readline 모듈을 가져옵니다.
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let currentPassengers = 0;
let maxPassengers = 0;

// 한 줄씩 입력을 처리합니다.
rl.on('line', (line) => {
  const [out, in] = line.split(' ').map(Number);
  currentPassengers = currentPassengers - out + in;
  if (currentPassengers > maxPassengers) {
    maxPassengers = currentPassengers;
  }
}).on('close', () => {
  console.log(maxPassengers);
  process.exit(0);
});
