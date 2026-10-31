class Account:
    def __init__(self,owner,pin):
        self.owner=owner
        self.pin=pin
    def show_pin_status(self):
        print("Account owner:",self.owner)
        print("PIN is safely stored inside the class.")
    def set_pin(self,new_pin):
        if len(new_pin)==4 and new_pin.isdigit():
            self.pin=new_pin
            print("PIN updated sucsessfully.")
        else:
            print("Invalid PIN.")
    def check_pin(self,entered_pin):
        if entered_pin==self.pin:
            print("Acsess granted.")
        else:
            print("Acsess denied.")
    def __str__(self):
        return "Account holder:"+self.owner
my_account=Account("Riya","1234")
print(my_account)
my_account.show_pin_status()
my_account.pin="9999"
print("Tried changing PIN  from the outside")
my_account.check_pin("9999")
my_account.check_pin("1234")
my_account.set_pin("9999")
my_account.check_pin("9999")