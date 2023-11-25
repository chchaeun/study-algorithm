def solution(n, tops):
    DIVISOR = 10007
    memo = [0 for _ in range(2 * n + 1)]

    memo[0] = 1
    memo[1] = 3 if tops[0] == 1 else 2
    
    for i in range(2, 2 * n + 1):
        if i % 2 == 1:
            if tops[i//2] == 1:
                memo[i] = (memo[i - 1] * 2 + memo[i - 2]) % DIVISOR
            else:
                memo[i] = (memo[i - 1] + memo[i - 2]) % DIVISOR
        else:
            memo[i] = (memo[i - 1] + memo[i - 2]) % DIVISOR

    return memo[2 * n]

print(solution(4, [1, 1, 0, 1]))