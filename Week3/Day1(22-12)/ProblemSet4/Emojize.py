import emoji

def emojize():
    this_list = []
    str_input = input("Input: ")
    emoji.emojize(str_input)
    this_list.append(str_input)
    print(emoji.emojize(str_input))

emojize()
