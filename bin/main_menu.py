import bin.Account as Account
import os

def main_menu():
    clear = lambda:os.system('cls' if os.name=='nt' else 'clear')
    clear()
    data = Account.fetch_user_data()[0]
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
    print(f"""

Welcome, {data[2]}
    1. View Account Details
    2. Withdraw
    3. Deposit
    4. Transfer
    5. View Transaction History
    9. Logout
    """)
    
    while True:
        usr_in = int(input('(Choose)> '))
        if usr_in == 1:
            Account.print_details()
        elif usr_in == 2:
            Account.withdraw()
        elif usr_in == 3:
            Account.deposit()
        elif usr_in == 4:
            Account.transfer()
        elif usr_in == 5:
            Account.tsn_history()
        elif usr_in == 9:
            from .login import menu
            clear()
            from .Account import clear_config_cache
            clear_config_cache()
            menu()
        else:
            print("Invalid Option, Please Choose From the List")
        
