from Data import resources,MENU,coins
# Chick Resources
def checkResources(resources,Responce):
    if Responce == "e":
        if orderRecources(Responce)['water'] <= resources['water'] and orderRecources(Responce)['coffee'] <= resources['coffee']:
            return True
        else:
            return  False
    elif Responce == "l" or Responce == "c":
        if orderRecources(Responce)['water'] <= resources['water'] and orderRecources(Responce)['coffee'] <= resources['coffee'] and orderRecources(Responce)['milk'] <= resources['milk']:
            return True
        else:
            return  False
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
        return False
        print("Sorry that's not enough money. Money refunded.")

def orderCoin(Responce):
    if Responce == "e":
        return MENU['espresso']["cost"]
    elif Responce == "l":
        return MENU['latte']["cost"]
    elif Responce == "c":
        return MENU['cappuccino']["cost"]

def convertCoin():
    return ( (penny/100) + (Nicke/20) + (Dime/10) + (Quarter/4) )


Responce = input("What would you like? (E ==> espresso L ==> latte C ==> cappuccino): ").lower()

penny = int(input("how many penny: "))
Nicke =int(input("how many Nicke: "))
Dime = int(input("how many Dime: "))
Quarter = int(input("how many Quarter: "))

print(checkResources(resources,Responce))
print(orderCoin(Responce))
print(convertCoin())
print(checkCoins(Responce))