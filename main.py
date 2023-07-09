# TASK №1

# number_day = 0
# while number_day >= 1 or number_day <=7:
#     number_day = int(input("Введіть номер дня тижня: "))
#     print(" ")
#     if number_day == 1:
#         print("Понеділок.")
#         break
#     elif number_day == 2:
#         print("Вівторок.")
#         break
#     elif number_day == 3:
#         print("Середа.")
#         break
#     elif number_day == 4:
#         print("Четвер.")
#         break
#     elif number_day == 5:
#         print("П'ятниця.")
#         break
#     elif number_day == 6:
#         print("Субота.")
#         break
#     elif number_day == 7:
#         print("Неділя.")
#         break
#     else:
#         print("Не існує такого дня тижня.\n")

# TASK №2

# number_month = 0
# while number_month >= 1 or number_month <=12:
#     number_month = int(input("Введіть номер місяця: "))
#     print(" ")
#     if number_month == 1:
#         print("Січень.")
#         break
#     elif number_month == 2:
#         print("Лютий.")
#         break
#     elif number_month == 3:
#         print("Березень.")
#         break
#     elif number_month == 4:
#         print("Квітень.")
#         break
#     elif number_month == 5:
#         print("Травень.")
#         break
#     elif number_month == 6:
#         print("Червень.")
#         break
#     elif number_month == 7:
#         print("Ливень.")
#         break
#     elif number_month == 8:
#         print("Серпень.")
#         break
#     elif number_month == 9:
#         print("Вересень.")
#         break
#     elif number_month == 10:
#         print("Жовтень.")
#         break
#     elif number_month == 11:
#         print("Листопад.")
#         break
#     elif number_month == 12:
#         print("Грудень.")
#         break
#     else:
#         print("Не існує такого місяця.\n")

# TASK №3

# number = float(input("Enter a number: "))
# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Number is negative")
# elif number == 0:
#     print("Number is equal to zero")
# else:
#     print("WHAT IS THE NUMBER?")

# TASK №4

# number_one = float(input("Please enter the first number: "))
# number_two = float(input("Please enter the second number: "))
# if number_one == number_two:
#     print("These numbers are equal to")
# elif number_one > number_two:
#     print(number_one, " ", number_two)
# elif number_two > number_one:
#     print(number_two, " ", number_one)
# else:
#     print("I don't know what happened to these numbers!")

# TASK SHOP

products = {
    'яблука': 10,
    'банани': 15,
    'апельсини': 12,
    'груші': 8,
    'ківі': 20
}

print("Яблука ", products["яблука"], "грн, -- 1")
print("Банани", products["банани"], "грн, -- 2")
print("Апельсини ", products["апельсини"], "грн, -- 3")
print("Груші ", products["груші"], "грн, -- 4")
print("Ківі ", products["ківі"], "грн, -- 5\n")

balance = 100

shopping_cart = []
while balance >0:
    choice_products = int(input("Введіть номер продукту: "))
    if choice_products == 1:
        element = products["яблука"]
        shopping_cart.append(element)
        balance = balance - products["яблука"]

print(shopping_cart)
# for item in products:
#     print(products[item])