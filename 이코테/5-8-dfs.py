def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
# stack으로 pop하는 방식이 아니다. 
# 파이썬은 함수의 인자로 리스트를 넣었을 때 call by reference로 넘어간다. 
# 따라서 visited를 전역변수로 선언하지 않아도 함수가 호출될 때마다 visited가 업데이트 된다.

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)
