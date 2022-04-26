import csv
import numpy as np

def searchFood():
    cal_tag = int(input("What is your daily calorie target?: "))

    dail_cal_carbs = cal_tag * 0.4
    b1 = dail_cal_carbs / 4

    dail_cal_prot = cal_tag * 0.3
    b2 = dail_cal_prot / 4

    dail_cal_fats = cal_tag * 0.3
    b3 = dail_cal_fats / 9 

    food = input("Enter food 1: ")
    food2 = input("Enter food 2: ")
    food3 = input("Enter food 3: ")

    result = food.title()
    result2 = food2.title()
    result3 = food3.title()

    csv_file = csv.reader(open('MyFoodData.csv','r'))
    csv_file2 = csv.reader(open('MyFoodData.csv','r'))
    csv_file3 = csv.reader(open('MyFoodData.csv','r'))


    grams_f1 = int(input("How many grams of %s you had?: " % result))
    grams_f2 = int(input("How many grams of %s you had?: " % result2))
    grams_f3 = int(input("How many grams of %s you had?: " % result3))
    
    for row in csv_file:
        if result in row[1]:
            carbs_f1 = ((grams_f1 * float(row[4]))/100)
            proteins_f1 = ((grams_f1 * float(row[3]))/100)
            fats_f1 = ((grams_f1 * float(row[2]))/100)

    for row in csv_file2:
        if result2 in row[1]:
            carbs_f2 = ((grams_f2 * float(row[4]))/100)
            proteins_f2 = ((grams_f2 * float(row[3]))/100)
            fats_f2 = ((grams_f2 * float(row[2]))/100)

    for row in csv_file3:
        if result3 in row[1]:
            carbs_f3 = ((grams_f3 * float(row[4]))/100)
            proteins_f3 = ((grams_f3 * float(row[3]))/100)
            fats_f3 = ((grams_f3 * float(row[2]))/100) 

    x1 =  b1 - carbs_f1 - carbs_f2 - carbs_f3 
    x2 =  b2 - proteins_f1 - proteins_f2 - proteins_f3 
    x3 =  b3 - fats_f1 - fats_f2 - fats_f3

    bc = 0.44
    bp = 0.11
    bf = 0.02

    pc = 0
    pp = 0.27
    pf = 0.13

    ac = 0.09
    ap = 0.02
    af = 0.15
    
    A0 = np.array([[bc,pc,ac],[bp,pp,ap],[bf,pf,af]])
    A1 = np.array([[x1,pc,ac],[x2,pp,ap],[x3,pf,af]])
    A2 = np.array([[bc,x1,ac],[bp,x2,ap],[bf,x3,af]])
    A3 = np.array([[bc,pc,x1],[bp,pp,x2],[bf,pf,x3]])

    Ax0 = np.linalg.det(A0)
    Ax1 = np.linalg.det(A1)
    Ax2 = np.linalg.det(A2)
    Ax3 = np.linalg.det(A3)

    #determine value of x,y,z
    x = Ax1/Ax0
    y = Ax2/Ax0
    z = Ax3/Ax0
    
    print()
    print("Carbs for %s is = " % result, end = "")
    print('%.2f g'% carbs_f1)
    print("Proteins for %s is = " % result, end = "")
    print('%.2f g'% proteins_f1)
    print("Fats for %s is = " % result, end = "")
    print('%.2f g'% fats_f1)
    print()
    print("Carbs for %s is = " % result2, end = "")
    print('%.2f g'% carbs_f2)
    print("Proteins for %s is = " % result2, end = "")
    print('%.2f g'% proteins_f2)
    print("Fats for %s is = " % result2, end = "")
    print('%.2f g'% fats_f2)
    print()
    print("Carbs for %s is = " % result3, end = "")
    print('%.2f g'% carbs_f3)
    print("Proteins for %s is = " % result3, end = "")
    print('%.2f g'% proteins_f3)
    print("Fats for %s is = " % result3, end = "")
    print('%.2f g'% fats_f3)
    print()
    print("Remainding carbs needed: %d g"%x1)
    print("Remainding proteins needed: %d g"%x2)
    print("Remainding fats needed: %d g"%x3)

    print()

    print("We recommend these foods in your diet!")
    print("1. Bread - High in Carbs")
    print("2. Pork - High in Protein")
    print("3. Avocado - High in Fats")

    print("You need to eat %.2fg of bread" %x)
    print("You need to eat %.2fg of pork" %y)
    print("You need to eat %.2fg of avocado" %z)
        

searchFood()