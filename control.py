import constants

def take_input(symbol):
    # 1.функция принимает от пользователя то что он ставит
    # 2.определяет что он ставит,
    # 3.определяет не занята ли клетка
    while True:
        value = input('куда поставить ' + symbol + '? ')  # запятая не проходит , только плюс
        if not (value in '123456789'):
            print('ошибочный ввод')
            continue
        value = int(value)
        if str(constants.board[value - 1]) in 'XO':
            print('эта клетка уже занята')
            continue
        constants.board[value - 1] = symbol
        break


def check_win():
    """проверка на выигрыш"""
    for each in constants.wins_coord:  # если нет условия окончания цикла (break, continue, return),
        # то цикл переходит на else
        if (constants.board[each[0] - 1]) == (constants.board[each[1] - 1]) == (constants.board[each[2] - 1]):
            return constants.board[each[1] - 1]
    else:  # не для условия а для цикла
        return False
