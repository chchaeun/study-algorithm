n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

# result=0
# count=0
# for i in range(m):
#     if count != k:
#         result += first
#         count+=1
#     else:
#         result += second
#         count=0
# print(result)

count = int(m/(k+1)) * k + m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
