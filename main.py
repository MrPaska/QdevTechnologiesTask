import csv

red = yellow = green = 0
red_s = yellow_s = green_s = 0
green_active = []
lines_of_mistakes = 0
cycles_of_colors = 0
cycles_dict = {"Red": 0, "Yellow": 0, "Green": 0}

with open("data.txt", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")  # Also it could be done using csv.DictReader() instead csv.reader()
    next(reader)  # Using csv.DictReader() heading would be handled already
    for line in reader:
        red += 1 if line[0] == "1" else 0  # It would be keys: line["Red"]
        yellow += 1 if line[1] == "1" else 0
        green += 1 if line[2] == "1" else 0
        multi_color = [i for i, x in enumerate(line[:3]) if x == "1"]
        # [key for key, value in line.items() if value == "1" and key != "TimeActive"]

        if len(multi_color) != 1:
            lines_of_mistakes += 1

        red_s += int(line[3]) if line[0] == "1" else 0
        yellow_s += int(line[3]) if line[1] == "1" else 0
        green_s += int(line[3]) if line[2] == "1" else 0

        if line[2] == "1" and int(line[3]) != 0:
            green_active.append(line[4])

        if len(multi_color) == 1:
            if line[0] == "1":
                cycles_dict["Red"] += 1
            else:
                if cycles_dict["Red"] == 1:
                    if cycles_dict["Yellow"] == 0 and line[1] == "1":
                        cycles_dict["Yellow"] += 1
                    elif cycles_dict["Yellow"] == 1 and cycles_dict["Green"] == 0 and line[1] == "1":
                        cycles_dict = {key: 0 for key in cycles_dict}
                    if cycles_dict["Yellow"] == 1 and cycles_dict["Green"] == 0 and line[2] == "1":
                        cycles_dict["Green"] += 1
                    elif cycles_dict["Yellow"] == 0 and line[2] == "1":
                        cycles_dict = {key: 0 for key in cycles_dict}
                    elif cycles_dict["Green"] == 1 and line[2] == "1":
                        cycles_dict = {key: 0 for key in cycles_dict}
                    if cycles_dict["Green"] == 1 and line[1] == "1":
                        cycles_dict["Yellow"] += 1
                    if cycles_dict["Yellow"] > 2:
                        cycles_dict = {key: 0 for key in cycles_dict}
                elif cycles_dict["Red"] == 2 and cycles_dict["Yellow"] == 2 and cycles_dict["Green"] == 1:
                    cycles_of_colors += 1
                    cycles_dict = {key: 0 for key in cycles_dict}
                else:
                    cycles_dict = {key: 0 for key in cycles_dict}

print("1. Find the number of red, yellow & green occurrences.")
print(f"\tRed={red}, Yellow={yellow}, Green={green}")
print("2. Find how long each colour was active for.")
print(f"\tRed={red_s} seconds, Yellow={yellow_s} seconds, Green={green_s} seconds")
print("3. Find all times when Green was active (by time)")
print(f"\tTimes: {green_active}")
print("4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data")
print(f"\tCycles: {cycles_of_colors}")
print("5. Find number of lines with mistakes (multiple colours active at the same time or no colours active)")
print(f"\tNumber of lines: {lines_of_mistakes}")
