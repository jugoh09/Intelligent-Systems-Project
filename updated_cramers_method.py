import numpy as np
import math

cal_tag = int(input("What is your daily calorie target?: "))
dail_cal_carbs = cal_tag * 0.4
b1 = dail_cal_carbs / 4

dail_cal_prot = cal_tag * 0.3
b2 = dail_cal_prot / 4

dail_cal_fats = cal_tag * 0.3
b3 = dail_cal_fats / 9


grams_f1 = int(input("How many grams of bread you had?: "))
carbs_f1 = grams_f1 * 0.49
proteins_f1 = grams_f1 * 0.09
fats_f1 = grams_f1 * 0.03 

grams_f2 = int(input("How many grams of fish you had?: "))
carbs_f2 = grams_f2 * 0
proteins_f2 = grams_f2 * 0.22
fats_f2 = grams_f2 * 0.12 

grams_f3 = int(input("How many grams of milk you had?: "))
carbs_f3 = grams_f3 * 0.05
proteins_f3 = grams_f3 * 0.03
fats_f3 = grams_f3 * 0.01

print()

#M = np.array([[0.6 * carbs_f1,-0.4 * proteins_f1,-0.4 * fats_f1],[-0.3 * carbs_f2,0.7 * proteins_f2,-0.3 * fats_f2],[-0.3 * carbs_f3,-0.3 * proteins_f3,0.7 * fats_f3]])
#c = np.array([[(-0.6 * carbs_f1) + (0.4 * proteins_f1) + (0.4 * fats_f1)], [(0.3 * carbs_f2) + (-0.7 * proteins_f2) + (0.3 * fats_f2)], [(0.3 * carbs_f3) + (0.3 * proteins_f3) + (-0.7 * fats_f3)]])

#M = np.array([[-0.6,0.3,0.3],[0.4,-0.7,0.3],[0.4,0.3,-0.7]])
#M = np.array([[0.85,0,0.5],[0.05,0.95,0.4],[0.1,0.5,0.3]])
c = np.array([[b1],[b2],[b3]])
M = np.array([[carbs_f1, proteins_f1, fats_f1], [carbs_f2, proteins_f2, fats_f2], [carbs_f3, proteins_f3, fats_f3]])
y = np.linalg.solve(M,c)


print("Carbs for f1: ", carbs_f1)
print("Protein for f1: ", proteins_f1)
print("Fats for f1: ", fats_f1)

print()

print("Carbs for f2: ", carbs_f2)
print("Protein for f2: ", proteins_f2)
print("Fats for f2: ", fats_f2)

print()

print("Carbs for f3: ", carbs_f3)
print("Protein for f3: ", proteins_f3)
print("Fats for f3: ", fats_f3)

print()

print("M = ", M)
print()
print("c = ", c)
print()
print("y = ", y)
