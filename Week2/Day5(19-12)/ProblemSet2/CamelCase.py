def main():
    camel_input: str = input("camelCase: ")
    snake_output: str = convert_to_snake_case(camel_input)
    print(f"snake_case: {snake_output}")


def convert_to_snake_case(camel_str: str) -> str:
    result: str = ""
    for char in camel_str:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result

main()
