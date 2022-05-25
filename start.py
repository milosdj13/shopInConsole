from createDb import *
# ovo pravi pycache folder
# ADD USERNAME AND PASSWORD IN createDb.py


def start():
    
    print ("\n\n Welcome to our shop!:")
    print("==========================")

    option = pickOptionStart()
    if(option == "1"):
        logInEmployee()
    elif(option == "2"):
        logInCustomer()
    elif (option == "3"):
        print("make acc for customer")
    elif (option == "4"):
        print("show products")
    elif (option == "5"):
        print("exit")
            

def pickOptionStart():
    showStartMenu()
    option = input("Pick option:  ")
    while option not in ("1", "2", "3", "4", "5"):
        print ("\n ERROR! You picked invalid option.")
        showStartMenu()
        option = input("Pick valid option: ")
    return option


def showStartMenu():
    print ("    1 - Log in as admin")
    print ("    2 - Log in as customer")
    print ("    3 - Create new account (customers only)")
    print ("    4 - See our products")
    print ("    5 - Exit")




def logInEmployee():
    print("\n\n---Welcome to the Employee logIn---")
    print("Please enter your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")
        try:
            # username is in [] because i need to pass list in SQL query 
            myCursor.execute("SELECT password FROM Employee WHERE userName = %s", [userName])
            userDb = myCursor.fetchone()
            if userDb[0] == password:
                isFound = True
                print("\n Welcome back "+userName)
            else:
                print("\nWrong password! Try again")
        except Exception as e:
            print("\nWrong username! Try again")
            print(e)
    
    picked = employeeOptions()
    pickedEmployee(picked)



def employeeOptions():
    showEmployeeOptions()
    option = input("Pick option:  ")
    while option not in ("1", "2", "3", "4", "5"):
        print ("\n ERROR! You picked invalid option.")
        showEmployeeOptions()
        option = input("Pick valid option: ")
    return option



def showEmployeeOptions():
    print("\nType in number based off of what you want to do: ")
    print("  1 - Make new account for employee")
    print("  2 - Add new article")
    print("  3 - Show graph")
    print("  4 - Log out")
    print("  5 - Exit program")






def pickedEmployee(picked):
    if picked == "1":
        print("Picked 1")
    if picked == "2":
        print("Picked 2")
    if picked == "3":
        print("Picked 3")
    if picked == "4":
        print("Picked 4")
    if picked == "5":
        print("Picked 5")
        





def logInCustomer():
    print("\n\n---Welcome to the Customer logIn---")
    print("Please enter your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")
        try:
            # username is in [] because i need to pass list in SQL query 
            myCursor.execute("SELECT password FROM Customer WHERE userName = %s", [userName])
            userDb = myCursor.fetchone()
            if userDb[0] == password:
                isFound = True
                print("\n Welcome back "+userName)
            else:
                print("\nWrong password! Try again")
        except Exception as e:
            print("\nWrong username! Try again")
            print(e)
    
    picked =customerOptions()
    pickedCustomer(picked)






def customerOptions():
    showCustomerOptions()
    option = input("Pick option:  ")
    while option not in ("1", "2", "3", "4", "5"):
        print ("\n ERROR! You picked invalid option.")
        showCustomerOptions()
        option = input("Pick valid option: ")
    return option





def showCustomerOptions():
    print("showing customer options")






def pickedCustomer(picked):
    if picked == "1":
        print("option 1")
    if picked == "2":
        print("option 2")
    if picked == "3":
        print("option 3")
    if picked == "4":
        print("option 4")
        





start()











