A = int(input("ведите число: "))
B = int(input("ведите число: "))
C = int(input("ведите число: "))

cond_1 = A < 45 and B >= 45 and C >= 45
cond_2 = A >= 45 and B < 45 and C >= 45
cond_3 = A >= 45 and B >= 45 and C < 45

if cond_1 or cond_2 or cond_3:
    print(True)
else:
    print(False)
