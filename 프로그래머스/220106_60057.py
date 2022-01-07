'''
Lv2: 문자열 압축

데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 
더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.

간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 
이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 
예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. 
"어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 
더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 
2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 
다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 
이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 
3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 
이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 
위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 
표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(s):
    answer = 1001
    # 압축 단위가 문자열 길이의 반을 넘어가면 압축할 수 없으므로 max_unit을 문자열 길이의 반으로 설정
    # 문자열 길이가 1일 때 2로 나누면 0이 되기 때문에 max_unit = 1로 설정
    if len(s)==1:
        max_unit = 1
    else:
        max_unit = len(s)//2

    # 압축할 단위 1 ~ max_unit 만큼 반복
    for i in range(1, max_unit+1):
        stack=[]
        top=-1
        
        # 문자열 처음부터 끝까지 반복
        # 단위만큼 증가하면서 반복
        for j in range(0, len(s), i):
            
            # j ~ j+i 단위만큼 떼어서 확인하는데, 
            # 단위만큼 나누어 떨어지지 않으면 뒤의 문자열이 단위보다 적게 남는다. 
            # 그럴 때 j부터 끝까지로 설정
            if j+i>=len(s):
                top_str = s[j:]
            else:
                top_str = s[j:j+i]
            
            # 스택에 아무것도 안 들어있을 때    
            if top==-1:
                stack.append(top_str)
                top=0
            
            # 현재 기준 문자열과 새로 들어오는 문자열이 같을 때
            elif stack[top]==top_str:
                
                # top 문자 뒤에 숫자 없을 때
                if len(stack) - 1 == top:
                    stack.append(2)
                # 숫자 있을 때 
                else:
                    stack[top+1] +=1
                    
            # 기준 문자열과 새로 들어오는 문자열이 다를 때 
            else:
                stack.append(top_str)
                top=len(stack)-1
                
        # 카운트
        temp = 0
        for k in stack:
            # 자료형이 integer일 경우 string으로 바꾸어 세어준다.
            # temp+=1를 해주면 안되는 이유는 만약 k가 10이라면 temp+=2로 체크돼야 하기 때문
            if isinstance(k, int):
                temp += len(str(k))
            else:
                temp += len(k)
        answer = min(answer, temp)
    return answer

test_case = ["acacacbacacac", "acacacacacacbacacacacacac", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]

for t in test_case:
    print(solution(t))
    
    
'''
# 좋은 풀이

def compress(text, tok_len):
    
    # 문자열 전체 반복, 단위만큼씩 증가
    # 단위 토큰으로 잘라서 words 리스트에 넣음
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    print(words)
    print(words[1:] + [''], end="\n\n")
    
    # 맨 앞에 거 하나 빼고 뒤에 빈 문자열 합해서 리스트 만들고 zip으로 반복
    for a, b in zip(words, words[1:] + ['']):
        # a, b가 같으면 count
        # a는 항상 b의 한 칸 앞
        if a == b:
            cur_cnt += 1
            
        # 다르면 a와 count를 res 리스트에 추가
        # b를 cur_word로 바꿈 -> 다음 걸로 업데이트
        # cur_cnt 초기화
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    # word의 길이 + count를 string으로 바꾼 것의 길이 더해서 리턴
    # cnt가 1 이하일 때는 0으로
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    # 단위 토큰 길이 리스트
    # list(range(1, int(len(text)/2) + 1)) + [len(text)]
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))
'''