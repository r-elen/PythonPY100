def task(num: int):
    list_digits = [int(d) for d in str(num)]  # TODO сформировать список цифр

    if 4 in list_digits and 8 in list_digits or 9 in list_digits:  # TODO записать условие
        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
