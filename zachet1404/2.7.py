a = int(input("Введите число: "))


def is_sum_first_last_equal(num: int) -> bool:
    list_num = [int(d) for d in str(num)]
    if 3 < len(list_num) < 5:  # len(list_num) != 4
        sum_first = sum(list_num[:2])
        sum_last = sum(list_num[2:])
        return True if sum_first == sum_last else False
    else:
        print("Вы ввели не четырехзначное число")


def is_sum_equal_7(num: int) -> bool:
    list_num = [int(d) for d in str(num)]
    if 3 < len(list_num) < 5:
        return True if sum(list_num) % 7 == 0 else False
    else:
        print("Вы ввели не четырехзначное число")


if __name__ == '__main__':
    print(is_sum_first_last_equal(a))
    print(is_sum_equal_7(a))
