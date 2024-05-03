# 여분이 있는 학생들 중 옷 도난 당한 사람은 
# 다른사람 못 빌려주지만, 자기는 체육 참여 가능
# 도난 문제(p_solved)에 해당되지 않는 것으로 제거

def removeIntersection(lost, reserve) : 
    return set(lost) - set(reserve), set(reserve) - set(lost)

def borrowFrom(lost_stu, t_reserve) :
    if lost_stu-1 in t_reserve:
        return lost_stu-1
    elif lost_stu+1 in t_reserve:
        return lost_stu+1
    return 0


def solution(n, lost, reserve):
    t_lost, t_reserve = removeIntersection(lost,reserve)
    p_solved = 0
    for lost_stu in t_lost:
        stu = borrowFrom(lost_stu, t_reserve)
        if stu != 0 : # 0이라는 학생은 없음. 즉 빌릴 수 없는 상태
            t_reserve.remove(stu) #stu가 lost_stu에게 빌려주면, 체육복 리스트에서 제거.
            p_solved+=1 #문제해결
        
    return n - (len(t_lost) - p_solved ) #체육복 못 받은 사람들은 참가 못함. 