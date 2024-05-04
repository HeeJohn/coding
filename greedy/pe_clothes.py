# 여분이 있는 학생들 중 옷 도난 당한 사람은 
# 다른사람 못 빌려주지만, 자기는 체육 참여 가능
# 도난 문제(p_solved)에 해당되지 않는 것으로 제거

# def removeIntersection(lost, reserve) : 
#     return set(lost) - set(reserve), set(reserve) - set(lost)

# def borrowFrom(lost_stu, t_reserve) :
#     if lost_stu-1 in t_reserve:
#         return lost_stu-1
#     elif lost_stu+1 in t_reserve:
#         return lost_stu+1
#     return 0


# def solution(n, lost, reserve):
#     t_lost, t_reserve = removeIntersection(lost,reserve)
#     p_solved = 0
#     for lost_stu in t_lost:
#         stu = borrowFrom(lost_stu, t_reserve)
#         if stu != 0 : # 0이라는 학생은 없음. 즉 빌릴 수 없는 상태
#             t_reserve.remove(stu) #stu가 lost_stu에게 빌려주면, 체육복 리스트에서 제거.
#             p_solved+=1 #문제해결
        
#     return n - (len(t_lost) - p_solved ) #체육복 못 받은 사람들은 참가 못함. 



def solution(k, dungeons):
    n = len(dungeons)
    # n은 던전의 개수(현재 3)
    dp = [-1] * (1 << n)  # 모든 상태에 대해 dp 배열을 -1로 초기화
    # (1 << 3) -> 1000 총 8가지 경우 (4비트 2진수)
    # 000 아무데도 안 간 경우
    # 001 1번 던전만 간 경우
    # 101 3번, 1번 던전만 간 경우
    # 111 모든 던전을 간 경우
    # 000  ~ 111 총 7가지
    dp[0] = k  # 아무 던전도 방문하지 않은 초기 상태에서의 피로도
# dp[0] == 000, 체력이 80
    for mask in range(1 << n): # range(8)과 동일
        if dp[mask] == -1:
            continue  # 이 상태는 도달할 수 없는 상태
        for i in range(n): # n은 현재 3
            if mask & (1 << i) == 0 and dp[mask] >= dungeons[i][0]:
                # i번째 던전을 아직 방문하지 않았고, 방문 가능한 경우
                # 000 & (1 << 0) == 000 & 001 == 0이다
                # dp[000](80) >= dungeons[i][0] 최소 필요 피로도인 경우
                new_mask = mask | (1 << i) # mask를 현재 방문한 마스크로 변경
                new_energy = dp[mask] - dungeons[i][1] # 소모된 에너지로 변경
                if new_energy >= 0: # 에너지가 남아있다면
                    dp[new_mask] = max(dp[new_mask], new_energy)
                    # 이전에 저장된 값과 새로 갱신된 에너지 중 더 큰 값으로 저장
                    # 첫 번째 순회의 경우 -1에서 갱신
                    # dp 배열은 각 상태에 대한 최대 남은 피로도를 기록하는 것

    # 최대 방문 던전 수 계산
    max_dungeons = 0
    for mask in range(1 << n):
        if dp[mask] != -1:
            max_dungeons = max(max_dungeons, bin(mask).count('1'))
            # bin 메서드는 2진수를 Ob 접두어를 포함한 이진수 문자열로 반환하는 것

    return max_dungeons

print(solution(80, [[80,20],[50,40],[30,10]]	))