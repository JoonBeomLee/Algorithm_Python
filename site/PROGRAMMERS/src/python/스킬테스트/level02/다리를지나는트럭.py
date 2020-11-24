def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    seconds = 0
    
    while True:
        # 기다리는 트럭이 없을경우 종료
        if not truck_weights: break
            
        # 1초뒤 지나갈 트럭이기에 1초뒤부터 합산하여 비교
        if sum(bridge[1:]) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:    
        # 앞에 0인 값들 한개 빼고 모두 제거 
            while bridge[1] == 0:
                bridge.pop(0)
                bridge.append(0)
                answer += 1
            bridge.append(0)

        answer += 1
        bridge.pop(0)


    # 남아있는 트럭에 대해 계산 
    answer += len(bridge)            
    return answer