from this import d
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

#high carbs
recommend_bread = 5
#high protein
recommend_chicken = 18
#high fats
recommend_olive = 10


print()

# Calcaulates the REMAINDING number of carbs, proteins and fats user should consume based on their daily calorie
# intake

x1 =  b1 - carbs_f1 - carbs_f2 - carbs_f3 
x2 =  b2 - proteins_f1 - proteins_f2 - proteins_f3 
x3 =  b3 - fats_f1 - fats_f2 - fats_f3 

rx1 = x1/recommend_bread
rx2 = x2/recommend_chicken
rx3 = x3/recommend_olive




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

print("Carbs in grams needed for user: ", x1)
print("Proteins in grams needed for user: ", x2)
print("Fats in grams needed for user: ", x3)

print("We recommend these foods in your diet!")
print("1. Bread")
print("2. Chicken")
print("3. Olive oil")
print("You should take %d grams of bread" % rx1)
print("You should take %d grams of chicken" % rx2)
print("You should take %d grams of olive oil" % rx3)
