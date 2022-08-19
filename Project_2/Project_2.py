import sys

categ = [{'catId': 0, 'Name': 'Desk', 'Description': 'Free standing'},
         {'catId': 1, 'Name': 'Monitor', 'Description': 'PC monitors'}]  # List of dictionaries for Categories
prod = [{'pId': 0, 'Name': 'Big Desk', 'Price': 200.0, 'CategoryId': 0},
        {'pId': 1, 'Name': 'Oled Monitor', 'Price': 120.0, 'CategoryId': 1}]  # List of dictionaries for Products
orders = [{'order_id': 0, 'customer_id': 0, 'product_id': 0, 'product_quantity': 2, 'order_status': 'Shipped',
           'total_price': 400.0}, {'order_id': 1, 'customer_id': 1, 'product_id': 1, 'product_quantity': 5,
                                   'order_status': 'Shipped', 'total_price': 1100.0}]  # List of dictionaries for Orders
customers = [{"cId": 0, "Name": "Eugene", "Email": "dgsdf@fgd.com", "Number": "01296583999",
              "Street": "11 Fleet Street", "Town": "Southampton", "Country": "United Kingdom", "Password": "123"},
             {"cId": 1, "Name": "Edward", "Email": "dfsf@fgd.com", "Number": "01236583999",
              "Street": "25 Row Lane", "Town": "Oxford", "Country": "United Kingdom",
              "Password": "123"}]  # List of dictionaries for Customers
admins = [{'adId': 0, 'Name': 'Abas', 'Password': "hello"}, {'adId': 1, 'Name': 'Beatrice', 'Password': "hello"},
          {'adId': 2, 'Name': 'Haze', 'Password': "hello"}]  # List of dictionaries for Admins


# Function for Main Menu
def dashboard(isAdmin, id):
    if isAdmin:  # checks if the user is an admin and shows admin panel
        print("[1] Insert Category\n[2] Insert Products\n[3] Total Sales\n[4] Logout\n")
        admin = input("What would you like to do: ")  # admin choice
        print()
        if admin == "1":  # option 1
            insertCategory(categ, id)  # call function for creating new category
        elif admin == "2":  # option 2
            insertProducts(prod, categ)  # call function for creating new product
        elif admin == "3":  # option 3
            print("[1] Sales by Product\n[2] Sales by Category \n[3] Sales by Price Range\n[4] Sales by "
                  "Location\n[5] Go back to dashboard")
            sales = input("What would you like to do: ")  # sales choice
            print()
            if sales == "1":
                for currentProd in prod:
                    print("Product ID:", currentProd["pId"], "|| Product Name: ", currentProd["Name"],
                          "|| Product Price: ",
                          currentProd["Price"], "|| Category ID: ", currentProd["CategoryId"], "\n")
                product_id = input("Enter product ID you are looking for: ")
                salesByID(product_id, id)  # call function for displaying all sales by product id
            elif sales == "2":
                for currentCat in categ:
                    print("Category ID:", currentCat["catId"], "|| Category Name: ", currentCat["Name"],
                          "|| Category Description: ", currentCat["Description"], "\n")
                category_name = input("Enter category name you are looking for: ")
                salesByCategory(category_name, id)  # call function for displaying all sales by category name
            elif sales == "3":
                price_range = input("What range are you looking for [1] Ascending [2] Descending: ")
                salesByPriceRange(price_range, id)  # call function for displaying all sales by price range
            elif sales == "4":
                salesByLocation(id)
            elif sales == "5":
                dashboard(True, id)
        else:
            print("\nYou have been logged out.\n")
            login(customers, admins, True)

    else:  # otherwise display customer panel
        print("[1] Place Order\n[2] Order Status\n[3] Change Details\n[4] Logout")
        customer = input("What would you like to do: ")  # customer choice
        if customer == "1":
            place_order(id, orders, prod)  # call function for placing an order
            print("\nOrder has been placed!\n")
            dashboard(False, id)  # return to dashboard
        elif customer == "2":
            print()
            order_status = int(input("What is the order number: "))  # order status
            found = False  # bool for if order is found
            for order in orders:  # loop for order in the orders list
                if order_status == order["order_id"] and id == order[
                    "customer_id"]:  # check if status of order is the same as the order we're searching for
                    found = True
                    if order["order_status"] != "Delivered":
                        print()
                        choice = int(input("Have you received this order [1] Yes [2] No: "))  # customer choice
                        print()
                        if choice == 1:
                            order["order_status"] = "Delivered"  # change order status to delivered if option is Yes
                    print(f"Order ID:|| Product Name: || Quantity:  || Price:  || Order Status:  ")
                    for i in prod:  # loop through product list
                        if i["pId"] == order["product_id"]:  # check if the product id is equal to the one in the list
                            name = i["Name"]  # name of product id at the position i
                    print(order["order_id"], "\t\t", "\t", name, "\t  ", order["product_quantity"], "\t\t ",
                          order["total_price"], "\t\t", order["order_status"] + "\n")
            if not found:  # if order not found
                print("\nOrder doesn't exist!\n")
            return dashboard(False, id)  # return to dashboard
        elif customer == "3":
            insertCustomerDetails(customers, id)  # call function for updating the customer details
        else:
            print("\nYou have been logged out.\n")
            login(customers, admins, True)  # return to log in menu


