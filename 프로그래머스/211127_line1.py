from collections import deque
def solution(record):
    answer = []
    fifo = deque()
    lifo = []
    a=0
    b=0
    top=-1
    for i in range(2):
        for r in record:
            r_list = r.split()
            if i==0:
                if r_list[0]=='P':
                    temp=[]
                    temp.append(int(r_list[1]))
                    temp.append(int(r_list[2]))
                    fifo.append(temp)
                else:
                    fifo_quan = int(r_list[2])
                    while fifo_quan>0:
                        if fifo[0][1]<= fifo_quan:
                            a+= fifo[0][0]*fifo[0][1]
                            fifo_quan-=fifo[0][1]
                            fifo.popleft()
                        else:
                            a+= fifo[0][0]*fifo_quan
                            fifo[0][1]-=fifo_quan
                            fifo_quan=0
            else:
                if r_list[0]=='P':
                    temp=[]
                    temp.append(int(r_list[1]))
                    temp.append(int(r_list[2]))
                    lifo.append(temp)
                    top+=1
                else:            
                    lifo_quan = int(r_list[2])        
                    while lifo_quan>0:
                        if lifo[top][1]<= lifo_quan:
                            b+= lifo[top][0]*lifo[top][1]
                            lifo_quan-=lifo[top][1]
                            lifo.pop()
                            top-=1
                        else:
                            b+= lifo[top][0]*lifo_quan
                            lifo[top][1]-=lifo_quan
                            lifo_quan=0       

    answer.append(a)
    answer.append(b)
    return answer

record = ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]
print(solution(record))