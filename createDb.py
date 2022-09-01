import mysql.connector as con


# Connecting to mysql
try:
    db = con.connect(
        host = "localhost",
        user = "",  #enter your username
        passwd = "" #enter your password
    )
    print("\nConnected to mysql")
except Exception as e:
    print("\nFailed to connect")
    print(e)


# Creating a database
try:
    myCursor = db.cursor(buffered=True)
    myCursor.execute("CREATE DATABASE project")
    print("\nProject database has been created")
except Exception as e:
    print("\nFailed to create database")
    print(e)


# Connecting to database
try:
    db1 = con.connect(
        host = "localhost",
        user = "",      #enter your username
        passwd = "",    #enter your password
        database = "project"
    )
    print("\nConnected to the project database")
except Exception as e:
    print("\nFailed to connect to project database")
    print(e)
    




# Creating tables in database
# Employee
try:
    #                   buffered=True - for fetches
    myCursor = db1.cursor(buffered=True)
    myCursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, userName VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE)")
    print("\nTable Employee created!")
except Exception as e:
    print("\nFailed to create Employee table in database")
    print(e)

# Customer
try:
    myCursor.execute("CREATE TABLE Customer (id INT AUTO_INCREMENT PRIMARY KEY, userName VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, age INT NOT NULL, money DOUBLE)")
    print("\nTable Customer created!")
except Exception as e:
    print("\nFailed to create Customer table in database")
    print(e)

# Article
try:
    myCursor.execute("CREATE TABLE Article (id INT AUTO_INCREMENT PRIMARY KEY, brand VARCHAR(50) NOT NULL, model VARCHAR(50) NOT NULL, type VARCHAR(50) NOT NULL, price DOUBLE NOT NULL, quantity INT NOT NULL, size VARCHAR(10) NOT NULL )")
    print("\nTable Article created!")
except Exception as e:
    print("\nFailed to create Article table in database")
    print(e)

# Bill
try:
    myCursor.execute("CREATE TABLE Bill (id INT AUTO_INCREMENT PRIMARY KEY, totalPrice DOUBLE NOT NULL, customerId INT NOT NULL, articleId INT NOT NULL , quantity INT NOT NULL,  FOREIGN KEY (customerId) REFERENCES Customer(id), FOREIGN KEY (articleId)REFERENCES Article(id))")
    print("\nTable Bill created!")
except Exception as e:
    print("\nFailed to create Bill table in database")
    print(e)



# Adding rows in tables
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# everything MUST BE %s, or error "Not all parameters were used in the SQL statement"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # Employee
try:
    query = "INSERT INTO Employee (userName, password, email) VALUES (%s, %s, %s)"
    vals = [("admin1", "admin1123", "admin1@gmail.com"),
        ("admin2", "admin2123", "admin2@gmail.com"),
        ("a", "a", "a"),
        ("s", "s", "s"),
        ("admin3", "admin3123", "admin3@gmail.com")]

    myCursor.executemany(query, vals)
    db1.commit()
    print()
    print(myCursor.rowcount, "Employees added!")
except Exception as e:
    print("\nFailed to add employees")
    print(e)



# Customer
try:
    query = "INSERT INTO Customer (userName, password, email, age, money) VALUES (%s, %s, %s,%s, %s)"
    vals = [("customer1", "customer1123", "customer1@gmail.com", 22, 100.00),
        ("customer2", "customer2123", "customer2@gmail.com", 25, 123.45),
        ("a", "a", "a", 28, 10),
        ("s", "s", "s", 31, 1000),
        ("customer3", "customer3123", "customer3@gmail.com", 20, 212.33)]

    myCursor.executemany(query, vals)
    db1.commit()
    print()
    print(myCursor.rowcount, "Customers added!")
except Exception as e:
    print("\nFailed to add customers")
    print(e)




# Article
try:
    query = "INSERT INTO Article (brand, model, type, price, quantity, size) VALUES (%s, %s, %s, %s, %s, %s)"
    vals = [("nike", "air max", "shoes", 100, 7, '40'),
        ("adidas", "predator", "shoes", 110, 3, '39'),
        ("puma", "something", "shirt", 40, 10, 'M')]

    myCursor.executemany(query, vals)
    db1.commit()
    print()
    print(myCursor.rowcount, "Articles added!")
except Exception as e:
    print("\nFailed to add articles")
    print(e)


# Bill
try:
    query = "INSERT INTO Bill (totalPrice, customerId, articleId, quantity) VALUES (%s, %s, %s, %s)"
    vals = [(300, 2, 3, 1),
        ( 200, 1, 1, 1),
        (400, 3, 2, 1)]

    myCursor.executemany(query, vals)
    db1.commit()
    print()
    print(myCursor.rowcount, "Bills added!")
except Exception as e:
    print("\nFailed to add Bills")
    print(e)

