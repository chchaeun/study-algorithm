def solution(money, minratio, maxratio, ranksize, threshold, months):
    actual_money = money

    for _ in range(months):
        suppose_money = (actual_money // 100) * 100

        if suppose_money < threshold:
            ratio = 0
        else:
            ratio = minratio + (suppose_money - threshold) // ranksize

        if ratio > maxratio:
            ratio = maxratio

        charge = suppose_money * ratio / 100
        actual_money -= int(charge)

    return actual_money

solution(12345678, 10, 20, 250000, 10000000, 4)
print(solution(1000000000, 50, 99, 100000, 0, 6))
print(solution(123456789, 0, 0, 1, 0, 360))
print(solution(1000000000, 0, 100, 1, 0, 360))