def replace_numbers():
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))

    if x != y:
        smaller = min(x, y)
        larger = max(x, y)
        x = (smaller + larger) / 2
        y = 2 * smaller * larger
    else:
        x = y = 0

    print("Замінені значення:")
    print("x =", x)
    print("y =", y)

replace_numbers()