# Login function for customers and admins
def login(customers, admins, c):
    if c == True:
        sys.exit()
    while True:
        print("[1] Customer Login\n[2] Admin Login\n[3] Customer Registration\n[4] Exit")
        check = input(
            "\nAre you a Customer or an Admin: ")  # check if the user is customer or admin
        print()
        if check == "2":  # admin
            try:
                a_username = int(input(
                    "Enter admin ID: "))  # admin username
                a_password = input(
                    "Enter admin password: ")  # admin password
                if a_username <= len(
                        admins) - 1:  # username must be less or equal to the list of admins - 1
                    if a_password == admins[a_username][
                        "Password"]:  # if passwords match
                        print("\nSuccessful!\n{} has been logged in.\n".format(admins[a_username]["Name"]))
                        dashboard(True,
                                  a_username)  # return to the dashboard
            except:
                pass
        elif check == "1":
            try:
                c_username = int(input(
                    "Enter customer ID: "))  # customer username
                c_password = input(
                    "Enter customer password: ")  # customer password
                if c_username <= len(
                        admins) - 1:  # username must be less or equal to the list of admins - 1
                    if c_password == customers[c_username][
                        "Password"]:  # if passwords match
                        print("\nSuccessful!\n{} has been logged in.\n".format(customers[c_username]["Name"]))
                        dashboard(False,
                                  c_username)  # return to the dashboard
            except:
                pass
        elif check == "3":
            insertCustomerDetails(customers,
                                  "-1")  # update customer details
        else:
            sys.exit()
            break


def format_email(email):
    if len(email.split("@")[0]) < 1 or email.count(".") != 1 or email.count("@") != 1 \
            or (not email.endswith(".co") and not email.endswith(".com")
                and not email.endswith(".in") and not email.endswith(
                ".org")):  # If Left split is left than or the number of "@" characters is over 1, or if the email ends in .co,.com,.in or .org
        return False
    else:
        return True

    # Function for registering a new customer (used as update customer details also)


