def outdated():
    month_list = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        str_date = input("Date: ").strip()
        if "/" in str_date:
            try:
                parts = str_date.split("/")
                if len(parts) != 3:
                    continue
                month, day, year = parts
                month = int(month)
                day = int(day)
                year = int(year)
            except ValueError:
                continue

        elif "," in str_date:
            try:
                parts = str_date.split(",")
                if len(parts) != 2:
                    continue
                month_day = parts[0].strip()
                year_str = parts[1].strip()

                month_day_parts = month_day.split()
                if len(month_day_parts) != 2:
                    continue

                month_name = month_day_parts[0].strip()
                day_str = month_day_parts[1].strip()

                if month_name not in month_list:
                    continue

                month = month_list.index(month_name) + 1
                day = int(day_str)
                year = int(year_str)

            except ValueError:
                continue

        else:
            continue

        if month < 1 or month > 12:
            continue
        if day < 1 or day > 31:
            continue

        break

    print(f"{month:02d}/{day:02d}/{year}")

outdated()
