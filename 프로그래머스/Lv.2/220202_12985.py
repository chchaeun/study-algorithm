def solution(n, a, b):
    answer = 1
    _max = max(a, b)
    _min = min(a, b)
    while True:
        n/=2
        if _min==1 and _max == 2:
            break
        # 다른쪽
        if _min <= n < _max:
            _max = (_max+1)//2
            _min = (_min+1)//2
            answer+=1
        # 같은 쪽인데 오른쪽일때
        elif _min>n and _max>n:
            _max -= n
            _min -= n
    return answer
print(solution(4, 1, 2))

# 짧은 풀이
# 정확한 원리는 이해 못하겠음
# 아마 앞에서부터 2씩 자르기 때문에 그렇게 되는 것 같음

# 만약에 a가 1이면 계속 1이 나온다
# a=2, b=3이면 1, 2 / 1, 1이 된다.
# a=3, b=4면 2, 2가 돼서 바로 같아진다.

'''
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
'''