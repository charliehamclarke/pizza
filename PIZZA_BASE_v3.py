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
        error = "Sorry looks like your phone # is invalid, Please enter a valid Phone # 📞 "
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
        error = f"Please enter a valid number between {low} and {high} 🍕"
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
        error = f"Please enter a valid option from the list... "
        user_response = input(question).lower()
        for item in valid_ans:
            if user_response == item.lower() or user_response == item[0].lower():
                return item
            elif user_response == item.lower().replace("ml", "").replace("l", ""):
                return item
        print(error)
        print()

def username_checker(question):
    error = "Whoops! Please only use letters and spaces 😬"
    while True:
        user_name = input(question)
        if all(char.isalpha() or char.isspace() for char in user_name):
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
    print("<--- 🍕 Welcome to Charman Pizzaria 🍕 --->")
    time.sleep(1)

    # Variables
    yes_no_options = ["yes", "no"]
    deliv_option = ["delivery", "pick up"]
    pizza_size_option = ["large", "medium", "small"]
    drink_size_option = ["330ml", "750ml", "1.5L"]
    total_time = 0
    users_address = ""

    # Pizza names mapped by ID
    pizza_names = {
        1: "Lamb Kebab",
        2: "Crispy BBQ Pork Belly",
        3: "Chicken Bacon & Aoli",
        4: "Smokehouse Meat lover",
        5: "Peri-Peri Chicken",
        6: "The Lot",
        7: "Philly Cheese Steak",
        8: "Supreme",
        9: "Double Bacon Cheeseburger",
        10: "Butter Chicken",
        11: "BBQ Meat lovers",
        12: "Chicken Supreme",
        13: "Cheesy Garlic Pizza",
        14: "Pepperoni",
        15: "Ham Cheese",
        16: "Simply Cheese",
        17: "Hawaiian",
        18: "Mega Pepperoni"
    }

    # Drink names mapped by ID
    drink_names = {
        1: "Lift",
        2: "Fanta",
        3: "Coke",
        4: "L & P",
        5: "Sprite"
    }

    pizza_order = []
    pizza_order_size = []
    drink_order = []
    drink_order_size = []

    # Delivery or pickup details
    d_or_p = string_checker("Is this order for delivery or pick up? ", deliv_option)

    if d_or_p == "delivery":
        cost_delivery = 6
        print("There is a $6 surcharge for delivery")
        name = username_checker("Enter your name: ")
        phone_num = phone_num_checker("Enter your phone number: ", 100000000, 9999999999)
        post_code = post_code_num_checker("Enter post code: ")
        address = address_checker("Enter your address: ")
        print()
    else:
        cost_delivery = 0
        name = username_checker("Enter your name: ")
        phone_num = phone_num_checker("Enter your phone number: ", 100000000 , 99999999999)

    # Menu and order process
    want_menu = yes_no(f"Hello {name}, would you like the menu? ")

    if want_menu == "yes":
        print('''\n
|------------MENU------------|  
----------------------------------------|                        
Gourmet:                         Num id |
Lamb Kebab                          1   |
Crispy BBQ Pork Belly               2   | 
Chicken Bacon & Aoli                3   |
Smokehouse Meat lover               4   |
Peri-Peri Chicken                   5   |
The Lot                             6   |
----------------------------------------|                                    
Traditional:                            |
Philly Cheese steak                 7   |
Supreme                             8   |
Double Bacon Cheeseburger           9   |
Butter Chicken                      10  |
BBQ Meat lovers                     11  |
Chicken Supreme                     12  |
----------------------------------------|
Value:                                  |
Cheesy Garlic Pizza                 13  |
Pepperoni                           14  |
Ham Cheese                          15  |
Simply Cheese                       16  |
Hawaiian                            17  |
Mega Pepperoni                      18  |
----------------------------------------|
Small | Medium | Large |
 $9   |   $12  |  $16  |
------|--------|-------|
''')

        keep_going = "yes"
        while keep_going == "yes":
                pizza_num_id = p_id_num_checker("Enter the pizza number: ", 1, 18)
                pizza_order.append(pizza_num_id)
                size = string_checker("What Size | Small | Medium | Large |: ", pizza_size_option)
                pizza_order_size.append(size)
                pizza_name = pizza_names[pizza_num_id]
                print(f"Great! You have selected a {size} {pizza_name} pizza.")
                print()
                keep_going = yes_no("Do you want to order another pizza? ")

    small_food_count = pizza_order_size.count("small")
    medium_food_count = pizza_order_size.count("medium")
    large_food_count = pizza_order_size.count("large")

    cost_food = 8.99 * small_food_count + 11.99 * medium_food_count + 15.99 * large_food_count

    # Display the ordered pizzas with their sizes
    if len(pizza_order) == 0:
        print("You have not ordered any pizzas...  🍕\n ")
    else:
        print("You have ordered the following pizzas :")
        for i, pizza_id in enumerate(pizza_order):
            print(f"- {pizza_order_size[i]} {pizza_names[pizza_id]}\n")

    # Drink menu and order process
    want_drink_menu = yes_no(f"Hello {name}, would you like the drink menu? ")

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
Sizes: 330ml , 750ml, 1.5L
''')

        keep_going = "yes"
        while keep_going == "yes":
                drink_num_id = d_id_num_checker("Enter the drink number: ", 1, 5)
                drink_order.append(drink_num_id)
                drink_size = string_checker("What size | 330ml | 750ml | 1.5L |: ", drink_size_option)
                drink_order_size.append(drink_size)
                drink_name = drink_names[drink_num_id]
                print(f"Great! You have selected a {drink_size} {drink_name}.")
                print()
                keep_going = yes_no("Do you want to order another drink? ")

    small_drink_count = drink_order_size.count("330ml")
    medium_drink_count = drink_order_size.count("750ml")
    large_drink_count = drink_order_size.count("1.5L")

    cost_drinks = 2.49 * small_drink_count + 3.49 * medium_drink_count + 4.99 * large_drink_count

    # Display the ordered drinks with their sizes
    if len(drink_order) == 0:
        print("You have not ordered any drinks... 🥤 \n ")
    else:
        print("You have ordered the following drinks:")
        for i, drink_id in enumerate(drink_order):
            print(f"- {drink_order_size[i]} {drink_names[drink_id]}\n")

    if want_menu != "yes" and want_drink_menu != "yes":
        print("What? You ordered nothing? 😭")
        time.sleep(1)
        print("How about we try that again.. 🤔")
        return  # This will end the function and let the loop handle restarting

    else:
        # Evaluate the cost of each product and service & display the final cost
        if d_or_p == "delivery":
            print("Cost of Delivery 🛵 = " + str(cost_delivery))
            time.sleep(1)
        else:
            print("")
        print("Cost of Food 🍕 = " + str(cost_food))
        time.sleep(1)
        print("Cost of Drink 🥤 = " + str(cost_drinks))
        time.sleep(1)
        print("Calculating total cost", end="")
        sys.stdout.flush()
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
        time.sleep(1)
        print(".")
        time.sleep(2)
        cost_total = cost_delivery + cost_drinks + cost_food
        print()
        print("Total cost = ${:.2f}".format(cost_total))
        # Estimate of delivery / pickup time

        current_time = datetime.now()
        time_15_minutes_later = current_time + timedelta(minutes=15)
        time_30_minutes_later = current_time + timedelta(minutes=30)

        if d_or_p == "delivery":
            print("Your pizza should arrive at around:", time_30_minutes_later.strftime("%I:%M %p"))
        else:
            print("Your pizza should be ready for pickup at around:", time_15_minutes_later.strftime("%I:%M %p"))

        print()

        # loading bar
        time.sleep(0.5)
        print("               ⣠⣤⣶⣶⣦⣄⣀")
        time.sleep(0.5)
        print("⠀            ⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀")
        time.sleep(0.5)
        print("⠀    ⠀       ⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀")
        time.sleep(0.5)
        print("      ⠀   ⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⣿⣿⣿⣿⣿⣆⠀⠀⠀")
        time.sleep(0.5)
        print("⠀ ⠀       ⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀")
        time.sleep(0.5)
        print(" ⠀     ⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇")
        time.sleep(0.5)
        print("⠀⠀    ⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇")
        time.sleep(0.5)
        print("⠀⠀   ⡰⠉⠖⣀⠀⠀⢀⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀")
        time.sleep(0.5)
        print("⠀  ⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀")
        time.sleep(0.5)
        print(" ⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀")
        time.sleep(0.5)
        print(" ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀")
        time.sleep(0.5)
        print(" ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀")
        time.sleep(0.5)
        print(" ⠈⠓⠾⠇⠀⠀⠀⠀")

if __name__ == "__main__":
    while True:
        main()
        restart = yes_no("Do you want to start a new order? (yes/no): ").strip().lower()
        if restart != "yes":
            break