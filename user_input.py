meals_a_day = int(input("How many meals you had today?:"))

foods = ["Bread","Fish","Milk"]

for m in range(1, meals_a_day + 1):
    ask = input("What was your %d st meal?: " % m)
print(ask)


