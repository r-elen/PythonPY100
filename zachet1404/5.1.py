a = int(input("Введите число: "))

while a != 1:
    if a % 2 == 0:
        a /= 2
    elif a % 2 != 0:
        a *= 3
        a += 1

print(a)


