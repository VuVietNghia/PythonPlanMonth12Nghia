import json

teams = {
    "Team": "McLaren",
    "Drive": "Lando Norris",
    "Car": "McLaren MCL39"
}

file_path = "/home/nghiavu/Desktop/F1.json"

try:
    with open(file_path, "w") as file:
        json.dump(teams, file)
        print(f"file '{file_path}' da duoc tao")
except FileExistsError:
    print(f"file '{file_path}' da ton tai")