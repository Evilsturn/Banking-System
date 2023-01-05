# Creates all the Tables if it does not exists
def inital_setup(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS BANK;")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS USERS(
            User_Name varchar(20),
            Password varchar(20),
            First_Name varchar(30),
            Last_Name varchar(30),
            Email varchar(50),
            Phone varchar(10), 
            Account_no Bigint
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS BALANCE(
            Account_no Bigint Primary Key,
            Balance Bigint
        ) """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS TRANSACTIONS(
            Account_no Bigint, 
            Transaction_id varchar(50),
            amount varchar(50),
            Date_Time DATETIME)
        """)


if __name__ == "__main__":
    from configparser import ConfigParser
    import os


    print(r"""
    ---------------------------------------------------------------------------------------------------------
    $$\      $$\                 $$$$$$\  $$$$$$\ $$\             $$\      $$$$$$\  $$$$$$\ $$$$$$\$$\   $$\ 
    $$$\    $$$ |               $$  __$$\$$  __$$\$$ |            $$ |    $$  __$$\$$  __$$\\_$$  _$$$\  $$ |
    $$$$\  $$$$ $$\   $$\       $$ /  \__$$ /  $$ $$ |            $$ |    $$ /  $$ $$ /  \__| $$ | $$$$\ $$ |
    $$\$$\$$ $$ $$ |  $$ |      \$$$$$$\ $$ |  $$ $$ |            $$ |    $$ |  $$ $$ |$$$$\  $$ | $$ $$\$$ |
    $$ \$$$  $$ $$ |  $$ |       \____$$\$$ |  $$ $$ |            $$ |    $$ |  $$ $$ |\_$$ | $$ | $$ \$$$$ |
    $$ |\$  /$$ $$ |  $$ |      $$\   $$ $$ $$\$$ $$ |            $$ |    $$ |  $$ $$ |  $$ | $$ | $$ |\$$$ |
    $$ | \_/ $$ \$$$$$$$ |      \$$$$$$  \$$$$$$ /$$$$$$$$\       $$$$$$$$\$$$$$$  \$$$$$$  $$$$$$\$$ | \$$ |
    \__|     \__|\____$$ |       \______/ \___$$$\\________|      \________\______/ \______/\______\__|  \__|
                $$\   $$ |                    \___|                                                          
                \$$$$$$  |                                                                                   
                \______/       
    ---------------------------------------------------------------------------------------------------------                                                                                                                                                                                                                                      
    """)  
    while True:
        usr_name = input("Username: ")
        psswd = input("Password: ") 

        # Stores the user session info into a config file
        config = ConfigParser()
        config["SESSION"]= {
            "user" : usr_name,
            'psswd': psswd,
            'db': 'bank'
        }

        with open('config.ini','w') as f:
            config.write(f)

        # Checks for MySQL connection & creates a Database
        from connection import do_connection
        from login import menu
        connec = do_connection()
        cursor = connec.cursor()
        if connec.is_connected():
            print('Connection Established')
            inital_setup(cursor)
            os.system('cls' if os.name=='nt' else 'clear')
            menu()
        else:
            print("Invalid Credentials")
