print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split bill?"))

bill_per_person = (bill + bill* tip_percentage/ 100 )/number_of_people
bill_per_person = round(bill_per_person,2)
bill_per_person= "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")