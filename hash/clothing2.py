def solution(clothes):
    clothes_map ={}
    
    for cloth in clothes : 
        if cloth[1] in clothes_map :
            clothes_map[cloth[1]]+=1
        else :
            clothes_map[cloth[1]]=1
            
    answer = 1
    
    for key, val in clothes_map.items() :
        answer*=(val+1)
        
    return answer-1
    

cloth = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
cloth1= [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(cloth))
print(solution(cloth1))
