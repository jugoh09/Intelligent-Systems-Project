import numpy as np
import math


meals_a_day = int(input("How many meals you had today?:"))
rows = 3

M = []
for m in range(1, meals_a_day + 1):
    ask = input("What was your %d st meal?: " % m)

for i in range(rows):
    a = []
    for j in range(meals_a_day):
        a.append(int(input()))
    M.append(a)
    
M = np.array([[0.85,0,0.5],[0.05,0.95,0.5],[0.1,0.5,0.3]])
c = np.array([0.4,0.3,0.3])
y = np.linalg.solve(M,c)

print(y)
