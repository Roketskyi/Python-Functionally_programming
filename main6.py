def replace_integers():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))

    if a != b:
        replacement = max(a, b)
        a = replacement
        b = replacement
    else:
        a = b = 0

    print("Замінені значення:")
    print("a =", a)
    print("b =", b)

replace_integers()
