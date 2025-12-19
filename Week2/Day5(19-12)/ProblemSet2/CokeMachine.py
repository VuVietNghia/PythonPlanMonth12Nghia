def coke_machine():
    due = 50
    while due > 0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            due -= coin
    change = abs(due)
    print(f"Change Owed: {change}")

coke_machine()