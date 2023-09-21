arr = [1, 2, 3, 4, 5]

def nCr(comb, n, depth):
    if len(comb) == n or len(arr) == depth:
        finish(comb)
        return

    # n 이하의 모든 조합 찾고 싶으면
    # len(comb) == n and len(arr) == depth

    comb.append(arr[depth])
    nCr(comb, n, depth + 1)
    
    comb.pop()
    nCr(comb, n, depth + 1)


def finish(comb):
    print(comb)

nCr([], 3, 0)