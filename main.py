import place as p
import control as c

def main():  # совмещение функций
    counter = 0  # отвечает за нумерацию хода
    while True:
        p.create_board()
        if counter % 2 == 0:
            c.take_input('X')
        else:
            c.take_input('O')
        if counter > 3:  # Сделано  3 хода одним игороком.
            # проверка выигрышных комбинаций
            winner = c.check_win()
            if winner:
                p.create_board()
                print(winner, 'выиграл')
                break
        counter += 1
        if counter > 8:  # когда поле заполниться и никто не выиграл
            p.create_board()
            print('ничья')
            break

if __name__ == "__main__":
    main()