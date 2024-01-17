'''
5. Develop a finance management application with the following features:
* 		The user records their total income.
* 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 		The user can list their expenses within the categories and get the total for each category.
* 		The user can obtain the total of their expenses.
* 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
* 		If the user spends more than they earn, the system will display advice to improve the user's financial health.
'''
import time 

totalIncome = 0
expenses = {}
medical = {}
household = {}
leisure = {}
savings = {}
education = {}
max_total = 0
max_dict = None

def countdown(seconds):
    print ("\nReturning to main menu in...")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

def totalIncomeRecord ():
    global totalIncome
    global expenses
    print("Enter your total income: ")
    income = input("\n>> ")
    totalIncome += int(income)
    print(f"Your reported total income is: {totalIncome}")
    categories()
    
def categories():
    print("\nHello!\n\nThere are four categories: \n\t [1] Medical expenses\n\t [2] Household expenses\n\t [3] Leisure\n\t [4] Savings\n\t [5] Education\n\t --------------------- \n\t [6] View Total\n\t [7] Evaluation")
    print("\n What should we view and update?")
    prompt = input(">> ")
    if int(prompt) == 1:
        expenses_check(medical, "Medical")
    elif int(prompt) == 2:
        expenses_check(household, "Household")
    elif int(prompt) == 3:
        expenses_check(leisure, "Leisure")
    elif int(prompt) == 4:
        expenses_check(savings, "Savings")
    elif int(prompt) == 5:
        expenses_check(education, "Education")
    elif int(prompt) == 6:
        total_expenses()
    elif int(prompt) == 7:
        evaluation()
    else:
        print ("That's not a menu option\n\nReturning to the expenses menu...")
        countdown(2)
        categories()

def listing(x):
    #This lists the items in the medical expenses dictionary in list form.
    #X Refers to a dictionary
    for key, value in x.items():
        print(f"\n{key}: {value}")
        
#Nos quedamos aqui         
def update(x , y):
    #Y refers to a name of a key
    #X Refers to the name of the dictionary
    global expenses
    print ("\n Add item")
    item = input("Item: ")
    
    if item == "stop":
        countdown(2)
        categories()
    else:    
        value = input("Add expense: ")
        value1 = int(value)
        x[item] = value1
        
        if y in expenses:
            expenses[y] += value1
        else:
            expenses[y] = value1
            
        expenses_tot = sum(x.values())
        print (f"{item}: {value1}")
        print (f"\nYour total for {y} expenses is: {expenses_tot}\n")
        print ("\nType 'stop' to go back to categories menu\n")
        update(x,y)
    

def total (x):
    #X refers to the name of the dictionary
    aList = []
    anotherList = []
    for value in x.values():
        aList.append(value)
    for key in x.keys():
        anotherList.append(key)
    #foo = x(x.values())
    total_sum = sum(aList)
    print(f"\nTotal {anotherList[0]} expenses: {total_sum}\n")
    

def expenses_check(x,y):
    
    #X Refers to the name of a dictionary
    #Y Refers to the name of the key
    global expenses 
    if not x:
        print(f"Your {y} expenses list appears to be empty.\nLet's add some items: ")
        prompt = input("\n\t[1] Yes\n\t[2] No\n\n\t >> ")
        if int(prompt) == 1:
            x[y] = 0
            foo = x[f"{y}"]
            print (f"\nCurrent {y} expenses: {foo}\n")
            update(x,y)
        elif int(prompt) == 2:
            expenses[y] = 0
            bar = x[f"{y}"]
            print (f"Current {y} expenses: {bar}")
            print ("Returning to the expenses menu...")
            countdown(2)
            categories()
    else:
        print("Do you want to: \n\n [1] View expenses\n [2] Update Medical Expenses\n")
        prompt1 = input(">> ")
        if int(prompt1) == 1:
            listing(x)
            total(x)
            prompt1 = input("Press any key to return to the categories menu")
            categories()
        elif int(prompt1) == 2:
            update(x, y)
        
        else:
            categories()
            
def total_expenses():
    #To be used inside update() (option 6)
    global expenses
    global max_total
    totalExp = 0
    for value in expenses.values():
        totalExp += sum(expenses.values())
        max_total += totalExp
        
    print (f"\nYour total for expenses this session is: {totalExp}\n")
    countdown(2)
    categories()
    
def calculate_total(x):
    #x Refers to expenses dictionary
    #To be used in highest_expense()
    return sum(x.values())

def evaluation():
    global expenses
    global totalIncome
    global max_total
    
    current_total = sum(expenses.values())
    
    if max_total ==0:
        max_total = current_total
        
    if max_total == totalIncome:
        highest_expense()
        countdown(2)
        categories()
    elif max_total < totalIncome:
        print("\nCongratulations! Your reported income is higher than your expenses!\n")
        print("\nDon't forget to treat yourself\n")
        prompt = input ("\nPress any key to return to the main menu\n")
        categories()
    
    elif max_total > totalIncome:
        print("\nYour expenses exceed your reported income. Please make adjustments to reduce stress.\n")
        prompt = input ("Press any key to return to the main menu\n")
        categories()
    else:
        prompt = input ("Will this block ever be executed in the script?")
        catagories()
        
def highest_expense():
    #To be used in evaluation()
    global expenses
    global max_total
    global max_dict
    
    for category in expenses:
        total = calculate_total(expenses)
        if total > max_total:
            max_total = total
            max_dict = category
    
    if max_dict:
        print ("\n You are 'breaking even'. You should reduce expenses!\n")
        print (f"\nThe category with the highest total expense is: {max_dict}")
        print (f"\nTotal expenses: {max_total}\n")
        prompt = input("Press any key to return to the main menu")
        categories()
        
    else:
        print ("No categories found.")
        countdown(2)
        categories()

def savings(x,y):
    
    
def main_menu():
    print("\nWelcome to your finance manager!\n")
    print("Let's record your total income first to get started!")
    totalIncomeRecord()

main_menu()
    
    
    