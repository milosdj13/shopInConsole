from createDb import *
from matplotlib import pyplot as plt


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
    elif (option == "4"):
        showArticles()
        start()
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
    print ("    1 - Log in as employee")
    print ("    2 - Log in as customer")
    print ("    3 - Create new account (customers only)")
    print ("    4 - See our articles")
    print ("    5 - Exit")




# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================
# ======================================   EMPLOYEE    ================================================

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
            passDb = myCursor.fetchone()
            if passDb[0] == password:
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
    while option not in ("1", "2", "3", "4", "5", "6"):
        print ("\n ERROR! You picked invalid option.")
        showEmployeeOptions()
        option = input("Pick valid option: ")
    return option



def showEmployeeOptions():
    print("\nType in number based off of what you want to do: ")
    print("  1 - Make new account for employee")
    print("  2 - Add new article")
    print("  3 - Show money per customer - Graph")
    print("  4 - Change password")
    print("  5 - Log out")
    print("  6 - Exit program")






def pickedEmployee(picked):
    if picked == "1":
        addNewEmployee()
    if picked == "2":
        addNewArticle()
    if picked == "3":
        showGraph()
    if picked == "4":
        changePassword("Employee")
    if picked == "5":
        print("Logging out....")
        start()
    if picked == "6":
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
        print("\nSomething went wrong. Couldnt add new employee!")
        print(e)




def addNewArticle():
    print("\n\nPlease enter informations about new article")
    brand = input("Brand : ")
    model = input("Model : ")
    type = input("Type : ")
    price = input("Price : ")
    quantity = input("Quantity : ")
    size = input("Size : ")

    try:
        query ="INSERT INTO Article(brand, model, type, price, quantity, size) VALUES (%s,%s,%s,%s,%s,%s)"
        queryVals = (brand, model, type, price, quantity, size)
        
        myCursor.execute(query, queryVals)
        db1.commit()
        print(" Article successfully added!")
    except Exception as e:
        print("\nSomething went wrong! Couldn't add new article!")
        print(e)




def showGraph():
    myCursor.execute("SELECT * FROM Customer")
    customers = myCursor.fetchall()
    userNames = []
    banks = []

    for i in customers:
        userNames.append(i[1])
        banks.append(i[5])

    plt.bar(userNames, banks)
    plt.xlabel('Username: ')
    plt.ylabel('Money in bank: ')
    plt.show()




# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================
# ======================================   CUSTOMER    ================================================

def logInCustomer():
    print("\n\n---Welcome to the Customer logIn---")
    print("Please enter your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")

        try:
            myCursor.execute("SELECT password FROM Customer WHERE userName = %s", [userName])
            passDb = myCursor.fetchone()
            if passDb[0] == password:
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
    while option not in ("1", "2", "3", "4", "5", "6", "7"):
        print ("\n ERROR! You picked invalid option.")
        showCustomerOptions()
        option = input("Pick valid option: ")
    return option



def showCustomerOptions():
    print("\nType in number based off of what you want to do: ")
    print("  1 - Show articles")
    print("  2 - Show my purchases")
    print("  3 - See my balance")
    print("  4 - Buy something")
    print("  5 - Change password")
    print("  6 - Log out")
    print("  7 - Exit program")




def pickedCustomer(picked):
    if picked == "1":
        showArticles()
    elif picked == "2":
        showMyPurchases()
    elif picked == "3":
        seeMyBalance()
    elif picked == "4":
        buySomething()
    elif picked == "5":
        changePassword("Customer")
    elif picked == "6":
        print("Logging out....")
        start()
    elif picked == "7":
        print("Exiting program....")
        exit()
        
        



def showMyPurchases():
    print("Please confirm your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")
        try:
            myCursor.execute("SELECT password FROM Customer WHERE userName = %s", [userName])
            passDb = myCursor.fetchone()
            if passDb[0] == password:
                isFound = True
                print("\nAuthentification confirmed! You can see your purchases below: ")
                idCust = getId(userName)
                myCursor.execute("SELECT totalPrice FROM Bill WHERE customerId = %s", idCust)
                purchases = myCursor.fetchall()
                for i in purchases:
                    print(i)
            else:
                print("\nWrong username/password! Try again!")
        except Exception as e:
            print("\nSorry, something went wrong!")
            print(e)



def getId(userName):
    try:
        myCursor.execute("SELECT id FROM Customer WHERE userName = %s", [userName])
        id = myCursor.fetchone()
        return id
    except Exception as e:
        print("\nWe are sorry, something went wrong!")
        print(e)





