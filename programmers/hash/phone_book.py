# def solution(phone_book) :
#     # sort()가 필요한 이유
#     # 1. 문자열의 길이가 다르기 때문에 현재 string과 나머지 스트링을 슬라이싱해서 비교할 때 에러가 날 수 있음
#     # ex ) 현재 string의 길이가 5이고, 비교 대상이 3일때 3의 길이를 가진 스트링을 5까지 슬라이싱할 수 없음.
#     # 2. 정렬되지 않은 경우 현재 문자열을 대상으로 모든 문자열을 계속 비교해서 이중 for 문 -> O(n)  
#     phone_book.sort() # 오름차순 정렬
    
#     length = len(phone_book)

#     for current in range(length-1) :
#         # 정렬했기 때문에 이전에 비교한 문자열과 같은 것이 없다면, 이전 문자열은 앞으로 비교할 필요가 없음.
#         if phone_book[current] == phone_book[current+1][0:len(phone_book[current])] :
#             return False 

#     return  True




def solution(phone_book):

    for phone in phone_book:
        prefix = ""
        for number in phone:
            prefix += number
            if prefix in phone_book and prefix != phone:
                return False        
    return True



phone_book = ["119", "97674223", "1195524421"];

phone_book1 = ["123","456","789"];

phone_book2 = ["12","123","1235","567","88"]

print(solution(phone_book))

print(solution(phone_book1))

print(solution(phone_book2))

