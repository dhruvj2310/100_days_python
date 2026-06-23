## 

print("Welcome to bill split calculator!")

## Get information ##
bill_amt = int(input("\nWhat is the bill amount?: "))
tip_pc = int(input("What percent tip you would like to give?: "))
no_of_people = int(input("How many people have contributed to the bill?: "))

## Calculations ##
tip_amt = bill_amt * (tip_pc / 100)
total_bill = bill_amt + tip_amt
split_amt = total_bill / no_of_people

print(f"""
Your total bill is ${total_bill}
including a tip of ${tip_amt}.
Each person has to pay ${split_amt}
      """)