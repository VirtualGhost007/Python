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
earning = 0
# TODO 1. create a system that calculates money inserted
while True:
    try:
        print("Welcome to ☕️ shop")
        # TODO 2. create a system that asks for drink and depletes the resources
        item = input("What would you like? (espresso/latte/cappuccino): ")
        if item == "off":
            break
        elif item == "report":
            resources["earning"] = earning
            print(resources)
            break
        else:
            for resource in resources:
                resources[resource] -= MENU[item]["ingredients"][resource]
            if resources["water"] <= 0 or resources["milk"] <= 0 or resources["coffee"] <= 0:
                print("No resources to make coffee")
                resources["earning"] = earning
                print(resources)
                break
            dime = 0.10
            nickle = 0.05
            penny = 0.01
            quarter = 0.25

            n_dime = int(input("dime: "))
            n_nickle = int(input("nickle: "))
            n_penny = int(input("penny: "))
            n_quarter = int(input("quarter: "))

            total = (n_dime * dime) + (n_nickle * nickle) + (n_penny * penny) + (n_quarter * quarter)
            print(total)

            # TODO 3. shows the remaining change
            cost = MENU[item]["cost"]

            if total < cost:
                print("Insufficient amount entered.")
            else:
                earning += cost
                rem = abs(total - cost)
                if rem == 0:
                    print("No change.")
                else:
                    print(f"Your remaining change is ${rem}")
    except KeyError:
        continue
    except ValueError:
        continue
