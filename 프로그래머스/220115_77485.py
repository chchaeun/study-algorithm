def solution(rows, columns, queries):
    board = [i for i in range((rows*columns)+1)]
    answer = []
    for q in queries:
        x1, y1, x2, y2 = map(int, q)
        # 시계방향 회전
        move_count = [y2-y1, x2-x1, y2-y1, x2-x1-1]
        move = [1, columns, -1, -columns]
        
        # 바뀌는 것들의 인덱스
        change = [(x1-1)*columns+y1]
        
        for mc, m in zip(move_count, move):
            for i in range(mc):
                change.append(change[-1]+m)
        
        # 바꾸면서 최솟값 찾기        
        _min = 10001
        temp = board[change[-1]]
        for i in range(len(change)-1, 0, -1):
            board[change[i]] = board[change[i-1]]
            _min = min(_min, board[change[i]])
        board[change[0]] = temp
        _min = min(_min, board[change[0]])
        answer.append(_min)
        
    return answer


test_rows = [6, 3, 100]
test_cols = [6, 3, 97]
test_queries = [
    [[2,2,5,4],[3,3,6,6],[5,1,6,3]], 
    [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]], 
    [[1,1,100,97]]
]

for r, c, q in zip(test_rows, test_cols, test_queries):
    print(solution(r, c, q))
