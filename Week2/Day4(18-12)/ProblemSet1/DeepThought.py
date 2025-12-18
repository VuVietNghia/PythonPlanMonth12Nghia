def check_answer(answer: str) -> str:
    """
    Check if the answer to the Great Question is correct.
    
    Args:
        answer: The user's answer as a string
        
    Returns:
        "Yes" if correct, "No" if incorrect
    """
    # Check for valid answers: "42", "forty-two", "Forty-two"
    if answer == "42" or answer == "forty-two" or answer == "Forty-two":
        return "Yes"
    else:
        return "No"


def deep_thought():
    """
    Main function that interacts with user via input/output.
    This function uses check_answer() for the logic.
    """
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    result = check_answer(answer)
    print(result)


# Only run deep_thought() when this file is executed directly
# NOT when it's imported by unit tests
if __name__ == "__main__":
    deep_thought()