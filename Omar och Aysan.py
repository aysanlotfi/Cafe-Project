print("Välkommen till vårt Café!")
print()


# FOOD MENU

food = ["Pizza", "Hamburger", "Sushi", "Sallad"]
food_prices = [100, 80, 120, 60]

# We define the function that prints food and price next to each other.
def show_food_menu():
    print("Maträtter:")

    for i in range(len(food)):
        print(i + 1, food[i], "-", food_prices[i], "kr")

# RECALL 
show_food_menu()

food_choice = (input("Välj en maträtt (1-4): "))
# This helps avoiding putting anything other than integers, or numbers between 1 and 4
while  not food_choice.isdigit() or int(food_choice) < 1 or int(food_choice) > 4 :
    print("Ogiltigt val.")
    food_choice = (input("Välj en maträtt (1-4): "))

# Now that the food is chosen, we need the quantity
food_quantity = (input("Hur många vill du beställa? "))
# This helps avoiding putting anything other than integers. Also the customer orders at least 1.

while not food_quantity.isdigit() or int(food_quantity) < 1:
    print("Ogiltigt antal.")
    food_quantity = (input("Hur många vill du beställa? "))

# The calculation of the price based on order.
food_total = food_prices[int(food_choice) - 1] * int(food_quantity)

print()
print("Du beställde", food_quantity, "st", food[int(food_choice) - 1])
print("Pris:", food_total, "kr")


# DRINK MENU

print()

drinks = ["Kaffe", "Te", "Juice", "Vatten"]
drink_prices = [30, 20, 25, 10]


def show_drink_menu():
    print("Drycker:")

    for i in range(len(drinks)):
        print(i + 1, drinks[i], "-", drink_prices[i], "kr")

#We have this as an innitial value so that if someone orders no drink, we can still have this.
drink_total = 0

drink_question = input("Vill du beställa en dryck? (ja/nej): ")
#This turns all letters to lowercase so that JA Ja jA Nej NEJ, etc are all accepted, and it will decide which path to go with.
while drink_question.lower() != "ja" and drink_question.lower() != "nej" :
    print("Skriv ja eller nej.")
    drink_question = input("Vill du beställa en dryck? (ja/nej): ")


if drink_question.lower() == "ja":

    print()
    show_drink_menu()

    drink_choice = (input("Välj en dryck (1-4): "))
# This helps avoiding putting anything other than integers, or numbers between 1 and 4
    while not drink_choice.isdigit() or int(drink_choice) < 1 or int(drink_choice) > 4:
        print("Ogiltigt val.")
        drink_choice = (input("Välj en dryck (1-4): "))


    drink_quantity = (input("Hur många vill du beställa? "))
# This helps avoiding putting anything other than integers. Also the customer orders at least 1.
    while not drink_quantity.isdigit() or int(drink_quantity) < 1:
        print("Ogiltigt antal.")
        drink_quantity = (input("Hur många vill du beställa? "))

# The calculation of the price based on order.
    drink_total = drink_prices[int(drink_choice) - 1] * int(drink_quantity)

    print()
    print("Du beställde", drink_quantity, "st", drinks[int(drink_choice) - 1])
    print("Pris:", drink_total, "kr")

else:
    print("Ingen dryck beställd.")


# CHECKOUT

print()
print("---------- KASSA ----------")

total_price = food_total + drink_total

print("Totalt pris:", total_price, "kr")


# MEMBER DISCOUNT

print()
#We have this as an innitial value so that if someone is not a member, we can still have this.
discount = 0

member = input("Är du medlem? Som medlem får du 10% rabatt. (ja/nej): ")

while member.lower() != "ja" and member.lower() != "nej":
    print("Skriv ja eller nej.")
    member = input("Är du medlem? Som medlem får du 10% rabatt. (ja/nej): ")


if member.lower() == "ja":

    mobile_number = input("Ange ditt mobilnummer för att bekräfta ditt medlemskap: ")
#We helps validating the swedish mobile number.
    while not mobile_number.isdigit() or len(mobile_number) != 10 or mobile_number[:2] != "07":
        print("Ditt mobilnummer är inte korrekt. Försök igen.")
        mobile_number = input("Ange ditt mobilnummer för att bekräfta ditt medlemskap: ")
#Calculating the discount; we just chose 10% as the only possible dicound percent.
    discount = total_price * 0.10
    total_price = total_price - discount

    print("Ditt medlemskap är bekräftat.")
#syntax highlighting-inside quotation marks, so Python treats the entire thing as text. 
# The % is just a character being displayed to the customer not an operator.
    print("Du får 10% rabatt.")
    print("Rabatt:", discount, "kr")

else:
    print("Ingen rabatt.")


print("Att betala:", total_price, "kr")


# PAYMENT

print()
print("Betalning:")
print("1. Swish")
print("2. Kort")

payment = (input("Välj betalningsmetod (1-2): "))
#This helps us only provide 2 valid options; card or swish.
while not payment.isdigit() or int(payment) < 1 or int(payment) > 2:
    print("Ogiltigt val.")
    payment = (input("Välj betalningsmetod (1-2): "))


if payment == "1":
    print()
    print("Skanna QR-koden för att betala med Swish.")


else:
    print()
    print("Sätt i eller blippa ditt kort för att betala.")


# RECEIPT
#This is only a random number we chose just to simplify.
order_number = 101

print()
print("---------- KVITTO ----------")
print("Mat:", food_total, "kr")
print("Dryck:", drink_total, "kr")
print("Rabatt:", discount, "kr")
print("Totalt betalt:", total_price, "kr")
print("Ordernummer:", order_number)

print()
print("Glöm inte att ta ditt ordernummer (kvitto).")
print("Vänta tills ditt ordernummer visas på skärmen.")
print()
print("Tack för din beställning!")