import csv

header = ["id", "name", "email", "article"]

with open("new.csv", "w") as file:
    writer= csv.writer(file)
    writer.writerow(header)
    

