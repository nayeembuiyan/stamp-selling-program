import csv

users = {}


def login():
    student_id = 32659814
    key = student_id % 128
    with open('../../Desktop/Assessment 1/user_details.txt', 'r', encoding="utf-8") as file:  # Reading users.txt in encoded form
        user = file.readlines()
        for i in user:
            i = i.rstrip('\n')
            users[i.split(':')[0]] = int(i.split(':')[1])  # Retrieving user details

    while True:
        username = input("Enter your username: ")
        # Encoding the username
        cipher_username = ''
        for i in username:
            cipher_username += chr(ord(i) + key)
        if cipher_username in users:
            break
        else:
            print("User doesn't exist")

    while True:
        password = input("Enter your password")
        if int(password) == users[cipher_username]:
            print("Login successful!!!")
            break
        else:
            print("Incorrect password")


def register():
    student_id = 32659814
    key = student_id % 128
    with open('../../Desktop/Assessment 1/user_details.txt', 'r', encoding="utf-8") as file:
        user = file.readlines()
        for i in user:
            i = i.rstrip('\n')
            users[i.split(':')[0]] = int(i.split(':')[1])

    while True:
        username = input("Create a username: ")
        if username.isalpha() and len(username) == 8:
            # Encoding the username
            cipher_username = ''
            for i in username:
                cipher_username += chr(ord(i) + key)
            break
        else:
            print("Username should be 8 characters long and should only contain alphabetical characters")

    while True:
        password = input("Create your password: ")
        if password.isdigit() and len(password) == 4:
            users[cipher_username] = int(password)

            # Writing all the user details in encoded form
            with open('../../Desktop/Assessment 1/user_details.txt', 'w', encoding="utf-8") as f:
                for key, value in users.items():
                    f.write('%s:%s\n' % (key, value))
            print("Registration successful")
            login()
            break
        else:
            print("Password should only be 4 digits")
