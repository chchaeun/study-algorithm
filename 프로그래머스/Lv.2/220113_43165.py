from itertools import combinations

# 마이너스가 되는 요소가 무엇인지 경우의 수로 나눔
# 모두 더한 것에서 마이너스 요소를 빼는 식으로 target을 만들었는데,
# 빼는 과정에서 sum에서 더해준 요소도 빼줘야 하기 때문에 *2 를 해줘야 했음.
# sum에서 x*2를 해줬을 때 target이 나오는 x 값을 찾고, 리스트의 요소들을 더해 x가 나오는 경우의 수가 나오면 답
# sum - target / 2가 나누어 떨어지지 않으면 x를 만들 수 없기 때문에 배제

def solution(numbers, target):
    answer = 0
    temp = sum(numbers) - target
    if temp % 2 != 0:
        return 0
    temp //= 2
    filtered = list(filter(lambda x: x<=temp, numbers))
    combinated=[]
    for i in range(1, len(filtered)+1):
        c = combinations(filtered, i)
        combinated.extend(c)
    for j in combinated:
        if sum(j)==temp:
            answer+=1
    return answer

print(solution([1, 2, 3, 4, 5], 3))