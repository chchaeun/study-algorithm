import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0])
    result = 1
    best = arr[0][1]
    for i in range(1, n):
        if best>arr[i][1]:
            result+=1
            best = arr[i][1]
    print(result)

# 리스트를 따로 만들 필요없고, 
# 앞에 걸 기준으로 오름차순으로 정렬했으면 
# 뒤에 것의 best 순위를 업데이트하면서 비교하면 된다. 
# 어차피 앞에 건 정렬 돼있으니까 지나오면 그 뒤에 것만 보고 떨어뜨리면 됨