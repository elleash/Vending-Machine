cold_drinks = {'A - Iced tea': 3, 
    'B - Coke': 2, 
    "C - Sprite ": 2,} #dictionary of cold drinks

hot_drinks = {'A - Coffee': 2,
    'B - Tea': 2,
    'C - Hot Chocolate': 2,} #dictionary of ot drinks

water = {'A - Cold':1,
    'B - Hot':1,
    'C - Room Temperature' :1} #dictionary of water

hard_snacks = {'A - Cookies': 3, 
    'B - Chips':3,  #dictionary of hard snacks
    'C - Chocolate':4}

soft_snacks = {'A - Cake':3,
    'B - Muffin':3,
    'C - Pudding': 4} #dictionary of soft snacks


def change(x,y): #function for the change of user
    return x-y #calculating the change

def new_moneys(x,y,z,a): #function to calculate the suggestion
    if x < y:
        return print("Insufficient amount") #shows that the user put little money
    else:
        print("You have inputted $", x, "and your change is $",change(x, y)) #displays a message with the users inputted money and calculates the change
        print([key for key in cold_drinks.keys()][z],"and",[key for key in hard_snacks.keys()][a], "has been dispensed. Enjoy!!") #dispenses the products


def n_moneys(x,y,z,a): #function to calculate the suggestion
    if x < y:
        return print("Insufficient amount") #shows that the user put little money
    else:
        print("You have inputted $", x, "and your change is $",change(x, y)) #displays a message with the users inputted money and calculates the change
        print([key for key in hot_drinks.keys()][z],"and",[key for key in hard_snacks.keys()][a], "has been dispensed. Enjoy!!") #dispenses the products

def c_moneys(x, y,z): #function to calculate and dispense product
    if x < y:
        return print("Insufficient amount") #shows that the user put little money
    else:
        print("You have inputted $", x, "and your change is $",change(x, y)) #displays a message with the users inputted money and calculates the change
        print([key for key in cold_drinks.keys()][z], "has been dispensed. Enjoy!!") #dispenses the product

def d_moneys(x, y,z): #function to calculate and dispense product but for the hot drinks section
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in hot_drinks.keys()][z], "has been dispensed. Enjoy!!")

def w_moneys(x, y,z): #function to calculate and dispense product but for the water section
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in water.keys()][z], "has been dispensed. Enjoy!!")

def hs_moneys(x, y,z): #function to calculate and dispense product but for the hard snacks section
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in hard_snacks.keys()][z], "has been dispensed. Enjoy!!")

def s_moneys(x, y,z): #function to calculate and dispense product but for the soft snacks section
    if x < y:
        return print("Insufficient amount")
    else:
        print("You have inputted $", x, "and your change is $",change(x, y))
        print([key for key in soft_snacks.keys()][z], "has been dispensed. Enjoy!!")
        
        

