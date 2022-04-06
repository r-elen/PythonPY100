def is_lucky_number(num: int) -> bool:
    if len(str(num)) != 6:
        raise ValueError('исло должно быть шестизначным') # TODO проверить что число шестизначное

    list_digits = [int(d) for d in str(num)]
    return True if sum(list_digits[:3]) == sum(list_digits[-3:]) else False  # TODO проверить счастливое число или нет


if __name__ == "__main__":
    print(is_lucky_number(123321))
    print(is_lucky_number(111111))
    print(is_lucky_number(123456))
    print(is_lucky_number(456243))
