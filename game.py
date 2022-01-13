import random

I = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага:"))  
C = random.randint(1, 3)
print(I, C)
if I == 1 and C == 1:
    print("Ничья")
elif I == 1 and C == 2:
    print("Вы выйграл!")
elif I == 1 and C == 3:
    print("Вы проиграли")
elif I == 2 and C == 1:
    print("Вы проиграли")
elif I == 2 and C == 2:
    print("Ничья")
elif I == 2 and C == 3:
    print("Вы выйграли!")
elif I == 3 and C == 1:
    print("Вы выйграли!")
elif I == 3 and C == 2:
    print("Вы проиграли")
elif I == 3 and C == 3:
    print("Ничья")
