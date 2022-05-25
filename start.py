from createDb import *

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
        createAccCustomer()
        start()
        print("make acc for customer")
    elif (option == "4"):
        showArticles()
    elif (option == "5"):
        exit()
            

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
    print ("    4 - See our articles")
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
    
    while(True):
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
        print("\nMake new account for employee")
        addNewEmployee()
    if picked == "2":
        addNewArticle()
        print("Add new article")
    if picked == "3":
        print("Show graph")
    if picked == "4":
        print("Logging out....")
        start()
    if picked == "5":
        print("Exiting program....")
        exit()
        




def addNewEmployee():
    print("\n\nPlease enter informations about new employee")
    userName = input("Username : ")
    password = input("Password : ")
    email = input("Email : ")

    try:
        query ="INSERT INTO Employee(userName, password, email) VALUES (%s,%s,%s)"
        queryVals = (userName, password, email)
        myCursor.execute(query, queryVals)
        db1.commit()
        print(userName + " account successfully made!")
    except Exception as e:
        print("\n Couldnt add new employee")
        print(e)




def addNewArticle():
    print("Need to finish this")











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
            
    while(True):
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
        












def createAccCustomer():
    print("\n\nPlease enter your informations!")
    userName = input("Username : ")
    password = input("Password : ")
    email = input("Email : ")
    gender = input("Gender: ")
    money = input("How much money do you want to put on your account: ")
    try:
        query ="INSERT INTO Customer(userName, password, email, gender, money) VALUES (%s,%s,%s,%s,%s)"
        queryVals = (userName, password, email, gender, money)
        myCursor.execute(query, queryVals)
        db1.commit()
        print(userName + " account successfully made!")
    except Exception as e:
        print("\n Couldn't create account. Try again!")
        print(e)







def showArticles():
    try:
        myCursor.execute("SELECT * FROM Article")
        articles = myCursor.fetchall()
        for i in articles:
            print(f"\nItem number: {i[0]}, brand:{i[1]}, model:{i[2]}, type:{i[3]}, price:{i[4]}, quantity: {i[5]}, size: {i[6]}")
    
    except Exception as e:
        print("\nSomething went wrong! Couldn't read articles")
        print(e)




start()











