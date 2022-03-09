from math import ceil

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for i in range(len(people)):
        if len(people)-1<i: break
        if people[i]<=limit//2:
            answer+=ceil((len(people)-i)/2)
            break
        if people[i]+people[-1]<=limit:
            people.pop()
        answer+=1
        
    return answer
    
print(solution([80, 20], 100))