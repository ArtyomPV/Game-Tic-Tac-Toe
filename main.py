desk = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
count_steps = 9

change_gamer = True
gamer = 'X'
def showDesk(desk):
    print(' ', 0, 1, 2)
    for i in range(3):
        print(i, end = ' ')
        print(*desk[i])

def valid_coordinates(x, y, desk):
    if desk[x][y] == 'X' or desk[x][y] == 'O': 
        return False
    else: 
        return True

def check_winner(desk, symbol):
    for i in range(3):
        if all(desk[i][j] == symbol for j in range(3)):
            return True
        elif all(desk[j][i] == symbol for j in range(3)):
            return True
        elif all(desk[j][j] == symbol for j in range(3)):
            return True
        elif all(desk[j][2 - j] == symbol for j in range(3)):
            return True
    return False

showDesk(desk)
while count_steps:

    print(f'Ходит игрок {gamer}')
    X, Y = map(int, input("Введите координаты ряда и столбца через пробел ").split())
    count_steps -= 1

    if valid_coordinates(X,Y,desk):
        if change_gamer:
            desk[X][Y] = 'X'
            showDesk(desk)
            gamer = 'O'
            change_gamer  = False
        else: 
            desk[X][Y] = 'O'
            showDesk(desk)
            gamer = 'X'
            change_gamer = True
    else:
        print('Клетка занята. Выберите другую ячейку')
        # showDesk(desk)
        count_steps += 1
    if check_winner(desk, 'O'):
        print('Winner gamer O')
        break
    if check_winner(desk, 'X'):
        print('Winner gamer X')
        break