def insertCustomerDetails(customers, id):
    check = 0
    if id == "-1":  # if customer id is less than 0
        check = 1
        cId = len(
            customers)  # customer id is equal to the length of the list
    else:
        cId = id  # else customer id will be equal to id
    while True:
        try:
            name = input("What's your name: ")
            if name.isalpha() and len(
                    name) >= 1:  # check for name to be all letters and length >= 1
                break
        except:
            pass
    while True:
        try:
            email = input(
                "What's your email address: ")  # email address
            if format_email(
                    email):  # check for email to be in format
                break
        except:
            pass
    while True:
        try:
            number = int(input(
                "What's your phone number: "))  # phone number
            if 15 <= number >= 10:  # phone number has to be >= 10 and <= 15
                break
        except:
            pass
    while True:
        try:
            street = input("What's your street name: ")
            if len(street) >= 1:  # street name has to be >= 1
                break
        except:
            pass
    while True:
        try:
            town = input(
                "What is the name of your city: ")  # city name
            if len(town) >= 1:  # city name has to be >= 1
                break
        except:
            pass
    while True:
        try:
            country = input(
                "What is the name of your country: ")  # country name
            if len(country) >= 1:  # country name has to be >= 1
                break
        except:
            pass
    while True:
        try:
            password = input(
                "What is the password you want to use: ")  # customer password
            if len(password) >= 8:  # password must be at least 8 characters
                break
        except:
            pass

    details = {
        # dictionary for customer details
        "cId": cId,
        "Name": name,
        "Email": email,
        "Number": number,
        "Street": street,
        "Town": town,
        "Country": country,
        "Password": password
    }
    if check != 0:
        customers.append(
            details)  # appending the current customer details to the end of the list
    else:
        customers.insert(id,
                         details)  # inserting the new updated customer details
    print(
        "\nCustomer ID: {} || Password: {} || Name: {} || Email: {} || Phone Number: {} || Street: {} || City: {} || Country: {} \n".format(
            details["cId"],
            details["Password"],
            details["Name"],
            details["Email"], details["Number"],
            details["Street"],
            details["Town"],
            details["Country"]), end="\n")
    if check == 1:
        login(customers, admins,
              False)  # go back to log in menu
    else:
        dashboard(False,
                  id)  # go back to the dashboard


# Function for inserting a new category
def insertCategory(categ, id):
    catId = len(categ)  # category id is equal to the length of the list

    while True:
        catName = input("Enter category name: ")  # category name
        if catName.isalpha() and len(catName) > 1:  # checks if the category name contains letters and length is > 1
            break
    while True:
        catDesc = input("Enter category description: ")  # category description
        if len(catDesc) > 1:  # checks if the length is > 1
            break
    cat = {  # dictionary for category details
        "catId": catId,
        "Name": catName,
        "Description": catDesc,
    }
    categ.append(cat)  # appending the current category details to the end of the list
    print("\n" + cat["Name"] + " is now a new category.\n")
    for currentCat in categ:
        print("Category ID:", currentCat["catId"], "|| Category Name: ", currentCat["Name"],
              "|| Category Description: ", currentCat["Description"], "\n")
    dashboard(True, id)  # go back to dashboard


# Function for inserting new products
def insertProducts(prod, categ):
    pId = len(prod)  # order id is equal to the length of the list
    while True:
        try:
            proName = input("Enter product name: ")  # product name
            if len(proName) > 1:  # product name must have the length > 1
                break
        except:
            print("\nInvalid Input.\n")
    while True:
        try:
            price = input("Enter product price: ")  # price of product
            if price.isdigit():  # check if price contains numbers
                price = float(price)  # change price value to a float
                break
        except:
            print("\nInvalid Input.\n")
    while True:  # Error handling
        try:
            catId = int(input("Enter category ID: "))  # category id
            if 0 <= catId < len(categ):  # check if category id is >= 0 and < length of category list
                break
        except:
            print("\nInvalid Input.\n")
    pro = {  # dictionary for product details
        "pId": pId,
        "Name": proName,
        "Price": price,
        "CategoryId": catId,
    }
    prod.append(pro)  # appending the current product details to the end of the list
    print(pro["Name"] + " is now a new product.\n")
    for currentProd in prod:
        print("Product ID:", currentProd["pId"], "|| Product Name: ", currentProd["Name"], "|| Product Price: ",
              currentProd["Price"], "|| Category ID: ", currentProd["CategoryId"], "\n")
    dashboard(True, id)  # go back to dashboard


