MASTI = {1: 'пик', 2: 'треф', 3: 'бубен', 4: 'червей'}
KARDS = {
    6: 'Шестерка',
    7: 'Семерка',
    8: 'Восьмерка',
    9: 'Девятка',
    10: 'Десятка',
    11: 'Валет',
    12: 'Дама',
    13: 'Король',
    14: 'Туз',
}

num_card = int(input("Введите номер карты от 6 до 14: "))
num_mast = int(input("Введите номер масти от 1 до 4: "))


def identify_card(k: int, m: int):
    if 6 <= k <= 14 and 1 <= m <= 4:
        print(f'{KARDS[k]} {MASTI[m]}')
    elif k < 6 or k > 14:
        print("Вы ввели неверный номер карты")
    else:
        print("Вы ввели неверный номер масти")


if __name__ == '__main__':
    identify_card(num_card, num_mast, )
