def taqueria():
    dict_of_food = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    title_cased = 0.0

    while True:
        try:
            item = input("Item: ")
            if item.lower() == "x":
                break
            if item in dict_of_food.keys():
                title_cased += dict_of_food[item]
                print(title_cased)

        except ValueError:
            pass

taqueria()

