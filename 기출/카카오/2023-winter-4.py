from collections import deque

def solution(coin, cards):
    answer = 1

    N = len(cards)
    dq = deque(cards[N // 3:])
    
    current = sorted(cards[:N // 3])

    removed = []
    
    while dq:
        removed.extend([dq.popleft() for _ in range(2)])

        if comb_cards(N, current):
            answer += 1
        elif coin >= 1 and comb_current_removed(N, current, removed):
            answer += 1
            coin -= 1
        elif coin >= 2 and comb_cards(N, removed):
            answer += 1
            coin -= 2
        else:
            break

    return answer

def comb_cards(N, numbers):
    length = len(numbers)
    
    if length < 2:
        return False

    for i in range(length - 1):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == N+1:
                numbers.pop(j)
                numbers.pop(i)
                return True

    return False

def comb_current_removed(N, current, removed):
    c_length = len(current)
    d_length = len(removed)

    for i in range(c_length):
        for j in range(d_length):
            if current[i] + removed[j] == N+1:
                current.pop(i)
                removed.pop(j)
                return True

    return False


print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))  # 5
print(solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))  # 2
print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))  # 4
print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))  # 1
