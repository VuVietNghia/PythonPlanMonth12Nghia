this_list = ["Nghia", "Vu", "Nguyen", "Son", "Hai"]

def count_node():
    result_list = []

    for name in this_list:
        if len(name) >= 5:
            upper_name = name.upper()
            result_list.append(upper_name)
    print(result_list)

count_node()
