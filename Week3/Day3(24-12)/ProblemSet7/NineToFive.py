import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s.strip())
    if matches:
        pieces = correct_format(matches)
        if pieces:
            return pieces
    raise ValueError
    

def correct_format(matches):
    start_hour = int(matches.group(1))
    start_minute = matches.group(2)
    start_period = matches.group(3)
    end_hour = int(matches.group(4))
    end_minute = matches.group(5)
    end_period = matches.group(6)
    
    if start_minute is None:
        start_minute = "00"
    if end_minute is None:
        end_minute = "00"
    
    if not (1 <= start_hour <= 12) or not (1 <= end_hour <= 12):
        return None
    
    if not (0 <= int(start_minute) <= 59) or not (0 <= int(end_minute) <= 59):
        return None
    
    start_hour_24 = convert_to_24h(start_hour, start_period)
    end_hour_24 = convert_to_24h(end_hour, end_period)
    
    return f"{start_hour_24:02d}:{start_minute} to {end_hour_24:02d}:{end_minute}"


def convert_to_24h(hour: int, period: str) -> int:
    if period == "AM":
        if hour == 12:
            return 0
        return hour
    else:
        if hour == 12:
            return 12
        return hour + 12



if __name__ == "__main__":
    main()
