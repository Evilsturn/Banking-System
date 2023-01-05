from configparser import ConfigParser
from connection import do_connection
from datetime import datetime
import os


connec = do_connection()
cursor = connec.cursor()
clear = lambda:os.system('cls' if os.name=='nt' else 'clear')

def fetch_user_data():
    config = ConfigParser()
    config.read('ac.ini')
    cfg = config['AC_DETAILS']
    cursor.execute(f"SELECT * FROM USERS WHERE User_Name = '{cfg['u_n']}'")
    data = cursor.fetchall()
    return data


def get_balance(ac_no):
    cursor.execute(f"SELECT balance FROM BALANCE WHERE Account_no = {ac_no}")
    data = cursor.fetchone()
    return data[0]

def print_details():
    clear()
    print("------------------")
    print("ACCOUNT DETAILS :-")
    print("------------------")
    data = fetch_user_data()
    bal = get_balance(data[0][6])

    print(f'BALANCE :- {bal}')
    print(f"ACCOUNT HOLDER :- {data[0][2]} {data[0][3]}")
    print(f"ACCOUNT NO :- {data[0][6]}")
    print(f"Registered Email :- {data[0][4]}")
    print(f"Registered Phone :- {data[0][5]}")

    print("0) Back")
    print("1) Quit")
    
    while True:
        usr_in = int(input("> "))
        if usr_in == 0:
            from main_menu import main_menu
            clear()
            main_menu()
            break

        elif usr_in == 1:
            exit(0)
        else:
            print("Invalid Option")

def deposit():
    clear()
    data = fetch_user_data()
    amt = int(input("Deposit Amount: "))
    cursor.execute(f"UPDATE BALANCE SET Balance=Balance+{amt} WHERE ACCOUNT_NO={data[0][6]}")
    now = datetime.now()
    id = gen_tsn_id()
    cursor.execute(f"INSERT INTO TRANSACTIONS VALUES({data[0][6]},'{id}','+{amt}','{now}')")
    bal = get_balance(data[0][6])
    print("Amount Deposited Successfully")
    print(f"BALANCE :- {bal}")
    connec.commit()

    print("0) Back")
    print("1) Quit")
    
    while True:
        usr_in = int(input("> "))
        if usr_in == 0:
            from main_menu import main_menu
            clear()
            main_menu()
            break

        elif usr_in == 1:
            exit(0)
        else:
            print("Invalid Option")


def withdraw():
    clear()
    data = fetch_user_data()
    amt = int(input("Withdrawl Amount: "))
    bal = get_balance(data[0][6])
    if bal > 0 and (bal-amt) > 0:
        cursor.execute(f"UPDATE BALANCE SET Balance=Balance-{amt} WHERE ACCOUNT_NO={data[0][6]}")
        now = datetime.now()
        id = gen_tsn_id()
        cursor.execute(f"INSERT INTO TRANSACTIONS VALUES({data[0][6]},'{id}','-{amt}','{now}')")
        print("Withdrawl Successful")
        print(f"AVAILABLE BALANCE:- {get_balance(data[0][6])}")
        connec.commit()
    else:
        print("Insufficient Balance")
        print(f"AVAILABLE BALANCE:- {get_balance(data[0][6])}")
        
    print("0) Back")
    print("1) Quit")
    
    while True:
        usr_in = int(input("> "))
        if usr_in == 0:
            from main_menu import main_menu
            clear()
            main_menu()
            break

        elif usr_in == 1:
            exit(0)
        else:
            print("Invalid Option")

def transfer():
    clear()
    data = fetch_user_data()
    acc_no = int(input('Transfer to Account No:- '))
    cursor.execute(f"SELECT * FROM BALANCE WHERE Account_No={acc_no}")
    search = cursor.fetchall()
    if acc_no == data[0][6] or search == [] :
            print("Invalid Account No")
            clear()
            transfer()
    amt = int(input("Transfer Amount: "))
    bal = get_balance(data[0][6])
    if amt > bal:
        print("Insufficient Balance")
        clear()
        transfer()
    else:
        cursor.execute(f"UPDATE BALANCE SET Balance=Balance-{amt} WHERE ACCOUNT_NO={data[0][6]}")
        cursor.execute(f"UPDATE BALANCE SET Balance=Balance+{amt} WHERE ACCOUNT_NO={acc_no}")
        now = datetime.now()
        id = gen_tsn_id()
        cursor.execute(f"INSERT INTO TRANSACTIONS VALUES({data[0][6]},'{id}','-{amt}','{now}')")
        cursor.execute(f"INSERT INTO TRANSACTIONS VALUES({acc_no},'{id}','+{amt}','{now}')")
        print("Transferred Successfully")
        connec.commit()
    
    print("0) Back")
    print("1) Quit")
    
    while True:
        usr_in = int(input("> "))
        if usr_in == 0:
            from main_menu import main_menu
            clear()
            main_menu()
            break

        elif usr_in == 1:
            exit(0)
        else:
            print("Invalid Option")
    
def tsn_history():
    data = fetch_user_data()
    cursor.execute(f"SELECT * FROM TRANSACTIONS WHERE Account_No={data[0][6]} ORDER BY Date_Time DESC")
    tsn_data = cursor.fetchall()
    clear()
    print("--------------------")
    print("TRANSACTION HISTORY")
    print("--------------------")
    for item in tsn_data:
        print(f"Acc-No: {item[0]}  Tsn-id: {item[1]}  Amount: {item[2]}  Date-Time: {str(item[3])}")
    
    print("0) Back")
    print("1) Quit")
    
    while True:
        usr_in = int(input("> "))
        if usr_in == 0:
            from main_menu import main_menu
            clear()
            main_menu()
            break

        elif usr_in == 1:
            exit(0)
        else:
            print("Invalid Option")

def gen_tsn_id():
    import uuid
    return str(uuid.uuid4())