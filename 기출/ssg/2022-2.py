from typing import Final
from itertools import permutations

def compare_postfix(word, value):
    if word[len(word) - len(value):] == value:
        return True
    return False

def compare_prefix(word, value):
    if word[:len(value)] == value:
        return True
    return False

def search_pre(dictionary, value, length = None):
    new_dic = []

    for word in dictionary:
        if length and len(word) != length:
            continue
        if compare_prefix(word, value):
            new_dic.append(word)

    return new_dic

def search_post(dictionary, value, length = None):
    new_dic = []

    for word in dictionary:
        if length and len(word) != length:
            continue
        if compare_postfix(word, value):
            new_dic.append(word)

    return new_dic

def search_length(dictionary, value):
    WILD: Final = '@'

    if value[-1] == WILD:
        return search_pre(dictionary, value.split(WILD)[-1], len(value))
    if value[0] == WILD:
        return search_post(dictionary, value.split(WILD)[0], len(value))

def error(dictionary):
    new_dic = dictionary

    for element in list(permutations(dictionary, 2)):
        new_dic.append(''.join(element))

    return new_dic

def solution(dictionary, command):
    POSTFIX: Final = "postfix"
    PREFIX: Final = "prefix"
    LENGTH_MATCH: Final = "lengthMatch"

    answer = error(dictionary)

    for cmd in command:
        order , value = cmd

        if order == POSTFIX:
            answer = search_post(answer, value)
        if order == PREFIX:
            answer = search_pre(answer, value)
        if order == LENGTH_MATCH:
            answer = search_length(answer, value)
        
    return answer

# print(solution(["popop", "abcd", "dsfsdfs", "serwerwe", "werwerwer" ,"dfdfderwer", "abee", "abeef"], [["postfix", "wer"]]))
print(solution(['123', '456', '789'], [['prefix', '123']]))