def solution(cap, n, deliveries, pickups):
    answer = 0

    range_check = n-1
    d_sum = sum(deliveries)
    p_sum = sum(pickups)
    while d_sum > 0 and p_sum > 0:
        d_truck, p_truck = cap, cap
        distance = 0
        for i in range(range_check, -1, -1):
            if deliveries[i] and d_truck > 0:
                if deliveries[i] > d_truck:
                    deliveries[i] -= d_truck           
                    d_sum -= d_truck
                    d_truck = 0
                else:
                    d_truck -= deliveries[i]
                    d_sum -= deliveries[i]
                    deliveries[i]= 0

                distance = max(distance, i + 1)

            if pickups[i] and p_truck > 0:
                if pickups[i] > p_truck:
                    pickups[i] -= p_truck     
                    p_sum -= p_truck      
                    p_truck = 0
                else:
                    p_truck -= pickups[i]
                    p_sum -= pickups[i]
                    pickups[i]= 0
                distance = max(distance, i + 1)

            range_check = distance - 1

            if not d_truck and not p_truck:
                break
        answer += distance * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))