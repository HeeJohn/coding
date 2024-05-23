def is_weekend(d) :
    if d == '일' or d == '토' :
        return True
    else :
        return False

def is_holiday(H, today) :
    if  today in H :
        return True
    else :
        return False

def is_normalday(H, today, X) :
    if not(is_weekend(X) or  is_holiday(H, today)) :
        return True
    else :
        return False

# def find_month(weight_of_months, i) :
#     month = len(weight_of_months) //2

#     while not (weight_of_months[month-1] < i <= weight_of_months[month]) :

#         if i > weight_of_months[month] :
            
#            month = (len(weight_of_months) + month) //2

#         elif i < weight_of_months[month] :
#             month = (0 + month) //2

#     return month


def find_alter(month, date, days, X, H, last_d_of_months) :
    found = False
    t = 0 
    
    if days[X] == '토' :
        while month > -1 and not found :
            for d in range(date, 0, -1) :
                if is_normalday(H, [month+1, d], days[X]) : #주말도 공휴일도 아님
                    found = True
                    t=1 #과거로 가기 때문에 추가 입력
                    H.append([month+1, d]) # 임시 공휴일 지정
                    break
                X = (X-1)%7
            month-=1
            date = last_d_of_months[month]

    else :
        
        while month < len(last_d_of_months) and not found : 
            for d in range(date, last_d_of_months[month] +1) :
                if is_normalday(H, [month+1, d], days[X]) : #주말도 공휴일도 아님
                    found = True
                    H.append([month+1, d]) # 공휴일 지정
                    break
                X = (X+1)%7
            month+=1
            date = 1

    
    return t, H
def find_alter_p(month, Y, days, X, H, last_d_of_months) :
    found = False
    left, right = 0, 0
    when =[0,0]
    t_x = X
    df = Y # 디폴트, 값을 찾지 못했을 때

    for d in range(Y, 0, -1) :
        if is_normalday(H, [month+1, d], days[t_x]) : #주말도 공휴일도 아님
            found = True
            when[0] = d
            break

        t_x = (t_x-1)%7
        left+=1

    t_x = X
    for d in range(Y, last_d_of_months[month] +1) :
        if is_normalday(H, [month+1, d], days[t_x]) : #주말도 공휴일도 아님
            found = True
            when[1] = d
            break

        right+=1
        t_x = (t_x+1)%7

    print(left, right, when)
    if found :
        if left > right :
            return when[1]
        elif left < right :
            return when[0]
        else :
            if days[X] == '토' :
                return when[0]
            else :
                return when[1]
    else :
        return df

def solution(X, H, Y):
    last_d_of_months =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # weight_of_months = find_weight_of_month(last_d_of_months)
    days = ['일', '월', '화', '수', '목', '금', '토']
    total_break = 0
    on_time = []
    X%= len(days)
    tx = X

    for month in range(len(last_d_of_months)) :
        for date in range(1, last_d_of_months[month]+1) :

            isHoliday = is_holiday(H, [month+1, date])
            isWeekend = is_weekend(days[tx])

            if isHoliday and isWeekend:
                t, H = find_alter(month, date, days, tx, H, last_d_of_months)
                total_break+=(1+t)
            
            elif isHoliday or isWeekend:
                total_break+=1

            else : # 아무날도 아닌 날은 월급을 받을 수 있음
                if date == Y :
                    on_time.append(month)

            tx = (tx+1)%len(days)

    print(H)
    pay_day = []
    tx = X
    for month in range(len(last_d_of_months)) :
        if month in on_time :
            pay_day.append(Y)
        else :
            pay_day.append(find_alter_p(month, Y, days, (tx+Y-1)%len(days), H, last_d_of_months))

        tx = (tx+last_d_of_months[month])%len(days)

    print(pay_day)

    return pay_day



########################################## 1
# def is_weekend(d) :
#     if d == '일' or d == '토' :
#         return True
#     else :
#         return False


# def solution(X):
#     last_d_of_months =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     # weight_of_months = find_weight_of_month(last_d_of_months)
#     days = ['일', '월', '화', '수', '목', '금', '토']
#     total_break = 0
#     on_time = []
#     X%= len(days)
#     tx = X

