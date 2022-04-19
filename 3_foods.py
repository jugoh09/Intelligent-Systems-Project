import csv

def searchFood():
    lst = []

    n = int(input("Enter number of meals: "))

    for i in range(0,n):
        food = input("Enter food %d: " %(i+1))
        result = food.title()
        lst.append(result)

        if result in lst:
            grams_f1 = int(input("How many grams of %s you had?: " % result))
            csv_file = csv.reader(open('MyFoodData.csv','r'))
            
            for row in csv_file:
                if result in row[1]:
                    carbs_f1 = ((grams_f1 * float(row[4]))/100)
                    proteins_f1 = ((grams_f1 * float(row[3]))/100)
                    fats_f1 = ((grams_f1 * float(row[2]))/100)

                    print("Carbs for %s is = " % result, end = "")
                    print('%.2f g'% carbs_f1)
                    print("Proteins for %s is = " % result, end = "")
                    print('%.2f g'% proteins_f1)
                    print("Fats for %s is = " % result, end = "")
                    print('%.2f g'% fats_f1)
        

searchFood()