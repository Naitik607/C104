# Meadian

import csv

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

n = len(new_data)
new_data.sort()

if n % 2 == 0:
    medain1 = float(new_data[n//2])
    medain2 = float(new_data[n//2 - 1])
    medain = (medain1 + medain2)/2
else:
    medain = new_data[n//2]

