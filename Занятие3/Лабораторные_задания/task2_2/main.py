def is_palindrome(str_: str):
    str_no_space = ''.join(str_.lower().split())  # TODO привести строку к единому регистру и избавиться от пробелов

    if str_no_space == str_no_space[::-1]:  # TODO проверка палиндрома
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


if __name__ == "__main__":
    is_palindrome("Кит на море не романтик")
    is_palindrome("Прочая строка")
