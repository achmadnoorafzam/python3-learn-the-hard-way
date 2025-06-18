# More Variables and Printing using f-string

my_name = 'Achmad Noorafzam'
my_age = 2025 - 1989 # year now - year born
my_height = 166 # cm
my_weight = 90 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about my {my_name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He's {my_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} I get {total}.")


# Real World application for f-string
import time

total = 100
for i in range(total + 1):
    progress = i / total
    bar_length = 10
    filled = "=" * int(progress * bar_length)
    remaining = " " * (bar_length - len(filled))
    print(f"\rProgress: [{filled}{remaining}] {progress:.0%}", end="", flush=True)
    time.sleep(0.1)  # Simulation process
print()