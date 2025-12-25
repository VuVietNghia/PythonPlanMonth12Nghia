from datetime import date
import inflect


def main():
    while True:
        try:
            birthday = input("Date of birth: ")
            birthday = date.fromisoformat(birthday)
            time_now = date.today()
            live = time_now - birthday
            
            minutes = live.days * 24 * 60
            p = inflect.engine()
            minutes_in_words = p.number_to_words(minutes, andword="")
            print(f"{minutes_in_words.capitalize()} minutes")
            break
        except ValueError:
            print("Invalid date")


if __name__ == "__main__":
    main()