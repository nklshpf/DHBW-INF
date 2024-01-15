import re

transaktion = [
    {"type": "purchase", "amount": 50, "date": "15-01-2024"},
    {"type": "sale", "amount": 20.5, "date": "14-01-2024"},
]

transaktion_type =transaktion[0]["type"]
transaktion_amount = transaktion[0]["amount"]
transaktion_date = transaktion[0]["date"]

def list_of(my_key):
    amount_values = [transaktion[my_key] for transaktion in transaktion]
print(list_of("amount"))

def sum_up(my_type):
    amount_values = [transaktion["amount"] for transaktion in transaktion
    if transaktion["type"] == my_type]
    return(sum(amount_values))

income = sum_up("purchase")
expenses = sum_up("sale")
print("income =", income)
print("expenses =", expenses)

if (income > expenses): print("You made Money!")
else: print("You lost money!")

def find_all(my_key,my_value):
    values = [transaktion for transaktion in transaktion if transaktion[my_key] == my_value]
    return(values)
my_transaktion = find_all("date","14-01-2024")
print(my_transaktion)
print(len(my_transaktion))

def is_valid_date_format(date_string):
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return bool(date_pattern.match(date_string))

my_date = my_transaktion[0]["date"]
print(my_transaktion[0]["date"])
print(type(my_date))
print(is_valid_date_format(my_date))