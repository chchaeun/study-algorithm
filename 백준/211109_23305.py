'''
20XX년, 전국 유일의 마일리지 수강신청 제도를 채택하고 있는 연세대는 
수강변경에서도 혁신적인 시스템을 도입하려고 한다.

20XX년을 기점으로 수강변경 기간 동안에는 "수업 교환"이 허용된다!

수업 교환은 두 사람이 서로 다른 수업을 교환하는 것으로, 
두 사람 모두의 동의가 있어야만 수업 교환이 가능하다.

이때, 삼자 교환은 불가능하지만, 두 사람이 수업을 교환하고, 
교환한 사람 중 다른 사람이 그 수업을 또 다른 사람과 교환하는 것은 허용된다.

처음 제도가 도입되었을 때는 말이 많았지만, 
서로의 전공 수업을 수강하고 싶은 학생들이 수업을 교환하거나, 
마일리지가 많이 남는 졸예자들이 후배들에게 수업을 물려주는 등의 좋은 상황이 많이 생기고 있다.

어느 때와 같이 수강변경이 시작되었다. 
학생들이 수강하고 싶은 수업이 1개씩 주어지고, 
교환하고 싶은 수업이 1개씩 주어질 때, 
수업 교환이 끝나고 본인이 원하는 수업을 수강하지 못하는 인원의 최솟값을 구해보자.
'''

import sys

n = int(input())
a=[0 for _ in range(10000001)]
b=[0 for _ in range(10000001)]

maxLen=0
a_input = list(map(int,sys.stdin.readline().split()))
for i in a_input:
    a[i] += 1
    maxLen = max(i, maxLen)

b_input = list(map(int,sys.stdin.readline().split()))
for i in b_input:
    b[i] += 1
    maxLen = max(i, maxLen)

result=0
for i in range(maxLen+1):
    if b[i]>a[i]:
        result += b[i]-a[i]

print(result)