#     for month in range(len(last_d_of_months)) :
#         for date in range(1, last_d_of_months[month]+1) :
#             isWeekend = is_weekend(days[tx])
#             if isWeekend:
#                 total_break+=1

#             tx = (tx+1)%len(days)

#     return total_break




################################################2
# def is_weekend(d) :
#     if d == '일' or d == '토' :
#         return True
#     else :
#         return False

# def is_holiday(H, today) :
#     if  today in H :
#         return True
#     else :
#         return False


# def solution(X, H):
#     last_d_of_months =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     # weight_of_months = find_weight_of_month(last_d_of_months)
#     days = ['일', '월', '화', '수', '목', '금', '토']
#     total_break = 0
#     on_time = []
#     X%= len(days)
#     tx = X

#     for month in range(len(last_d_of_months)) :
#         for date in range(1, last_d_of_months[month]+1) :

#             isHoliday = is_holiday(H, [month+1, date])
#             isWeekend = is_weekend(days[tx])

#             if isHoliday:
#                 total_break+=(1)
            
#             elif isWeekend:
#                 total_break+=1
#             tx = (tx+1)%len(days)
        
#     return total_break


######################################################## 3차

# def find_alter(month, date, days, X, H, last_d_of_months) :
#     found = False
#     t = 0 
    
#     if days[X] == '토' :
#         while month > -1 and not found :
#             for d in range(date, 0, -1) :
#                 if is_normalday(H, [month+1, d], days[X]) : #주말도 공휴일도 아님
#                     found = True
#                     t=1 #과거로 가기 때문에 추가 입력
#                     H.append([month+1, d]) # 임시 공휴일 지정
#                     break
#                 X = (X-1)%7
#             month-=1
#             date = last_d_of_months[month]

#     else :
        
#         while month < len(last_d_of_months) and not found : 
#             for d in range(date, last_d_of_months[month] +1) :
#                 if is_normalday(H, [month+1, d], days[X]) : #주말도 공휴일도 아님
#                     found = True
#                     H.append([month+1, d]) # 공휴일 지정
#                     break
#                 X = (X+1)%7
#             month+=1
#             date = 1

    
#     return t, H

# def find_alter(month, date, days, X, H, last_d_of_months) :
#     found = False
#     t = 0 
    
#     if days[X] == '토' :
#         while month > -1 and not found :
#             for d in range(date, 0, -1) :
#                 if is_normalday(H, [month+1, d], days[X]) : #주말도 공휴일도 아님
#                     found = True
#                     t=1 #과거로 가기 때문에 추가 입력
#                     H.append([month+1, d]) # 임시 공휴일 지정
#                     break
#                 X = (X-1)%7
#             month-=1
#             date = last_d_of_months[month]

#     else :
        
#         while month < len(last_d_of_months) and not found : 
#             for d in range(date, last_d_of_months[month] +1) :
#                 if is_normalday(H, [month+1, d], days[X]) : #주말도 공휴일도 아님
#                     found = True
#                     H.append([month+1, d]) # 공휴일 지정
#                     break
#                 X = (X+1)%7
#             month+=1
#             date = 1

    
#     return t, H

# def solution(X, H):
#     last_d_of_months =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     # weight_of_months = find_weight_of_month(last_d_of_months)
#     days = ['일', '월', '화', '수', '목', '금', '토']
#     total_break = 0
#     on_time = []
#     X%= len(days)
#     tx = X

#     for month in range(len(last_d_of_months)) :
#         for date in range(1, last_d_of_months[month]+1) :

#             isHoliday = is_holiday(H, [month+1, date])
#             isWeekend = is_weekend(days[tx])

#             if isHoliday and isWeekend:
#                 t, H = find_alter(month, date, days, tx, H, last_d_of_months)
#                 total_break+=(1+t)
            
#             elif isHoliday or isWeekend:
#                 total_break+=1


#             tx = (tx+1)%len(days)

   
#     return total_break
