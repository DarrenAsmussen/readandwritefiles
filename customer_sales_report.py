import csv

sales_report = open("salesreport.csv", "w", newline="")

reader = csv.reader(sales_report)

next(reader)

writer = csv.writer(sales_report, delimiter=",")

fieldnames = ["Customer ", "Total"]
writer.writerow(fieldnames)


id_salaryDict = {}

for row in reader:
    customer_ID = int(row[0])

    SubTotal = float(row[3])

    TaxAmt = float(row[4])

    Freight = float(row[5])

    Total = SubTotal + TaxAmt + Freight

    if customer_ID in id_salaryDict:
        id_salaryDict[customer_ID] += Total

    else:
        id_salaryDict[customer_ID] = Total


for cust_ID, Total in id_salaryDict.items():
    new_row = [format(cust_ID, ">d"), format(Total, "<.2f")]
    writer.writerow(new_row)

sales_report.close()
