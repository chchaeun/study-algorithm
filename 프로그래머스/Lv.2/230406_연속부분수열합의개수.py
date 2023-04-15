def solution(elements):
    sum_numbers = set()
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            if j+i < len(elements):
                _sum = sum(elements[j:j+i])
            else:
                _sum = sum(elements[j:]+elements[:i-(len(elements)-j)])
            sum_numbers.add(_sum)
   
    return len(sum_numbers)

print(solution([7,9,1,1,4]))