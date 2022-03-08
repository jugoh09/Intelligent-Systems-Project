# An upadted version of cramers method
import numpy as np
import math


grams_f1 = int(input("How many grams of bread you had?: "))
carbs_f1 = grams_f1 * 13
proteins_f1 = grams_f1 * 2
fats_f1 = grams_f1 * 1 

grams_f2 = int(input("How many grams of fish you had?: "))
carbs_f2 = grams_f2 * 13
proteins_f2 = grams_f2 * 39.2
fats_f2 = grams_f2 * 12.5 

grams_f3 = int(input("How many grams of milk you had?: "))
carbs_f3 = grams_f3 * 0.013
proteins_f3 = grams_f3 * 0.008
fats_f3 = grams_f3 * 0.002 


#M = np.array["Carbs","Proteins","Fats"]
M = np.array([[0.6,-0.4,-0.4],[-0.3,0.7,-0.3],[-0.3,-0.3,0.7]])
c = np.array([[(-0.6 * carbs_f1) + (0.4 * proteins_f1) + (0.4 * fats_f1)], [(0.3 * carbs_f2) + (-0.7 * proteins_f2) + (0.3 * fats_f2)], [(0.3 * carbs_f3) + (0.3 * proteins_f3) + (-0.7 * fats_f3)]])

#M = np.array([[-0.6,0.3,0.3],[0.4,-0.7,0.3],[0.4,0.3,-0.7]])
#M = np.array([[0.85,0,0.5],[0.05,0.95,0.4],[0.1,0.5,0.3]])
#c = np.array([0.4,0.3,0.3])
y = np.linalg.solve(M,c)


print(carbs_f1)
print(proteins_f1)
print(fats_f1)

print(carbs_f2)
print(proteins_f2)
print(fats_f2)


print(carbs_f3)
print(proteins_f3)
print(fats_f3)


print(y)
print(c)
print(M)

