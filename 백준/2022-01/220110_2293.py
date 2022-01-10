import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d = [0 for _ in range(k+1)]
d[0] = 1
for i in coin:
    for j in range(1, k+1):
        if j-i >= 0:
            d[j] += d[j-i]
print(d[k])

# 1. 전체의 문제를 부분 문제로 잘 나누었는가? 그렇다면 전체 문제를 해결하기 위한 부분 문제의 점화식은 무엇인가?
# 2. 부분 문제들을 해결하며 얻는 결과값을 메모이제이션하는가?
# 3. 부분 문제의 점화식은 부분 문제들 사이의 관계를 빠짐없이 고려하는가?
# 풀이: https://mong9data.tistory.com/68