# TODO запишите здесь функцию factorial
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num

    return result


if __name__ == "__main__":
    print(factorial(5))  # TODO распечатать результат выполнения функции factorial от числа 5
