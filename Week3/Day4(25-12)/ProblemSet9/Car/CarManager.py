from Car import Car
import csv

class CarManager:
    def __init__(self):
        self.cars = []

    def show_all_cars(self):
        for car in self.cars:
            print(f"ID: {car.id_car}, Team: {car.team}, Engine Supply: {car.engine_supply}, Driver: {car.driver}, Car Number: {car.car_number}")

    def add_car(self):
        id_car = len(self.cars) + 1
        team = input("Enter team: ").strip()
        engine_supply = input("Enter engine supply: ").strip()
        driver = input("Enter driver: ").strip()
        car_number = input("Enter car number: ").strip()
        self.cars.append(Car(id_car, team, engine_supply, driver, car_number))

    def update_car(self):
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

if __name__ == "__main__":
    car_manager = CarManager()

    while True:
        print("\n" + "="*50)
        print("CAR MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Car")
        print("2. Update Car")
        print("3. Remove Car")
        print("4. Find Car")
        print("5. Show All Cars")
        print("6. Export to CSV")
        print("7. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            car_manager.add_car()
        elif choice == "2":
            car_manager.update_car()
        elif choice == "3":
            car_manager.remove_car()
        elif choice == "4":
            car_manager.find_car()
        elif choice == "5":
            print("\n--- All Cars ---")
            car_manager.show_all_cars()
        elif choice == "6":
            if car_manager.export_to_csv():
                print("Cars exported to CSV successfully!")
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")