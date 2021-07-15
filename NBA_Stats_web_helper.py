import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
stats_description={"PTS" : "The amount of points per game a player scores. Points can be acquired by scoring field goals (2 or 3 points) and free throws (1 point).",
                  "AST" : "The amount of passes a player makes that leads directly to a score.",
                  "TRB" : "The amount of times a player gains possession of the ball after a missed field goal or free throw.",
                  "FG%" : "The number of made shots over the number of shot attempts.",
                  "eFG%" : "Modifies FG% to account for the fact that 3-point field goals are worth 1.5 times 2-point field goals.",
                  "FT%" : "The number of made free throws over the number of free throw attempts.",
                  "2P%" : "The number of made two point shots over the number of two point shot attempts.",
                  "3P%" : "The number of made two point shots over the number of three point shot attempts."
                  }

stats_expansion={"PTS" : "POINTS PER GAME",
                 "AST" : "ASSISTS PER GAME",
                 "TRB" : "TOTAL REBOUNDS",
                 "FG%" : "FIELD GOAL PERCENTAGE",
                 "eFG%" : "EFFECTIVE FIELD GOAL PERCENTAGE",
                 "FT%" : "FREE THROW PERCENTAGE",
                 "2P%" : "TWO POINT PERCENTAGE",
                 "3P%" : "THREE POINT PERCENTAGE"
                 }

NBA_data=pd.read_csv('2018-19 NBA Data.csv')
#print(NBA_data.head())

def threePravsPER(NBA_data):
    player_list_PG_SG=NBA_data[(NBA_data.Pos =='PG') | (NBA_data.Pos == 'SG') & (NBA_data.G >= 60)].Player
    player_list_PG_SG=player_list_PG_SG.tolist()
    #print(player_list.head())

    PER_list_PG_SG=NBA_data[(NBA_data.Pos == 'PG') | (NBA_data.Pos == 'SG') & (NBA_data.G >= 60)].PER
    PER_list_PG_SG=PER_list_PG_SG.tolist()
    #print(PER_list.head())

    threePAr_PG_SG=NBA_data[(NBA_data.Pos == 'PG') | (NBA_data.Pos == 'SG') & (NBA_data.G >= 60)]['3PAr']
    threePAr_PG_SG=threePAr_PG_SG.tolist()
    #print(threePAr.head())

    plt.figure(figsize=(10,10))
    plt.scatter(threePAr_PG_SG, PER_list_PG_SG)
    ax=plt.subplot()
    ax.set_xlim(0, 0.8)
    ax.set_ylim(0, 32)

        
    name=["0","Jimmy Butler","Donovan Mitchell","James Harden","Stephen Curry","0.8"]
    xticks=[0,0.213,0.339,0.539,0.604,0.8]
    yticks=[0,20.2,17.2,30.6,24.4,32]

    xticklabels=[]
    i = 0
    while i < len(xticks):
        xticklabels.append(name[i])
        i+=1
    yticklabels=[]
    i = 0
    while i < len(yticks):
        yticklabels.append(str(yticks[i]))
        i += 1


    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_xticklabels(xticklabels, fontsize=10, rotation=30)
    ax.set_yticklabels(yticklabels, fontsize=10, rotation=45)


    i = 1
    while i < len(xticks)-1:
        plt.stem(xticks[i], yticks[i], linefmt=('-.'), markerfmt=('rs'))
        i += 1
    plt.xlabel("3PAr (3-Point Attempt Rate)")
    plt.ylabel("PER (Player Efficiency Rate)")
    plt.title("3PAr vs. PER for PG and SG (60 Games Min.)")
    plt.savefig('plots/3PAr vs. PER for PG and SG 60 Games Min.')
    plt.show()

def TOVpctvsOWS(NBA_data):
    player_list=NBA_data[(NBA_data.G >= 60)].Player
    TOVpct_list=NBA_data[(NBA_data.G >= 60)].TOV_Pct
    OWS_list=NBA_data[(NBA_data.G >= 60)].OWS
    
    plt.figure(figsize=(10,10))
    plt.scatter(TOVpct_list,OWS_list)
    plt.annotate("Stephen Curry", xy=(11.6,7.2), xytext=(15,6),arrowprops = dict(facecolor ='red',
                                  shrink = 0.05),)
    plt.annotate("James Harden", xy=(14.5,11.4), xytext=(10,10),arrowprops = dict(facecolor ='red',
                                  shrink = 0.05),)
    plt.annotate("Donvan Mitchell", xy=(11.3,1.3), xytext=(20,1),arrowprops = dict(facecolor ='red',
                                  shrink = 0.05),)
    plt.annotate("Rudy Gobert", xy=(12.1, 8.7), xytext=(12.4, 7.8),arrowprops = dict(facecolor ='red',
                                  shrink = 0.05),)

    m, b = np.polyfit(TOVpct_list, OWS_list, 1)
    plt.plot(TOVpct_list, m*TOVpct_list + b, color='red')
    plt.title("TOV% vs. OWS (60 Games Min.)") 
    plt.xlabel("TOV% (Turnover Percentage)")
    plt.ylabel("OWS (Offensive Win Shares)")


    ax=plt.subplot()
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 12)

    xticks=[0,5,10,15,20,25,30]
    yticks=[0,2,4,6,8,10,12]
    xticklabels=[str(i) + "%" for i in xticks]
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_xticklabels(xticklabels)
    
    plt.savefig('plots/TOV% vs OWS 60 Games Min.')
    plt.show()

TOVpctvsOWS(NBA_data)