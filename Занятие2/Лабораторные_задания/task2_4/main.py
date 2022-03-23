if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = '    '  # TODO чему равно начальное смещение?
    # TODO как использовать начальное смещение в команде enumerate?
    for i, val in enumerate(phrase):
        initial_offset += ' '
        print(initial_offset, val)
