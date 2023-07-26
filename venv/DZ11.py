while True:
    print("Введите первое число, затем операцию, затем второе число:")
    Number_1 = float(input("Введите первое число: "))
    Operation = input("Введите операцию :")
    Number_2 = float(input("Введите второе число: "))
    if Operation == "+":
        result = Number_1 + Number_2
    elif Operation == "-":
        result = Number_1 - Number_2
    elif Operation == "*":
        result = Number_1 * Number_2
    elif Operation == "/":
        if Number_2 != 0:
            result = Number_1 / Number_2
    else:
        print("Неверная операция!")
    print(result)

    choice = input("Хотите продолжить? (Y/N): ")
    if choice.lower() != "y":
        break