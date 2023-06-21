# Day 2 - Tip Calculator
print("Welcome to Tip Calculator")
bill = float(input("What was the total bill?\n₹"))
tip = int(input("How much tip would you like to give?\n"))
people = int(input("How many people to split the bill\n"))

tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)

print("+──────────────────────────────+")
print(f"│Each person should pay: {final_bill} │")
print("+──────────────────────────────+")
