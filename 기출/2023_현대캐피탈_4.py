N = 50
quantities = [[1, 20], [2, 70], [3, 80]]

global answer
answer = -1

def nCr(numOfChoices, depth, totalQuantity):
    global answer
    if numOfChoices == len(quantities) or depth == len(quantities):
        answer = max(answer, totalQuantity)
        return

    date, quantity = quantities[depth]

    if date * N - totalQuantity >= quantity:
        nCr(numOfChoices + 1, depth + 1, totalQuantity + quantity)
        nCr(numOfChoices, depth + 1, totalQuantity)
    else:
        nCr(numOfChoices, depth + 1, totalQuantity)

nCr(0, 0, 0)
print(answer)