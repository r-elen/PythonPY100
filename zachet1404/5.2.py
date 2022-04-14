n_km = int(input("Введите км: "))
y_proc = int(input("Введите проценты: "))
x_days = int(input("Введите кол-во дней: "))

while x_days == 0:
    n_km += n_km * (y_proc / 100)
    x_days -= 1

print(n_km)
