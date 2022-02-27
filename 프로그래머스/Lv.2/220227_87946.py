from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for case in permutations(dungeons, len(dungeons)):
        count=0
        temp = k
        for c in case: 
            if temp>=c[0]:
                temp-=c[1]
                count+=1
            else:
                break
        answer = max(answer, count)
    return answer
            
            
print(solution(80,[[80,20],[50,40],[30,10]]))