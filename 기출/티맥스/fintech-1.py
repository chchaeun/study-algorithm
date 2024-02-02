
def in_circle(tx, ty, xs, ys, rs):
    for x, y, r in zip(xs, ys, rs):
        if (tx - x) ** 2 + (ty - y) ** 2 <= r ** 2:
            return True
    return False

def translate(x, y, rect):
    l, r, b, t = rect

    return l + x % (r - l), b + y % (t - b)

def get_area(k, rect):
    left, right, bottom, top = rect

    return int(k * (right - left) * (top - bottom))


def little_rectangle(xs, ys, rs):
    INF = int(1e9)

    left, bottom = INF, INF
    right, top = 0, 0
    for x, y, r in zip(xs, ys, rs):
        left = min(x - r, left)
        right = max(x + r, right)
        bottom = min(y - r, bottom)
        top = max(y + r, top)

    return left, right, bottom, top

def solution(x, y, r, v):
    rect = little_rectangle(x, y, r)
    count = 0

    for i in range(0, len(v), 2):
        tx, ty = translate(v[i], v[i+1], rect)
        
        if in_circle(tx, ty, x, y, r):
            count += 1
        
    return get_area(count / (len(v) // 2), rect)

print(solution([5], [5], [5], [92, 83, 14, 45, 66, 37, 28, 9, 10, 81]))

print(solution([3,4], [3,5], [2,3], [12, 83, 54, 35, 686, 337, 258, 95, 170, 831, 8, 15]))