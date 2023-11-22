def solution(alp, cop, problems):
    goal_alp, goal_cop = 0, 0
    
    for problem in problems:
        alp_req, cop_req = problem[:2]

        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    INF = int(1e9)

    dp = [[INF] * (goal_cop + 1) for _ in range(goal_alp + 1)]

    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)

    dp[alp][cop] = 0

    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            if i < goal_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < goal_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, goal_alp)
                    new_cop = min(j + cop_rwd, goal_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    
    return dp[goal_alp][goal_cop]

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))