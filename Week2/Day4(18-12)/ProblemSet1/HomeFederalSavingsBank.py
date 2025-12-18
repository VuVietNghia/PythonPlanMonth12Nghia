def home_federal_savings_bank():
    while True:
        str_input = input("Getting: ")

        if str_input == "x":
            break

        if str_input == "Hello" or str_input == "Hello, Newman":
            print("$0")
        elif str_input == "Hey" or str_input == "How you doing?" or str_input == "How's it going?":
            print("$20")
        else:
            print("$100")

home_federal_savings_bank()