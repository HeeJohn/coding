import sys
import itertools

def solution():
    fix = set({'a', 'n', 't', 'i', 'c'})
    _input = list(map(int, sys.stdin.readline().split()))
    N, K = _input[0], _input[1]
    K -= len(fix)

    if K < 0:
        print(0)
        return

    words = []
    unique_chars = set()
    
    for _ in range(N):
        word = set(sys.stdin.readline().strip()[4:-4])
        words.append(word)
        unique_chars |= (word - fix)
    
    if len(unique_chars) <= K:
        print(N)
        return

    max_words = 0
    
    for comb in itertools.combinations(unique_chars, K):
        comb_set = set(comb)
        count = 0
        
        for word in words:
            if word - fix <= comb_set:
                count += 1
        max_words = max(max_words, count)

    print(max_words)

solution()
	