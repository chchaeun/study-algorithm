from collections import Counter
def solution(card, word):
    answer = []
    card_count = []
    for c in card:
        card_count.append(Counter(c))
    for w in word:
        visited = [0]*3
        count = 0
        word_count = Counter(w).items()
        for wc in word_count:
            for i in range(3):
                if card_count[i][wc[0]]>=wc[1]:
                    count += 1
                    visited[i] = 1
                    break
        if count == len(word_count) and not (0 in visited):
            answer.append(w)
    return answer if answer else ['-1']

print(solution(['ABACDEFG', 'NOPQRSTU', 'HIJKLKMM'], ['GPQM', 'GPMZ', 'EFU', 'MMNA']))
print(solution(['AABBCCDD', 'KKKKJJJJ', 'MOMOMOMO'], ['AAAKKKKKMMMMM', 'ABCDKJ']))