# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from mechdatas import resources, MENU, coins

alive = True
credit = 0.0


def print_report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


def operation(drink):
    global credit
    print("Please insert coins.")
    new_credit = get_credit()
    credit += new_credit
    if credit < drink['cost']:
        credit -= new_credit
        print("Sorry that's not enough money. Money refunded.")
    else:
        # TODO: 1. Check if to much credit
        resources['money'] += drink['cost']
        credit -= drink['cost']
        ingredient = drink['ingredients']
        for i in ingredient:
            resources[i] -= ingredient[i]
        print(f"Here is your {drink}. Enjoy!")


def get_credit():
    total = 0.0
    for coin in coins:
        value = input(f"how many {coin}?:")
        total += float(value) * coins[coin]
    return total


def check_ressources(drink):
    ingredient = drink['ingredients']
    filled = True
    for i in ingredient:
        if ingredient[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            filled = False
    return filled


def turn_off():
    global alive
    alive = False


while alive:
    cmd = input("What would you like? (espresso/latte/cappuccino): ")
    while not (cmd == "off" or cmd == "report" or cmd == "espresso" or cmd == "latte" or cmd == "cappuccino"):
        cmd = input("What would you like? (espresso/latte/cappuccino): ")
    if cmd == "off":
        turn_off()
    elif cmd == "report":
        print_report()
    elif cmd == "latte" or cmd == "espresso" or cmd == "cappuccino":
        if check_ressources(MENU[cmd]):
            operation(MENU[cmd])
