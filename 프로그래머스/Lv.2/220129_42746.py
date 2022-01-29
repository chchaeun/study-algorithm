def solution(numbers):
    numbers.sort(key=lambda n: str(n)*3, reverse=True)
    return str(int(''.join(list(map(str, numbers)))))

print(solution([0, 0, 0]))