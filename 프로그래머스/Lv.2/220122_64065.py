
def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{')
    result=[]
    for i in s:
        result.append(i.split(','))
    result.sort(key=len)
    
    answer = []
    for i in result:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

# s	result
# "{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
# "{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
# "{{20,111},{111}}"	            [111, 20]
# "{{123}}"	                        [123]
# "{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")