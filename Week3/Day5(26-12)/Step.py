def step():
    step_1 = 1
    step_2 = 2
    total = 0
    for i in range(1, 5):
        total += step_1
        step_1, step_2 = step_2, step_1 + step_2
    return total

print(step())