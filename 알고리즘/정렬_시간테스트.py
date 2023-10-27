import random, time, heapq

arr = [random.randrange(1, 100000000000) for _ in range(10000000)]

sorted_hq = []

heap_start = time.time()

for i in range(1000000):
    heapq.heappush(sorted_hq, arr[i])
heap_end = time.time()


sort_start = time.time()

# sorted = []
# for i in range(100000):
#     sorted.append(arr[i])
# sorted.sort()
# print(sorted[99])

arr.sort()

sort_end = time.time()


# heapify_start = time.time()

# heapq.heapify(arr)

# heapify_end = time.time()

print(heap_end - heap_start)
print(sort_end - sort_start)
# print(heapify_end - heapify_start)