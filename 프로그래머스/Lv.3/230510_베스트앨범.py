from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    play_count = defaultdict(int)
    genre_order = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_count[genre] += play
        heapq.heappush(genre_order[genre], (-play, i))

    for pc in sorted(list(play_count.items()), key=lambda x: x[1], reverse=True):
        for _ in range(2):
            if genre_order[pc[0]]:
                answer.append(heapq.heappop(genre_order[pc[0]])[1])
    return answer

print(solution(["classic", "classic", "classic", "classic", "pop"], [500, 800, 800, 800, 2500]))