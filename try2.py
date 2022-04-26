import csv

food =[]
food_input = ''
grams_input = -1
csv_file = csv.reader(open('MyFoodData.csv','r'))
is_done=''

#while food_input != 'Done' and grams_input != 0:
while is_done != "y":
    food_input = input("Enter food: ")
    result = food_input.title()
    grams_input = int(input("How many grams?: "))
    food.append(result)
    is_done=input("Is that all of your foods? (y/n):")

    print(food)

    for col in food: 
        for row in csv_file:
            if result in row[1]:
                carbs_f1 = ((grams_input * float(row[4]))/100)
                proteins_f1 = ((grams_input * float(row[3]))/100)
                fats_f1 = ((grams_input * float(row[2]))/100)

                print("Carbs for %s is = " % result, end = "")
                print('%.2f g'% carbs_f1)
                print("Proteins for %s is = " % result, end = "")
                print('%.2f g'% proteins_f1)
                print("Fats for %s is = " % result, end = "")
                print('%.2f g'% fats_f1)
    
