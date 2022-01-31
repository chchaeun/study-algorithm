def solution(name):
    # 아스키코드로 변환
    name = list(map(ord, list(name)))
    
    # 상하 먼저 계산
    answer = sum([min(n-ord('A'), ord('Z')-n+1) for n in name])
    
    # 문자열 최대 길이 20
    _min = 21
    
    # 처음에 움직이는 방향 오른쪽/왼쪽
    for d in [1, -1]:
        
        # 어느 인덱스에서 한번 꺾을 건지
        for i in range(len(name)):
            direct = d
            
            # 문자 바꾸기 위해 가야 할 곳(A가 아닌 곳)을 1로 표시
            togo = [0 if n==ord('A') else 1 for n in name]
            
            # 출발
            cur = 0
            count = 0
            
            while True:
                # 도는 곳 만나면 방향 바꿈 (음수 인덱스도 따져야 함)
                if cur == i or len(name)+cur == i :
                    direct = -direct
                togo[cur] = 0
                
                # 모든 배열 방문하면 중단
                if sum(togo)==0: break
                
                count += 1
                cur += direct
            _min = min(_min, count)
    answer+=_min
    return answer

print(solution('ABABAAAAAAABA'))