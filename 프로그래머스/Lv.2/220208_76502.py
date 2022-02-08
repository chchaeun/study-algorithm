def solution(s):
    answer =0 
    for i in range(len(s)):
        new_s = s[i:len(s)]+s[0:i]
        if check(new_s):
            answer +=1
    return answer

def check(s):
    left = ['[', '{', '(']
    right = [']', '}', ')']
    stack = []
    for i in s:
        if not stack:
            if i in left:
                stack.append(i)
            else: return False
        elif i in right:
            if right.index(i)==left.index(stack[-1]):
                stack.pop()
            else:
                return False
        elif i in left:
            if stack[-1] in left:
                stack.append(i)
            else:
                return False
    if not stack:
        return True
    else:
        return False
    
print(solution("}}}"))