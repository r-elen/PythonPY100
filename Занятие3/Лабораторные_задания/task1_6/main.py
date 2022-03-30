# TODO написать функцию для поиска необходимой суммы денег
def sum_money(salary, spend, month=10, rost=0.03):
    need = 0
    for _ in range(month):
        need += spend - salary
        spend *= 1 + rost

    return need


if __name__ == "__main__":
    print(sum_money(5000, 6000))  # TODO вызвать функцию и проверить работоспособность

