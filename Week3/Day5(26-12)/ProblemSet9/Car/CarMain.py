from CarManager import CarManager

if __name__ == "__main__":
    car_manager = CarManager()

    while True:
        print("\n" + "=" * 50)
        print("CAR MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Car")
        print("2. Update Car")
        print("3. Remove Car")
        print("4. Find Car")
        print("5. Show All Cars")
        print("6. Export to CSV")
        print("7. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            # Collect input from user
            team = input("Enter team: ").strip()
            engine_supply = input("Enter engine supply: ").strip()
            driver = input("Enter driver: ").strip()
            car_number = input("Enter car number: ").strip()
            
            # Pass to CarManager
            car = car_manager.add_car(team, engine_supply, driver, car_number)
            print(f"✅ Car added successfully! ID: {car.id_car}")
            
        elif choice == "2":
            # Collect car number to update
            car_number = input("Enter car number to update: ").strip()
            
            # Collect new values (allow empty to skip)
            print("(Press Enter to skip a field)")
            team = input("Enter new team: ").strip() or None
            engine_supply = input("Enter new engine supply: ").strip() or None
            driver = input("Enter new driver: ").strip() or None
            new_car_number = input("Enter new car number: ").strip() or None
            
            # Pass to CarManager
            if car_manager.update_car(car_number, team, engine_supply, driver, new_car_number):
                print("✅ Car updated successfully!")
            else:
                print("❌ Car not found")
                
        elif choice == "3":
            # Collect car number to remove
            car_number = input("Enter car number to remove: ").strip()
            
            # Pass to CarManager
            if car_manager.remove_car(car_number):
                print("✅ Car removed successfully!")
            else:
                print("❌ Car not found")
                
        elif choice == "4":
            # Collect car number to find
            car_number = input("Enter car number to find: ").strip()
            
            # Pass to CarManager
            car = car_manager.find_car(car_number)
            if car:
                print("✅ Car found!")
                print(f"ID: {car.id_car}, Team: {car.team}, Engine Supply: {car.engine_supply}, Driver: {car.driver}, Car Number: {car.car_number}")
            else:
                print("❌ Car not found")
                
        elif choice == "5":
            print("\n--- All Cars ---")
            car_manager.show_all_cars()
            
        elif choice == "6":
            if car_manager.export_to_csv():
                print("✅ Cars exported to CSV successfully!")
                
        elif choice == "7":
            print("👋 Exit")
            break
            
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 7.")