#!/usr/bin/env python
import random

unit = 5

def payoutHardWays():
    """resolve HardWays bets"""
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



