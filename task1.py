# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number

day = InputNumbers("Введите число: ")

if 6 <= day <= 7:
        print("Да")
elif 0 < day < 6:
        print("Нет")
else:
        print("число вне пределов 7 дней")