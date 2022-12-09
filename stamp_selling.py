from user import register, login
from add import item_list
from view import view
from amend import amend
from remove import remove
from checkout import checkout

""" 
References

Python Software Foundation 2021, Documentation - The Python Tutorial (Compound Statements), viewed 22 July 2021
https://docs.python.org/3/reference/compound_stmts.html#while 

Python Software Foundation 2021, Documentation - The Python Standard Library (CSV File Reading and Writing), 
viewed 22 July 2021, https://docs.python.org/3/library/csv.html 

Python Software Foundation 2021, Documentation - The Python Tutorial (Data Structures), viewed 22 July 2021
https://docs.python.org/3/tutorial/datastructures.html

Python Software Foundation 2021, Documentation - The Python Tutorial (Datetime), viewed 24 July 2021
https://docs.python.org/3/library/datetime.html

Python Software Foundation 2021, Documentation - The Python Tutorial (More Control Flow Tools), viewed 22 July 2021
https://docs.python.org/3/tutorial/controlflow.html 

Python Software Foundation 2021, Documentation - The Python Standard Library (String Operations), viewed 22 July 2021, 
https://docs.python.org/3/library/string.html 

user7480449, dheiberg (2018), 'Python login through text file' showed how to create a login system using a txt file
https://stackoverflow.com/questions/51710341/python-login-through-text-file

"""


def menu():
    order = {}
    while True:
        print("To exit press E")
        print("To add item in your cart press A")
        print("To view shopping cart press V")
        print("To amend an item in the cart press M")
        print("To remove any item from the cart press R")
        print("To checkout press C")

        select = input("Enter your choice: ")
        if select.lower() == 'e':
            break
        if select.lower() == 'a':
            order = item_list()  # Calling function to add items
        if select.lower() == 'v':
            view(order)  # Calling function to view items
        if select.lower() == 'm':
            amend(order)  # Calling function to amend items
        if select.lower() == 'r':
            remove(order)  # Calling function to remove items
        if select.lower() == 'c':
            checkout(order)  # Calling function to checkout


def welcome():
    print("New user - press 1 for registration")
    print("Existing user - press 2 for login")
    print("Press 3 for exit")

    select = input("Enter your choice: ")

    if select == '1':
        register()  # Calling function to register
    elif select == '2':
        login()  # Calling function to login
        menu()  # Calling menu function
    elif select == '3':
        exit()
    else:
        print("Invalid choice")


welcome()
