def count_integers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = sum(num.is_integer() for num in [a, b, c])

    print("Кількість цілих чисел:", count)

count_integers()
