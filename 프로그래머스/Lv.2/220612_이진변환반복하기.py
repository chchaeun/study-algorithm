from collections import Counter

def solution(s):
    answer = 0
    count = 0
    while s != '1':
        zero = Counter(s)['0']
        answer += zero
        s = bin(len(s)-zero)[2:]
        count += 1
    return [count, answer]


print(solution('110010101001'))
print(solution("01110"))
print(solution("1111111"))
