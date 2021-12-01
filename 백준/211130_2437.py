import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

target = 1

for a in arr:
    if target >= a:
        target += a
    else:
        break
print(target)

# target이 ___일 때 a보다 작으면, a로 target을 만들 수 없는 것이다.
# arr를 앞에서부터 차례로 더했을 때, 다음에 나오는 숫자가 만들어야 하는 숫자보다 크면
# 만들고 싶은 숫자를 만들 수가 없다. 
# 예를 들어서 1, 2, 5면 1, 2, 3까진 만들 수 있는데 4를 5로 만들 수 없다.
# 여태까지의 수로 target까지의 수를 다 만들 수 있다고 어떻게 확신하는지는 모르겠다... 탐구가 필요
# 주어진 테스트 케이스에서는 마지막 숫자를 제외하고 거기에 1을 더하면 답이 나와서 
# 그런 식으로 접근을 해보려고 했는데 정답과 맥락은 비슷한 것 같다.