# -*- coding: utf-8 -*-
#####################################################
#   Here we are simulating an investment portfolio  #
#####################################################

class Portfolio:
#Create a class called Portfolio
    def __init__(self, cash_value = 0, stock_value = 0, mf_value = 0):
       self.cash_value = int(cash_value)
       self.stock_value = stock_value
       self.mf_value = mf_value
       self.accounts = [] #list for child object
       
#this allows me to add cash to my account
    def addCash(self, amount):
        self.cash_value += amount
        print("Your balance is now %d " + self.cash_value())

#this allows me to add cash to my account
    def withdrawCash(self, amount):
        self.cash_value -= int(amount)
        print("Your balance is now %d " + self.cash_value())       

#define the method buyStock
    def buyStock(shares, name):
        stock_purchase = s.sale_price * int(shares)
        if stock_purchase <= portfolio.cash_value:
            portfolio.withdrawCash(stock_purchase)
        elif stock_purchase > portfolio.cash_value:
            print("You don't have enough funds to make this purchase!")
       
#define the method sellStock        
    def sellStock(ticker, shares):
        stock_profit = s.sale_price * s.shares
        portfolio.cash_value = portfolio.cash_value + stock_profit
        print("Your balance is now %d " + portfolio.cash_value())
        
#define method to buy MutualFunds
    def buyMutualFund(shares, name):
        mf_purchase = shares
        if mf_purchase <= portfolio.cash_value:
            portfolio.withdrawCash(mf_purchase)
        elif mf_purchase > portfolio.cash_value:
            print("You don't have enough funds to make this purchase!")
       
#define method to sell MutualFunds        
    def sellMutualFund(ticker, shares):
        mf_profit = mf.sale_price * mf.shares
        portfolio.cash_value = portfolio.cash_value + mf_profit
        print("Your balance is now %d " + portfolio.cash_value())        

#####################################################
#          Now I'll define the subclass Cash        #
#####################################################

class Cash(Portfolio):
    pass
        
#####################################################
#        Now I'll define the subclass Stock         #
#####################################################
class Stock(Portfolio):
#Stock is subclass of portfolio that has two attributes: price and ticker symbol
#I define those here:
    def __init__(self, price = abs(int()), ticker = str()):
        self.price = price
        self.ticker = ticker
#create new stock
s = Stock()

#define sale price using random module
import random
Stock.sale_price = int(random.uniform(0.5 * s.price, 1.5 * s.price))

#####################################################
#       Now I'll define the subclass MutualFund     #
#####################################################            

class MutualFund(Portfolio):
    #Can be purchased or sold
    #purchased as fractions
    #this initiatizes the attribute of MF: ticker symbol
    def __init__(self,  ticker = str()):
        self.ticker = ticker 
        
#create new MutualFund
mf = MutualFund()    

#define sale price using random module
import random
MutualFund.sale_price = random.uniform(0.9, 1.2)
    
#####################################################
#     Let's see if this portfolio project works     #
#####################################################   
        
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
print(s.sale_price)
print(mf.sale_price)
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio: cash amount, stock value, mf value
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions
#ordered by time