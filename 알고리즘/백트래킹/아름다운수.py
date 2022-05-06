n = int(input())
answer = 0
num = []
def choose(count, beautiful):
    global answer
    if n == count:
        if len(num)==n:
            answer += 1
        return
    for i in range(1, 5):
        if i>n: break
        if not num or num[-1]==i and beautiful%num[-1]!=0:
            num.append(i)
            choose(count+1, beautiful+1)
            num.pop()
        elif beautiful % num[-1]==0 and n-len(num)>=i:
            num.append(i)
            choose(count+1, 1)
            num.pop()
choose(0, 0)
print(answer)