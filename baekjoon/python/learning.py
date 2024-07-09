# 모든 단어는 anta * tica 로 이루어짐
# k개의 글자밖에 못 가르침. 
# 입력이 N과 K로 주어질 때, 최대 읽을 수 있는 단어의 개수를 구해야 함.
# anta * tica => antic (5) 글자
# 기본적으로 하나라도 읽으려면 5글자는 필수임
# k가 5보다 작으면, 0

# 입력 1 분석
# antarctica
# antahellotica
# antacartica


#설계
#k가 5보다 작으면, 0
#k가 5보다 크면, k - 5개를 추가로 배울 수 있음.
#앞 뒤 anta * tica를 자르고, * 를 set으로 만듬. (중복되는 알파벳 제거)
#set의 크기가 k-5랑 같거나 작으면, 고려 대상임.
#고려해야 될 대상 중에서 읽을 있는 단어의 개수를 늘리려면, 
#공통으로 포함되는 알파벳 위주로 배워야 함.

import sys


def solution() : 
	fix = set({'a','n','t','i','c'})
	_input = list(map(int, sys.stdin.readline().split()))
	N, K  = _input[0], _input[1]
	K-=5
	
	
	if K < 0:
	    print(0)
	    return
	
	
	words =[]
	for _ in range(N) :
		words.append(set(sys.stdin.readline().strip()[4 : -4]))
	
	
	p_words = []
	common = set({})
	for word in words :
	    diff = word - fix
	    if len(diff) <= K :
	        p_words.append(diff)
	        common.update(diff)
	

def makeComb(source, k) :
    
    combination = []
    
    for i in range(len(source)) :
        
        
        
solution()	
	
	
