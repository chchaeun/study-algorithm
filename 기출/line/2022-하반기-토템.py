from collections import deque
from typing import List

def fire(n: int, town: List[List[int]], x: int, y: int, minutes: int):
    x, y = x - 1, y - 1
    for i in range(x - minutes, x + minutes + 1):
        for j in range(y - minutes, y + minutes + 1):
            if 0 <= i < n and 0 <= j < n:
                town[i][j] += 1

    return town

def ice(n: int, town: List[List[int]], x: int, y: int, minutes: int):
    x, y = x - 1, y - 1

    for i in range(n):
        for j in range(n):
            if 0 <= abs(x-i) + abs(y-j) <= minutes:
                town[i][j] -= 1

    return town


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    town = [[0 for _ in range(n)] for _ in range(n)]

    for minutes in range(1, m+1):
        for x, y in fires:
            town = fire(n, town, x, y, minutes)
        for x, y in ices:
            town = ice(n, town, x, y, minutes)

    return town

print(solution(3, 2, [[1, 1]], [[3, 3]]))
print(solution(5, 3, [[5, 5], [1, 3], [5, 2]], [[1, 5], [3, 2]]))
