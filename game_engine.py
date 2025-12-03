import json
from bosses import bosses1
with open("locations.json", encoding="utf-8") as file:
    location = json.load(file)

current_location = 'start'

while "ending" not in current_location:
    
    current_location_info = location[current_location]
    print(current_location_info["lore"])

    if current_location_info["id"] == "boss1":
        if bosses1.boss1():
            current_location = current_location_info["next_good"]
        else:
            current_location = current_location_info["next_bad"]
    elif current_location_info["id"] == "boss2":
        if bosses1.boss2():
            current_location = current_location_info["next_good"]
        else:
            current_location = current_location_info["next_bad"]
    elif current_location_info["id"] == "patriot_test":
        result = bosses1.test()
        if result == 0:
            current_location = current_location_info["next_bad"]
        elif result == 1:
            current_location = current_location_info["next_neutral"]
        else:
            current_location = current_location_info["next_good"]
    elif current_location_info["id"] == "location2":
        print(current_location_info["question"])
        print(*current_location_info["answers"], sep="\n")
        vvod = input()
        while vvod != "1" and vvod != "2" and vvod != "3":
            print("Введите число от 1 до 3")
            vvod = input()
        vvod = int(vvod)
        if vvod == 1:
            current_location = current_location_info["next_bad"]
        elif vvod == 2:
            current_location = current_location_info["next_good"]
        else:
            current_location = current_location_info["next_neutral"]
    else:
        print(current_location_info["question"])
        print(*current_location_info["answers"], sep="\n")

        vvod = input()
        while vvod != "1" and vvod != "2":
            print("Введите число 1 или 2")
            vvod = input()

        vvod = int(vvod)
        if vvod == current_location_info["answer"]:
            current_location = current_location_info["next_good"]
        else:
            current_location = current_location_info["next_bad"]
print(location[current_location]["lore"])
