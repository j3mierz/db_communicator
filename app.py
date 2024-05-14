from models import Users, Messages

# 1 - utwórz nowe kotno
#
#
#
#
#
#
#
#

command = "q"
while command == "q":
    print("""
        1 - create new account
        2 - change password 
        3 - remove account
        4 - show all users
        5 - write message 
        6 - show all messages
        q - return to main menu
    """)
    command = input("What do you want to do? ")
    while command == "1":
        username = input("Username: ")
        password = input("Password: ")
        main_object = Users(username, password)
        if len(main_object.load_user_by_username(username)) > 0:
            print("ERROR: this name is already taken")
            command = "q"
        if len(password) >= 8:
            main_object.new_user_to_db()
            command = "q"
            print("User created successfully")
        else:
            print("password must be at least 8 characters")
            command = "q"

    while command == "2":
        username = input("Username: ")
        password = input("Password: ")
        new_password = input("New password: ")
        main_object = Users(username, new_password)
        user = main_object.load_user_by_username(username)
        if len(user) > 0 and user[0][2] == password:
            command = "q"
            if len(new_password) >= 8:
                main_object.change_user(user[0][1], new_password)
                command = "q"
                print("password changed")
            else:
                print("password must be at least 8 characters")
                command = "q"
        else:
            print("wrong password")

    while command == "3":
        username = input("Username: ")
        password = input("Password: ")
        main_object = Users(username, password)
        current_user = main_object.load_user_by_username(username)
        if len(current_user) > 0 and current_user[0][2] == password:
            main_object.delete_user_by_id(current_user[0][0])
            print("user deleted")
            command = "q"
        else:
            print("password or username are incorrect")
    if command == "4":
        current_user = Users.load_all_users()
        for i in current_user:
            print("id: ", i[0], "username:", i[1])
        command = "q"

    while command == "5":
        message = ''
        username = input("Username: ")
        password = input("Password: ")
        recipient = input("to who?: ")
        main_object = Users(username, password)
        current_user = main_object.load_user_by_username(username)
        if len(current_user) > 0 and current_user[0][2] == password:
            recipient = Users.load_user_by_username(recipient)
            if len(recipient) == 1:
                message = input("Message: ")
                if len(message) >= 255:
                    print("Message too long")
                    command = "q"
                else:
                    Messages(current_user[0][0], recipient[0][0], str(message)).save_to_db()
                    print("Message sent")
                    command = "q"
            else:
                print("this user does not exist")
                command = "q"
        else:
            print("password or username are incorrect")
            command = "q"

    if command == "6":
        username = input("Username: ")
        password = input("Password: ")
        current_user = Users.load_user_by_username(username)
        if len(current_user) > 0 and current_user[0][2] == password:
            messages = Messages.load_all_messages(current_user[0][0])
            for i in messages:
                print(f"message from {Users.load_user_by_id(i[1])[0][1]}: ", i[4])
        else:
            print("password or username are incorrect")
        command = "q"