# Printing, Printing

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "or a song about love"
))

# Real World using .format
# Dynamic SQL Query Building

table = "customer"
columns = "id, name, email"
condition = "status = 'active'"

query = "SELECT {} FROM {} WHERE {}".format(columns, table, condition)
print(query)

# Real World using .format
# Constructing URLs for API Requests

base_url = "https://api.examples.com/users"
user_id = 42
params = "post?limit=5"

url = "{}/{}/{}".format(base_url, user_id, params)
print(url)