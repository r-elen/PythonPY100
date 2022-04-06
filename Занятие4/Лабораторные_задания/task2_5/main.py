def is_palindrome_number(num: int) -> bool:
    if num < 0:
        raise ValueError('Неверное число')  # TODO проверить что число больше или равно нулю

    return True if str(num) == str(num)[::-1] else False  # TODO проверить является ли число палиндром


if __name__ == "__main__":
    print(is_palindrome_number(1234))
    print(is_palindrome_number(1234321))
