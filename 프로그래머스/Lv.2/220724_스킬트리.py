from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0

    skill_dict = defaultdict(int)
    for i, s in enumerate(skill):
        skill_dict[s] = i+1

    for skill_tree in skill_trees:
        if checkTree(skill_dict, skill_tree):
            answer += 1

    return answer

def checkTree(skill_dict, skill_tree):
    priority = 0
    for st in skill_tree:
        if not skill_dict[st]:
            continue
        elif priority + 1 != skill_dict[st]:
            return False
        else:
            priority = skill_dict[st]
    return True

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))