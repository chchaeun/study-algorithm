t = int(input())

for case in range(1, t + 1):
    n = int(input())
    board = [list(input().split()) for _ in range(n)]
    results = []

    for _ in range(3):
        board = list(zip(*board[::-1]))
        results.append(board)

    print("#{}".format(case))
    for i in range(n):
        for result in results:
            print("".join(result[i]), end=" ")
        print()