def get_max_length_word(str_words):
    words_list = str_words.split()  # TODO получить список непустых слов

    max_len = 0  # пусть изначально длина самого длинного слова равна 0
    for word in words_list:
        if len(word) > max_len:
            max_len = len(word)

    # TODO составить список из слов, длина которых равна самой большой
    list_max_words = []
    for word in words_list:
        if len(word) == max_len:
            list_max_words.append(word)

    return list_max_words


if __name__ == "__main__":
    print(get_max_length_word("раз два три"))
    print(get_max_length_word("раз два три четыре"))
