def value(greeting):
    if greeting == "Hello" or greeting == "Hello, Newman":
        return 0
    elif greeting == "Hey" or greeting == "How you doing?" or greeting == "How's it going?":
        return 20
    else:
        return 100


def main():
    while True:
        str_input = input("Greeting: ")
        
        if str_input == "x":
            break
        
        price = value(str_input)
        print(f"${price}")


if __name__ == "__main__":
    main()