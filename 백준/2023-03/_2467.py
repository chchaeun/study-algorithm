n = int(input())
numbers = list(map(int, input().split()))

left, right = 0, n-1

mix = abs(numbers[left] + numbers[right])
answer = [numbers[left], numbers[right]]
while left < right:
    cur_mix = numbers[left] + numbers[right]
    if mix > abs(cur_mix):
        mix = abs(cur_mix)
        answer = [numbers[left], numbers[right]]

    if cur_mix == 0:
        break

    if cur_mix > 0:
        right -= 1
    else:
        left += 1


print(*answer)