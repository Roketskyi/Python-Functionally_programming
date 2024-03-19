def count_positive_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = sum(num > 0 for num in [a, b, c])

    print("Кількість додатніх чисел:", count)

count_positive_numbers()
