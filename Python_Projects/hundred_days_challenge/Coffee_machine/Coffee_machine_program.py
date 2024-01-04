from Coffee_machine.Machine_instructions import MENU, resources


def check_resources(coffee_type, resources_list, money_amount):
    if coffee == "report":
        resources_list["Money"] = f"$ {money_amount}"
        for key in resources_list.keys():
            print(key, ":", resources_list[key])
        return False
    else:
        for liquid in MENU[coffee_type]["ingredients"]:
            if MENU[coffee_type]["ingredients"].get(liquid) > resources_list.get(liquid):
                print(f"Sorry there is not enough {liquid}.")
                return False
    return True


def payment(coffee_type, money):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_amount = quarters + dimes + nickles + pennies
    if total_amount >= MENU[coffee_type].get("cost"):
        change = round((total_amount - MENU[coffee_type].get("cost")), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} ☕ Enjoy!")
        money = money + MENU[coffee_type].get("cost")
        return money
    else:
        print(f"Sorry that's not enough money. Money refunded.")


money_in_machine = 0
while True:
    coffee = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    if coffee == 'off':
        break

    resource_checker = check_resources(coffee, resources, money_in_machine)
    if resource_checker:
        money_in_machine = payment(coffee, money_in_machine)
        for ingredient in MENU[coffee]["ingredients"]:
            resources[ingredient] = resources.get(ingredient) - MENU[coffee]["ingredients"].get(ingredient)
