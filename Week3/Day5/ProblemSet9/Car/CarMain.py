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