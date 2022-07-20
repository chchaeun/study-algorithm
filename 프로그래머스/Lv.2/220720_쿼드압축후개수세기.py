def solution(a):
    global zero, one, arr
    arr = a[:]
    n = len(arr[0]) 
    one = sum(map(sum, arr))
    zero = n*n-one

    checkScope(0, 0, n)

    return [zero, one]

def checkScope(y, x, n):
    global zero, one, arr
    if n == 1: return

    _sum = press(y, x, n)

    if _sum < 0:
        nsize = n//2
        dys, dxs = [0, 0, nsize, nsize], [0, nsize, 0, nsize]
        for dy, dx in zip(dys, dxs):
            ny, nx = y+dy, x+dx
            checkScope(ny, nx, nsize)
    elif _sum == 1:
        one -= n*n - 1
    else:
        zero -= n*n - 1


def press(y, x, size):
    global arr
    temp = arr[y][x]
    for i in range(size):
        for j in range(size):
            if temp != arr[y+i][x+j]:
                return -1
    return temp

# solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],
[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])