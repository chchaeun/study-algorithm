HEIGHT = 10

bowls = input()
answer = HEIGHT

for i in range(1, len(bowls)):
    if bowls[i-1] == bowls[i]:
        answer += HEIGHT // 2
    else:
        answer += HEIGHT

print(answer)