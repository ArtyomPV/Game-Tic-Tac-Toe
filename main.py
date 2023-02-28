desk = [[' ', '0', '1', '2'],
        ['0', '-', '-', '-'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-']]

def showDesk(desk):
    for i in range(4):
        print(*desk[i])

showDesk(desk)