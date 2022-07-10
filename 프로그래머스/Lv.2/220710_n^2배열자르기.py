import math
def solution(n, left, right):
    arr = [i for i in range(1, n+1)]
    lrow = math.ceil((left + 1) / n)
    rrow = math.ceil((right + 1) / n)

    answer = []

    for i in range(lrow, rrow+1):
        arr = [i]*i + arr[i:]
        answer.extend(arr)
    start = left % n
    end = len(answer) - (n - (right % n))
    return answer[start:end+1]

print(solution(4, 7, 14))