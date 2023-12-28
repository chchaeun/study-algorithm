t = int(input())
for i in range(t):
    print("#{} {}".format(i+1, max(list(map(int, input().split())))))