def is_exist_fruit(cart_dict: dict, fruit_key: str) -> bool:
    return True if fruit_key in cart_dict else False  # TODO записать с помощью inline if


if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    exist_fruit = "apple"
    missing_fruit = "pineapple"

    print(is_exist_fruit(cart, exist_fruit))
    print(is_exist_fruit(cart, missing_fruit))
