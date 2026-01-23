def main():
    text = input("Text: ")
    print(count(text))


def count(s):
    um_count = 0
    
    text_lower = s.lower()
    
    words = text_lower.split()
    
    for word in words:
        clean_word = remove_punctuation(word)
        if clean_word == "um":
            um_count += 1
    
    return um_count


def remove_punctuation(word):
    punctuation = ".,!?;:'\"-()[]{}..."

    clean = word

    while clean and clean[0] in punctuation:
        clean = clean[1:]

    while clean and clean[-1] in punctuation:
        clean = clean[:-1]
    
    return clean


if __name__ == "__main__":
    main()