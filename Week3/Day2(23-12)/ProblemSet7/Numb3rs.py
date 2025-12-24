import re


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    match = re.search(pattern, ip)
    
    if not match:
        return False
    
    for i in range(1, 5):
        octet = int(match.group(i))
        if octet < 0 or octet > 255:
            return False
    
    return True


def main():
    ip = input("IPv4 Address: ").strip()
    
    if validate(ip):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()