import Account
import os
from configparser import ConfigParser

def main_menu():
    clear = lambda:os.system('cls' if os.name=='nt' else 'clear')
    clear()
    data = Account.fetch_user_data()[0]
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
            from login import menu
            clear()
            config = ConfigParser()
            with open('config.ini','r+') as f:
                config.readfp(f)
                config.remove_section('AC_DETAILS')
                f.seek(0)
                config.write(f)
                f.truncate()
            menu()
        else:
            print("Invalid Option, Please Choose From the List")
        
