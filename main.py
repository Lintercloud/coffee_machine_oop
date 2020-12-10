from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
maker = CoffeeMaker()
account = MoneyMachine()

while True:  
    print(f"there are {menu.get_items()}")
    order_name = input("select your choice\n")
    if order_name == "report":
        maker.report()
        account.report()
    else:
        drink = menu.find_drink(order_name)
        if maker.is_resource_sufficient(drink):
            if account.make_payment(drink.cost):
                maker.make_coffee(drink)