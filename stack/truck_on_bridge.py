# Description
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	[]	[]	[7,4,5,6]
# 1~2	[]	[7]	[4,5,6]
# 3	[7]	[4]	[5,6]
# 4	[7]	[4,5]	[6]
# 5	[7,4]	[5]	[6]
# 6~7	[7,4,5]	[6]	[]
# 8	[7,4,5,6]	[]	[]
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.
# 입출력 예
# bridge_length	weight	truck_weights	return
# 2	10	[7,4,5,6]	8
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110
# 출처 : programmars

# 경우의 수 

# 1. 트럭이 꽉 찼는데, 무게는 안 찬 경우     [트럭의 흐름 ==> 트럭이 하나 빠지고, 들어갈 트럭의 무게가 괜찮으면 하나 들어감]
# 2. 트럭은 꽉 차지 않았는데, 무게는 찬 경우 [트럭의 흐름 ==> 트럭이 내부에서 한칸 전진]
# 3. 트럭도 무게도 꽉 찬 경우    [트럭의 흐름 ==> 트럭이 하나 빠지고, 들어갈 트럭의 무게가 괜찮으면 들어감.]
# 4. 트럭도 무게도 괜찮은 경우 [ 트럭의 흐름 ==> 트럭이 내부에서 전진하고, 들어갈 트럭의 무게가 괜찮으면 들어감 ]
def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    second =0
    current_weight = 0
    while truck_weights :
        second +=1

        if bridge[0]!=0 :
            current_weight -= bridge[0]
        bridge.pop(0)
        bridge.append(0)
        incomming = truck_weights[0]

        if current_weight + incomming <= weight :
            bridge [-1] = truck_weights.pop(0)
            current_weight +=incomming
   
    return second + bridge_length


#test case 1
bridge_length1 =2
weight1 =10
truck_weights1 =[7,4,5,6]

print(solution(bridge_length1,weight1,truck_weights1))

#test case 2
bridge_length2 =100
weight2 =100
truck_weights2 =[10]	

print(solution(bridge_length2,weight2,truck_weights2))
#test case 3
bridge_length3 =100
weight3 =100
truck_weights3 =[10,10,10,10,10,10,10,10,10,10]	

print(solution(bridge_length3,weight3,truck_weights3))


