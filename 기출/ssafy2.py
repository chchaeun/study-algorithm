T = int(input())

for case in range(1, T + 1):
    N, P = map(int, input().split())

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    grow = [first, second]

    FOOD_1, FOOD_2 = 0, 1

    global answer
    answer = 0

    def search(plant, prev_food, total):
        if plant == N:
            global answer
            answer = max(answer, total)
            return

        for next_food in [FOOD_1, FOOD_2]:
            if prev_food == next_food:
                search(plant + 1, next_food, total + grow[next_food][plant] - P)
            else:
                search(plant + 1, next_food, total + grow[next_food][plant])

    search(0, -1, 0)

    print("#{} {}".format(case, answer))