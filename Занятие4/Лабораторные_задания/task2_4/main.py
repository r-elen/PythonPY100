def digit_sum(num: int) -> bool:
    # TODO не забыть проерить, что число дожно быть четырехзначное
    if len(str(num)) != 4:
        raise ValueError("Число не четырехзначное :( ")

# TODO проверить кратность суммы цифр
    list_digits = [int(d) for d in str(num)]
    return True if sum(list_digits) % 7 == 0 else False


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(7777))

