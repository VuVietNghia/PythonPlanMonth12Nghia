from Car import Car
import csv

class CarManager:
    def __init__(self):
        self.cars = []

    def show_all_cars(self):
        for car in self.cars:
            print(f"ID: {car.id_car}, Team: {car.team}, Engine Supply: {car.engine_supply}, Driver: {car.driver}, Car Number: {car.car_number}")

    def add_car(self):
        try:
            id_car = len(self.cars) + 1
            team = input("Enter team: ").strip()
            engine_supply = input("Enter engine supply: ").strip()
            driver = input("Enter driver: ").strip()
            car_number = input("Enter car number: ").strip()
            self.cars.append(Car(id_car, team, engine_supply, driver, car_number))
        except ValueError:
            pass

    def update_car(self):
        try:
            car_number = input("Enter car number to update: ").strip()
            for car in self.cars:
                if car_number == car.car_number:
                    team = input("Enter team: ").strip()
                    engine_supply = input("Enter engine supply: ").strip()
                    driver = input("Enter driver: ").strip()
                    car_number = input("Enter car number: ").strip()
                    if team is not None:
                        car.team = team
                    if engine_supply is not None:
                        car.engine_supply = engine_supply
                    if driver is not None:
                        car.driver = driver
                    if car_number is not None:
                        car.car_number = car_number
                    print("Car updated successfully")
                    return True
            print("Car not found")
            return False
        except ValueError:
            pass

    def remove_car(self):
        car_number = input("Enter car number to remove: ").strip()
        for car in self.cars:
            if car_number == car.car_number:
                self.cars.remove(car)
                print("Car removed successfully")
                return True
        print("Car not found")
        return False
    
    def find_car(self):
        car_number = input("Enter car number to find: ").strip()
        for car in self.cars:
            if car_number == car.car_number:
                print(f"ID: {car.id_car}, Team: {car.team}, Engine Supply: {car.engine_supply}, Driver: {car.driver}, Car Number: {car.car_number}")
                return car
        print("Car not found")
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
