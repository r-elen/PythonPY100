def print_digits_a():
    a = 10
    while a < 31:
        print(a)
        a += 1


def print_digits_b():
    a = 10
    while True:
        if a < 31:
            print(a)
            a += 1
        else:
            break

        if not a < 31:
            break
        print(a)
        a += 1




if __name__ == '__main__':
    print_digits_a()
    print('-' * 20)
    print_digits_b()
