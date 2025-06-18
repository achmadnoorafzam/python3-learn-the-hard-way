# Strings and Text

# Example 1
MyName = "My name is {}"
print(MyName.format("Achmad Noorafzam"))
print(f"My name is {'Achmad Noorafzam'} <-- Use f-string")

# Example 2
age = 2025 - 1989
template1 = "{} age is {} years old."
Name = "Bobby"
print(template1.format(Name, age))
print(f"{Name} age is {age} years old. <-- Use f-string")

# Example 3
template2 = "{1} is son of {0}."
print(template2.format("Ali", "Abu")) # Cannot use f-string.

# Real world application example
# Sales Report

product = "Laptop"
quantity = 5
price = 4500

report = "You bought {} in total quantity {} with price RM{}."
print(report.format(product, quantity, price * quantity))
print(f"You bought {product} in total quantity {quantity} with price RM{price * quantity} <-- Use f-string")

# Notification Example

customer_name = "Achmad Noorafzam"
delivery_date = "17 June 2025"
invoice_number = "INV1234"

message = """
Hello {}! Order.No (#{}) has been delivered on {}.
Thank you for using our service.
"""

print(message.format(customer_name, invoice_number, delivery_date))
# TODO: Try do f-string version below.

# Command Line (CLI) Progress Bar

progress = 0.5 # nilai 1 adalah 100%
print("Progress: [{:<20}] {:.1%}".format("="*int(progress*20), progress))
print(f"Progress: [{'=' * int(progress * 20):<20}] {progress:.1%} <-- Use f-string")

# Dynamic HTML generation
tag = "div"
content = "Welcome Home"
attributes = {'class': 'header', 'id': 'welcome-msg'}

html = "<{tag} {attrs}>{content}</{tag}>".format(
    tag=tag,
    attrs=" ".join(f'{key}="{value}"' for key,value in attributes.items()),
    content=content
)
print(html)
