from collections import defaultdict
import math

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for s, d in zip([str1, str2], [d1, d2]):
        for i in range(len(s)-1):
            if s[i:i+2].isalpha():
                d[s[i:i+2]]+=1
    # 교집합
    intersec = 0
    for d1_key in list(d1.keys()):
        if d2[d1_key]:
            intersec += min(d1[d1_key], d2[d1_key])
    # 합집합
    union = 0
    keys = list(set(d1.keys())|set(d2.keys()))
    for key in keys:
        union += max(d1[key], d2[key])
    return math.floor(intersec / union * 65536) if union!=0 else 65536

# str1	str2	answer
# FRANCE	french	16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	43690
# E=M*C^2	e=m*c^2	65536

test_1 = ['FRANCE', 'handshake', 'aa1+aa2', 'E=M*C^2']
test_2 = ['french', 'shake hands', 'AAAA12', 'e=m*c^2']

for t1, t2 in zip(test_1, test_2):
    print(solution(t1, t2))