
import csv

line_count=0
total_pay = 0

f_out = open("LIMCO1.csv", "a", newline="")
writer = csv.writer(f_out)

with open("LIMCO.csv", "r") as f_in:
    reader = csv.reader(f_in)
    for line in reader:
        if line_count>0:
             CustomerID=line[0]
             Customer_Name=line[1]
             Contact_Name=line[2]
             Address=line[3]
             City=line[4]
             Postal_Code=line[5]
             Country=line[6]
             writer.writerow([CustomerID, Customer_Name, Contact_Name, Address, City, Postal_Code, Country])