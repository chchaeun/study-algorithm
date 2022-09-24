def solution(queue1, queue2):
    
    queue = queue1 + queue2
    
    sum1, sum2 = sum(queue1), sum(queue2)
    length = len(queue)

    count = 0
    
    index1, index2 = 0, 0
    
    while count < length*2:
        if sum1 < sum2:
            sum2 -= queue[index2]
            sum1 += queue[index2]
            index2 = (index2 + 1) % length
        elif sum1 > sum2:
            sum1 -= queue[index1]
            sum2 += queue[index1]
            index1 = (index1 + 1) % length
        else:
            return count
        count += 1
        
    return -1