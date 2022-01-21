from itertools import permutations

def solution(expression):
    ops = ['+', '-', '*']
    priority = list(permutations(ops))
    
    exp = []
    op_index = -1
    for i in range(len(expression)):
        if expression[i] in ops:
            exp.append(expression[op_index+1:i])
            exp.append(expression[i])
            op_index = i
    exp.append(expression[op_index+1:])
    
    _max = 0
    for p in priority:
        _max = max(_max, reward(p, exp))
    
    return _max    
    
def reward(p, exp):
    i=0
    while i<3:
        if p[i] in exp:
            j = exp.index(p[i])
            exp = exp[:j-1] +[calculate(exp[j-1], exp[j+1], p[i])]+exp[j+2:]
        else:
            i+=1
    return abs(int(exp[0]))

def calculate(n1, n2, op):
    return str(eval(n1+op+n2))

solution("50*6-3*2")