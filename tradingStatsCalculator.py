
#This script calculates certain statistics of the statemen of a trading account on mt4

import pandas as pd
import numpy as np
import matplotlib as plt
import re

def GJ():
    
    stats = pd.read_excel(r"GJ.Stats.1.xlsx", sheet_name = 'GJStats', engine = 'openpyxl')

    index = stats.index
    numberOfTrades = len(index)

    #Full Profit
    
    FullProfit1 = stats[stats['Close Price'] == stats['TP']]
    FullProfit = FullProfit1['TP']
    index1 = FullProfit.index
    FullProfit = len(index1)/numberOfTrades*100
    
    #We can add a condition to filter by 'scratched trades'
    
    #Full Loss
        
    FullLossBuys1 = stats[(stats['Close Price'] == stats['SL']) & (stats['SL'] < stats['Entry Price'])]
    FullLossBuys = FullLossBuys1['SL']
    index2 = FullLossBuys.index
    FullLossBuys = len(index2)/numberOfTrades*100
    
    FullLossSells1 = stats[(stats['Close Price'] == stats['SL']) & (stats['SL'] > stats['Entry Price'])]
    FullLossSells = FullLossSells1['SL']
    index3 = FullLossSells.index
    FullLossSells = len(index3)/numberOfTrades*100
    
    FullLoss = FullLossBuys + FullLossSells

    #BreakEven
    
    BreakEven1 = stats[(stats['Close Price'] - stats['Entry Price']).between(-0.010,0.010)]
    BreakEven = BreakEven1['Close Price']
    index4 = BreakEven.index
    BreakEven = len(index4)/numberOfTrades*100
    
    #For buys
    
    Buys = stats[stats['Type'].fillna(0).str.contains("buy",na=False)] 
    BuysFilter = Buys['Type']
    index5 = BuysFilter.index
    BuysFilter = len(index5)/numberOfTrades*100
    
        #Buys Partial winws
    
    BuysPartialWins1 = Buys[(Buys['Close Price'] > Buys['Entry Price']) & (Buys['Close Price'] < Buys['TP'])]
    index6 = BuysPartialWins1.index
    BuysPartialWins = len(index6)/numberOfTrades*100    
    
        #Buys Partial loss 
    
    BuysPartialLoss1 = Buys[(Buys['Close Price'] < Buys['Entry Price']) & (Buys['Close Price'] > Buys['SL'])]   
    index7 = BuysPartialLoss1.index
    BuysPartialLoss = len(index7)/numberOfTrades*100   
    
    #For sells
    Sells = stats[stats['Type'].fillna(0).str.contains("sell",na=False)] 
    SellsFilter = Sells['Type']
    index8 = SellsFilter.index
    SellsFilter = len(index8)/numberOfTrades*100
    
        #Sells Partial winws
        
    SellsPartialWins1 = Sells[(Sells['Close Price'] < Sells['Entry Price']) & (Sells['Close Price'] > Sells['TP'])]
    index9 = SellsPartialWins1.index
    SellsPartialWins = len(index9)/numberOfTrades*100    
    
        #Sells Partial loss
    
    SellsPartialLoss1 = Sells[(Sells['Close Price'] > Sells['Entry Price']) & (Sells['Close Price'] < Sells['SL'])]
    index10 = SellsPartialLoss1.index
    SellsPartialLoss = len(index10)/numberOfTrades*100 
    
    #Stats
        #Win Rate
            #Ratio of positive trades divided by total number trades.
    WinRate = FullProfit + BreakEven + BuysPartialWins + SellsPartialWins
    
        #Loss Rate
            #Ratio of negative trades divided by total number trades.
    LossRate = FullLossBuys + FullLossSells + BuysPartialLoss + SellsPartialLoss
    
        #Average loss
            #Average loss of negative trades.
        
        
    #Merge all 'negative' df onto one

    LossesDfs = [FullLossBuys1, FullLossSells1, BuysPartialLoss1, SellsPartialLoss1]

    LossesDfConcat = pd.concat(LossesDfs)

    #for each row, calculate the absolute value between the open and close price. Then, calculate the mean.

    LossesDfConcat['Price difference Loss'] = LossesDfConcat['Entry Price'] - LossesDfConcat['Close Price']

    LossesDfConcat['Price difference Loss Abs'] = LossesDfConcat['Price difference Loss'].abs()

    AverageLosses = LossesDfConcat['Price difference Loss Abs'].mean()

    #allocate the for loop onto a variable and calculate the mean. 

    
        #     Average Profit
        #     Average profit of positive trades.
    
        
    #Merge all 'negative' df onto one

    WinsDfs = [FullProfit1, BreakEven1, BuysPartialWins1, SellsPartialWins1]

    WinsDfConcat = pd.concat(WinsDfs)

    #for each row, calculate the absolute value between the open and close price. Then, calculate the mean.

    WinsDfConcat['Price difference Win'] = WinsDfConcat['Entry Price'] - WinsDfConcat['Close Price']

    WinsDfConcat['Price difference Win Abs'] = WinsDfConcat['Price difference Win'].abs()

    AverageWins = WinsDfConcat['Price difference Win Abs'].mean()

        
    #     Average RRR
    #         Ratio between the average profit and average loss
    
    RRR = AverageWins/AverageLosses
    
        #Gross loss
        
            #Total $$ losses
        
        #Gross Profit
        
            #Total $$ Wins
        

    #     Profit factor
    #         Ratio of gross profit dividied by gross losses. If the profit factor is above 1, the trading system indicates
    #         profitability. The higher the Profit factor, the better.
    

    #     Expectancy
    #         Expectancy projects the hypothetical value of any future single trade, based on the ratio of your account win
    #         win ratio, loss ratio and RRR.
    
        #Gross Profit - Gross loss /Number of trades

        
    print(RRR)
GJ()
