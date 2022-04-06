def task(num: int) -> bool:  # TODO добавить аннотацию типов
    # TODO найти сумму цифр числа и понять двузначная ли она
    sum_digits = sum([int(d) for d in str(abs(num))])
    return True if sum_digits / 10 >= 1 else False


if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
