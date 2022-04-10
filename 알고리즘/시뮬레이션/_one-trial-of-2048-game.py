grid = [list(map(int, input().split())) for _ in range(4)]
dist = input().strip()

def shift():
    next_grid = [[0 for _ in range(4)] for _ in range(4)]
    
    for j in range(4):
        keep_num, next_row = -1, 3
        
        for i in range(3, -1, -1):
            if not grid[i][j]:
                continue
            
            if keep_num == -1:
                keep_num = grid[i][j];
            
            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num * 2
                keep_num = -1
                next_row -= 1
            else:
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                
                next_row -= 1
        
        if keep_num != -1:
            next_grid[next_row][j] = keep_num
            next_row -= 1

    for i in range(4):
        for j in range(4):
            grid[i][j] = next_grid[i][j]

def rotate():
    ngrid = [[] for _ in range(4)]
    for j in range(4):
        for i in range(3, -1, -1):
            ngrid[j].append(grid[i][j])
    for i in range(4):
        for j in range(4):
            grid[i][j] = ngrid[i][j]

dist_dict = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

for _ in range(dist_dict[dist]):
    rotate()
shift()
for _ in range(4-dist_dict[dist]):
    rotate()
    
for g in grid:
    print(*g)
