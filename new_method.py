import numpy as np
import math

# Ask user what's his/her daily calorie target
cal_tag = int(input("What is your daily calorie target?: "))

# Converts % of carbs, proteins, grams into grams
# 40% = 0.4, 30% = 0.3
# Each gram of carbs provides 4 grams of calories
# Each gram of proteins provides 4 grams of calories
# Each gram of fats provides 9 grams of calories

# Eg: Calculate the REQURIED number of carbs user should consume with a 2000 daily calorie target
# 2000 calories × 0.5 = 1000 calories
# 1000 calories ÷ 4 calories/gram = 250 grams
# if you want to consume 50 percent of a 2,000-calorie diet in carbohydrates, that works out to 250 
# grams of carbohydrates.

dail_cal_carbs = cal_tag * 0.4
b1 = dail_cal_carbs / 4

dail_cal_prot = cal_tag * 0.3
b2 = dail_cal_prot / 4

dail_cal_fats = cal_tag * 0.3
b3 = dail_cal_fats / 9

# Calculate number of grams of bread, fish and milk user had
# 0.49 = number of carbs in 1 gram of bread, etc
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

def rec_food():
    bc = 44
    bp = 11
    bf = 2

    pc = 0
    pp = 27
    pf = 13

    ac = 9
    ap = 2
    af = 15

    pbc = bc / (bc + bp + bf)
    pbp = bp / (bc + bp + bf)
    pbf = bf / (bc + bp + bf)

    ppc = pc / (pc + pp + pf)
    ppp = pp / (pc + pp + pf)
    ppf = pf / (pc + pp + pf)

    pac = ac / (ac + ap + af)
    pap = ap / (ac + ap + af)
    paf = af / (ac + ap + af)

    x1 =  b1 - carbs_f1 - carbs_f2 - carbs_f3 
    x2 =  b2 - proteins_f1 - proteins_f2 - proteins_f3 
    x3 =  b3 - fats_f1 - fats_f2 - fats_f3 

    A0 = np.array([[pbc,ppc,pac],[pbp,ppp,pap],[pbf,ppf,paf]])
    A1 = np.array([[x1,ppc,pac],[x2,ppp,pap],[x3,ppf,paf]])
    A2 = np.array([[pbc,x1,pac],[pbp,x2,pap],[pbf,x3,paf]])
    A3 = np.array([[pbc,ppc,x1],[pbp,ppp,x2],[pbf,ppf,x3]])

    #determinant of array
    Ax0 = np.linalg.det(A0)
    Ax1 = np.linalg.det(A1)
    Ax2 = np.linalg.det(A2)
    Ax3 = np.linalg.det(A3)

    #determine value of x,y,z
    x = Ax1/Ax0
    y = Ax2/Ax0
    z = Ax3/Ax0

    print("You need this amount of carbs: %dg" %x1)
    print("You need this amount of protein: %dg" %x2)
    print("You need this amount of fats: %dg" %x3)

    print()

    print("We recommend these foods in your diet!")
    print("1. Bread")
    print("2. Pork")
    print("3. Avocado")

    print("You need to eat %.2fg of bread" %x)
    print("You need to eat %.2fg of pork" %y)
    print("You need to eat %.2fg of avocado" %z)


# Calcaulates the REMAINDING number of carbs, proteins and fats user should consume based on their daily calorie
# intake

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

print("40% of carbs in grams: ", b1)
print("30% of protein in grams : ", b2)
print("30% of fats in grams: ", b3)

print()

rec_food()


