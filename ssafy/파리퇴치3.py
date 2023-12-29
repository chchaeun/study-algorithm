T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    answer = 0
    board = [list(map(int, input().split())) for _ in range(N)]

    plus = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    multiply = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N

    for i in range(N):
        for j in range(N):
            plus_sum = board[i][j]
            multiply_sum = board[i][j]

            for k in range(4):
                pdy, pdx = plus[k]
                mdy, mdx = multiply[k]
                for l in range(1, M):
                    py, px = i + pdy * l, j + pdx * l
                    if in_range(py, px):
                        plus_sum += board[py][px]

                    my, mx = i + mdy * l, j + mdx * l
                    if in_range(my, mx):
                        multiply_sum += board[my][mx]

            answer = max(answer, plus_sum, multiply_sum)

    print("#{} {}".format(case, answer))
