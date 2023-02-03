MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 0
should_continue = True
while should_continue:
    # TODO: inserting coins and returning total amount entered
    def coin_input():
        print("Please insert coins.")
        q = int(input("How many quarters?: "))
        d = int(input("How many dimes?: "))
        n = int(input("How many nickles?: "))
        p = int(input("How many pennies?: "))
        return (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)

    # TODO: printing and calculation
    def print_calc(string):
        global total_money
        if resources['water'] >= MENU[string]['ingredients']['water']:
            if resources['milk'] >= MENU[string]['ingredients']['milk']:
                if resources['coffee'] >= MENU[string]['ingredients']['coffee']:
                    user_amount = coin_input()
                    coffee_amount = MENU[string]['cost']
                    if user_amount >= coffee_amount:
                        change_amount = user_amount - coffee_amount
                        print(f"Here is ${round(change_amount, 2)} in change.")
                        print(f"Here is your {string} Enjoy")
                        resources['water'] = resources['water'] - MENU[string]['ingredients']['water']
                        resources['milk'] = resources['milk'] - MENU[string]['ingredients']['milk']
                        resources['coffee'] = resources['coffee'] - MENU[string]['ingredients']['coffee']
                        total_money = total_money + coffee_amount
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")

# TODO: user choice
    choice = input("What would you like?(Espresso/Latte/Cappuccino): ").lower()
    if choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total_money}")

    elif choice == 'off':
        should_continue = False

    else:
        print_calc(choice)
