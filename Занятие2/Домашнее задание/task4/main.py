if __name__ == "__main__":
    # Write your solution here
    list_ = [12, 4, 6, 5, -1, 35, -5]
    print(list_)

    max_elem = 0
    i_max_elem = 0

    for i, val in enumerate(list_):
        if val > max_elem:
            max_elem = val
            i_max_elem = i

    list_[0], list_[i_max_elem] = list_[i_max_elem], list_[0]
    print(list_)
    pass
