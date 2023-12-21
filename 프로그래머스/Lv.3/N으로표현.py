def solution(N, number):
    global answer 
    answer = int(1e9)
    orders = ['+', '-', '*', '/']

    def getOrderResult(order, num1, num2):
        if order == '+':
            return num1 + num2
        if order == '-':
            return num1 - num2
        if order == '*':
            return num1 * num2
        if order == '/':
            return int(num1 / num2)

    def dfs(current, count):
        if current == number:
            global answer
            answer = min(answer, count)
            return

        if count == 9:
            return

        for order in orders:
            dfs(getOrderResult(order, current, N), count+1)
            for i in range(2, 8-count+1):
                dfs(getOrderResult(order, current, int(str(N) * i)), count+i)

    dfs(0, 0)
    
    return answer if answer < 9 else -1

solution(5, 12)
solution(2, 11)