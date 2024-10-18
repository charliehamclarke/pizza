import pandas as pd
import time
import sys
from datetime import datetime, timedelta

# Functions
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no")

def phone_num_checker(question, low, high):
    while True:
        error = "Sorry, looks like your phone # is invalid. Please enter a valid phone number 📞."
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)

def p_id_num_checker(question, low, high):
    while True:
        error = f"Please enter a valid number between {low} and {high} 🍔"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)

def d_id_num_checker(question, low, high):
    while True:
        error = f"Please enter a valid number between {low} and {high} 🥤"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)

def string_checker(question, valid_ans):
    while True:
        error = "Please enter a valid option from the list."
        user_response = input(question).lower()
        for item in valid_ans:
            if user_response == item.lower() or user_response == item[0].lower():
                return item
        print(error)
        print()

def username_checker(question):
    error = "Whoops! Please only use letters and spaces 😬"
    while True:
        user_name = input(question).strip()  # Remove leading and trailing spaces
        if user_name and all(char.isalpha() or char.isspace() for char in user_name):
            return user_name
        else:
            print(error)


def address_checker(question):
    error = "Please input your address again.. 🏠"
    while True:
        users_address = input(question).capitalize()
        if yes_no("Are you sure this is right?") == "yes":
            return users_address
        else:
            print(error)

def post_code_num_checker(question):
    while True:
        error = "Invalid response, Please input a 4 digit Post Code 📬"
        try:
            user_response = input(question)
            if len(user_response) == 4 and user_response.isdigit():
                return int(user_response)
            else:
                print(error)
        except ValueError:
            print(error)

