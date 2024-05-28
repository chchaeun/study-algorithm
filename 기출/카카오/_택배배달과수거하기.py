def solution(cap, n, deliveries, pickups):
    answer = 0

    remaining_deliveries = 0
    remaining_pickups = 0

    for i in range(n, 0, -1):
        remaining_deliveries += deliveries[i-1]
        remaining_pickups += pickups[i-1]

        while remaining_deliveries > 0 or remaining_pickups > 0:
            remaining_deliveries -= cap
            remaining_pickups -= cap

            answer += i * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))