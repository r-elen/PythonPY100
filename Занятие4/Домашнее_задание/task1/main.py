def task(num: int) -> bool:
    list_digits = [int(d) for d in str(num)]
    return True if len(set(list_digits)) == 1 else False


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))
