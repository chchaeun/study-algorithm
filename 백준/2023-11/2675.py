T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for str in S:
        print(str * R, end="")
    print()