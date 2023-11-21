T = int(input())

for _ in range(T):
    N = int(input())
    max_univ, max_amount = '', 0

    for _ in range(N):
        university, amount = input().split()
        amount = int(amount)

        if max_amount < amount:
            max_univ = university
            max_amount = amount

    print(max_univ)