from Data import resources,MENU,coins

# Chick Responce
def checkRes(Responce):
    if Responce =="l":
        return 'latte'
    elif Responce =="c":
        return 'cappuccino'
    elif Responce =="e":
        return 'espresso'
# Chick Resources
def checkResources(resources,Responce):
    if Responce == "e":
        if orderRecources(Responce)['water'] <= resources['water'] and orderRecources(Responce)['coffee'] <= resources['coffee']:
            return True
        else:
            if orderRecources(Responce)['water'] > resources['water']:
                print("Sorry there is not enough water.")
                return False
            else:
                print("Sorry there is not enough Coffe.")
                return False
    elif Responce == "l" or Responce == "c":
        if orderRecources(Responce)['water'] <= resources['water'] and orderRecources(Responce)['coffee'] <= resources['coffee'] and orderRecources(Responce)['milk'] <= resources['milk']:
            return True
        else:
            if orderRecources(Responce)['water'] > resources['water']:
                print("Sorry there is not enough water.")
                return False
            elif orderRecources(Responce)['Coffe'] > resources['Coffe']:
                print("Sorry there is not enough Coffe.")
                return False
            else:
                print("Sorry there is not enough Milk.")
                return False
def orderRecources(Responce):
    if Responce == "e":
        return MENU['espresso']['ingredients']
    elif Responce == "l":
        return MENU['latte']['ingredients']
    elif Responce == "c":
        return MENU['cappuccino']['ingredients']

# Chick Coines
def checkCoins(Responce):
    if orderCoin(Responce) <= convertCoin():
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def orderCoin(Responce):
    if Responce == "e":
        return MENU['espresso']["cost"]
    elif Responce == "l":
        return MENU['latte']["cost"]
    elif Responce == "c":
        return MENU['cappuccino']["cost"]

def convertCoin():
    return ( (penny/100) + (Nicke/20) + (Dime/10) + (Quarter/4) )
money = 0
game = True
while game:
    Responce = input("What would you like? (E ==> espresso L ==> latte C ==> cappuccino): ").lower()
    if Responce == "off":
        game = False
    elif Responce =="report":
        print(f"Water :{resources['water']} \nmilk :{resources['milk']}\ncoffee :{resources['coffee']}\nmoney :{money}")
    elif Responce in ['l','e','c']:
        penny = int(input("how many penny: "))
        Nicke =int(input("how many Nicke: "))
        Dime = int(input("how many Dime: "))
        Quarter = int(input("how many Quarter: "))
        if checkCoins(Responce) == True :
            if checkResources(resources,Responce) == True :
                print(f"Here is your {checkRes(Responce)}. Enjoy!")
                money += orderCoin(Responce)
                if convertCoin() > orderCoin(Responce):
                    charged = round(convertCoin() - orderCoin(Responce),2)
                    print(f"please find charged {charged}")
                resources['water'] = resources['water'] - orderRecources(Responce)['water']
                if Responce !='e':
                    resources['milk'] = resources['milk'] - orderRecources(Responce)['milk']
                resources['coffee'] = resources['coffee'] - orderRecources(Responce)['coffee']