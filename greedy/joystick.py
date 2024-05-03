"""Description
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
"JEROEN"	56
"JAN"	23"""


# 'A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z'
# '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'


def takeMinUD(letter) :
    return min(abs(ord('A')-ord(letter)), abs(ord('Z')-ord(letter)+1))
# 01234
# 'ABAAC'

def inBound(index, length) :
    new = index % length
    
    if new >= 0 : return new
    return length + new 


def takeMinLR(letters, index) :
    mv = 1
    length = len(letters)
    
    while length != mv :
        newP = inBound(index+mv, length)
        newN = inBound(index-mv, length)
        if  letters[newP] != 'A' :
            return newP, mv
        if letters[newN] != 'A' :
            return newN, mv
        mv+=1
    
    return 0,0
        
def solution(name):
    letters = list(name)
    movement = 0 #첫번째 자리부터 시작
    index = 0
    
    while True :
        print(letters[index])
        movement+=takeMinUD(letters[index]) #up/down
        letters[index] = 'A' # 마킹
        index, mv = takeMinLR(letters, index) #left /right
        if mv == 0 : return movement
        movement += mv 
        