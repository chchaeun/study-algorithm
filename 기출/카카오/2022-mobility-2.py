from collections import defaultdict

def solution(id_list, k):
    coupon = defaultdict(int)
    for ids in id_list:
        for id in set(ids.split()):
            if coupon[id] < k:
                coupon[id] += 1

    answer = sum(coupon.values())

    return answer

print(solution(["A B C D", "A D", "A B D", "B D"],2))
print(solution(['jay', 'jay elle jay may', 'may elle may', 'elle may', 'elle elle elle', 'may'],3))