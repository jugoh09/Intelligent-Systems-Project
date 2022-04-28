import csv
import numpy as np

def main():
    food_list = []
    add_food_list = []
    gram = []
    add_gram = []
    carbs_lst = []
    pro_lst = []
    fats_lst = []
    add_carbs_lst = []
    add_pro_lst = []
    add_fats_lst = []
    is_done = ''
    add_is_done =''

    cal_input = int(input("What is your daily calorie target?: "))

    dail_cal_carbs = cal_input * 0.4
    b1 = dail_cal_carbs / 4
    total_carbs = 0
    add_total_carbs = 0

    dail_cal_prot = cal_input * 0.3
    b2 = dail_cal_prot / 4
    total_pro = 0
    add_total_pro = 0

    dail_cal_prot = cal_input * 0.3
    b3 = dail_cal_prot / 4
    total_fats = 0
    add_total_fats = 0

    while is_done != 'y':
        findfood(food_list,gram)
        is_done=input("Is that all of your foods? (y/n):")

    search(food_list,gram)
    carbs_need(food_list,gram,carbs_lst)
    pro_need(food_list,gram,pro_lst)
    fats_need(food_list,gram,fats_lst)

    for ele in range(0, len(carbs_lst)):
        total_carbs = total_carbs + carbs_lst[ele]
        x1 = b1 - total_carbs

    for ele in range(0, len(pro_lst)):
        total_pro = total_pro + pro_lst[ele]
        x2 = b2 - total_pro

    for ele in range(0, len(fats_lst)):
        total_fats = total_fats + fats_lst[ele]
        x3 = b3 - total_fats

    print()
    print("Total carbs needed = %d g " %x1)
    print("Total proteins needed = %d g "%x2)
    print("Total fats needed = %d g "%x3)

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
    print("We recommend these foods in your diet!")
    print("1. Bread - High in Carbs")
    print("2. Pork - High in Protein")
    print("3. Avocado - High in Fats")
    print()
    print("You need to eat %.2f g of bread" %x)
    print("You need to eat %.2f g of pork" %y)
    print("You need to eat %.2f g of avocado" %z)
    
    print()
    while add_is_done != 'y':
        add_findfood(add_food_list,add_gram)
        add_is_done=input("Is that all of your foods? (y/n):")

    add_food(add_food_list,add_gram)
    add_carbs_need(add_food_list,add_gram,add_carbs_lst)
    add_pro_need(add_food_list,add_gram,add_pro_lst)
    add_fats_need(add_food_list,add_gram,add_fats_lst)

    for ele in range(0, len(add_carbs_lst)):
        add_total_carbs = add_total_carbs + add_carbs_lst[ele]
        new_x1 = x1 - add_total_carbs

    for ele in range(0, len(add_pro_lst)):
        add_total_pro = add_total_pro + add_pro_lst[ele]
        new_x2 = x2 - add_total_pro

    for ele in range(0, len(add_fats_lst)):
        add_total_fats = add_total_fats + add_fats_lst[ele]
        new_x3 = x3 - add_total_fats

    print()
    print("Updated total carbs needed = %d g " %new_x1)
    print("Updated total proteins needed = %d g "%new_x2)
    print("Updated total fats needed = %d g "%new_x3)



def findfood(food_list,gram):
    found = False
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        to_find = input("Enter food: ").title()
        for item in reader:
            if to_find in item[1]:
                food_list.append(to_find)
                gram_input = int(input("How much gram of %s?: "%item[1]))
                gram.append(gram_input)
                found = True
                break

    if not found:
        print("The item `{}` does not exist in the CSV".format(to_find))
        findfood(food_list,gram)
    else:
        print("The item `{}` exist in the CSV".format(to_find))
        print(food_list)
        print(gram)

def search(food_list,gram):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(gram)): 
            for row in reader:
                for item in food_list:
                    if item in row[1]:
                        carbs = (gram[i]*(float(row[4]))/100)
                        proteins= (gram[i]*(float(row[3]))/100)
                        fats = (gram[i]*(float(row[2]))/100)

                        print()
                        print("(%s):" %item)
                        print("Carbs = %.2f g" %carbs)
                        print("Proteins = %.2f g" %proteins)
                        print("Fats = %.2f g" %fats)

def carbs_need(food_list,gram,carbs_lst):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(gram)): 
            for row in reader:
                for item in food_list:
                    if item in row[1]:
                        carbs = (gram[i]*(float(row[4]))/100)
                        carbs_lst.append(carbs)
    
def pro_need(food_list,gram,pro_lst):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(gram)): 
            for row in reader:
                for item in food_list:
                    if item in row[1]:
                        protein = (gram[i]*(float(row[3]))/100)
                        pro_lst.append(protein)
    
def fats_need(food_list,gram,fats_lst):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(gram)): 
            for row in reader:
                for item in food_list:
                    if item in row[1]:
                        fats = (gram[i]*(float(row[2]))/100)
                        fats_lst.append(fats)

def add_findfood(add_food_list,add_gram):
    found = False
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        to_find = input("Anything else to add: ").title()
        for item in reader:
            if to_find in item[1]:
                add_food_list.append(to_find)
                gram_input = int(input("How much gram of %s?: "%item[1]))
                add_gram.append(gram_input)
                found = True
                break

    if not found:
        print("The item `{}` does not exist in the CSV".format(to_find))
        findfood(add_food_list,add_gram)
    else:
        print("The item `{}` exist in the CSV".format(to_find))
        print(add_food_list)
        print(add_gram)

    
def add_food(add_food_list,add_gram):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(add_gram)): 
            for row in reader:
                for item in add_food_list:
                    if item in row[1]:
                        carbs = (add_gram[i]*(float(row[4]))/100)
                        proteins= (add_gram[i]*(float(row[3]))/100)
                        fats = (add_gram[i]*(float(row[2]))/100)

                        print()
                        print("(%s):" %item)
                        print("Carbs = %.2f g" %carbs)
                        print("Proteins = %.2f g" %proteins)
                        print("Fats = %.2f g" %fats)

def add_carbs_need(add_food_list,add_gram,add_carbs_lst):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(add_gram)): 
            for row in reader:
                for item in add_food_list:
                    if item in row[1]:
                        carbs = (add_gram[i]*(float(row[4]))/100)
                        add_carbs_lst.append(carbs)
    
def add_pro_need(add_food_list,add_gram,add_pro_lst):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(add_gram)): 
            for row in reader:
                for item in add_food_list:
                    if item in row[1]:
                        protein = (add_gram[i]*(float(row[3]))/100)
                        add_pro_lst.append(protein)
    
def add_fats_need(add_food_list,add_gram,add_fats_lst):
    with open("MyFoodData.csv", "r") as f:
        reader = csv.reader(f)
        for i in range(0, len(add_gram)): 
            for row in reader:
                for item in add_food_list:
                    if item in row[1]:
                        fats = (add_gram[i]*(float(row[2]))/100)
                        add_fats_lst.append(fats)

main()



