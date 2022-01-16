def solution(s):
    answer = -1
    stack = []
    
    for i in range(0, len(s)):
        if not stack:
            stack.append(s[i])
            continue
        if stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if stack:
        answer = 0
    else:
        answer = 1
    
    return answer

for t in ['baabaa', 'cdcd']:
    print(solution(t))