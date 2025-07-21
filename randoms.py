import random
import pandas as pd
import matplotlib as plt

count = 10
min_value = 3
max_value = 13

random_numbers = [random.randint(min_value, max_value) for _ in range(count)]

number_indices = {}
for idx, num in enumerate(random_numbers):
    if num not in number_indices:
        number_indices[num] = []
    number_indices[num].append(idx)

with open("dataset.txt", "w") as file:
    for key, indices in number_indices.items():
        line = f"{key}: {indices}\n"
        file.write(line)

number_of_keys = len(number_indices)
print("Valori unice:", number_of_keys)

minim_of_keys = min(number_indices)
print("Cea mai mică valoare:", minim_of_keys)

maxim_of_keys = max(number_indices)
print("Cea mai mare valoare:", maxim_of_keys)

stdev_of_keys = pd.std(number_indices)
print("Standard deviation:", stdev_of_keys)


