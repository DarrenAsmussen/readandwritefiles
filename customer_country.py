import csv

customers = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")
customer_file = csv.reader(customers, delimiter=",")


count = -1

for record in customer_file:
    outfile.write(record[1] + "," + record[2] + "," + record[4] + "\n")
    count += 1

print(count)

outfile.close()
