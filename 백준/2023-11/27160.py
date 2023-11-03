N = int(input())

cards = dict()

for _ in range(N):
    fruit, num_of_fruits = input().split()
    num_of_fruits = int(num_of_fruits)
    if fruit in cards:
        cards[fruit] += num_of_fruits
    else:
        cards[fruit] = num_of_fruits

if 5 in cards.values():
    print("YES")
else:
    print("NO")
