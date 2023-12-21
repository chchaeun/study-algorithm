from collections import defaultdict

def solution(friends, gifts):
    next_month = defaultdict(int)

    board = defaultdict(int)
    score = defaultdict(lambda: [0, 0])

    visited = defaultdict(bool)

    for friend in friends:
        visited[(friend, friend)] = True
    
    for gift in gifts:
        give, take = gift.split()
        board[(give, take)] += 1
        score[give][0] += 1
        score[take][1] += 1

    for friend_i in friends:
        for friend_j in friends:
            if not visited[(friend_i, friend_j)]:
                p1, p2 = board[(friend_i, friend_j)], board[(friend_j, friend_i)]

                if p1 > p2:
                    next_month[friend_i] += 1
                elif p1 < p2:
                    next_month[friend_j] += 1
                else:
                    p1_score = score[friend_i][0] - score[friend_i][1]
                    p2_score = score[friend_j][0] - score[friend_j][1]

                    if p1_score > p2_score:
                        next_month[friend_i] += 1
                    elif p1_score < p2_score:
                        next_month[friend_j] += 1

                visited[(friend_i, friend_j)], visited[(friend_j, friend_i)] = True, True
                
    answer = max(next_month.values()) if next_month else 0
    return answer

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi","ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))

print(solution(['a', 'b', 'c'], ['a b', 'b a', 'c a', 'a c', 'a c', 'c a']))