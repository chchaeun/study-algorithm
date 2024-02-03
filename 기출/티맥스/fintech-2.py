from collections import defaultdict


def in_range(y, x, n):
    # 오른쪽 변 진행 시 아래, 왼쪽 변 진행 시 위로 넘어가는 경우 
    if y < n-1 and x == -(n-1) or 3 * (n-1) < y and x == n-1:
        return False

    return 0 <= y <= 4 * (n-1) and -(n-1) <= x <= n-1

def solution(n):
    # 6방향으로 진행, 일자로 가는 경우는 2칸으로 처리
    # 대각선은 1칸 처리
    dys, dxs = [1, 2, 1, -1, -2, -1], [1, 0, -1, -1, 0, 1]

    bee = defaultdict(int)

    num = 1
    direction = 0
    y, x = 0, 0

    while True:
        bee[(y, x)] = num

        ny, nx = y + dys[direction], x + dxs[direction]

        # 벗어나거나 이미 방문했으면 방향 전환
        # 6번 전부 방문할 수 없으면 완전히 종료
        for _ in range(6):
            if not in_range(ny, nx, n) or bee[(ny, nx)]:
                direction = (direction + 1) % 6
                ny, nx = y + dys[direction], x + dxs[direction]

            if in_range(ny, nx, n) and not bee[(ny, nx)]:
                break
        else:
            break

        y, x = ny, nx
        num += 1

    answer = []
    for key in sorted(bee.keys()):
        if bee[key]:
            answer.append(bee[key])

    return answer

print(solution(2))
print(solution(3))
print(solution(4))