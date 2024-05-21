import csv
with open('Aprildata.csv','r') as file:
    readdata=csv.reader(file)
    for row in readdata:
        print(row)