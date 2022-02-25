# Code to read a csv file

import csv
import numpy as np
import math

rows = []
with open("Food_Content.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

# data = []
# with open('Food_Content.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         data.append(row)

# food = input("What did you ate: ")
# col = [x[0] for x in data]

# if food in col:
#     for x in range(0, len(data)):
#         if food == data[x][0]:
#             print(data[x])

# else:
#     print("Food does not exist") 


# M = np.array([["Carbs"],["Proteins"],["Fats"]])
# M = np.array([[0.85,0,0.5],[0.05,0.95,0.5],[0.1,0.5,0.3]])
# c = np.array([0.4,0.3,0.3])

# print(M)
#y = np.linalg.solve(M,c)