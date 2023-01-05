from .connection import do_connection

connec = do_connection()
cursor = connec.cursor()
def user_login(usr_name, psswd):
        cursor.execute(f"SELECT Password FROM USERS WHERE User_name='{usr_name}'")
        data = cursor.fetchone()
        if str(data[0]) == psswd:
            return True
            
def register_user(user):
    cursor.execute(f"INSERT INTO USERS VALUES('{user.usr_name}','{user.passwd}','{user.f_name}','{user.l_name}','{user.email}','{user.phone}',{user.acc_no})")
    cursor.execute(f"INSERT INTO BALANCE VALUES({user.acc_no},0)")
    connec.commit()
