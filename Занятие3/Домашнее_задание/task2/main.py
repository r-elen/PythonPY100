def check_string(str_):
    # TODO проверить что в строку входят только символы 1 и 0
    if not str_:
        return False
    possible_digits = ['0', '1']
    for i in str_:
        if i not in possible_digits:
            return False

    return True


if __name__ == "__main__":
    print(check_string("1010101010"))
    print(check_string("101021231010103"))
    print(check_string("asdawqe"))
    print(check_string(""))
