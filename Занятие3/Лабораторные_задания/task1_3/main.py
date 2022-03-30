def get_list_number_divisors(number):
    # TODO найти список делителей числа number
    list_num = []
    for num in range(1, number + 1):
        if number % num == 0:
            list_num.append(num)
    return list_num


if __name__ == "__main__":
    print(get_list_number_divisors(42))
