MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def get_payment(type_of_coffee, name):
    if check_resources(type_of_coffee):
        if insert_coins(type_of_coffee, name):
            make_coffee(type_of_coffee, name)
            return
        else:
            return
    return


def check_resources(type_of_coffee):
    for item in type_of_coffee["ingredients"]:
        if resources[item] < type_of_coffee["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(type_of_coffee, name):
    for item in type_of_coffee["ingredients"]:
        resources[item] -= type_of_coffee["ingredients"][item]
    print(f"Here is your {name} ☕️. Enjoy!")


def insert_coins(type_of_coffee, name):
    global profit
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 00.1
    change_money = total_money - type_of_coffee["cost"]
    if change_money < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round(change_money,2)} in change.")
        profit += type_of_coffee["cost"]
        return True


while True:
    users_choice = input("What would you like? (espresso/latte/cappuccino):")
    if users_choice == "report":
        print_report()
    elif users_choice in MENU:
        get_payment(MENU[users_choice], users_choice)
    else:
        if users_choice != "off": 
            print("Invalid selection.")
        else:
            break




