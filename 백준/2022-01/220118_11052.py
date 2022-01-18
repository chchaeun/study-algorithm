import sys
input = sys.stdin.readline

n = int(input().strip())
price = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(1, i):
        price[i] = max(price[i], price[i-j]+price[j])
    
print(price[n])