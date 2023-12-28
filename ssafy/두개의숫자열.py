t = int(input())

for case in range(1, t + 1):
    n, m = map(int, input().split())
    temp1 = list(map(int, input().split()))
    temp2 = list(map(int, input().split()))

    if n < m:
        small = temp1
        large = temp2
    else:
        small = temp2 
        large = temp1
    
    answer = 0

    for i in range(len(large)):
        _sum = 0
        for j in range(len(small)):
            if i + j < len(large):
                _sum += large[i + j] * small[j]
            else:
                break
            if j == len(small)-1:
                answer = max(answer, _sum)
    print("#{} {}".format(case, answer))