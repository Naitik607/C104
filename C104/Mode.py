# Mode

import csv
from collections import Counter

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

data = Counter(new_data)
mode_data_for_range = {
    '75-85':0,
    '85-95':0,
    '95-105':0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0

}

for Weight, occurence in data.items():
    if 75 < float(Weight) < 85:
        mode_data_for_range['75-85'] += occurence
    elif 85 < float(Weight) < 85:
        mode_data_for_range['85-95'] += occurence
    elif 95 < float(Weight) < 105:
        mode_data_for_range['95-105'] += occurence
    elif 105 < float(Weight) < 115:
        mode_data_for_range['105-115'] += occurence
    elif 115 < float(Weight) < 125:
        mode_data_for_range['115-125'] += occurence
    elif 125 < float(Weight) < 135:
        mode_data_for_range['125-135'] += occurence
    elif 135 < float(Weight) < 145:
        mode_data_for_range['135-145'] += occurence
    elif 145 < float(Weight) < 155:
        mode_data_for_range['145-155'] += occurence
    elif 155 < float(Weight) < 165:
        mode_data_for_range['155-165'] += occurence
    
mode_range,mode_occurence = 0,0
for range , occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
