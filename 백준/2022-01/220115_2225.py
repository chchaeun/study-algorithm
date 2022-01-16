n, k = map(int, input().split())
mod = 1000000000
d = [0 for _ in range(n+1)]
d[0] = 1
for i in range(1, k+1):
    for j in range(1, n+1):
        d[j] = d[j]+d[j-1]

print(d[n]%mod)

# n=2, k=3이라고 하면
# n=1, k=3인 경우 (0, 0, 1) (0, 1, 0) (1, 0, 0)에서 
#                 (0, 0, 2) (2, 0, 0), (0, 2, 0)을 만들고
# n=2, k=2인 경우 (0, 2) (2, 0) (1, 1)에서
#                 (0, 1, 1) (1, 1, 0) (1, 0, 1)을 만든다