# Function for placing an order
def place_order(cId, orders, prod):
    print()
    for currentProd in prod:
        print("Product ID:", currentProd["pId"], "|| Product Name: ", currentProd["Name"], "|| Product Price: ",
              currentProd["Price"], "\n")
    ordId = len(orders)  # order id is equal to the length of the list
    while True:  # Error handling
        try:
            pId = int(input("Enter product ID: "))  # product id
            if 0 <= pId < len(prod):  # product id has to be > 0 and < length of Product list
                break
        except:
            print("\nInvalid Input.\n")
    while True:  # Error handling
        try:
            qty = int(input("Enter Quantity: "))  # product quantity
            if 0 < qty:  # quantity has to be > 0
                break
        except:
            print("\nInvalid Input.\n")
    totalPrice = prod[pId]["Price"] * qty  # the total price is equal to the product price into the qty
    status = "Shipped"  # initial order status is set to Shipped the moment it is placed

    orders_dict = {  # dictionary for order details
        "order_id": ordId,
        "customer_id": cId,
        "product_id": pId,
        "product_quantity": qty,
        "order_status": status,
        "total_price": totalPrice
    }
    orders.append(orders_dict)  # appending the current order details to the end of the list
    print("\nOrder ID: {} || Customer ID: {} || Product ID: {} \n".format(orders[ordId]["order_id"],
                                                                          orders[ordId]["customer_id"],
                                                                          orders[ordId]["product_id"]), end="")
    print("\nProduct Quantity: {} || Order Status: {} || Total Price: {} \n".format(orders[ordId]["product_quantity"],
                                                                                    orders[ordId]["order_status"],
                                                                                    orders[ordId]["total_price"]),
          end="")


# Function for retrieving the total sales by product id
def salesByID(input, id):
    if not input.isdigit():
        print("\nInput can only be numbers. Please try again. \n")
        dashboard(True, id)
    else:
        input = int(input)
    productIds = {}  # Create an Empty Dictionary for found products
    for i in orders:  # Loops through each order
        if i['product_id'] in productIds:  # If the product of the current order is in product dictionary
            productIds[i['product_id']].append(
                i['order_id'])  # Adds order id to the values of the key matching the product id in product dictionary
        else:  # If product of the current order is not in product dictionary
            productIds[i['product_id']] = [i[
                                               'order_id']]  # Create a key of the current product, and initialise a list with the current order id as it's sole value
    if input in productIds:  # Checks if the entered product id exists in the product dictionary
        #numberSold = 0  # Initialise numberSold to 0
        print(f"Order ID: || Quantity Sold  || Total Price")
        grandtotal = 0; totalSales = 0
        for currentProd in productIds[input]:  # Loops through each order id associated with the entered product id
            numberSold = 0  # Initialise numberSold to 0
            totalPrice = 0  # Initialise totalPrice to 0

            for order in orders:  # Loops through each order
                if order["order_id"] == currentProd:  # If the order id of the current order matches the target order id
                    numberSold += order["product_quantity"]  # Increase numberSold by quantity in order
                    totalPrice += order["total_price"]  # Increase totalPrice by total price in order
                    totalSales+=order["product_quantity"]
                    grandtotal+=order["total_price"]
            print(str(currentProd) + " " * 15, end="")
            print(str(numberSold) + " " * 15, end="")
            print("£", totalPrice)
        print()
        print(f"Total amount sold  :{totalSales} || Net amount in sales made £{grandtotal} \n")

    else:  # If the entered input doesn't as a product id
        print("\nProduct doesn't exist!\n")  # Let user know the product doesn't exist
    dashboard(True, id)  # Return to Dashboard menu


