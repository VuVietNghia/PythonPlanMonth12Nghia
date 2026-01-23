def dict_insert():
    this_list = []
    while True:
        n = int(input("Nhap so luong key-value: "))
        if n == 0:
            break
        this_dict = {}
        for i in range(n):
            key = input("Nhap key: ")
            value = input("Nhap value: ")
            this_dict[key] = value
        this_list.append(this_dict)
        print(this_list)

dict_insert()


def highest_value():
    this_dict = {
        "diem_toan": 7,
        "diem_van": 5,
        "diem_anh": 8,
    }
    max_value = max(this_dict.values())
    print(max_value)

highest_value()