import math

def solution(k, d):
    answer = 0

    x = 0
    x_square, d_square = x * x, d * d
    while x_square <= d_square:
        answer += int(math.sqrt(d_square - x_square) // k) + 1
        x += k
        x_square = x * x

    return answer

print(solution(2, 4))
print(solution(1, 5))