import constants as con

def take_input(symbol):#вывод либо крестикка либо нолика
    # 1.функция принимает от пользователя то что он ставит
    # 2.определяет что он ставит,
    # 3.определяет не занята ли клетка
    while True:
        value = input('куда поставить ' + symbol + '? ')  # запятая не проходит , только плюс
        if not (value in '123456789'):
            print('некорректный ввод, введите цифру от 1 до 9 на не занятую позицию')
            continue # возвращение выполнения цикла в начало цикла
        value = int(value) # преобразование значения к целому типу
        if str(con.board[value - 1]) in 'XO': #предупреждение некорректного ввода
            print('эта клетка уже занята')
            continue
        con.board[value - 1] = symbol
        break


def check_win():
    """проверка на выигрыш"""
    for i in con.wins_coord:  # если нет условия окончания цикла (break, continue, return),
        # то цикл переходит на else
        if (con.board[i[0] - 1]) == (con.board[i[1] - 1]) == (con.board[i[2] - 1]):
            return con.board[i[1] - 1]
    else:  # не для условия а для цикла
        return False
