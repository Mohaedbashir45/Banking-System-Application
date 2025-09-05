import sqlite3
import random as r

class Bank:
    print("WELCOME TO THE BANK")

    def __init__(self):
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()

    def CreateAccount(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS Bank (
                          account_name TEXT,
                          acc_num INTEGER,
                          balance INTEGER                                             
                      )""")
        
        n1 = input("Enter Your First Name: ").upper()
        n2 = input("Enter Your Second Name: ").upper()
        
        if n1.isalpha() and n2.isalpha():
            name = n1 + " " + n2
            num = r.randint(10000, 99999) 
            amount = 0
            self.c.execute("INSERT INTO Bank VALUES (?,?,?)", (name, num, amount))
            print("Your {} Account got created successfully...!".format(name))
            print("Please note down your account number: {}".format(num))
            self.con.commit()
        else:
            print("Enter valid name. Try again...!")

    def OpenAccount(self): 
        a_num = int(input("Enter your account number: "))
        check = True
        flag = False
        for a, b, c in self.c.execute("SELECT * FROM Bank"):
            if b == a_num:
                check = False
                flag = True
                val = c
                na = a

                print("(d)- Deposit")
                print("(w)- Withdraw")
                print("(c)- Check Balance")
                ope = input("Enter any of the operation (c)/(d)/(w): ")

                if flag and (ope == 'd' or ope == 'D'):
                    dep = int(input("Enter the amount to deposit: "))
                    deposit = dep + val
                    self.c.execute("UPDATE Bank SET balance = ? WHERE acc_num = ?", (deposit, a_num))
                    self.con.commit()
                    print("Amount Deposited {}$. Available balance is {}$".format(dep, deposit))

                elif flag and (ope == 'w' or ope == 'W'):
                    wit = int(input("Enter the Amount to withdraw: "))
                    if val >= wit:
                        withdraw_bal = val - wit
                        self.c.execute("UPDATE Bank SET balance = ? WHERE acc_num = ?", (withdraw_bal, a_num))
                        self.con.commit()
                        print("Withdraw {}$, done successfully. Available balance {}$".format(wit, withdraw_bal))
                    else:
                        print("Low Balance.")

                elif flag and (ope == 'c' or ope == 'C'):
                    print("Hello {}, Your Account balance is {}$".format(na, val))

        if check:
            print("Invalid Account Number...")

bank = Bank()

print("(c)- Create account")
print("(o)- Open Account")
op = input("Enter your choice (c)/(o): ")

if op.lower() == 'c':
    bank.CreateAccount()
elif op.lower() == 'o':
    bank.OpenAccount()
else:
    print("Invalid choice. Please select 'c' or 'o'.")

