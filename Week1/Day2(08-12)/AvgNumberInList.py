def avg_number(the_list):
    count = len(the_list)
    total = sum(the_list)
    avg = total / count

    print(f"Trung binh cua list la: {avg}")

avg_number([2, 4, 6, 8, 10])

def avg_number_v2():
    the_list = []
    while True:
        n = input("Nhap vao so nguyen(x de huy): ")
        if n.lower() == 'x':
            break
        if n == '':
            continue
        the_list.append(int(n))

    count = len(the_list)
    total = sum(the_list)
    avg = total / count

    print(f"Trung binh cua list la: {avg}")

avg_number_v2()