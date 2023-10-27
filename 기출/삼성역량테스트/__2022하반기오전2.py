from collections import defaultdict

Q = int(input())
create = list(map(int, input().split()))
# create=list(map(int, '100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17'.split()))
N, M = create[1], create[2]
create = create[3:]
belt = []
box = defaultdict(lambda: None)

for i in range(0, N, N//M):
    belt.append([create[i], create[i+M]])
    box[create[i]] = [None, create[i+1], create[i+N]]
    box[create[i + M]] = [create[i+M-1], None, create[i+M+N]]
    for j in range(1, M):
        box[create[i+j]] = [create[i+j-1], create[i+j+1], create[i+j+N]]

DOWN, DELETE, CHECK, BRAKE = 200, 300, 400, 500

def down(w_max):
    result = 0
    for num, b in enumerate(belt):
        if b is None:
            continue

        front, back = b
        if front is None:
            continue

        prev, next, weight = box[front]
        if weight <= w_max:
            box[front] = None
            if next is not None:
                box[next][0] = None
            belt[num][0] = next
            result += weight
        else:
            box[front] = [back, None, weight]
            if next is not None:
                box[next][0] = None
            box[back][1] = front
            belt[num] = [next, front]

        front, back = b
        if front is None:
            belt[num][1] = None

    return result

def delete(r_id):
    if box[r_id] is None:
        return -1
    prev, next, weight = box[r_id]

    if prev is not None:
        box[prev][1] = next
    if next is not None:
        box[next][0] = prev

    box[r_id] = None

    for num, b in enumerate(belt):
        if b is None:
            continue

        front, back = b
        if r_id == front:
            belt[num][0] = next
        if r_id == back:
            belt[num][1] = prev

    return r_id

def check(f_id):
    if box[f_id] is None:
        return -1

    result = -1
    search, front_id = box[f_id][0], f_id
    while search is not None:
        search, front_id = box[search][0], search

    for num, b in enumerate(belt):
        if b is None:
            continue
        if b[0] == front_id:
            result = num

    front, back = belt[result]
    prev, next, weight = box[f_id]

    if f_id != front:
        box[f_id][0] = None
        box[prev][1] = None
        box[front][0] = back
        box[back][1] = front

    belt[result] = [f_id, prev]
    if belt[result][1] is None:
        belt[result][1] = f_id

    return result + 1

def brake(b_num):
    if belt[b_num-1] is None:
        return -1

    length = len(belt)
    next_belt = b_num % length
    while belt[next_belt] is None:
        next_belt = (next_belt + 1) % length

    bfront, bback = belt[b_num-1]
    nfront, nback = belt[next_belt]

    if nfront is not None and nback is not None:
        box[nback][1] = bfront
        box[bfront][0] = nback
        belt[next_belt][1] = bback

    belt[b_num-1] = None

    return b_num

for _ in range(Q-1):
    order, num = map(int, input().split())

    if order == DOWN:
        print(down(num))
    if order == DELETE:
        print(delete(num))
    if order == CHECK:
        print(check(num))
    if order == BRAKE:
        print(brake(num))

    print(box)
    print(belt)