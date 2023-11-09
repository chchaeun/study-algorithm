N, K = map(int, input().split())

K = min(K, N-K)

parent = 1
child = 1
for i in range(K):
    parent *= N - i
    child *= K - i

print((parent // child) % 10007)