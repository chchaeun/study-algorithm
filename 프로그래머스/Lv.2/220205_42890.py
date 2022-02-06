from collections import defaultdict
from itertools import combinations
def solution(relation):
    idxs = [str(i) for i in range(len(relation[0]))]
    answer = []
    for i in range(1, len(idxs)+1):
        keys = list(map(''.join, list(combinations(idxs, i))))
        for key in keys:
            if not isFind(key, answer): 
                continue
            dict = makeDict(relation, key)
            if len(dict)==len(relation):
                answer.append(key)
                
    return len(answer)

def isFind(key, answer):
    # 연속되지 않은 숫자들을 키로 가지고 있을 경우 확인을 위해
    # set을 사용해서 걸러주었음
    # (Ex. 이미 존재하는 키가 03 이고 확인하려는 키가 013일 때)
    for a in answer:
        if len(set(key) & set(a)) == len(a):
            return False
    return True

def makeDict(relation, key):
    dict = defaultdict(int)
    for row in range(len(relation)):
        dkey=''
        for j in list(key):
            dkey+=relation[row][int(j)]
        dict[dkey]+=1
    return dict

test_r = [["100","ryan","music","2"],
          ["200","apeach","math","2"],
          ["300","tube","computer","3"],
          ["400","con","computer","4"],
          ["500","muzi","music","3"],
          ["600","apeach","music","2"]
          ]
print(solution(test_r))