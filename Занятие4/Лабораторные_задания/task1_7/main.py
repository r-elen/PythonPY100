if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]

    mean = sum(list_)/len(list_)
    new_list = [i - mean for i in list_ ]  # TODO Заполните список с помощью list comprehension

    print(new_list)
