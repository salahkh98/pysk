print("welcom to Database emulator app")

database = {
    "admin":"112",
    "salah":"123",
    "noor":"321",
    "zain":"99",
    "amerbg":"123321"
}

username = database.keys()
password = database.values()


login_username = input("username: ")
while login_username not in username:
    print("this username not in database.")
    login_username = input("username: ")
    

login_pass = input("password: ")
while login_pass != database[login_username]:
    print("wrong password try again")
    login_pass = input("password: ")

if login_username and login_pass == database["admin"]:
    print(database)


login = True

while login is True:

    
    print("\tWelcom " + str(login_username) + " to your account")

    print(" ----------------------------------------")
    print("|  1- choose (1) to change your password  |")
    print("|  2- chosse (2) to change your username  |")
    print(" ----------------------------------------")


    choices = input("choose (1) , (2) : ")

    if choices == "1":
        password_change = str(input("your current password ("+login_pass+")\nnew password: "))
        database[login_username] = password_change
        print("your old password is",str(login_pass) ,"the new one is",password_change)
        new_log = input("would you like to login with new password (yse/no): ")
        
        if new_log == "yes":
            login_username = input("username: ")
            while login_username not in username:
                print("this username not in database. ")
                login_username = input("username: ")
                

            login_pass = input("password: ")
            while login_pass not in database[login_username]:
                print("wrong password try again")
                login_pass = input("password: ")

        elif new_log == "no":
            print("Goodbye",str(login_username))
            break


    elif choices == "2":
        username_change = str(input("your username is "+str(login_username)+"\nwhat is the new username: "))
        database[username_change] = database.pop(login_username)
        print("your old username is",login_username,"new one is",username_change)

        new_log = input("would you like login with new username (yse/no) ")
        
        if new_log == "yes":
            login_username = input("username: ")
            while login_username not in username:
                print("this username not in database.")
                login_username = input("username: ")
                

            login_pass = input("password: ")
            while login_pass not in database[login_username]:
                print("wrong password try again")
                login_pass = input("password: ")

        elif new_log == "no":
            print("Goodbye",str(login_username))
            break