import random
from datetime import datetime


class customer:
    customer_id = 10011
    full_name = "Alice Smith"
    email = "alice.smith@example.com"
    account_number = 220610060796001


class transaction:
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

    random_amount_list = [50000, 100000, 250000, 45000, 500000, 370000]

    xid = random.randrange(10000, 99999)
    amount = random.choice(random_amount_list)
    date = dt_string
    description = "Deposit"
