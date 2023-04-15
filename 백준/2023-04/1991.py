n = int(input())

node = {}

for _ in range(n):
    root, left, right = input().split()
    node[root] = [left, right]

def order(root, type):
    if type=='PRE':
        print(root, end='')

    left, right = node[root]

    if left!='.':
        order(left, type)

    if type=='IN':
        print(root, end="")

    if right!='.':
        order(right, type)

    if type=='POST':
        print(root, end="")
        
    if left=='.' and right=='.':
        return

order('A', 'PRE')
print()
order('A', 'IN')
print()
order('A', 'POST')