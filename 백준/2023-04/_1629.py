a, b, c = map(int, input().split())

def cal(a, b):
    if b==1:
        return a % c

    temp = cal(a, b//2)
    
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c

print(cal(a, b))