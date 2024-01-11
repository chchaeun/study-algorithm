from collections import defaultdict, deque

EMPTY, WALL, DOC = '.', '*', '$'

T = int(input())
answer =[]
for _ in range(T):
  H, W = map(int, input().split())
  keys = defaultdict(bool)
  board = [list(input()) for _ in range(H)]
  
  for my_key in list(input()):
    if my_key == '0':
      break
    keys[my_key] = True
  
  def in_range(y, x):
    return 0 <= y < H and 0 <= x < W

  def getExit():
    exit = []
    answer = 0
    for y in range(H):
      for x in range(W):
        if board[y][x] == WALL or not (y in [0, H-1] or x in [0, W-1]) or board[y][x].isupper() and not keys[board[y][x].lower()]:
          continue

        exit.append((y, x))

    return exit

  docs = set()
  
  for y, x in (getExit()):
    if board[y][x].islower():
      keys[board[y][x]] = True

    if board[y][x] == DOC:
      docs.add((y, x))


  dq = deque(getExit())
  visited = defaultdict(bool)
  dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
  
  while dq:
    y, x = dq.popleft()
    
    for dy, dx in zip(dys, dxs):
      ny, nx = y + dy, x + dx
      
      if not in_range(ny, nx) or board[ny][nx] == WALL or visited[(ny, nx)]:
        continue
  
      if board[ny][nx] == DOC:
        docs.add((ny, nx))
        visited[(ny, nx)] = True
        dq.append((ny, nx))
  
      elif board[ny][nx] == EMPTY or board[ny][nx].isupper() and keys[board[ny][nx].lower()]:
        visited[(ny, nx)] = True
        dq.append((ny, nx))
  
      elif board[ny][nx].islower():
        if not keys[board[ny][nx]]:
          keys[board[ny][nx]] = True
          dq = deque(getExit())
          visited = defaultdict(bool)
        visited[(ny, nx)] = True
        dq.append((ny, nx))
        
  answer.append(len(docs))

for a in answer:
  print(a)
