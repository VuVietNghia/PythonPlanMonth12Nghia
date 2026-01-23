def fizz_buzz(num):
    this_list = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            this_list.append("FizzBuzz")
        elif i % 3 == 0:
            this_list.append("Fizz")
        elif i % 5 == 0:
            this_list.append("Buzz")
        else:
            this_list.append(str(i))
    return this_list

print(fizz_buzz(15))