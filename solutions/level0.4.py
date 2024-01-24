'''
4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.  
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
'''

import time
import random 

db = {}
db_item = {}
attempts = 0

def countdown(seconds):
    print ("Returning to main menu in...")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

def main_menu():
    print("\nWelcome to an online shipping system!\n")
    prompt = input("Do you want to:\n[1] Login?\n[2] Create a new account?\n[3] Exit the app\n\t>> ")
    
    if int(prompt) == 1:
        sucess = login()
        if sucess:
            user_menu(sucess)
    elif int(prompt) == 2:
        new_account()
    elif int(prompt) == 3:
        print("\nGoodbye!!\n")
    else:
        main_menu()

def user_menu(x):
    global db 
    print (f"\nHello {x}, welcome to your dashboard!\n")
    
    prompt = input("\nDo you want to:\n[1] Send a package?\n[2] Exit the system to main menu?\n\t>> ")
    if int(prompt) == 1:
        list_item(x)
    elif int(prompt) == 2:
        main_menu()
    elif int(prompt) == 3:
        print (db_item)
    else:
        print("\nThat's not an option!\n")
        user_menu(x)

def list_item(x):
    #x Refers to the username
    
    global db_item
    global db
    print("\nWhat is the item you wish to ship?")
    prompt = input("\n>> ")
    users = {"Users": {
        "Username": x, 
        "item": prompt
    }}
    y = prompt
    update_dict(users)
    send_package(x, y)
    receive_package(x)
    ship()    

def ship():
    global db_item
    print(f"\n{db_item['Sender Info']['from']}, your item ({db_item['Users']['item']}) will be sent from {db_item['Sender Info']['SenderAddress']} to {db_item['Receiver Info']['to']} in {db_item['Receiver Info']['ReceiverAddress']}\n")
    print(f"Here's your item number {db_item["Item Info"]["Number"]}\n") 

def update_dict(x):
    #x Refers to a dictionary that will update db_item
    global db_item
    for key, value in x.items():
        if key in db_item:
            db_item[key].update(value)
        else:
            db_item[key] = value


def item_weight():
    '''
    This function asks for item weight and calcultates shipping 
    costs at $2 per kg. Then it assigns a random number to the item.
    '''
    global db_item 
    print("\nEnter the weight of the item you wish to send: ")
    weight = input("\n>> ")
    cost = float(weight) * 2
    package_number = random.randint(1000, 999999)
    db_item_weight = { "Item Info": {
        "weight": weight,
        "cost": cost,
        "Number": package_number
    }}
    
    update_dict(db_item_weight)
    
    print (f"\nYour item weights {weight} kilograms and the shipping cost is {cost}\n")
    
def send_package(x, y):
    #x refers to the username in session
    #y refers to the name of the item
    global db_item
    global db
    send_name = input("Enter your name: ")
    send_address = input("Enter your address: ")
    
    db_item_send = { "Sender Info": {
        "item" : y,
        "from" : send_name,
        "SenderAddress" : send_address,
    }}
    
    update_dict(db_item_send)
    item_weight()
    
def receive_package(x):
    #x refers to the username in session. 
    global db_item
    global db
    
    rec_name = input ("Enter the receiver's name: ")
    rec_add = input ("Enter the receiver's address: ")
    
    db_item_rec = { "Receiver Info": {
        "to": rec_name,
        "ReceiverAddress": rec_add,
    }}
    update_dict(db_item_rec)
    
def login():
    global attempts
    global db
    print("\nHello! Enter your credentials: ")
    log_user = input("\nEnter your Username: ")
    log_passwd = input("Enter your Password: ")
    
    if log_user in db and log_passwd == db[log_user][0]:
        print ("Match!")
        return log_user 
    else:
        attempts += 1
        if attempts < 3:
            print ("\nCredentials do not match our records.\nPlease try again!")
            return login()
        elif attempts == 3:
            print ("Maximum attempts reached (3).")
            print ("The app has been locked for 30 seconds.")
            countdown(30)
            main_menu()
            return False
        else:
            login()

def new_account():
    user = input ("Enter new username: ")
    passwd = input ("Enter a password: ")
    addUser_db(user, passwd)
    print (f"\nNew account created!\n\tUsername: {user}\n\tPassword: {passwd}")
    countdown(2)
    main_menu()
    
def addUser_db(x,y):
    global db
    if x not in db:
        db[x] = [y]
    else:
        print(f"Username '{x}' already exists with password '{y}'.")

main_menu()