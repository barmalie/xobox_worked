import constants, place, control




def main():  # совмещение функций
    counter = 0  # отвечает за нумерацию хода
    while True:
        place.create_board()
        if counter % 2 == 0:
            control.take_input('X')
        else:
            control.take_input('O')
        if counter > 3:  # Сделано  3 хода одним игороком.
            # проверка выигрышных комбинаций
            winner = control.check_win()
            if winner:
                place.create_board()
                print(winner, 'выиграл')
                break
        counter += 1
        if counter > 8:  # когда поле заполниться и никто не выиграл
            place.create_board()
            print('ничья')
            break

if __name__ == "__main__":
    main()