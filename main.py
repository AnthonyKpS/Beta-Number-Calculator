import os
import csv
import decimal

# Greeting
print("====================[Welcome to the Beta number calculator | Made by Nikolaos Prinianakis - "
      "l7190179]====================")

# Instruction
print("Your .csv file's header should be like this: Institution-delimiter-index")

# Filename prompt
filename = input("Please state the name of your .csv file: ")

path = "./" + filename
check = os.path.exists(path)

while not check:
    filename = input("That file does not exist, please try again: ")
    path = "./" + filename
    check = os.path.exists(path)

# Delimiter prompt
delimiters = [';', ',', ' ', '  ', '.']
delimiter = input("Now, please tell me what delimiter you are using ")
while delimiter not in delimiters:
    delimiter = input("Not supported delimiter, please change your delimiter and try again")

# Replacing ',' to '.' for decimal values
if delimiter != ',':
    text = open(filename, "r")
    text = ''.join([i for i in text]) \
        .replace(",", ".")
    x = open("data.csv", "w")
    x.writelines(text)
    x.close()

# Opening file
file = open("data.csv", 'r')

# creating a csv reader object
csv_reader = csv.reader(file, delimiter=delimiter)

# Parsing the .csv
# getting the first row
fields = next(csv_reader)

# extracting each column to columnX and columnY
columnX = []
columnY = []

for row in csv_reader:
    columnX.append(float(row[0]))
    columnY.append(float(row[1]))

file.close()

# n = population
n = len(columnX)

# SUMS
sums = [sum(columnX), sum(columnY), sum(columnX) ** 2]

sum_xiyi = 0
sum_x_squared = 0

for i in range(n):
    sum_xiyi += columnX[i] * columnY[i]
    sum_x_squared += columnX[i] ** 2

sums.append(sum_xiyi)
sums.append(sum_x_squared)

beta = decimal.Decimal((n * sums[3] - (sums[0] * sums[1]))) / decimal.Decimal(n * sums[4] - sums[2])

# Results
print("The data you provided referred to", fields[0], " and the beta number is b = ", beta)
