A = 5
B = 51
C = 7

cond_1 = A < 45 and B >= 45 and C >=45
cond_2 = B < 45 and C >= 45 and A >=45
cond_3 = C < 45 and A >= 45 and B >=45

if cond_1 or cond_2 or cond_3:
    print('True')
else:
    print('False')
