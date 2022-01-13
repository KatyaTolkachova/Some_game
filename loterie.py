import random

a = random.randint(1,99)
b = int(input("Введите номер вашего билета:"))
if a == b:
    print("Ваш билет выйграл!")
else:
    print("Ваш билет не выйграл")
