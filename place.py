import constants
"""
Создаем поле используем список, можно использовать массив
"""


def create_board():  # создаем поле, без параметров
    for i in range(3):  # выводим поле в три линииб от нуля до двух
        print('-------------')  # верхняя граница
        print('|', constants.board[0 + i * 3], '|', constants.board[1 + i * 3], '|', constants.board[2 + i * 3],
              '|')  # заполняю числами из списка board, перебор всего списка (при помощи принт визуализируем линии поля)
    print('-------------')  # нижняя граница
