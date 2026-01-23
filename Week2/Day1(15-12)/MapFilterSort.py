# ----- map -----

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = [(temp * 9/5) + 32 for temp in celsius_temps]

print(fahrenheit_temps)

# ----- filter -----

grades = [91, 32, 83, 44, 75, 56, 67]

passing_grades = [i for i in grades if i >= 60]

print(passing_grades)

# ----- sort, sorted -----

# List
car = ["McLaren", "Ferrari", "Williams", "Aston Martin", "Mercedes"]

car.sort(reverse=True)

print(car)

# Tuple
car_tuple = ("McLaren", "Ferrari", "Williams", "Aston Martin", "Mercedes")

car_tuple = tuple(sorted(car_tuple))

print(car_tuple)

# Dict
fruits = {"banana": 105,
          "orange": 73,
          "apple": 72,
          "coconut": 354}

fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

print(fruits)

# Object

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [
    Fruit("banana", 105),
    Fruit("apple", 72),
    Fruit("orange", 73),
    Fruit("coconut", 354)
]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)