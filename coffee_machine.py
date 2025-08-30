from Menu import MENU
from resource import resources


class CoffeeMachine:
    def __init__(self):
        # Copy resources into the machine's state
        self.resources = resources.copy()

    def report(self):
        print(f"milk : {self.resources['milk']}ml")
        print(f"water : {self.resources['water']}ml")
        print(f"coffee: {self.resources['coffee']}gms")
        print(f"money: ${self.resources.get('money', 0)}")

    @staticmethod
    def dollar_convertor(money):
        coin_values = {"quarter": 0.25, "dimes": 0.10, "nickel": 0.05, "pennies": 0.01}
        result = 0
        for key in money:
            result += (coin_values[key] * money[key])
        return result

    def is_money_enough(self, money_dict, coffee_type):
        require_money = self.get_cost(coffee_type)
        converted_money = self.dollar_convertor(money_dict)

        if converted_money < require_money:
            print(f"You don't have enough money for {coffee_type}. "
                  f"Cost is ${require_money}.")
            return False
        else:
            self.resources["money"] = round(self.resources.get("money", 0) + require_money, 2)
            if converted_money > require_money:
                refund = round(converted_money - require_money, 2)
                print(f"💰 You overpaid. Refunding ${refund}...")
        return True

    @staticmethod
    def get_ingredient(coffee_type):
        return MENU[coffee_type]["ingredients"]

    @staticmethod
    def get_cost(coffee_type):
        return MENU[coffee_type]["cost"]

    def is_ingredient_enough(self, coffee_type):
        coffee_ingredients = self.get_ingredient(coffee_type)
        for key in coffee_ingredients:
            if key in self.resources:
                if self.resources[key] < coffee_ingredients[key]:
                    print(f"We don't have enough {key}. "
                          f"Current available {key}: {self.resources[key]}")
                    return False
                else:
                    self.resources[key] -= coffee_ingredients[key]
            else:
                print(f"Ingredient {key} not available.")
                return False
        print(f"✅ Your {coffee_type} is ready, Enjoy ☕")
        return True
