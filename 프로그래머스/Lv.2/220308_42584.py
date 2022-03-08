def solution(prices):
    n = len(prices)
    answer = [i for i in range(n-1, -1, -1)]
    prices_idx = []
    for i in range(n):
        prices_idx.append((prices[i], i))
        
    stack = []
    top = -1
    for i in range(n):
        if not stack or stack[top]<=prices_idx[i]:
            stack.append(prices_idx[i])
            top += 1
        else:
            while stack and stack[top]>prices_idx[i]:
                answer[stack[top][1]] = i-stack[top][1]
                stack.pop()
                top -= 1
            stack.append(prices_idx[i])
            top+=1
    return answer
print(solution([1, 2, 3, 2, 3, 1, 2]))