# Function for retrieving the total sales by the category name
def salesByCategory(input, id):
    found = False
    if input.isdigit():
        print("\nInput can only be letters. Please try again. \n")
        dashboard(True, id)
    targetCat = False  # Flag to dictate if the entered category exists or not
    for i in categ:  # Loops through each category
        if input.lower() == i["Name"].lower():  # If entered category matches the name of the current category
            targetCat = i["catId"]  # Sets targetCat ID to the value of the matched category
            found = True
    if (targetCat > -1) and found:
        print(f"Category: {input} ||    Price  || Total Sales")
        aList = []  # List used to hold the names of products within target category
        bList = []  # List used to hold the product ids
        for order in orders:  # Loops through each order
            for products in prod:  # Loops through each product
                if products[
                    "CategoryId"] == targetCat:  # If the current products category id matches the target category id
                    if not products["Name"] in aList:  # If the current product name isn't in aList
                        aList.append(products["Name"])  # Adds current product name to aList
                        bList.append(products["pId"])  # Adds current product id to bList
        for i in range(len(aList)):  # Loops for the length of aList(bList will be the same size)
            total = 0  # Initialise total to hold the total price
            for y in orders:  # Loops through each order
                if bList[i] == y[
                    "product_id"]:  # If the product id in bList matches the product id of the current order
                    total += y["total_price"]  # Add to the total price from the product total price
            biggestnum = " " * (11 - len(input) + 1) if len(input) > len(aList[i]) else " " * (11 - len(aList[i]) + 1)
            print(aList[i] + biggestnum, end="\t\t")
            for y in prod:
                if y["Name"] == aList[i]:
                    print("£", y["Price"], end="\t\t")
                    print("£", total)
            print()
        if len(aList) == 0:
            print()
            print("Category has no sales of products. ")

        print()
    else:
        print("\nCategory doesn't exist!\n")
    dashboard(True, id)


# Function for retrieving the total sales by the price range
def salesByPriceRange(input, id):
    if not input.isdigit():
        print("\nInput can only be 1 or 2. Please try again. \n")
        dashboard(True, id)
    else:
        input = int(input)
    flags = [False, True]  # List told hold the bool values that determine how the function will show the order of data
    if not input in [1, 2]:  # Checks if the entered value is not in range
        print("\nInput can only be 1 or 2. Please try again. \n")
        dashboard(True, id)
    msg = "Descending" if flags[input - 1] else "Ascending"  # Changes message dependant on entered value
    print(f"Item Name({msg}):  ||    Sales:  ||")
    sales = {}  # Initialise an empty dictionary to hold product ids as a key and total money they have accumulated
    for i in orders:  # Loops through each order
        if i['product_id'] in sales:  # If the current order's product id is a key in sales dictionary
            sales[i['product_id']] += i['total_price']  # Increases the value of the found product id by price in order
        else:  # If the current order's product id is a key not in sales dictionary
            sales[i['product_id']] = i[
                'total_price']  # Adds a key of the current found product id as well as an initial value of the current order's total price
    x = []  # Creates a list for display purposes
    for i in sales.items():  # Loops through the dictionary of products in sales dictionary
        x.append([i[1], i[0]])  # Appends them to a list with price being the first item and name bring the second item
    x.sort(reverse=flags[input - 1])  # Sorts the list by it's first value(price) in the order selected
    for item in x:  # Loops through each product in the x list
        for i in prod:  # Loops through each product  of available products
            if item[1] == i["pId"]:  # If the current product's id matches target product's id
                print(i["Name"] + " " * (20 - len(i["Name"]) + 1), end="\t\t")
                print("£", item[0], end="")
                print()
    print()
    dashboard(True, id)


# Function for retrieving the total sales by location
def salesByLocation(id):
    print("Location:  ||   Sales:  ||")
    locations = {}  # Create an Empty Dictionary for found locations
    for i in range(len(customers)):  # Loop through each customer
        if customers[i]["Town"] in locations:  # If the Customer's Town is in locations dictionary
            locations[customers[i]["Town"]].append(
                i)  # Adds customer to the values of the key matching their town in locations dictionary
        else:  # If Customer's Town is not in locations dictionary
            locations[customers[i]["Town"]] = [
                i]  # Create a key of the Customer's Town, and initialise a list with the current customers as it's sole value

    for location in locations:  # Checks each location in locations list
        totalPrice = 0  # Initialise totalPrice to 0
        print(location + " " * (10 - len(location)), end="\t\t")  # Print the current location
        for customer in locations[location]:  # Loops through each customer in the current location
            for order in orders:  # Loops through each order
                if order["customer_id"] == customer:  # If the customer who made the order is the current customer
                    totalPrice += order["total_price"]  # Increase the total price by the price of the order
        print(f"£{totalPrice}", end="")
        print()
    print()
    dashboard(True, id)  # Returns to Dashboard Menu when finished


login(customers, admins, False)