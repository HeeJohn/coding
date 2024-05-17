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





# def dfs(tickets, flag):
    
#     if not flag['c'] or flag['done']: #
#         flag['done'] = True
#         return flag
    
#     for n, ticket in enumerate(tickets):
#         if not flag['used'][n] and flag['routes'][-1] == ticket[0]:
#             flag['used'][n] = True
#             flag['c'] -= 1
#             flag['routes'].append(ticket[1])
            
#             flag = dfs(tickets, flag)
#             if flag['done']: #경로 찾았음 모든 재귀 탈출
#                 return flag
            
#             #원상복구
#             flag['c'] += 1
#             flag['used'][n] = False
#             flag['routes'].pop()
		
#     return flag

# def solution(tickets):
#     tickets.sort()
#     flag = {'routes': ['ICN'], 'used': [False] * len(tickets), 'c': len(tickets), 'done': False}

#     return dfs(tickets, flag)['routes']




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
