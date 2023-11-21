from collections import defaultdict

def solution(alp, cop, problems):
    MAX_ABILITY = 150
    goal_alp, goal_cop = 0, 0
    
    problems.extend([(0, 0, 1, 0, 1), (0, 0, 0, 1, 1)])

    for problem in problems:
        alp_req, cop_req = problem[:2]

        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    INF = int(1e9)



print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
# print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))