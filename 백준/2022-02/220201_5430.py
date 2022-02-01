import sys; input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    func, n, arr = (input().rstrip() for _ in range(3))
    n = int(n)
    arr = arr[1:-1].split(',') if arr[1:-1] else []
    is_reverse = False
    front = rear = 0
    for f in func:
        if f=='R':
            is_reverse = not is_reverse
        elif f=='D' and not is_reverse:
            front += 1
        elif f=='D' and is_reverse:
            rear +=1
    if front+rear==n: result='[]'
    elif front+rear>n: result='error'
    else: 
        arr = arr[front:n-rear] if not is_reverse else list(reversed(arr[front:n-rear]))
        result='['+','.join(arr)+']'
    print(result)