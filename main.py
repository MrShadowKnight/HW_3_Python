# TASK №1

number_day = 0
while number_day >= 1 or number_day <=7:
    number_day = int(input("Введіть номер дня тижня: "))
    print(" ")
    if number_day == 1:
        print("Понеділок.")
        break
    elif number_day == 2:
        print("Вівторок.")
        break
    elif number_day == 3:
        print("Середа.")
        break
    elif number_day == 4:
        print("Четвер.")
        break
    elif number_day == 5:
        print("П'ятниця.")
        break
    elif number_day == 6:
        print("Субота.")
        break
    elif number_day == 7:
        print("Неділя.")
        break
    else:
        print("Не існує такого дня тижня.\n")

# TASK №2

number_month = 0
while number_month >= 1 or number_month <=12:
    number_month = int(input("Введіть номер місяця: "))
    print(" ")
    if number_month == 1:
        print("Січень.")
        break
    elif number_month == 2:
        print("Лютий.")
        break
    elif number_month == 3:
        print("Березень.")
        break
    elif number_month == 4:
        print("Квітень.")
        break
    elif number_month == 5:
        print("Травень.")
        break
    elif number_month == 6:
        print("Червень.")
        break
    elif number_month == 7:
        print("Ливень.")
        break
    elif number_month == 8:
        print("Серпень.")
        break
    elif number_month == 9:
        print("Вересень.")
        break
    elif number_month == 10:
        print("Жовтень.")
        break
    elif number_month == 11:
        print("Листопад.")
        break
    elif number_month == 12:
        print("Грудень.")
        break
    else:
        print("Не існує такого місяця.\n")

# TASK №3

number = float(input("Enter a number: "))
if number > 0:
    print("Number is positive\n")
elif number < 0:
    print("Number is negative\n")
elif number == 0:
    print("Number is equal to zero\n")
else:
    print("It's not a number!\n")

# TASK №4

number_one = float(input("Please enter the first number: "))
number_two = float(input("Please enter the second number: "))
if number_one == number_two:
    print("These numbers are equal to")
elif number_one > number_two:
    print(number_one, " ", number_two)
elif number_two > number_one:
    print(number_two, " ", number_one)
else:
    print("I don't know what happened to these numbers!")

# TASK SHOP

products = {
    'яблука': 10,
    'банани': 15,
    'апельсини': 12,
    'груші': 8,
    'ківі': 20
}
purchase_amount = 0
balance = 100
shopping_cart = []
while balance > 0:
    print("Яблука ", products["яблука"], "грн., -- 1")
    print("Банани", products["банани"], "грн., -- 2")
    print("Апельсини ", products["апельсини"], "грн., -- 3")
    print("Груші ", products["груші"], "грн., -- 4")
    print("Ківі ", products["ківі"], "грн., -- 5")
    
    print("Для виходу натисніть: Q\n")

    choice_products = input("Введіть номер продукту: ")
    if choice_products == "1" or choice_products == "2" or choice_products == "3" or choice_products == "4" or choice_products == "5":
        number_products = int(input("Введіть кількість продукдів: "))
        if choice_products == "1" and balance >= (products["яблука"] * number_products):
            element = "яблука"
            shopping_cart.append(number_products)
            shopping_cart.append(element)
            balance = balance - products["яблука"]* number_products
            purchase_amount = purchase_amount + products["яблука"]* number_products
            print("Товар додано до кошику!\n")
        elif choice_products == "2" and balance >= (products["банани"] * number_products):
            element = "банани"
            shopping_cart.append(number_products)
            shopping_cart.append(element)
            balance = balance - products["банани"]* number_products
            purchase_amount = purchase_amount + products["банани"]* number_products
            print("Товар додано до кошику!\n")
        elif choice_products == "3" and balance >= (products["апельсини"] * number_products):
            element = "апельсини"
            shopping_cart.append(number_products)
            shopping_cart.append(element)
            balance = balance - products["апельсини"]* number_products
            purchase_amount = purchase_amount + products["апельсини"]* number_products
            print("Товар додано до кошику!\n")
        elif choice_products == "4" and balance >= (products["груші"] * number_products):
            element = "груші"
            shopping_cart.append(number_products)
            shopping_cart.append(element)
            balance = balance - products["груші"]* number_products
            purchase_amount = purchase_amount + products["груші"]* number_products
            print("Товар додано до кошику!\n")
        elif choice_products == "5" and balance >= (products["ківі"] * number_products):
            element = "ківі"
            shopping_cart.append(number_products)
            shopping_cart.append(element)
            balance = balance - products["ківі"]* number_products
            purchase_amount = purchase_amount + products["ківі"]* number_products
            print("Товар додано до кошику!\n")
        elif choice_products == "1" or choice_products == "2" or choice_products == "3" or choice_products == "4" or choice_products == "5":
            print("На вашому балансі недостатньо коштів!\n")
    elif choice_products == "q":
        break
    else:
        print("Товар не знайдено!\n")
    print("Ваш баланс: ", balance, "грн.\n")

print("Ваші продукти: ", shopping_cart)
print("загальна сума покупок:", purchase_amount, "грн.")
print("Ваш баланс:", balance, "грн.\n")