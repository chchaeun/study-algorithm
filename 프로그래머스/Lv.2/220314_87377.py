from itertools import combinations
def solution(line):
    INF = 1000**6
    point = []
    answer = []
    for c in combinations(line, 2):
        ex1, ex2 = c[0], c[1]
        denom = ex1[0]*ex2[1]-ex1[1]*ex2[0]
        num1 = ex1[1]*ex2[2]-ex1[2]*ex2[1]
        num2 = ex1[2]*ex2[0]-ex1[0]*ex2[2]
        if denom!=0:
            x = num1/denom 
            y = num2/denom 
            if x==int(x) and y==int(y):
                point.append((int(x), int(y)))
    xmax, xmin, ymax, ymin = -INF, INF, -INF, INF
    for p in point:
        xmax, xmin = max(p[0], xmax), min(p[0], xmin)
        ymax, ymin = max(p[1], ymax), min(p[1], ymin)
    point.sort(key=lambda x: (-x[1], x[0]))
    for i in range(ymax, ymin-1, -1):
        str = ""
        for j in range(xmin, xmax+1):
            if (j, i) in point:
                str += "*"
            else:
                str += "."
        answer.append(str)
    return answer
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))