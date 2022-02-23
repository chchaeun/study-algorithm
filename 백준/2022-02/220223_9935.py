import sys; input=sys.stdin.readline
s = list(input().strip())
b = input().strip()

def bomb(s):
    stack=[]
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack)>=len(b) and ''.join(stack[len(stack)-len(b):])==b:
            for _ in range(len(b)):
                stack.pop()
    return stack

while True:
    new_s = bomb(s)
    if len(new_s)==len(s): break
    s=new_s
    
print(''.join(s) if s else "FRULA")