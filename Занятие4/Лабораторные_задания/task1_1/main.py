def task(n: int, m: int) -> list:  # TODO записать функцию с аннотацией типов
    return [i ** 2 for i in range(n, m + 1)]


if __name__ == "__main__":
    number_n = 10
    number_m = 20

    print(task(number_n, number_m))
