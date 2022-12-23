cold_drinks = {'A - Iced tea': 3, 
    'B - Coke': 2, 
    "C - Sprite ": 2,}

hot_drinks = {'A - Coffe': 2,
    'B - Tea': 2,
    'C - Hot Chocolate': 2,}

water = {'A - Cold':1,
    'B - Hot':1,
    'C - Room Temperature' :1}

hard_snacks = {'A - Cookies': 3, 
    'B - Chips':3, 
    'C - Chocolate':4}

soft_snacks = {'A - Cake':3,
    'B - Muffin':3,
    'C - Pudding': 4}


def change(x,y):
    return x-y

def c_moneys(x, y,z):
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in cold_drinks.keys()][z], "has been dispensed. Enjoy!!")

def d_moneys(x, y,z):
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in hot_drinks.keys()][z], "has been dispensed. Enjoy!!")

def w_moneys(x, y,z):
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in water.keys()][z], "has been dispensed. Enjoy!!")

def hs_moneys(x, y,z):
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in hard_snacks.keys()][z], "has been dispensed. Enjoy!!")

def s_moneys(x, y,z):
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in soft_snacks.keys()][z], "has been dispensed. Enjoy!!")
        
        

while True:

    print("Welcome to the Vending Machine! \nHere is a list of our items:")
    print("\n1 - Cold Drinks\n2 - Hot Drinks\n3 - Water\n4 - Hard Snacks\n5 - Soft Snacks")

    choice = int(input(("\nEnter the item number of your selected item or enter 0 to quit: ")))
    print("\n")

    if choice == 0:
        break

    if choice == 1:

        print("The following items are:\n")
        for key, value in cold_drinks.items():
            print(key.title(),": $",value)
        
        while True:
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")

            if item == 'q' or item == 'Q':
                print('\n')
                break
            
            if item == 'a' or item == 'A':
                print("Your item is: Iced Tea")
                money = int(input("Your item is $3. Please enter the amount of money you put in: "))
                c_moneys(money, 3, 0)
            
            elif item == 'b' or item == 'B':
                print("Your item is: Coke")
                money = int(input("Your item is $2. Please enter the amount of money you put in: "))
                c_moneys(money, 2, 1)
            
            elif item == 'c' or item == 'C':
                print("Your item is: Sprite")
                money = int(input("Your item is $2. Please enter the amount of money you put in: "))
                c_moneys(money, 2, 2)
    
    if choice == 2:
        print("The following items are:\n")
        for key, value in hot_drinks.items():
            print(key.title(),": $",value)
        
        while True:
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")

            if item == 'q' or item == 'Q':
                print('\n')
                break
            
            if item == 'a' or item == 'A':
                print("Your item is: Coffee")
                money = int(input("Your item is $2. Please enter the amount of money you put in: "))
                d_moneys(money, 2,0)
            
            if item == 'b' or item == 'B':
                print("Your item is: Tea")
                money = int(input("Your item is $2. Please enter the amount of money you put in: "))
                d_moneys(money, 2,1)
            
            if item == 'c' or item == 'C ':
                print("Your item is: Hot Chocolate")
                money = int(input("Your item is $2. Please enter the amount of money you put in: "))
                d_moneys(money, 2,2)
    
    if choice == 3:
        print("The following items are:\n")
        for key, value in water.items():
            print(key.title(),": $",value)
        
        while True:
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")

            if item == 'q' or item == 'Q':
                print('\n')
                break
            
            if item == 'a' or item == 'A':
                print("Your item is: Cold Water")
                money = int(input("Your item is $1. Please enter the amount of money you put in: "))
                w_moneys(money, 1, 0)
            
            if item == 'b' or item == 'B':
                print("Your item is: Hot Water")
                money = int(input("Your item is $1. Please enter the amount of money you put in: "))
                w_moneys(money, 1, 1)
            
            if item == 'c' or item == 'C ':
                print("Your item is: Room Temperature Water")
                money = int(input("Your item is $1. Please enter the amount of money you put in: "))
                w_moneys(money, 1, 2)
    
    if choice == 4:
        print("The following items are:\n")
        for key, value in hard_snacks.items():
            print(key.title(),": $",value)
        
        while True:
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")

            if item == 'q' or item == 'Q':
                print('\n')
                break
            
            if item == 'a' or item == 'A':
                print("Your item is: Cookies")
                money = int(input("Your item is $3. Please enter the amount of money you put in: "))
                hs_moneys(money, 3,0)
            
            if item == 'b' or item == 'B':
                print("Your item is: Chips")
                money = int(input("Your item is $3. Please enter the amount of money you put in: "))
                hs_moneys(money, 3,1)
            
            if item == 'c' or item == 'C ':
                print("Your item is: Chocolate")
                money = int(input("Your item is $4. Please enter the amount of money you put in: "))
                hs_moneys(money, 4,2)

    if choice == 5:
        print("The following items are:\n")
        for key, value in soft_snacks.items():
            print(key.title(),": $",value)
        
        while True:
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")

            if item == 'q' or item == 'Q':
                print('\n')
                break
            
            if item == 'a' or item == 'A':
                print("Your item is: Cake")
                money = int(input("Your item is $3. Please enter the amount of money you put in: "))
                s_moneys(money, 3,0)
            
            if item == 'b' or item == 'B':
                print("Your item is: Muffin")
                money = int(input("Your item is $3. Please enter the amount of money you put in: "))
                s_moneys(money, 3,1)
            
            if item == 'c' or item == 'C ':
                print("Your item is: Pudding")
                money = int(input("Your item is $4. Please enter the amount of money you put in: "))
                s_moneys(money, 4,2)
