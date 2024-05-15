# def bfs(tickets)  :
#     used = [False]*len(tickets) 
#     routes = ['ICN']
#     next_airport = routes[-1]

#     while next_airport != '' :
#         current_airport = next_airport
#         candidate = []
#         for n, ticket in enumerate(tickets) : 
#             if not used[n] and current_airport == ticket[0] : # FROM == TO
#                 candidate.append((n, ticket[1])) # 연결된 루트 후보
        
#         next_airport = ''  
        
#         if candidate :
#             n_to = pickFirstInABCOrder(candidate)
#             used[n_to[0]] = True
#             next_airport = n_to[1]
#             routes.append(next_airport)
        
#         print(routes, used) 
#     return routes
    
        
# def pickFirstInABCOrder(candidate) :
#     candidate.sort(key=lambda x : x[1])
#     return candidate[0]

# def solution(tickets) :
#     return bfs(tickets)

from collections import defaultdict

def solution(tickets):
    
    routes = defaultdict(list)
    
    for start, end in tickets:
        routes[start].append(end)
        
    for start in routes:
        routes[start].sort()
        
    stack = ['ICN']
    path = []
    
    while stack:
        top = stack[-1]
        
        if routes[top]:
            stack.append(routes[top].pop(0))
        else:
            path.append(stack.pop())
            
    return path[::-1]

tickets =  [["ICN", "D"], ["D", "ICN"], ["ICN", "B"]]

print(solution(tickets))