def main():
    # Welcome message
    print("<--- 🍔 Welcome to Charman Burger Joint 🍔 --->")
    time.sleep(1)

    # Variables
    deliv_option = ["delivery", "pick up"]
    burger_size_option = ["large", "medium", "small"]
    drink_size_option = ["330ml", "750ml", "1.5L"]

    # Burger and drink data
    burger_names = {
        1: "Classic Beef Burger", 2: "BBQ Bacon Burger", 3: "Cheese Lover's Burger",
        4: "Spicy Chicken Burger", 5: "Veggie Delight", 6: "Double Beef & Cheese",
        7: "Fish Fillet Burger", 8: "Mushroom Swiss Burger", 9: "Bacon and Egg Burger",
        10: "Grilled Chicken Deluxe", 11: "Pulled Pork Burger", 12: "Chili Beef Burger",
        13: "Classic Cheeseburger", 14: "Buffalo Chicken Burger", 15: "Teriyaki Burger",
        16: "Tofu Burger", 17: "Hawaiian Chicken Burger", 18: "Triple Cheese Burger"
    }

    drink_names = {1: "Lift", 2: "Fanta", 3: "Coke", 4: "L & P", 5: "Sprite"}

    burger_order = []
    burger_order_size = []
    drink_order = []
    drink_order_size = []

    # Delivery or pickup details
    d_or_p = string_checker("Is this order for delivery or pick up? ", deliv_option)

    if d_or_p == "delivery":
        cost_delivery = 6
        print("There is a $6 surcharge for delivery.")
        name = username_checker("Enter your name: ")
        phone_num = phone_num_checker("Enter your phone number: ", 100000000, 9999999999)
        post_code = post_code_num_checker("Enter post code: ")
        address = address_checker("Enter your address: ")
    else:
        cost_delivery = 0
        name = username_checker("Enter your name: ")
        phone_num = phone_num_checker("Enter your phone number: ", 100000000, 99999999999)

    # Burger order process
    want_menu = yes_no(f"Hello {name}, would you like to see the burger menu? ")

    if want_menu == "yes":
        print('''\n
|------------MENU------------|  
----------------------------------------|                        
Gourmet:                         Num id |
Classic Beef Burger                 1   |
BBQ Bacon Burger                    2   | 
Cheese Lover's Burger               3   |
Spicy Chicken Burger                4   |
Veggie Delight                      5   |
Double Beef & Cheese                6   |
----------------------------------------|                                  
Traditional:                            |
Fish Fillet Burger                 7   |
Mushroom Swiss Burger              8   |
Bacon and Egg Burger               9   |
Grilled Chicken Deluxe             10  |
Pulled Pork Burger                 11  |
Chili Beef Burger                  12  |
----------------------------------------|
Value:                                  |
Classic Cheeseburger               13  |
Buffalo Chicken Burger             14  |
Teriyaki Burger                    15  |
Tofu Burger                        16  |
Hawaiian Chicken Burger            17  |
Triple Cheese Burger               18  |
----------------------------------------|
Small | Medium | Large |
 $8.99| $11.99 |$15.99 |
------|--------|-------|
''')

        keep_going = "yes"
        while keep_going == "yes":
            burger_num_id = p_id_num_checker("Enter the burger number: ", 1, 18)
            burger_order.append(burger_num_id)
            size = string_checker("What Size | Small | Medium | Large |: ", burger_size_option)
            burger_order_size.append(size)
            burger_name = burger_names[burger_num_id]
            print(f"Great! You have selected a {size} {burger_name} burger.")
            keep_going = yes_no("Do you want to order another burger? ")

    # Drink order process
    want_drink_menu = yes_no("Would you like to see the drink menu? ")

    if want_drink_menu == "yes":
        print('''\n
|-------Drink Menu-------|
Num id | Drink           |
1      | Lift            |
2      | Fanta           |
3      | Coke            |
4      | L & P           |
5      | Sprite          |
|------------------------|
330ml |  750ml |  1.5L |
$2.49 |  $3.49 | $4.99 |
------|--------|-------|
''')

        keep_going = "yes"
        while keep_going == "yes":
            drink_num_id = d_id_num_checker("Enter the drink number: ", 1, 5)
            drink_order.append(drink_num_id)
            drink_size = string_checker("What size | 330ml | 750ml | 1.5L |: ", drink_size_option)
            drink_order_size.append(drink_size)
            drink_name = drink_names[drink_num_id]
            print(f"Great! You have selected a {drink_size} {drink_name}.")
            keep_going = yes_no("Do you want to order another drink? ")

    # Cost calculations
    cost_food = 8.99 * burger_order_size.count("small") + 11.99 * burger_order_size.count("medium") + 15.99 * burger_order_size.count("large")
    cost_drinks = 2.49 * drink_order_size.count("330ml") + 3.49 * drink_order_size.count("750ml") + 4.99 * drink_order_size.count("1.5L")
    cost_total = cost_delivery + cost_food + cost_drinks

    # Estimate time of delivery/pickup
    current_time = datetime.now()
    pickup_or_delivery_time = current_time + timedelta(minutes=30 if d_or_p == "delivery" else 15)

    # Generate the receipt
    print("\n" + "-" * 40)
    print("🍔 Charman Burger Joint Receipt 🍔")
    print("-" * 40)
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone_num}")
    if d_or_p == "delivery":
        print(f"Delivery Address: {address}")
        print(f"Post Code: {post_code}")
    print(f"Order Type: {d_or_p.capitalize()}")
    print("\nOrdered Burgers:")
    for i, burger_id in enumerate(burger_order):
        print(f"- {burger_order_size[i]} {burger_names[burger_id]}")
    print("\nOrdered Drinks:")
    for i, drink_id in enumerate(drink_order):
        print(f"- {drink_order_size[i]} {drink_names[drink_id]}")
    print("\nCost Breakdown:")
    print(f"Food Cost: ${cost_food:.2f}")
    print(f"Drink Cost: ${cost_drinks:.2f}")
    print(f"Delivery Cost: ${cost_delivery:.2f}")
    print(f"Total Cost: ${cost_total:.2f}")
    print(f"Estimated {d_or_p.capitalize()} Time: {pickup_or_delivery_time.strftime('%I:%M %p')}")
    print("-" * 40)
    print("Thank you for ordering at Charman Burger Joint! Enjoy your meal! 🍔")
    print("-" * 40)

    order_confirm = yes_no(f"Hello {name}, would you like to Confirm this Order? ")


    if order_confirm == "yes":
        keep_going == "yes"
    if order_confirm == "no":
        keep_going == "yes"

if __name__ == "__main__":
    while True:
        main()
        restart = yes_no("Do you want to start a new order? (yes/no): ").strip().lower()
        if restart != "yes":
            break
