def check_answer(answer: str) -> str:
    if answer == "42" or answer == "forty-two" or answer == "Forty-two":
        return "Yes"
    else:
        return "No"


def deep_thought():

    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    result = check_answer(answer)
    print(result)

if __name__ == "__main__":
    deep_thought()