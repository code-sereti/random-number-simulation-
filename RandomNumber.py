import random

random_numbers = []# Creates an empty list
for _ in range(10):
    number = random.randint(1, 10000)
    random_numbers.append(number)# Appends the generated numbers into the list.

print("10 Random Numbers in the Range 1-1000:")
print(random_numbers)
