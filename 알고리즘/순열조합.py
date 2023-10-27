outer = [1, 2, 3, 4, 5]

def finish(arr):
    print(arr)

def nCr(arr, n, depth):
    if len(arr) == n:
        finish(arr)
        return
        
    if len(outer) == depth:
        return

    # n 이하의 모든 조합 찾고 싶으면
    # len(arr) == n or len(outer) == depth

    arr.append(outer[depth])
    nCr(arr, n, depth + 1)
    
    arr.pop()
    nCr(arr, n, depth + 1)

# nCr([], 3, 0)


def nCr2(arr, n):
    if len(arr) == n:
        finish(arr)
        return
    
    for i in range(5):
        if not visited[i] and (not arr or arr[-1] <= outer[i]):
            arr.append(outer[i])
            visited[i] = True
            nCr2(arr, n)
            arr.pop()
            visited[i] = False

visited = [False] * 5
nCr2([], 3)


def nPr(arr, n):
    if len(arr) == n:
        finish(arr)
        return

    for i in range(5):
        if not visited[i]:
            arr.append(outer[i])
            visited[i] = True
            nPr(arr, n)
            arr.pop()
            visited[i] = False

# visited = [False] * 5
# nPr([], 3)

def nFr(arr, n):
    if len(arr) == n:
        finish(arr)
        return

    for i in range(5):
        arr.append(outer[i])
        nFr(arr, n)
        arr.pop()

# nFr([], 3)

def nHr(arr, n):
    if len(arr) == n:
        finish(arr)
        return

    for i in range(5):
        if not arr or outer[i] >= arr[-1]:
            arr.append(outer[i])
            nHr(arr, n)
            arr.pop()

# nHr([], 3)