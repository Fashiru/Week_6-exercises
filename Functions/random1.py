import random

# List
fruits = [ "apple", "banana", "cherry", "peach", "plum", "watermelon"]

# Random choice
random_choice = random.choice(fruits)
print(f"Random choice: {random_choice}")

# random sample
random_sample = random.sample(fruits, 3)
print(f"Random sample: {random_sample}")

# random shuffle *
random_shuffle = random.shuffle(fruits)
print(f"Shuffled fruiit: {fruits}")

#random Integer
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

#Random float
random_float = random.random()
print(f"Random float between 0 and 1: {random_float} ")
