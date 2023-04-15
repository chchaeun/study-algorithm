def solution(order):
    answer = 0
    stack = []
    index = 0
    for i in range(1, len(order)+1):
        if stack and stack[-1] == order[index]:
            stack.pop()
            answer += 1
            index += 1
            
        if i == order[index]:
            answer += 1
            index += 1
        else:
            stack.append(i)
    
    while stack and index < len(order):
        if stack[-1] == order[index]:
            stack.pop()
            answer += 1
            index += 1
        else:
            break
        
    return answer

print(solution([4,3,1,2,5]))
print(solution([5,4,3,2,1]))
print(solution([3,5,4,2,1]))
print(solution([1,2,4,3,5]))