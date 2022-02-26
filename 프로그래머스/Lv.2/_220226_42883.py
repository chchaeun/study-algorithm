def solution(number, k):
    stack=[number[0]]
    for n in number[1:]:
        while stack and stack[-1]<n and k>0:
            k-=1
            stack.pop()
        stack.append(n)
    if k!=0:
        stack = stack[:-k]
    return ''.join(stack)
print(solution('987654321', 5))