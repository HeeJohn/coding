"""Description
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다."""


# 뒷 번호를 기준으로, 판단해야 할까??

#1,3,5,7,11,13,17,19,23,29,37,41

#0 -> 0, 01, 07, 071, 017 
#--> 0이 들어간 정보는 필요 없음 최적화 가능
#--> 나중에 오차피 들어오는 값들.

#1 -> 1, 10, 17, 107, 171
#7 -> 7, 70, 71, 701, 710






def isPrime(num) :
    if num == 1 : return False
    if num ==2 : return True

    for i in range(2,num) :
        if num % i == 0 : return False
    return True


def selectNum(numbers, criteria, primes):
    if not numbers:  # 재귀함수 탈출 조건
        return primes
    for i in range(len(numbers)):
        str_num = criteria + numbers[i]  # 숫자 이어붙임
        int_num = int(str_num)

        if isPrime(int_num):  # 소수인지 확인
            primes.append(int_num)
        primes = selectNum(numbers[:i] + numbers[i+1:], str_num, primes)
    return primes

def solution(numbers):
    nums = list(numbers)  # 문자열을 리스트로 변환
    primes = []
    primes = selectNum(nums, '', primes)
    return len(set(primes))



# 예시 테스트

print(solution("011"))  # 출력: 2
# 2, 11, 211, 

