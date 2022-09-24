from collections import defaultdict
from typing import List
import re

def is_re_match(k, c, dic):
    r = re.compile(('[a-z]{1,%d}' % k).join(c.split('.')))
    for d in dic:
        if re.match(r, d):
            return True

    return False

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = []
    
    dic_dict = defaultdict(bool)
    
    for d in dic:
        dic_dict[d] = True

    chat_list = chat.split()

    for c in chat_list:
        if dic_dict[c] or is_re_match(k, c, dic):
            answer.append('#' * len(c))
        else:
            answer.append(c)

    return ' '.join(answer)


print(solution(2, ["slang", "badword"], "badword ab.cd bad.ord .word sl.. bad.word"))
print(solution(3, ["abcde", "cdefg", "efgij"], ".. ab. cdefgh .gi. .z."))