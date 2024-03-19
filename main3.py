def check_triangle():
    angle1 = float(input("Введіть величину першого кута: "))
    angle2 = float(input("Введіть величину другого кута: "))

    angle3 = 180 - angle1 - angle2

    if angle1 + angle2 + angle3 == 180:
        print("Такий трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Такого трикутника не існує.")

check_triangle()