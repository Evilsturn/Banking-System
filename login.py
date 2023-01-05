from Authenticate import user_login,register_user
from user import NewUser
from main_menu import main_menu
from configparser import ConfigParser
import os

def menu():
    clear = lambda:os.system('cls' if os.name=='nt' else 'clear')
    
    print("""
$$\    $$\                                                                   $$$$$$$\                      $$\       
$$ |   $$ |                                                                  $$  __$$\                     $$ |      
$$ |   $$ | $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\ 
\$$\  $$  |$$  __$$\ $$ |  $$ | \____$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |
 \$$\$$  / $$ /  $$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|      $$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  / 
  \$$$  /  $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<  
   \$  /   \$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |            $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\ 
    \_/     \______/  \____$$ | \_______| \____$$ | \_______|\__|            \_______/  \_______|\__|  \__|\__|  \__|
                     $$\   $$ |          $$\   $$ |                                                                  
                     \$$$$$$  |          \$$$$$$  |                                                                  
                      \______/            \______/                                                                                                                    
    """)

    print("""
    1. Login to Bank Account
    2. Register Bank Account
    3. Quit
    """)
    while True:
        try:
            usr_in = int(input("> "))
            if usr_in == 1:
                clear()
                usr_name = input("Username: ")
                psswd = input("Password: ")
                if user_login(usr_name,psswd):
                    config = ConfigParser()
                    config["AC_DETAILS"]= {"u_n": usr_name}
                    with open('config.ini',"a") as f:
                        config.write(f)
                    main_menu()
            elif usr_in == 2:
                clear()
                user = NewUser()
                register_user(user)
                menu()
            elif usr_in == 3:
                exit(0)
            else:
                print("Invalid Option, Please Choose From The List")

        except TypeError:
            print("Type only the integer associated with the action.")

