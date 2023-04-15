from typing import Final

def solution(cost, x):
    n = len(cost)
    paint = [[0 for _ in range(x+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        paint_index = i-1
        for j in range(x+1):
            if cost[paint_index] <= j:
                max_value = max(getValue(paint_index) + paint[i-1][j-cost[paint_index]], paint[i-1][j])
                paint[i][j] = modular(max_value)
            else:
                paint[i][j] = modular(paint[i-1][j])

    return modular(paint[n][x])

def getValue(index):
    return 2**index

def modular(dividend):
    DIVISOR: Final = 10**9 + 7

    return dividend % DIVISOR

print(solution([10, 20, 14, 40, 50], 70))
print(solution([3, 4, 1], 8))
print(solution([19, 78, 27, 18, 20], 25))