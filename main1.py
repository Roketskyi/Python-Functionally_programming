def process_numbers():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    num3 = float(input("Введіть третє число: "))

    def square_or_fourth_power(num):
        if num >= 0:
            return num ** 2
        else:
            return num ** 4

    result1 = square_or_fourth_power(num1)
    result2 = square_or_fourth_power(num2)
    result3 = square_or_fourth_power(num3)

    print("Результати піднесення до квадрата або четвертої ступеня:")
    print("Число 1:", result1)
    print("Число 2:", result2)
    print("Число 3:", result3)

process_numbers()
