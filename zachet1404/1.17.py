A = int(input("ведите число: "))
B = int(input("ведите число: "))
C = int(input("ведите число: "))
D = int(input("ведите число: "))

if A / B > C / D:
    print("A/B больше чем C/D")
elif C / D > A / B:
    print("C/D больше чем A/B")
else:
    print("Дроби равны")
