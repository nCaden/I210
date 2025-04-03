#Valid Password
special_characters = ["?", "@", "#", "$", "%", "&", "*", "!"]

#Have valid password return true or false depending on whether it is valid or not
def valid_password(username, password, first_name, last_name):

    #will want to make every variable lower case
    password = password.lower()
    username = username.lower()
    first_name = first_name.lower()
    last_name = last_name.lower()

    #check if pass is too short
    while len(password) <= 8:
        print("Password needs to be at least 8 characters")
        password = input("Enter a password: ")
            
    #check if it starts/ends with name/username
    while password.startswith(first_name) or password.endswith(first_name):
        print("Password cannot contain your first name, last name, or username")
        password = input("Enter a password: ")
    while password.startswith(last_name) or password.endswith(last_name):
        print("Password cannot contain your first name, last name, or username")
        password = input("Enter a password: ")
    while password.startswith(username) or password.endswith(username):
        print("Password cannot contain your first name, last name, or username")
        password = input("Enter a password: ")
    #look through each character in password, check if there is a special character or number
    while not any(char in special_characters for char in password):
        print("password must contain a special character")
        password = input("Enter a password: ")

    return True
    

#Main
print("Welcome to Account Creator")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
username = input("Enter a username: ")

while True:
 
    print("Before entering password, please read our criteria:\n- Must have a length of 8\n- Can't start or end with first name, last name, or username\n- Must include at least one number\n- Must include a special character", special_characters)
    password = input("Enter a password: ")

    if valid_password(username, password, first_name, last_name):
        print("That password is valid")
        break