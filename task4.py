# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
            if number == 0 or number > 4:
                okey = False
                print("Такого номера четвери нет! ")
        except ValueError:
            print("Это не число!")
    return number

def checkQuarters(x):
    text = "x > 0, y < 0"
    if x == 1:
        text = "x > 0, y > 0"
    elif x == 2:
        text = "x < 0, y > 0"
    elif x == 3:
        text = "x < 0, y < 0"
    print(f"диапазон возможных координат точек в этой четверти: {text}")

quarter = InputNumbers("Задайте номер четверти: ")
checkQuarters(quarter)  


    