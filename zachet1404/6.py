n = int(input("Введите число: "))

dict_money = {64: 0, 32: 0, 16: 0, 8: 0, 4: 0, 2: 0}

for key in dict_money:
    count = n // key
    if count >= 1:
        dict_money[key] = count
        n -= key * count

print(dict_money, '\n', sum(dict_money.values()))
