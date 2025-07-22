import random

count = 100
min_value = 10
max_value = 200
print(f"Generating {count} randoms in the range [{min_value}, {max_value}]")

randoms_map = {}
for i in range(0, count):
    r = random.randint(min_value, max_value)
    if r not in randoms_map:
        randoms_map[r] = []
    randoms_map[r].append(i)

# Write a text file "randoms_db.txt" with each random on a line, its value followed by the indexes where it occurred
with open("IntroToPy/randoms_db.txt", "w") as data_file:
    for r in randoms_map.keys():
        data_file.write(f"{r} {randoms_map[r]}\n")

