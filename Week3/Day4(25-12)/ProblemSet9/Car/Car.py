class Car:
    def __init__(self, id_car, team, engine_supply, driver, car_number):
        self.id_car = id_car
        self.team = team
        self.engine_supply = engine_supply
        self.driver = driver
        self.car_number = car_number

    def __str__(self):
        return f"{self.id_car} {self.team} {self.engine_supply} {self.driver} {self.car_number}"
