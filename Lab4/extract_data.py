import csv
import math

# This program is not completed. Look at Lab 4's question for
# how its supposed to be implemented 

file = open('FittsLawLog.xlsx', 'r')
key_value = {}

print(file.readline())

for line in file.readlines():
    line = line.strip().split(',')
    key_value[(line[1], line[2], line[3])] = line[4]
 
file.close()

print(key_value)

#file = open('summary.xlsx', 'w', newline='')
#writer = csv.writer(file)

#for item in key_value.items():
    #writer.writerow([item