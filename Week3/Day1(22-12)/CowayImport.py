import cowsay

def say_hello(name: str) -> None:
    cowsay.trex(f"Chào bạn {name}, rất vui được gặp bạn!")

if __name__ == "__main__":
    user_name = input("Nhập tên của bạn: ")

    say_hello(user_name)