def main():
    time_input = input("What time is it? ")

    time = convert(time_input)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    time_decimal = hours + (minutes / 60)

    return time_decimal


if __name__ == "__main__":
    main()