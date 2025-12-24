def main():
    text = input("Input: ")
    output = remove_vowels(text)
    print(f"Output: {output}")


def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    
    return result


if __name__ == "__main__":
    main()
