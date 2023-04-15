def solution(topping):
    answer = 0
    c_topping = [0 for _ in range(10001)]
    c_topping[topping[0]] = 1
    c_count = 1

    d_topping = [0 for _ in range(10001)]
    d_count = 0

    for i in range(1, len(topping)):
        if d_topping[topping[i]] == 0:
            d_count += 1
        d_topping[topping[i]] += 1

    if c_count == d_count:
        answer += 1

    for i in range(1, len(topping)-1):
        if c_topping[topping[i]] == 0:
            c_count += 1
        c_topping[topping[i]] += 1
        d_topping[topping[i]] -= 1
        if d_topping[topping[i]] == 0:
            d_count -= 1

        if c_count == d_count:
            answer += 1

    return answer

print(solution([1,2,1,3,1,4,1,2]))
print(solution([1,2,3,1,4]))