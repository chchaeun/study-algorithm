N = int(input())

count = [[0, 0] for _ in range(N)]
count[0] = [0, 1]

for i in range(1, N):
    count[i] = [count[i-1][0] + count[i-1][1], count[i-1][0]]

print(sum(count[N-1]))