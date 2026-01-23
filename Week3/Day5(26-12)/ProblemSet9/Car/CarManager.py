from Car import Car
import csv

class CarManager:
    def __init__(self):
        self.cars = []

    def show_all_cars(self):
        for car in self.cars:
            print(f"ID: {car.id_car}, Team: {car.team}, Engine Supply: {car.engine_supply}, Driver: {car.driver}, Car Number: {car.car_number}")

    def add_car(self, team: str, engine_supply: str, driver: str, car_number: str):
        id_car = len(self.cars) + 1
        new_car = Car(id_car, team, engine_supply, driver, car_number)
        self.cars.append(new_car)
        return new_car

    def update_car(self, car_number: str, team: str = None, engine_supply: str = None, 
                   driver: str = None, new_car_number: str = None):
        for car in self.cars:
            if car_number == car.car_number:
                if team:
                    car.team = team
                if engine_supply:
                    car.engine_supply = engine_supply
                if driver:
                    car.driver = driver
                if new_car_number:
                    car.car_number = new_car_number
                return True
        return False

    def remove_car(self, car_number: str):
        for car in self.cars:
            if car_number == car.car_number:
                self.cars.remove(car)
                return True
        return False
    
    def find_car(self, car_number: str):
        for car in self.cars:
            if car_number == car.car_number:
                return car
        return None

    def export_to_csv(self):
        if not self.cars:
            print("No cars to export!")
            return False
        
        try:
            with open("cars.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                writer.writerow(["ID", "Team", "Engine Supply", "Driver", "Car Number"])
                
                for car in self.cars:
                    writer.writerow([car.id_car, car.team, car.engine_supply, car.driver, car.car_number])
            
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
