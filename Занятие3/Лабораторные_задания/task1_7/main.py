# написать функцию для поиска количества месяцев
def count_months(money_capital, salary, spend, increase=0.05):
    months = 1
    money = money_capital + salary
    while money >= spend:
        money -= spend
        spend *= 1 + increase
        money_capital += salary
        months += 1

    return months


if __name__ == "__main__":
    print(count_months(10000, 5000, 6000))  # TODO вызвать функцию и проверить работоспособность
