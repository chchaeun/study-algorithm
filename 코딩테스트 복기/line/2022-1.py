def solution(logs):
    keys = ['team_name', 'application_name', 'error_level', 'message']
    correct = 0
    for log in logs:
        if len(log)>100: continue
        slog = log.split(" ")
        if len(slog) == 12:
            for i in range(0, 12, 3):
                if slog[i]!=keys[i//3]:
                    break
            else:
                for i in range(2, 12, 3):
                    if not slog[i].isalpha():
                        break
                else: correct += 1
    return len(logs)-correct


test1 = ["team_name : db application_name : dbtest error_level : info message : test", 
     "team_name : test application_name : I DONT CARE error_level : error message : x", 
     "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", 
     "team_name : oberervability application_name : LogViewer error_level : error"]

# test2 = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", 
#          "no such file or directory", 
#          "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", 
#          "team_name : recommend application_name : recommend error_level : info message : Success!", 
#          "   team_name : db application_name : dbtest error_level : info message : test", 
#          "team_name     : db application_name : dbtest error_level : info message : test", 
#          "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
print(solution(test1))
# print(solution(test2))
