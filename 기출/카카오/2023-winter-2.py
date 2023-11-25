from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    parent_x = find(parent, x)
    parent_y = find(parent, y)
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y


def max_vertex_count(edges):
    count = defaultdict(int)
    vertex_set = set()

    for edge in edges:
        v1, v2 = edge
        count[v1] += 1
        vertex_set.add(v1)
        vertex_set.add(v2)

    max_vertex, max_count = 0, 0

    for key, value in count.items():
        if max_count < value:
            max_count = value
            max_vertex = key

    return max_vertex, len(vertex_set)

def graph_count(parents, edges, add_num):
    donut, stick, eight = 0, 0, 0
    dict_list = defaultdict(lambda: [0, 0])

    for parent in parents[1:]:
        dict_list[parent][0] += 1

    for edge in edges:
        if edge[0] == add_num:
            continue
        else:
            dict_list[parents[edge[0]]][1] += 1

    for count in dict_list.values():
        c1, c2 = count
        
        if c1 == c2:
            donut += 1
        elif c1 - 1 == c2:
            stick += 1
        else:
            eight += 1

    stick -= 1

    return [donut, stick, eight]

def solution(edges):
    add_num, count = max_vertex_count(edges)
    parents = [i for i in range(count + 1)]

    for edge in edges:
        v1, v2 = edge
        if v1 == add_num:
            continue

        if find(parents, v1) != find(parents, v2):
            union(parents, v1, v2)

    for i in range(1, count + 1):
        parents[i] = find(parents, i)

    return [add_num] + graph_count(parents, edges, add_num)


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
# [2,1,1,0]
print(solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
     [11, 9], [3, 8]]))
# [4,0,1,2]
