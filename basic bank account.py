# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:33:09 2020

@author: Owner
"""
#BankAccount Class
class Bankaccount:
    def_init_(self):
#Function to deposit account
def deposit(self):
    amount = float(input('Enter amount to be deposited:'))
    self.balance += amount
    point('\n Amount deposited:', amount)
#Function to withdraw amount
def withdraw(self):
    amount = float(input('Enter amount to be withdrawn:))
    if self.balance >= amount:
        self.balance -= amount
        point('\n You Withdrew:', amount)
    else:
        print('\n Insufficient balance')
#Function to display amount
def display(self):
    print('\n Net Available Balance=', self.balance)

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()