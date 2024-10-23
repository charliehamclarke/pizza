import pandas as pd
import time
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


def b_id_num_checker(question, low, high):
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
        users_address = input(question).strip().capitalize()
        if users_address:  # Checks if the input is not empty
            if yes_no("Are you sure this is right?") == "yes":
                return users_address
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
    burger_data = {
        "Num ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        "Burger": ["Classic Beef Burger", "BBQ Bacon Burger", "Cheese Lover's Burger",
                   "Spicy Chicken Burger", "Veggie Delight", "Double Beef & Cheese",
                   "Fish Fillet Burger", "Mushroom Swiss Burger", "Bacon and Egg Burger",
                   "Grilled Chicken Deluxe", "Pulled Pork Burger", "Chili Beef Burger",
                   "Classic Cheeseburger", "Buffalo Chicken Burger", "Teriyaki Burger",
                   "Tofu Burger", "Hawaiian Chicken Burger", "Triple Cheese Burger"],
        "Type": ["Gourmet", "Gourmet", "Gourmet", "Gourmet", "Gourmet", "Gourmet",
                 "Traditional", "Traditional", "Traditional", "Traditional", "Traditional", "Traditional",
                 "Value", "Value", "Value", "Value", "Value", "Value"],

        # Adjusted prices based on burger type
        "Small": [8.99, 8.99, 8.99, 8.99, 8.99, 8.99, 6.99, 6.99, 6.99, 6.99, 6.99, 6.99, 4.99, 4.99, 4.99, 4.99, 4.99,
                  4.99],
        "Medium": [11.99, 11.99, 11.99, 11.99, 11.99, 11.99, 9.99, 9.99, 9.99, 9.99, 9.99, 9.99, 7.99, 7.99, 7.99, 7.99,
                   7.99, 7.99],
        "Large": [15.99, 15.99, 15.99, 15.99, 15.99, 15.99, 12.99, 12.99, 12.99, 12.99, 12.99, 12.99, 9.99, 9.99, 9.99,
                  9.99, 9.99, 9.99]
    }

    drink_data = {
        "Num ID": [1, 2, 3, 4, 5],
        "Drink": ["Lift", "Fanta", "Coke", "L & P", "Sprite"],
        "330ml": [2.49] * 5,
        "750ml": [3.49] * 5,
        "1.5L": [4.99] * 5
    }

    burger_menu = pd.DataFrame(burger_data)
    drink_menu = pd.DataFrame(drink_data)

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
        print("\nBurger Menu:\n")
        print(burger_menu.to_string(index=False))  # Display burger menu using pandas DataFrame

    if want_menu == "no" or "yes":
        keep_going = "yes"
        burger_order = []
        burger_order_size = []
        while keep_going == "yes":
            burger_num_id = b_id_num_checker("Enter the burger number: ", 1, 18)
            burger_order.append(burger_num_id)
            size = string_checker("What Size | Small | Medium | Large |: ", burger_size_option)
            burger_order_size.append(size)
            burger_name = burger_menu.loc[burger_menu['Num ID'] == burger_num_id, 'Burger'].values[0]
            print(f"Great! You have selected a {size} {burger_name} burger.")
            keep_going = yes_no("Do you want to order another burger? ")

    # Drink order process
    want_drink_menu = yes_no("Would you like to see the drink menu? ")

    if want_drink_menu == "yes":
        print("\nDrink Menu:\n")
        print(drink_menu.to_string(index=False))  # Display drink menu using pandas DataFrame

        keep_going = "yes"
        drink_order = []
        drink_order_size = []
        while keep_going == "yes":
            drink_num_id = d_id_num_checker("Enter the drink number: ", 1, 5)
            drink_order.append(drink_num_id)
            drink_size = string_checker("What size | 330ml | 750ml | 1.5L |: ", drink_size_option)
            drink_order_size.append(drink_size)
            drink_name = drink_menu.loc[drink_menu['Num ID'] == drink_num_id, 'Drink'].values[0]
            print(f"Great! You have selected a {drink_size} {drink_name}.")
            keep_going = yes_no("Do you want to order another drink? ")

    # Cost calculations
    cost_food = 8.99 * burger_order_size.count("small") + 11.99 * burger_order_size.count(
        "medium") + 15.99 * burger_order_size.count("large")
    cost_drinks = 2.49 * drink_order_size.count("330ml") + 3.49 * drink_order_size.count(
        "750ml") + 4.99 * drink_order_size.count("1.5L")
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
        burger_name = burger_menu.loc[burger_menu['Num ID'] == burger_id, 'Burger'].values[0]
        print(f"- {burger_order_size[i]} {burger_name}")
    print("\nOrdered Drinks:")
    for i, drink_id in enumerate(drink_order):
        drink_name = drink_menu.loc[drink_menu['Num ID'] == drink_id, 'Drink'].values[0]
        print(f"- {drink_order_size[i]} {drink_name}")
    print(f"\nDelivery Fee: ${cost_delivery:.2f}")
    print(f"Total Food Cost: ${cost_food:.2f}")
    print(f"Total Drinks Cost: ${cost_drinks:.2f}")
    print(f"Total Cost: ${cost_total:.2f}")
    print(f"Estimated {d_or_p.capitalize()} Time: {pickup_or_delivery_time.strftime('%I:%M %p')}")
    print("-" * 40)
    print("Thank you for choosing Charman Burger Joint!")

    order_confirm = yes_no(f"Hello {name}, would you like to Confirm this Order? ")

    if order_confirm == "yes":
        print("Your order has been confirmed")
    else:
        print("Your order has been cancelled")

    new_order = yes_no("Do you want to start a new order? (yes/no): ").strip().lower()

    if new_order == "yes":
        main()
    else:
        print("Ka kite")
        exit()


if __name__ == "__main__":
    while True:
        main()
