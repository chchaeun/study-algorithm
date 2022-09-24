def solution(alp, cop, problems):
    
    problems.sort(key=lambda x: (x[0], x[1]))

    alp_goal, cop_goal = alp, cop
    for problem in problems:
        alp_goal, cop_goal = max(alp_goal, problem[0]), max(cop_goal, problem[1])

    INF = 1000000000
    dp = [[INF for _ in range(cop_goal + 1)] for _ in range(alp_goal + 1)]
    dp[alp][cop] = 0

    for i in range(alp, alp_goal + 1):
        for j in range(cop, cop_goal + 1):
            compare = [dp[i][j], dp[i-1][j] + 1, dp[i][j-1] + 1]
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if alp_req <= i-alp_rwd and cop_req <= j-cop_rwd:
                    compare.append(dp[i-alp_rwd][j-cop_rwd]+cost)
                else:
                    break
            dp[i][j] = min(compare)
    
    for x in dp:
        for y in x:
            print(y, end=" ")
        print()

    return dp[alp_goal][cop_goal]

solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])
solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])