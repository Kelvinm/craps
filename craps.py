#!/usr/bin/env python
import random

unit = 5

class Bets(object):
    """docstring for Bet"""
    self.betList = []
    self.roll = None
    self.isHardWays = False
    self.isCraps = False
    self.Point = None
    self.ComeOut = True
    self.balance = 0
    
    def __init__(self, Point):
        self.Point = Point
    
    def add(self, betType, unit = 1):
        """function to add bets"""
        if betType.upper() not in ('PLACE', 'HARDWAY', 'TAKEODDS', 'LAYODDS', 'ANYSEVEN', 'ANYCRAPS', "DON'T", 'PASS', '2', '3', '11', '12', 'FIELD'):
            return 'Not a valid bet type.'
        else:
            self.betList.append({betType:unit})
        
    def resolveRoll(self, die1, die2):
        """docstring for resolveRoll"""
        
        self.roll = die1 + die2
        if die1 == die2:
            self.isHardWays = True
        
        balance = 0
        
        if self.ComeOut:
            if self.roll in (2, 3):
                for betType, unit in self.betList().items():
                    if betType == "DONT'T":
                        balance += unit * 2
                        return

            if self.roll in (7, 11)
                for betType, unit in self.betList().items():
                    if betType == 'PASS':
                        balance += unit * 2
                        return
                        
            if self.roll == 12:
                for betType, unit in self.betList().items():
                    if betType == "DON'T":
                        balance += unit
                        return
        else:
            if self.roll in (2, 3, 11, 12):
                for betType, unit in self.betList().items():
                    if betType in ('2', '3', '11', '12'):
                        balance += self.payProp(unit)
                
                    if betType == 'FIELD':
                        balance += self.payField(unit)
            elif self.roll in (4, 9 , 10):
                for betType, unit in self.betList().items():
                    if betType == 'PLACE':
                        balance += self.payPlace(unit)
                
                    if betType == 'PASS' and self.Point in (4, 9 , 10):
                        balance += self.payPass(unit)

                    if betType == 'FIELD':
                        balance += self.payField(unit)
                
                    if betType == 'HARDWAY' and die1 == die2:
                        balance += self.payHardWays(unit)
                
            elif self.roll in (5, 6, 8):
                for betType, unit in self.betList().items():
                    if betType == 'PLACE':
                        balance += self.payPlace(unit)
                
                    if betType == 'PASS' and self.Point in (5, 6 , 8):
                        balance += self.payPass(unit)
                
                    if betType == 'HARDWAY' and die1 == die2:
                        balance += self.payHardWays(unit)
            
            elif self.roll == 7:
                for betType, unit in self.betList().items():
                    if betType == 'PLACE':
                        balance += self.payPlace(unit)
                
                    if betType == 'PASS' and self.Point in (5, 6 , 8):
                        balance += self.payPass(unit)
                
                    if betType == 'HARDWAY' and die1 == die2:
                        balance += self.payHardWays(unit)
         
        
    def payProp(self, unit):
        """docstring for payProp"""
        if self.roll in (2, 12):
            balance = unit * 30
        elif self.roll in (3, 11):
            balance = unit * 15
        
        return balance
            
        
    def payHardWays(roll = None, units = 1):
        """resolve HardWays bets"""
        if roll in (6, 8)
            payout = units * 9
        elif roll in (4, 10):
            payout = units * 7
        return payout
    

    def payTakeOdds(roll = None, units = 1):
        '''resolve the odds bets'''
            if roll in (6, 8):
                payout = units * (6/5)
            elif roll in (5,9):
                payout = units * (3/2)
            elif roll in (4,10):
                payout = units * 2
    
        return payout

    def payoutLayOdds():
        """docstring for payoutLayOdds"""
        pass
    
    def payField(self):
        """docstring for payField"""
        pass
    
    def LayOdds(self):
        """docstring for LayOdds"""
        pass
        
def game():
    """throw simulator"""
    
    #place to apply betting strategies (inside, outside, do, dont, etc)
    
    while True:
    #throw
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
    
        roll = die1 + die2
    
        if comeout:
            balance += 25
        else:
            #resolve throw
            if die1 + die2 == 7:
                takeDo()
                payDont()
                break
            if die1 == die2:
                balance += payoutHardWays()
    
    return balance
        
def craps():
    """craps simulator"""

    bankRoll = 1000
    
    while bankRoll > 0:
        #number of units
        
        bankRoll += game()

    
if __name__ == '__main__':
    #assumption units of 10
     
    craps()



