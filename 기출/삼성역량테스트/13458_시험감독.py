N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in A:
    numofa = i
    numofa -= B

    if numofa < 0:
        answer += 1
        continue

    if numofa % C == 0:
        answer += numofa // C + 1
        continue

    answer += numofa // C + 2

print(answer)