a, b = map(int, input().split())

WIN = {
    1: 2,
    2: 3,
    3: 1
}

if WIN[a] == b:
    print('B')
else:
    print('A')