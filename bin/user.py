import uuid
class NewUser():
    def __init__(self):
        self.f_name = input("First Name: ")
        self.l_name = input("Last Name: ")
        self.email = input("Email Address: ")
        self.phone = input("Phone: ")
        self.usr_name = input("Username[For Login]: ")
        self.passwd = input("Password[For Login]: ")
        self.acc_no = int(str(uuid.uuid4().int)[:15])
