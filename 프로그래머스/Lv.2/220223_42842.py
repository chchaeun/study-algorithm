def solution(brown, yellow):
    for height in range(1, yellow+1):
        width = yellow//height if not yellow%height else 0
        if width<height: break
        if brown == (width+height+2)*2:
            return [width+2, height+2]
        
print(solution(50, 22))