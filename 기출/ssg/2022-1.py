from collections import defaultdict
from typing import Final

def solution(members, commands, messageIDs):
    MY: Final = "MY"
    WRITE: Final = "W"

    answer = []

    message_send_order = defaultdict(int)
    my_last_read_order = 0

    order = 1
    for command in commands:
        cmd, person, id = command

        if person == MY:
            my_last_read_order = order
        
        if cmd == WRITE:
            message_send_order[id] = order
            order += 1
        
    for id in messageIDs:
        isRead = message_send_order[id] <= my_last_read_order
        answer.append(isRead)

    return answer


test_members = ["A", "B"]
test_commands = [["W", "MY", "1"], ["W", "A", "7"], ["W", "B", "4"], ["W", "MY", "9"], ["W", "A", "11"], ["R","B",""]]
test_messages = ["7", "11"]

print(solution(test_members, test_commands, test_messages))