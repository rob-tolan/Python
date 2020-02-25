# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:24:38 2020

@author: Owner
"""
#consumer credit card
class CreditCard:
    def__init_(self,customer,bank,acnt,limit):
        The initial balance is zero.
    custoner's name.
    name of bank.
    acnt indentifier
    limit credit limit

self. .customer = customer
self. _bank = bank
self. .account = acnt
self. _1 imit = limit
self. _balance = 0

def get.customer(self):
#returh customer's name
return self.bank
def get.account(self):
#return card number
return self.account

def get limit(self):
#return current credit limit
return self.limit
def get.balance(self):
def charge(self, price):
    .charge given price to card, assuming sufficient credit.
return True if charge processed; False if denied.
if price + self._balance > self..limit:
    return False
else:
    self._balance += price
return True
def make_payment(self, amount):
#process customer payment that reduces balance.
self._balance-= amount