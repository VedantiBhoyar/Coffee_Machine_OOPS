from coffee_machine import  CoffeeMachine

should_continue = True
coffee_machine_instance = CoffeeMachine()

while should_continue:

   user_demand=input("What would you like? (espresso/latte/cappuccino):").strip().lower()
   if user_demand == "report":
       coffee_machine_instance.report()
   elif user_demand not in ["espresso" ,"latte" , "cappuccino"]:
     print("We only serve espresso, latte, cappuccino")
   elif user_demand == "off":
       should_continue= False
   else:
     quarter = int(input("how many quarter"))
     dimes = int(input("how many dimes "))
     nickel = int(input("how many nickel"))
     pennies = int(input("how many pennies"))

     money_dict = {"quarter": quarter, "dimes": dimes, "nickel": nickel, "pennies": pennies}
     money_enough =  coffee_machine_instance.is_money_enough(money_dict,user_demand)
     if money_enough:
         ingredients_enough = coffee_machine_instance.is_ingredient_enough(user_demand)
         if not ingredients_enough:
             print("Your full refund is in progress")
             coffee_machine_instance.resources["money"] -= coffee_machine_instance.get_cost(user_demand)

     should_rerun = input("Do you want to have something else type y or n").strip().lower()

     if should_rerun == "y":
        should_continue = True
     else:
       should_continue = False


