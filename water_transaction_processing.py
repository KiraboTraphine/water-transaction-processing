UNIT_PRICE = 10

transactions = {}


def valid_transaction_id(transaction_id):
    return (
        len(transaction_id) == 4
        and transaction_id[0] == "W"
        and transaction_id[1:].isdigit()
    )


def valid_customer(customer):
    return (
        len(customer) == 4
        and customer[0] == "C"
        and customer[1:].isdigit()
    )


def valid_supply_point(point):
    return (
        len(point) == 5
        and point[:3] == "KLA"
        and point[3:].isdigit()
    )


def add_transaction(transaction_id, customer, point, quantity):
    if not valid_transaction_id(transaction_id):
        print("Invalid transaction ID")
        return

    if transaction_id in transactions:
        print("Duplicate transaction ID")
        return

    if not valid_customer(customer):
        print("Invalid customer reference")
        return

    if not valid_supply_point(point):
        print("Invalid supply point")
        return

    if not isinstance(quantity, (int, float)):
        print("Quantity must be numeric")
        return

    if quantity < 0:
        print("Negative quantity is not allowed")
        return

    if quantity == 0:
        print("Zero quantity cannot be recorded as a valid sale")
        return

    amount = quantity * UNIT_PRICE

    transactions[transaction_id] = {
        "customer": customer,
        "supply_point": point,
        "quantity": quantity,
        "amount": amount
    }

    print(transaction_id, "registered successfully")


def display_transactions():
    if not transactions:
        print("No transactions available")
        return

    for transaction_id, record in transactions.items():
        print(
            transaction_id,
            record["customer"],
            record["supply_point"],
            record["quantity"],
            record["amount"]
        )


def search_customer(customer):
    found = False

    for transaction_id, record in transactions.items():
        if record["customer"] == customer:
            print(
                transaction_id,
                record["customer"],
                record["supply_point"],
                record["quantity"],
                record["amount"]
            )
            found = True

    if not found:
        print("No transactions found for", customer)


def calculate_total_quantity():
    total_quantity = 0

    for record in transactions.values():
        total_quantity += record["quantity"]

    return total_quantity


def calculate_total_revenue():
    total_revenue = 0

    for record in transactions.values():
        total_revenue += record["amount"]

    return total_revenue


def display_customer_totals():
    customer_totals = {}

    for record in transactions.values():
        customer = record["customer"]

        if customer not in customer_totals:
            customer_totals[customer] = {
                "quantity": 0,
                "revenue": 0
            }

        customer_totals[customer]["quantity"] += record["quantity"]
        customer_totals[customer]["revenue"] += record["amount"]

    for customer, totals in customer_totals.items():
        print(
            customer,
            "Quantity:", totals["quantity"], "litres",
            "Revenue: UGX", totals["revenue"]
        )


# SUPPLIED TRANSACTIONS

add_transaction("W001", "C102", "KLA01", 500)
add_transaction("W002", "C103", "KLA01", 750)
add_transaction("W003", "C102", "KLA02", 400)
add_transaction("W004", "C104", "KLA01", 0)
add_transaction("W005", "C105", "KLA02", 900)
add_transaction("W006", "C103", "KLA01", 600)


print("\nALL TRANSACTIONS")
display_transactions()


print("\nSEARCH FOR CUSTOMER C102")
search_customer("C102")


print("\nOVERALL TOTALS")
print("Total quantity supplied:", calculate_total_quantity(), "litres")
print("Total revenue collected: UGX", calculate_total_revenue())


print("\nCUSTOMER CUMULATIVE TOTALS")
display_customer_totals()