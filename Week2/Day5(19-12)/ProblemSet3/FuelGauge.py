def fuel():
    try:
        fuel =  input("Fraction: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)

        precent = x / y
        precent = precent * 100
        precent = round(precent)

        if precent <= 1:
            print("E")
        elif precent >= 99:
            print("F")
        else:
            print(f"{precent}%")

    except (ValueError, ZeroDivisionError):
        pass

fuel()