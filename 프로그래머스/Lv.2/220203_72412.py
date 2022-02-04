# 경우가 제한적이기 때문에 모든 경우의 수를 딕셔너리에 저장했음
# 효율성을 위해 몇 점 이상의 점수를 탐색할 땐 이분탐색 진행
from bisect import bisect_left
from collections import defaultdict 

def solution(info, query):
    global scores
    scores = defaultdict(list)
    answer = []
    
    for i in info:
        isplit = i.split()
        saveInfo(isplit, "", 0)    
    
    for key in scores.keys():
        scores[key].sort()
        
    for q in query:
        qsplit = q.split()
        qscore = int(qsplit[-1])
        qkey = ''.join(qsplit[:-1:2])
        answer.append(len(scores[qkey]) - bisect_left(scores[qkey], qscore))
    
    return answer
 
def saveInfo(isplit, case, idx):
    global scores
    if idx==4:
        scores[case].append(int(isplit[4]))
        return
    saveInfo(isplit, case+isplit[idx], idx+1)
    saveInfo(isplit, case+'-', idx+1)
    

print(solution([
                "java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"
                ],
               [
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"
                ]
               ))