while True: #loops through the vending machine until user wants to stop

    print("Welcome to the Vending Machine! \nHere is a list of our items:")
    print("\n1 - Cold Drinks\n2 - Hot Drinks\n3 - Water\n4 - Hard Snacks\n5 - Soft Snacks") #presents the menu of categorized items

    choice = int(input(("\nEnter the item number of your selected item or enter 0 to quit: "))) #asks user to input their choice of food or exit out
    print("\n")

    if choice == 0: #when user inputs a 0, they will exit out of the vending machine
        break #stops the loop

    if choice == 1: #user chooses the first option

        print("The following items are:\n") #informs the user of the items in the specific category
        for key, value in cold_drinks.items(): #accesses the cold drink dictionary
            print(key.title(),": $",value) #print the key and value of the cold drinks
        
        while True: #loops through the cold drinks
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ") #asks user what they want or go back to the main menu

            if item == 'q' or item == 'Q': #when user enter the letter q, it will go back to the main menu
                print('\n') #adds whitespace
                break #ends the loop
            
            if item == 'a' or item == 'A': #user chooses the first option
                print("Your item is: Iced Tea")
                money = int(input("Your item is $3. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                c_moneys(money, 3, 0) #calls the c_moneys function
            
            elif item == 'b' or item == 'B': #user chooses the second option
                print("Your item is: Coke")
                suggest = input("Would you like $3 Chips with this order? Enter 'yes' if you would or 'no' to proceed: ") #makes a suggestion to also buy chips
                if suggest == 'yes' or suggest == 'Yes': #user chooses to take suggestion
                    new_money = int(input("Great! Your total is now $5. Please enter the amount of money you put in:")) #asks user to enter any amount of money they put in
                    new_moneys(new_money, 5, 1, 1) #calls the new_moneys function
                
                else: #user doesn't take suggestion
                    money = int(input("Your item is $2. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                    c_moneys(money, 2, 1) #calls the c_moneys function
            
            elif item == 'c' or item == 'C': #user chooses the second option
                print("Your item is: Sprite")
                suggest = input("Would you like $3 Chips with this order? Enter 'yes' if you would or 'no' to proceed: ") #makes a suggestion to also buy chips
                if suggest == 'yes' or suggest == 'Yes': #user chooses to take suggestion
                    new_money = int(input("Great! Your total is now $5. Please enter the amount of money you put in:")) #asks user to enter any amount of money they put in
                    new_moneys(new_money, 5, 1, 1) #calls the new_moneys function

                else: #user doesn't take suggestion
                    money = int(input("Your item is $2. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                    c_moneys(money, 2, 2)  #calls the c_moneys function

            else:
                print("\nInvalid Input") #user did not input a valid ID

    elif choice == 2: #user chooses the second option
        print("The following items are:\n") #informs the user of the items in the specific category
        for key, value in hot_drinks.items(): #accesses the hot drink dictionary
            print(key.title(),": $",value) #print the key and value of the hot drinks
        
        while True: #loops through the hot drinks
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ") #asks user what they want or go back to the main menu

            if item == 'q' or item == 'Q': #when user enter the letter q, it will go back to the main menu
                print('\n') #adds whitespace
                break #ends the loop
            
            if item == 'a' or item == 'A':#user chooses the first option
                print("Your item is: Coffee")
                suggest = input("Would you like $3 Cookies with this order? Enter 'yes' if you would or 'no' to proceed: ") #makes a suggestion to also buy cookies
                if suggest == 'yes' or suggest == 'Yes': #user chooses to take suggestion
                    new_money = int(input("Great! Your total is now $5. Please enter the amount of money you put in:")) #asks user to enter any amount of money they put in
                    n_moneys(new_money, 5, 0, 0) #calls the n_moneys function

                else: #user doesn't take suggestion
                    money = int(input("Your item is $2. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                    d_moneys(money, 2,0) #calls the d_moneys function
            
            elif item == 'b' or item == 'B':
                print("Your item is: Tea")
                suggest = input("Would you like $3 Cookies with this order? Enter 'yes' if you would or 'no' to proceed: ") #makes a suggestion to also buy cookies
                if suggest == 'yes' or suggest == 'Yes': #user chooses to take suggestion
                    new_money = int(input("Great! Your total is now $5. Please enter the amount of money you put in:")) #asks user to enter any amount of money they put in
                    n_moneys(new_money, 5, 1, 0) #calls the n_moneys function
                
                else: #user doen't take suggestion
                    money = int(input("Your item is $2. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                    d_moneys(money, 2,1) #calls the d_moneys function
            
            elif item == 'c' or item == 'C ':
                print("Your item is: Hot Chocolate")
                money = int(input("Your item is $2. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                d_moneys(money, 2,2) #calls the d_moneys function
            
            else:
                print("\nInvalid Input\n") #user did not input a valid id
    
    elif choice == 3: #user chooses the third option
        print("The following items are:\n")#informs the user of the items in the specific category
        for key, value in water.items(): #accesses the water dictionary
            print(key.title(),": $",value) #print the key and value of the water
        
        while True: #loops through the water
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")  #asks user what they want or go back to the main menu

            if item == 'q' or item == 'Q': #when user enter the letter q, it will go back to the main menu
                print('\n') #adds whitespace
                break #ends the loop
            
            if item == 'a' or item == 'A': #user chooses the first option
                print("Your item is: Cold Water")
                money = int(input("Your item is $1. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                w_moneys(money, 1, 0) #calls the w_moneys function
            
            elif item == 'b' or item == 'B': #user chooses the second option
                print("Your item is: Hot Water")
                money = int(input("Your item is $1. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                w_moneys(money, 1, 1) #calls the w_moneys function
            
            elif item == 'c' or item == 'C ': #user chooses the third option
                print("Your item is: Room Temperature Water")
                money = int(input("Your item is $1. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                w_moneys(money, 1, 2) #calls the w_moneys function
            
            else:
                print("\nInvalid Input\n") #user did not input a valid ID

    elif choice == 4: ##user chooses the fourth option
        print("The following items are:\n") #informs the user of the items in the specific category
        for key, value in hard_snacks.items(): #accesses the hard snack dictionary
            print(key.title(),": $",value) #print the key and value of the hard snacks
        
        while True: #loops through the hard snacks
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")  #asks user what they want or go back to the main menu

            if item == 'q' or item == 'Q': #when user enter the letter q, it will go back to the main menu
                print('\n') #adds whitespace
                break #ends the loop
            
            if item == 'a' or item == 'A': #user chooses the first option
                print("Your item is: Cookies")
                money = int(input("Your item is $3. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                hs_moneys(money, 3,0) #calls the hs_moneys function
            
            elif item == 'b' or item == 'B': #user chooses the second option
                print("Your item is: Chips")
                money = int(input("Your item is $3. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                hs_moneys(money, 3,1) #calls the hs_moneys function
            
            elif item == 'c' or item == 'C ': #user chooses the third option
                print("Your item is: Chocolate")
                money = int(input("Your item is $4. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                hs_moneys(money, 4,2)#calls the hs_moneys function

            else:
                print("\nInvalid Input\n") #user did not input a valid ID

    elif choice == 5: #user chooses the fifth option
        print("The following items are:\n") #informs the user of the items in the specific category
        for key, value in soft_snacks.items(): #accesses the soft snacks dictionary
            print(key.title(),": $",value) #print the key and value of the soft snacks
        
        while True: #loops through the soft snacks
            item = input("\nEnter the item letter if there is anything you like or enter 'q' to go back!: ")  #asks user what they want or go back to the main menu

            if item == 'q' or item == 'Q': #when user enter the letter q, it will go back to the main menu
                print('\n') #adds whitespace
                break #ends the loop
            
            elif item == 'a' or item == 'A': #user chooses the first option
                print("Your item is: Cake")
                money = int(input("Your item is $3. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                s_moneys(money, 3,0) #calls the s_moneys function
            
            elif item == 'b' or item == 'B': #user chooses the second option
                print("Your item is: Muffin")
                money = int(input("Your item is $3. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                s_moneys(money, 3,1) #calls the s_moneys function
            
            elif item == 'c' or item == 'C ': #user chooses the third option
                print("Your item is: Pudding")
                money = int(input("Your item is $4. Please enter the amount of money you put in: ")) #asks user to enter any amount of money they put in
                s_moneys(money, 4,2) #calls the s_moneys function

            else:
                print("\nInvalid Input") #user did not input a valid ID


    else:
        print('Invalid Input\n') #user did not input a valid ID
