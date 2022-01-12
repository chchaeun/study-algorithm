import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [[0, 0]]+[list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = wv[i][0], wv[i][1]
        if j<w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
            # 이 물건을 넣을지 말지
            # 이 물건을 넣은 경우 가치 vs 이 물건을 넣기 위해 이 물건의 무게만큼 뺀 만큼의 가치
            # 이 물건의 무게만큼만 뺄 수 있는 이유는 
            # 그 무게에서 배낭이 가지는 최대의 가치가 들어있기 때문
            # https://hongcoding.tistory.com/50
        
print(d[n][k])