from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    ddict = defaultdict(int)

    for i in range(10):
        ddict[discount[i]] += 1

    start, end = 0, 10
    while end <= len(discount):
        for i, w in enumerate(want):
            if ddict[w] < number[i]:
                break
        else:
            answer += 1
        ddict[discount[start]] -= 1
        if end < len(discount):
            ddict[discount[end]] += 1
        start, end = start + 1, end + 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))