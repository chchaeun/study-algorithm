from collections import defaultdict
def solution(n, words):
    answer = []
    dict = defaultdict(int)
    dict[words[0]] = 1
    for i in range(1, len(words)):
        if words[i-1][-1]!=words[i][0] or dict[words[i]]:
            member = (i+1)%n if (i+1)%n else n
            turn = ((i+1)//n)+1 if (i+1)%n else (i+1)//n
            return [member, turn]
        else: dict[words[i]]+=1      
    return [0, 0]

test_n = [3, 5, 2]
test_words = [["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],
              ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"],
              ["hello", "one", "even", "never", "now", "world", "draw"]
              ]

for tn, tw in zip(test_n, test_words):
    print(solution(tn, tw))