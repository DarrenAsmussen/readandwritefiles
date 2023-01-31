import csv

customers = open("EmployeePay.csv", "r")
customer_file = csv.reader(customers, delimiter=",")
bonus = 0
total_pay = 0


next(customer_file)

for record in customer_file:
    bonus = float(record[3]) * float(record[4])
    total_pay = float(record[3]) + bonus
    print("First Name: ", record[1])

    print("Last Name: ", record[2])

    print("Salary $: ", "${:,.2f}".format(float(record[3])))

    print("Bonus $: ", "${:,.2f}".format(bonus))

    print("Total Pay: $", "${:,.2f}".format(total_pay))
