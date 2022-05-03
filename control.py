def take_input(player_token):
    # 1.функция принимает от пользователя то что он ставит
    # 2.определяет что он ставит,
    # 3.определяет не занята ли клетка
    while True:
        value = input('куда поставить ' + player_token + '? ')  # запятая не проходит , только плюс
        if not (value in '123456789'):
            print('ошибочный ввод')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('эта клетка уже занята')
            continue
        board[value - 1] = player_token
        break


def check_win():
    """проверка на выигрыш"""
    for each in wins_coord:  # если нет условия окончания цикла (break, continue, return),
        # то цикл переходит на else
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:  # стоит не для условия а для цикла
        return False
