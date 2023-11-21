T = int(input())

for _ in range(T):
    N = int(input())
    max_amount, max_player = 0, ''

    for _ in range(N):
        amount, player = input().split()
        amount = int(amount)

        if max_amount < amount:
            max_player = player
            max_amount = amount

    print(max_player)