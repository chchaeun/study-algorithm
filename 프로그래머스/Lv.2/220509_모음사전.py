def solution(word):
    global answer, count
    answer, count = 0, 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    arr = []
    def dfs(depth):
        global answer, count
        if ''.join(arr)==word:
            answer = count
            return
        if depth == 5:
            return
        for vowel in vowels:
            arr.append(vowel)
            count += 1
            dfs(depth + 1)
            arr.pop()
    dfs(0)
    return answer

print(solution('I'))