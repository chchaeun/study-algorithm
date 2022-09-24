from collections import defaultdict
from typing import List

def get_power(element):
    power = 2
    while power < element:
        power *= 2
    return power


def solution(queries: List[List[int]]) -> int:
    answer = 0

    arr = defaultdict(list)
    
    for query in queries:
        arr_num, new_element = query
        if not arr[arr_num]:
            arr[arr_num] = [get_power(new_element), new_element]
        else:
            arr_size, current_element = arr[arr_num]

            if arr_size < current_element + new_element:
                arr[arr_num] = [get_power(current_element + new_element), current_element + new_element]
                answer += current_element
            else:
                arr[arr_num][1] = current_element + new_element

    return answer

print(solution([[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]))
print(solution([[1, 1], [1, 2], [1, 4], [1, 8]]))
