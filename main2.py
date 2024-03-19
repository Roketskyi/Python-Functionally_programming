import math

def distance_to_origin(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def closer_point():
    x1 = float(input("Введіть координату x1: "))
    y1 = float(input("Введіть координату y1: "))
    x2 = float(input("Введіть координату x2: "))
    y2 = float(input("Введіть координату y2: "))

    dist1 = distance_to_origin(x1, y1)
    dist2 = distance_to_origin(x2, y2)

    if dist1 < dist2:
        print("Точка A ближче до початку координат.")
    elif dist2 < dist1:
        print("Точка B ближче до початку координат.")
    else:
        print("Точки розташовані на однаковій відстані до початку координат.")

closer_point()
