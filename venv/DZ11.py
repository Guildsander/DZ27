while True:
    print("Введите первое число, затем операцию, затем второе число:")
    number_1 = float(input("Введите первое число: "))
    operation = input("Введите операцию :")
    number_2 = float(input("Введите второе число: "))
    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "/":
        if number_2 != 0:
            result = number_1 / number_2
    else:
        print("Неверная операция!")
    print(result)

    choice = input("Хотите продолжить? (Y/N): ")
    if choice.lower() != "y":
        break