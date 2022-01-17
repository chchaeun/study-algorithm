def solution(p):
    # p가 없으면 빈 문자열 리턴
    if not p:
        return ""
    # u, v 나누기
    u, v = divide(p)
    
    # u가 올바른 문자열이면 u는 그대로 리턴
    if isCorrect(u):
        return u+solution(v)
    # 아니면 괄호 사이에 u를 뒤집어서 리턴
    else:
        answer = '('
        answer+=solution(v)
        answer+=')'
        for i in u[1:-1]:
            if i=='(':
                answer+=')'
            else:
                answer+='('
        return answer
        
def divide(s):
    left = right = 0
    for i in range(len(s)):
        if s[i]=='(':
            left +=1
        elif s[i]==')':
            right+=1
        if left==right:
            return s[:i+1], s[i+1:]

def isCorrect(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

test_p = ["(()())()", ")(", "()))((()"]

for t in test_p:
    print(solution(t))