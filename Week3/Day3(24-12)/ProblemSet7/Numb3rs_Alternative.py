import re


def validate_complex_regex(ip: str) -> bool:
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    return bool(re.search(pattern, ip))


def validate_simple(ip: str) -> bool:
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    
    if not match:
        return False
    
    for i in range(1, 5):
        octet = int(match.group(i))
        if octet < 0 or octet > 255:
            return False
    
    return True


if __name__ == "__main__":
    test_cases = [
        ("192.168.1.1", True),
        ("255.255.255.255", True),
        ("0.0.0.0", True),
        ("275.3.6.28", False),
        ("192.168.1", False),
        ("cat", False),
    ]
    
    print("Testing both methods:")
    for ip, expected in test_cases:
        simple = validate_simple(ip)
        complex_regex = validate_complex_regex(ip)
        
        status = "✓" if simple == expected and complex_regex == expected else "✗"
        print(f"{status} {ip:20s} | Simple: {str(simple):5s} | Complex: {str(complex_regex):5s} | Expected: {expected}")
