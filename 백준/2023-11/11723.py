import sys
input = sys.stdin.readline

ORDER = {
    'ADD': 'add',
    'CHECK': 'check',
    'REMOVE': 'remove',
    'TOGGLE': 'toggle',
    'EMPTY': 'empty',
    'ALL': 'all'
}

M = int(input().rstrip())
numbers = set()

for _ in range(M):
    order = input().rstrip()
    if " " in order:
        order, num = order.split()
        num = int(num)
    else:
        order, num = order, None

    if order == ORDER['ADD']:
        numbers.add(num)
    if order == ORDER['REMOVE']:
        if num in numbers:
            numbers.remove(num)
    if order == ORDER['CHECK']:
        if num in numbers:
            print(1)
        else:
            print(0)
    if order == ORDER['TOGGLE']:
        if num in numbers:
            numbers.remove(num)
        else:
            numbers.add(num)
    if order == ORDER['ALL']:
        numbers = set([i for i in range(1, 21)])
    if order == ORDER['EMPTY']:
        numbers = set()
