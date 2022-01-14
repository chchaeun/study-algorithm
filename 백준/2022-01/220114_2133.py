# 2일 땐 경우가 3개이고, 2씩 늘어날 때마다 새로운 패턴이 2개씩 늘어난다(상하 대칭).
# d[n]에는 경우의 수가 들어있다. 
# 예를 들어 n=6이라고 하면,
# d[6] = d[4]의 경우에 n=2의 경우를 붙인다 (d[4] * 3)
#      + d[2]의 경우에 n=4의 경우를 붙인다 (d[6] * 2)
#      + d[0]의 경우에 n=6에서 추가되는 경우를 붙인다 (d[0] * 2)

def solution(n):
    d[0], d[2] = 1, 3
    for i in range(4, n+1, 2):
        for j in range(2, i+1, 2):
            if j == 2:
                d[i]+= d[i-j]*3
            else:
                d[i]+= d[i-j]*2

n = int(input())
d = [0 for _ in range(n+1)]

if n % 2 == 0:
    solution(n)
    
print(d[n])