const readline = require('readline');

const rl = readline.createInterface({
    input : process.stdin,
    output  : process.stdout
});


let input = [];

rl.on('line', (line) => {
    input.push(parseInt(line));
});


rl.on("close", ()=>{
    let result = solve(input);
    result.forEach((output)=>
        console.log(output)
    );
});


function isPrime(num){

    if(num === 1){
        return false;
    }

    for(let i = 2; i<=Math.sqrt(num); i++){
        if(num%i === 0){
            return false;
        }
    }

    return true;
}

function solve(input){
    let minPrime = 0;
    let sum = 0;

    for(let i = input[0];i<=input[1]; i++){
        if(isPrime(i)) {
            if(minPrime === 0) minPrime = i;
            sum+=i;
        } 
    }
    
    if(minPrime === 0){
        return [-1];
    }else{
        return [sum, minPrime];
    }
}



