n = int(input())

numbers = ['4', '5', '6']

global seq
seq = ''

def choose(count):
    global seq
    if count == n:
        print(seq)
        exit()
    for number in numbers:
        length = len(seq)
        flag = True
        for i in range(1, length+1):
            if seq[length-i*2+1:length-i+1]==seq[length-i+1:]+number:
                flag = False
                break
        if flag:
            seq += number
            choose(count + 1)
            seq = seq[0:length]
        
choose(0)