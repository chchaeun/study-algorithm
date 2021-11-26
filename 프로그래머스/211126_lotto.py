# 문제 
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    zero=0
    count=0
    j=0
    for i in range(6):
        if lottos[i]==0:
            zero+=1
        else:
            while j<6:
                if lottos[i]==win_nums[j]:
                    count+=1
                    break
                elif lottos[i]<win_nums[j]:
                    break
                j+=1
    answer.append(7-count-zero)
    answer.append(7-count)
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))
