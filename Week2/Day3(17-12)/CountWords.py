def count_words(text: str) -> dict:
    this_list = []
    for i in text.lower().split():
        cleaned_word = i.strip('.,!?;:\"\'')
        this_list.append(cleaned_word)
    
    word_count = {}
    for word in this_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

print(count_words("Hello world python, hello world python"))