def count_integers():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))

    count = sum(isinstance(num, int) for num in [a, b, c])

    print("Кількість цілих чисел:", count)

count_integers()
