from collections import defaultdict

N = int(input())

answer = N

for _ in range(N):
    word = input()

    visited = defaultdict(bool)
    stack = []
    
    for w in word:
        if visited[w]:
            answer -= 1
            break

        if not stack:
            stack.append(w)
            continue

        if stack[-1] != w:
            visited[stack[-1]] = True
            
        stack.append(w)

print(answer)