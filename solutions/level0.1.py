'''
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
'''

'''def new_user ():
    user = "Create new username: "
    passwd = "Enter a password: "
'''

import time

db1 = {}

def new_account():
    user = input ("Enter new username: ")
    passwd = input ("Enter a password: ")
    db(user, passwd)
    print (f"New account created!\n\tUsername: {user}\n\tPassword: {passwd}")

def db(x,y):
    global db1
    if x not in db1:
        db1[x] = [y,2000]
    else:
        print(f"Username '{x}' already exists with password '{y}'.")

def global_db():
    print(db1)

def countdown(seconds):
    print ("Returning to main menu in...")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    
def names():
    global db1
    counter = 1
    for i in db1.keys():
        print(f"\t[{counter}] {i}")
        counter += 1


attempts = 0

def login():
    global attempts
    global db1
    print("Hello! Enter your credentials: ")
    log_user = input("Enter your Username: ")
    log_passwd = input("Enter your Password: ")
    
    #if log_user in db1 and log_passwd in db1.values():
    if log_user in db1 and log_passwd == db1[log_user][0]:
        print ("Match!")
        #global_db()
        return log_user
        #dashboard()
    else:
        attempts += 1
        if attempts < 3:
            print ("Credentials do not match our records.\nPlease try again!")
            return login()
        else:
            print ("Maximum attempts reached (3).")
            return False

def transaction(x, y):
    global db1
    if x in db1 and y in db1:
        print ("A match was found!")
        print ("\n\t Enter the quantity you wish to deposit on this account")
        prompt = input(">> ")
        if db1[x][1] >= int(prompt):
            db1[x][1] -= int(prompt)
            db1[y][1] += int(prompt)
            
            print(f"\nSucessfully transferred {prompt} from {x} account to {y}'s account.")
            print(f"\nYou now have {db1[x][1]} in your account.\n")
            countdown(3)
            dashboard(x)
        else:
            print("\nInsufficient funds.")
            dashboard(x)
    else:
        print("That account does not exist")
        dashboard(x)
        
def deposit(x):
    print("\nCurrent funds: ",db1[x][1])
    print("How much money do you want to add to your account?")
    deposit = input("\n\t>>: ")
    db1[x][1] += int(deposit)
    print("Current funds: ", db1[x][1])
    countdown(3)
    dashboard(x)

def withdraw(username):
    print("\nCurrent funds: ",db1[username][1])
    print("How much money do you want to withdraw from the account?")
    withdraw = input("\n\t>> :")
    db1[username][1] -= int(withdraw)
    print ("Current funds: ", db1[username][1])
    countdown(3)
    dashboard(username)

def viewMomo(username):
    print ("\n\tYou currently have: ",db1[username][1],"in your account\n")
    countdown(2)
    dashboard(username)
           
def dashboard(x):
    print(f"\nHello {x}! Welcome to online bank.")
    print("Would you like to do with your money? \n\t [1] Deposit more \n\t [2] Withdraw it \n\t [3] View it \n\t [4] Make a transfer \n\t [5] Nothing, just log out.")
    prompt = input (">> ")
    if int(prompt) == 1:
        deposit(x)
    elif int(prompt) == 2:
        withdraw(x)
    elif int(prompt) == 3:
        viewMomo(x)
    elif int(prompt) == 4:
        print ("\nEnter the name of the account you wish to make a deposit.\n")
        prompt1 = input(">> ")
        transaction(x,prompt1)
    elif int(prompt) == 5:
        return script()
    else:
        script()
 
def access_db(x):
    x = db
    print(x)

def main_menu():
    print("\nWelcome!\n")
    print("Would you like to create an account or log in to an existing account? ")
    ask = input("\t[1] Create an Account\n\t[2] Login\n\tInput: ")
    return ask 

def script():
    ask = main_menu()
    if int(ask) == 1:
        new_account()
        script()
    elif int(ask) == 2:
        success = login()
        if success:
            dashboard(success)
            print ("Session closed successfully.\nBye!!")
        else:
            print ("Login unsuccessful.\n")
            script()            
    else:
        print("Session terminated. Bye!")
    
    

script()