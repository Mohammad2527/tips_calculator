#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator\n")

bill = input("What was the total bill?\n")
print('$'+ bill)
bill_as_float = float(bill)
# bill_amount = '${:,.2f}'.format(bill_as_float)
# bill_amount = float(bill_amount)
# print(type(bill_as_float))


tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15\n")
tip_to_add = float(tip_percentage)/100
# print(type(tip_to_add))


number_of_customer = input("How many people to split the bill?\n")
no_of_customer_as_int = int(number_of_customer)
# print(type(no_of_customer_as_int))

bill_per_customer = (bill_as_float / no_of_customer_as_int) * (1 + tip_to_add)
# print(type(bill_per_customer))
# bill_rounded = "${:, .2f}".format(bill_per_customer)

print("Each person should pay: " + "${:,.2f}".format(bill_per_customer))