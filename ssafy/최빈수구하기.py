from collections import Counter

t = int(input())

for _ in range(t):
    case = int(input())
    numbers = list(map(int, input().split()))
    common = Counter(numbers).most_common()
    common.sort(key=lambda x: (-x[1], -x[0]))
    print("#{} {}".format(case, common[0][0]))