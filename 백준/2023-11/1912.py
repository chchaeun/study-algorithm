N = int(input())
numbers = list(map(int, input().split()))

change = [0 for _ in range(N)]
pin = [-int(1e9) for _ in range(N)]

change[0] = numbers[0]

for i in range(1, N):
    if numbers[i] < 0:
        pin[i] = max(change[i-1], pin[i-1])
    else:
        pin[i] = pin[i-1]

    change[i] = max(numbers[i], change[i-1] + numbers[i])

print(max(change[N-1], pin[N-1]))