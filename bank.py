class Bank:
    def __init__(self):
        self.bank_acct={}#{'username':'password'}
        self.bank_balance={}#{'username':5000}

    def create_acct(self,username,password):
        if username!='' and password!='':
            self.bank_acct[username]=password
            self.bank_balance[username]=5000
            return f"Hi {username}, your account has been created."
        else:
            return 'Please fill in the required fields'
    def check_balance(self,username,password):
        if password==self.bank_acct[username]:
            return f"Your current balance is {self.bank_balance[username]}"
        else:
            return"Incorrect credentials"
    def deposit_amount(self,username,password,amount):
        if password==self.bank_acct[username]:
            self.bank_balance[username]+=amount
            return f"Your balance after deposit is RM{self.bank_balance[username]}"
        else:
            return "Incorrect credentials above"

    def withdraw_amount(self,username,password,amount):
        if password==self.bank_acct[username]:#5000
            balance_after_withdraw = self.bank_balance[username]-amount#3000
            if balance_after_withdraw>0:
                self.bank_balance[username] -= amount

                return f"Your current balance after withdrawing is {self.bank_balance[username]}"
            else:
                return "Insufficient balance"
        else:
            return "Incorrect credentials"
    def transfer_amount(self,username,password,amount,transfer_to_name):
        if password == self.bank_acct[username]:  # 5000
            balance_after_transfer = self.bank_balance[username]-amount
            if balance_after_transfer>0:
                self.bank_balance[username] -= amount
                self.bank_balance[transfer_to_name] = self.bank_balance[transfer_to_name] + amount
                return "Transfer successful"
            else:
                return "Insufficient balance to transfer "
        else:
            return "Incorrect credentials"