def seeMyBalance():
    print("Please confirm your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")

        try:
            myCursor.execute("SELECT password FROM Customer WHERE userName = %s", [userName])
            passDb = myCursor.fetchone()
            if passDb[0] == password:
                isFound = True
                print("\nAuthentification confirmed! You can see your balance below: ")
                myCursor.execute("SELECT money FROM Customer WHERE userName = %s", [userName])
                balance = myCursor.fetchone()
                print(balance[0])
            else:
                print("\nWrong username/password! Try again!")
        except Exception as e:
            print("\nSorry, something went wrong!")
            print(e)





def buySomething():
    print("\n\nThis is the list of our available articles: ")
    articles =showArticles()
    option = input(" Enter the number of the article you want to buy: ")

    while int(option) not in range(1, len(articles)+1):
        print ("\n ERROR! You picked invalid option.")
        showArticles()
        option = input("Pick valid option: ")

    makePurchase(option)







def makePurchase(option):
    print("Please confirm your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")

        try:
            myCursor.execute("SELECT password FROM Customer WHERE userName = %s", [userName])
            passDb = myCursor.fetchone()
            if passDb[0] == password:
                isFound = True
                print("\nAuthentification confirmed! We are looking for article and then we will make a bill... ")
                
                
                myCursor.execute("SELECT * FROM Article WHERE id = %s", [option])
                article = myCursor.fetchone()

                myCursor.execute("SELECT * FROM Customer WHERE userName = %s", [userName])
                user = myCursor.fetchone()

                updateTables(article, user)
            else:
                print("\nWrong username/password! Try again!")
        except Exception as e:
            print("\nSorry, something went wrong!")
            print(e)






def updateTables(article, user):
    if int(article[4]) > int(user[5]):
        print("YOU DONT HAVE ENOUGH FUNDS FOR THIS TRANSACTION!")
    elif int(article[5]) < 1:
        print("Sorry, currently no items in storage!")
    else:

        try:
            quan = article[5]
            idArticle=article[0]
            myCursor.execute("UPDATE Article SET quantity=%s WHERE id = %s", (quan-1, idArticle))
            db1.commit()

            money = user[5] - article[4]
            idUser = user[0]
            myCursor.execute("UPDATE Customer SET money='%s' WHERE id = %s", (money, idUser))
            db1.commit()

            query = "INSERT INTO Bill (totalPrice, customerId, articleId) VALUES (%s, %s, %s)"
            vals = (article[4], user[0], article[0])

            myCursor.execute(query, vals)
            db1.commit()

            print("\nARTICLE PAID SUCCESSFULLY")
        except Exception as e:
            print("\n\nSomething failed")
            print(e)










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
        return articles
    except Exception as e:
        print("\nSomething went wrong! Couldn't read articles")
        print(e)




def changePassword(person):
    print("Please confirm your username and password!")
    isFound = False
    while (isFound == False):
        userName = input("Username : ")
        password = input("Password : ")
        print("============================")
        print(person)
        try:
            if person == "Customer":
                myCursor.execute("SELECT password FROM Customer WHERE userName = %s", [userName])
                passDb = myCursor.fetchone()
                if passDb[0] == password:
                    isFound = True
                    print("\nAuthentification confirmed! Please insert new password ")
                    newPassword = input("New password : ")
                    confirmPassword = input("Confirm new password : ") 

                    if  newPassword == confirmPassword:
                        query ="UPDATE Customer SET password = %s WHERE userName = %s"
                        queryVals = (newPassword, userName)
                        myCursor.execute(query, queryVals)
                        db1.commit()                                              
                        print("\nPassword succesfully changed! Redirecting you to the starting menu....")
                    else:
                        print("\nPasswords are not the same!")
                else:
                    print("\nWrong username/password! Try again!")
            else:
                myCursor.execute("SELECT password FROM Employee WHERE userName = %s", [userName])
                # myCursor.execute("SELECT * FROM Customer WHERE userName = %s", [userName])
                passDb = myCursor.fetchone()
                if passDb[0] == password:
                    isFound = True
                    print("\nAuthentification confirmed! Please insert new password ")
                    newPassword = input("New password : ")
                    confirmPassword = input("Confirm new password : ") 

                    if newPassword == confirmPassword:
                        query ="UPDATE Employee SET password = %s WHERE userName = %s"
                        queryVals = (newPassword, userName)
                        myCursor.execute(query, queryVals)
                        db1.commit()
                        print("Password succesfully changed! Redirecting you to the starting menu....")
                    else:
                        print("Passwords are not the same!")
                    
                else:
                    print("\nWrong username/password! Try again!")
        
        except Exception as e:
            print("\nSorry, something went wrong!")
            print(e)



start()











