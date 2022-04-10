

def encoding(string):
    encoded = []
    top = -2
    for s in string:
        if not encoded or encoded[top]!=s:
            encoded.append(s)
            encoded.append(1)
            top += 2
        else:
            encoded[top+1]+=1
    return ''.join(list(map(str, encoded)))

def shift(string):
    return string[-1]+string[:-1]

a = input()
answer = 100
for _ in range(len(a)):
    answer = min(answer, len(encoding(a)))
    a = shift(a)
print(answer)