def solve(n, k, order):
    multitap = []
    unplugs = 0
    
    for i in range(k):
        if order[i] in multitap:
            continue
        if len(multitap) < n:
            multitap.append(order[i])
        else:
            # 가장 나중에 사용할 기기를 찾기
            max_future_index = -1
            device_to_unplug = -1
            
            for device in multitap:
                if device not in order[i:]:
                    device_to_unplug = device
                    break
                else:
                    future_index = order[i:].index(device)
                    if future_index > max_future_index:
                        max_future_index = future_index
                        device_to_unplug = device
            
            multitap.remove(device_to_unplug)
            multitap.append(order[i])
            unplugs += 1
    
    return unplugs

# 입력 처리
n, k = map(int, input().split())
order = list(map(int, input().split()))

# 결과 출력
print(solve(n, k, order))
