from collections import defaultdict

def solution(dice):
    N = len(dice)
    memo = defaultdict(lambda: defaultdict(int))

    dice_id = list(range(N))
    for i, d in enumerate(dice):
        for el in d:
            memo[tuple([i])][el] += 1

    def compare(a):
        b = tuple(filter(lambda x: x not in a, dice_id))
        win_count = 0
        sorted_b = sorted(memo[b].items())

        for a_key, a_value in memo[a].items():
            for b_key, b_value in sorted_b:
                if a_key > b_key:
                    win_count += a_value * b_value
                else:
                    break
        return win_count
    
    def find_max(comb):
        max_win = 0
        max_dice = None
        
        for c in comb:
            win_count = compare(c)

            if win_count > max_win:
                max_win = win_count
                max_dice = c

        return max_dice

    def merge(c1, c2):
        m = tuple(sorted(set(c1 + c2)))
        for c1_key, c1_value in memo[c1].items():
            for c2_key, c2_value in memo[c2].items():
                memo[m][c1_key + c2_key] += c1_value * c2_value

    def make_comb(m1, m2):
        visited = defaultdict(bool)
        new_comb = []
        for c1 in m1:
            for c2 in m2:
                t = tuple(sorted(set(c1 + c2)))

                if not visited[t] and len(t) == len(c1+c2):
                    merge(c1, c2)
                    new_comb.append(t)
                    visited[t] = True

        return new_comb
    
    def make_comb_with_same(comb):
        return make_comb(comb, comb)

    def make_comb_with_1(comb):
        return make_comb(comb, [tuple([i]) for i in range(N)])

    comb = [tuple([i]) for i in range(N)]
    case = {
        2: [],
        4: [make_comb_with_same],
        6: [make_comb_with_same, make_comb_with_1],
        8: [make_comb_with_same, make_comb_with_same],
        10: [make_comb_with_same, make_comb_with_same, make_comb_with_1]
    }

    for do in case[N]:
        comb = do(comb)

    return sorted(list(map(lambda x: x + 1, find_max(comb))))

print(solution([[1,2,3,4,5,6], [2,2,4,4,6,6]]))
print(solution([[1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5]]))
# solution([[1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5]])
# solution([[1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5]])
# solution(
#     [
#     [1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5], [1,1,4,4,5,5], 
#     [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5], [1,1,4,4,5,5]
#     ]
# )

print(solution([
    [40, 41, 42, 43, 44, 45],
    [43, 43, 42, 42, 41, 41], 
    [1, 1, 80, 80, 80, 80],
    [70, 70, 1, 1, 70, 70]
]))