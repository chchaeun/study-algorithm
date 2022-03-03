def solution(n):
    tri = [[0]*i for i in range(1, n+1)]
    down = True
    number = 1
    flag=1
    floor = len(tri)-1
    down_i_start, down_i_end = 0, len(tri)
    up_i_start, up_i_end = len(tri)-1, -1
    j_level = 0
    while flag==1:
        flag=0
        if down:
            for i in range(down_i_start, down_i_end):
                for j in range(j_level, len(tri[i])-j_level):
                    if tri[i][j]==0:
                        tri[i][j] = number
                        number+=1
                        if floor!=i:
                            break
            floor-=1
            down_i_start+=2
            down_i_end -=1
            
        else:
            for i in range(up_i_start, up_i_end, -1):
                for j in range(len(tri[i])-1-j_level, -1+j_level, -1):
                    if tri[i][j] == 0:
                        tri[i][j] = number
                        number+=1
                        break   
            j_level+=1
            up_i_start-=1
            up_i_end+=2
        down = not down
        for t in tri:
            if 0 in t:
                flag=1
    answer = []
    for t in tri:
        answer.extend(t)
    return answer
print(solution(5))