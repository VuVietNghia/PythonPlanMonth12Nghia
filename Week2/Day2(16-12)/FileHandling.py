def file_handling():
    txt_data = input("Nhap vao du lieu: ")
    file_name = input("Nhap vao ten file: ")

    file_path = f"/home/nghiavu/Desktop/{file_name}.txt"

    try:
        with open(file_path, "w") as file:
            file.write(txt_data)
        print(f"File da duoc tao vao {file_path}")
    except FileExistsError:
        print("File da ton tai")

file_handling()
