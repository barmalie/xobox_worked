import constants as con
"""
Создаем поле используем список, можно использовать массив
"""


def create_board():  # создаем поле, без параметров
    for i in range(3):  # выводим поле в три линииб от нуля до двух
        print('-------------')  # верхняя граница
        print('|', con.board[0 + i * 3], '|', con.board[1 + i * 3], '|', con.board[2 + i * 3],
              '|')  # заполняю числами из списка board, перебор всего списка (при помощи принт визуализируем линии поля)
    print('-------------')  # нижняя граница
