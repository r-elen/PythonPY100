def task(str1: str, str2: str, k: int):
    # проверка совпадения строк
    if str1[:k] == str2[:k]:
        print('Да')
    else:
        print('Нет')


if __name__ == "__main__":
    task("abc", "abcde", 3)
    task("abcba", "abcde", 5)
