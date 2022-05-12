from multiprocessing.connection import answer_challenge
import sys; input=sys.stdin.readline

n = int(input().strip())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x: min(x))

global answer
answer = 0

arr = []

def is_overlap(prev, cur):
    prev_max = max(lines[prev])
    cur_min = min(lines[cur])
    if prev_max>=cur_min:
        return True
    else: return False

def choose(count):
    global answer
    if arr and arr[-1]==n-1:
        answer = max(answer, count)
        return
    for i in range(n):
        if not arr or arr[-1]<i and not is_overlap(arr[-1], i):
            arr.append(i)
            choose(count+1)
            arr.pop()
    return answer

print(choose(0))