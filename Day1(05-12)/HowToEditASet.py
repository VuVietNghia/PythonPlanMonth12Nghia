def edit_a_set(this_set):
    temp_list = list(this_set)
    temp_list.append("Nghia")
    temp_list.insert(1, "Mai")

    my_set.clear()
    my_set.update(temp_list)
    print(f"Set sau update la = {my_set}")

my_set = {1, 2, 3, 4, 5}
edit_a_set(my_set)


def edit_a_set_v2():
    this_set = set()
    while True:
        n = input("Nhap vao cac chu cua set(x de huy): ")
        if n.lower() == 'x':
            break
        if n == '':
            continue
        this_set.add(n)

    this_list = list(this_set) # ko hoat dong do set ko co thu tu
    idx = int(input("Nhap vao vi tri can sua: "))
    if idx < 0 or idx >= len(this_list):
        print("Vi tri khong hop le")
        return
    update_value = input("Nhap vao gia tri can sua: ")

    this_list[idx] = update_value
    this_set = set(this_list)
    print(this_list)
    print(this_set)

edit_a_set_v2()