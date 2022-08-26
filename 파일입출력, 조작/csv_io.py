import csv

with open("csv_test.csv", "w") as f:
    fieldname = ["name", "count"]
    
    writer = csv.DictWriter(f, fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'name':'A', 'count':1})
    writer.writerow({'name':'B', 'count':2})
    writer.writerow({'name':'C', 'count':3})
    writer.writerow({'name':'D', 'count':4})

with open("csv_test.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)