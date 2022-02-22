def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        temp = citations[i] if citations[i]<=len(citations)-i else len(citations)-i
        answer=max(answer, temp)
    return answer

print(solution([0, 1, 4, 4, 4]))