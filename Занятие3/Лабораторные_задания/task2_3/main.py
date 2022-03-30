def get_unique_words_my(str_words: str):
    # TODO найти список слов в строке исключив пустые строки
    words_set = set(str_words.split())

    # TODO вывести множество уникальных слов
    # words_set = set(words_list)

    return words_set


def get_unique_words(str_words: str):
    words_list_without_empty_string = []
    for word in str_words.split(" "):
        if word:
            words_list_without_empty_string.append(word)

    return set(words_list_without_empty_string)


if __name__ == "__main__":
    print(get_unique_words_my("Здесь много разных слов.   Возможно и много повторений."))
    print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
