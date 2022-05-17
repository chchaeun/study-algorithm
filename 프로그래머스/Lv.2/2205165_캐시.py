from collections import defaultdict, deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0: return 5*len(cities)
    cache = deque()
    cacheDict = defaultdict(int)
    for city in cities:
        city = city.upper()
        if cacheDict[city]==1:
            answer+=1
            cache.remove(city)
        else:
            if len(cache)>=cacheSize:
                old = cache.popleft()
                cacheDict[old] = 0
            cacheDict[city] = 1
            answer += 5
        cache.append(city)
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5, ['a', 'b', 'c', 'b']))