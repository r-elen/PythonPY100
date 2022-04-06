if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9, -1]
      # TODO получить два списка четных и нечетных чисел
    list_even = [i for i in list_ if i % 2 == 0]
    list_odd = [i for i in list_ if i % 2 != 0]

    len_even = len(list_even)  # TODO найти длины этих списков
    len_odd = len(list_odd)

    if len_even != len_odd:  # TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
        print(f'Четных: {len_even}') if len_even > len_odd else print(f'Нечетных: {len_odd}')
    else:
        print('Одинаковое кол-во четных и нечетных')
