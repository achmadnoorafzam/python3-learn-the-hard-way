# Prompting and Passing
# Using argv and input

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Wher do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alrigh, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice!.
""")

##
# To run this, type: python3 ex14.py "Achmad Noorafzam"
# I use " " to make Achmad Noorafzam as 1 value
##