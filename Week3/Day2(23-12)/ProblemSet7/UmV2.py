import re

def main():
    print(count(input("Text: ")))

def count(text):
    matches = re.findall(r'\bum\b', text, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
