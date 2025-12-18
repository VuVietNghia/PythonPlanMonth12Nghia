def making_face():
    str_input = input("Nhap vao chuoi ky tu: ")
    str_input = str_input.replace(":)", "🙂")
    str_input = str_input.replace(":(", "🙁")
    print(str_input)

making_face()