desk = [['X', '-', '-'],
        ['-', 'O', '-'],
        ['-', '-', '-']]
count_steps = 2
change_gamer = True
def showDesk(desk):
    print(' ', 0, 1, 2)
    for i in range(3):
        print(i, end = ' ')
        print(*desk[i])

def input_coordinates():
    pass

def valid_coordinates(x, y, desk):
    if desk[x][y] == 'X' or desk[x][y] == 'O': return False
    else: return True


while count_steps:
    # start code
    X, Y = map(int, input("Введите координаты ряда и столбца через пробел ").split())
    
    # end code
    count_steps -= 1

    if valid_coordinates(X,Y,desk):
        if change_gamer:
            desk[X][Y] = 'X'
            showDesk(desk)
            change_gamer  = False
        else: 
            desk[X][Y] = 'O'
            showDesk(desk)
            change_gamer = True
    else:
        print('Клетка занята. Выбирите другую ячейку')
        showDesk(desk)
        count_steps += 1


# showDesk(desk)