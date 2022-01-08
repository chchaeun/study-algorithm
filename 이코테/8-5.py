
x = int(input())

# Top-down (재귀)
c = [x]*(x+1)
def f(n, count):
    c[n] = count
    if n==1:
        return
    for i in [3, 2]:
        if n % i == 0 and c[n//i] > count+1:
            f(n//i, count+1)
    if c[n-i] > count+1:       
        f(n-1, count+1)

f(x, 0)
print(c[1])

# Bottom-up (반복)

# c = [0] * (x+1)
# # 1부터 시작해서 +1, *2, *3, *5를 하면서 x까지 가는 최소 경로 찾기
# for i in range(2, x+1):
#     c[i] = c[i-1] + 1
#     for j in [2, 3]:
#         if i%j==0:
#             c[i] = min(c[i], c[i//j]+1)
            
# print(c[x])