import random

a = random.randint(0, 100)
if a == 0:
    print("Дождя не будет")
elif a <= 24:
    print("Будет коротковременный дождь")
elif a >= 25 and a < 50:
    print("Будет небольшой дождь")
elif a >= 50 and a < 75:
    print("Будет сильный дождь")
else:
    print("Будет проливной дождь")