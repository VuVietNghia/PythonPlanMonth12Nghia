def even_odd_number_v2(the_list):
    even_list = []
    odd_list = []
    for i in the_list:
        if int(i) % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(f"Danh sach so chan: {even_list}, danh sach so le: {odd_list}")

even_odd_number_v2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def even_odd_number_v3():
    the_list = []
    even_list = []
    odd_list = []

    while True:
        n = input("Nhap so (x de huy): ")
        if n.lower() == 'x':
            break
        if n == '':
            continue
        the_list.append(int(n))

    for i in the_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(f"Danh sach so chan: {even_list} \n"
          f"danh sach so le: {odd_list}")

even_odd_number_v3()