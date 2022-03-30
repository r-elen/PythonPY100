def input_numbers():
    # TODO выберите нужный цикл, чтобы получать числа с клавиатуры
    list_num = []

    while True:
        input_num = int(input('Введите новое число: ', ))

        if input_num < 0:
            list_num.append(input_num)
            break

        if 3 <= input_num <= 13:
            list_num.append(input_num)

    return list_num


if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
