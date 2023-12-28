t = int(input())

for i in range(t):
    print("#{}".format(i+1), end=" ")
    print(sum(list(map(lambda x: 0 if x % 2 == 0 else x, list(map(int, input().split()))))))