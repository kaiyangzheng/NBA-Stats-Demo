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

df_2018_19_advanced=pd.read_csv('2018-19 NBA Data.csv')
df_advanced=pd.read_csv('NBA_Advanced_Current.csv')
i = 0
player_list_adv=[]
while i < len(df_advanced['Player']):
    player_list_adv.append(df_advanced['Player'][i])
    i+=1
i = 0
while i < len(player_list_adv):
    player_list_adv[i]=player_list_adv[i].split('\\')
    player_list_adv[i]=player_list_adv[i][0]
    i+=1
df_advanced.Player=player_list_adv

def threePravsPER(NBA_data):
    PER_list_PG_SG=NBA_data[(NBA_data.Pos == 'PG') | (NBA_data.Pos == 'SG') & (NBA_data.G >= 60)].PER
    #print(PER_list.head())

    threePAr_PG_SG=NBA_data[(NBA_data.Pos == 'PG') | (NBA_data.Pos == 'SG') & (NBA_data.G >= 60)]['3PAr']
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


def FTrvsOWS(NBA_data):
    player_list=NBA_data[(NBA_data.G >= 60)].Player
    FTr_list=NBA_data[(NBA_data.G >= 60)].FTr
    OWS_list=NBA_data[(NBA_data.G >= 60)].OWS

    top_FTr = np.quantile(FTr_list, 0.99)
    top_OWS = np.quantile(OWS_list, 0.01)
    plt.figure(figsize=(10,10))
    ax=plt.subplot()
    minX = np.min(FTr_list)
    minY = np.min(OWS_list)
    maxX = np.max(FTr_list)
    maxY = np.max(OWS_list)
    plt.xlim(0,0.8)
    plt.ylim(-2,12)
    m, b = np.polyfit(FTr_list, OWS_list, 1)
    plt.plot(FTr_list, m*FTr_list + b, color='red')
    plt.scatter(FTr_list, OWS_list)
    plt.title("FTr vs. OWS (60 Games Min.)")
    plt.xlabel("FTr (Free Throw rate)")
    plt.ylabel("OWS (Offensive Win Shares)")

    xticks= [0]
    yticks=[-2]
    xticklabels=['0']
    for index,value in player_list.items():
        new_df = NBA_data[(NBA_data.Player==value) & (NBA_data.G >= 60)]
        player_row = new_df.iloc[0]
        if (player_row.FTr>=top_FTr or player_row.OWS>=top_OWS):
            xticks.append(player_row.FTr)
            yticks.append(player_row.OWS)
            xticklabels.append(player_row.Player)
            annotate = '('+str(player_row.FTr) + ',' + str(player_row.OWS)+')'
            plt.annotate(annotate,xy=(player_row.FTr, player_row.OWS), xytext=(player_row.FTr+0.005, player_row.OWS-0.05))
    xticks.append(0.8)
    xticklabels.append('0.8')
    yticks.append(12)

    i = 1
    while i < len(xticks)-1:
        plt.stem(xticks[i], yticks[i], linefmt=('-.'), markerfmt=('rs'), bottom=-2)
        i += 1
    plt.legend(['Line of Best Fit','non-98th Percentile OWS or FTR','98th Percentile OWS or FTr'], loc=2)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels,fontsize=7,rotation=20)

    plt.savefig('plots/FTr vs OWS 60 Games Min.')
    plt.show()


def TOVpctvsOWS(NBA_data):
    player_list=NBA_data[(NBA_data.G >= 60)].Player
    TOVpct_list=NBA_data[(NBA_data.G >= 60)].TOV_Pct
    OWS_list=NBA_data[(NBA_data.G >= 60)].OWS

    topTOVpct=np.quantile(TOVpct_list,0.98)
    botOWS=np.quantile(OWS_list, 0.02) 
    
    plt.figure(figsize=(10,10))
    ax=plt.subplot()
    ax.set_xlim(0, 30)
    ax.set_ylim(-2, 12)
    minX = np.min(TOVpct_list)
    minY = np.min(OWS_list)
    maxX = np.max(TOVpct_list)
    maxY = np.max(OWS_list)
    plt.scatter(TOVpct_list,OWS_list)
    m, b = np.polyfit(TOVpct_list, OWS_list, 1)
    plt.plot(TOVpct_list, m*TOVpct_list + b, color='red')
    plt.title("TOV% vs. OWS (60 Games Min.)") 
    plt.xlabel("TOV% (Turnover Percentage)")
    plt.ylabel("OWS (Offensive Win Shares)")
    
    xticks=[0]
    xticklabels= ['0']
    yticks=[-2]
    for index, value in player_list.items():
        new_df=NBA_data[(NBA_data.Player==value) & (NBA_data.G>=60)]
        player_row = new_df.iloc[0]
        if (player_row.TOV_Pct>=topTOVpct or player_row.OWS <=botOWS):
            xticks.append(player_row.TOV_Pct)
            yticks.append(player_row.OWS)
            xticklabels.append(player_row.Player)
            annotate = player_row.Player
            plt.annotate(annotate,xy=(player_row.TOV_Pct, player_row.OWS), xytext=(player_row.TOV_Pct+0.5, player_row.OWS-0.05), size=8)
    xticks.append(30)
    xticklabels.append('30')
    yticks.append(12)

    i = 1
    while i < len(xticks)-1:
        plt.stem(xticks[i], yticks[i], linefmt=('-.'), markerfmt=('rs'), bottom=-2)
        i += 1
    plt.legend(['Line of Best Fit','non-98th Percentile OWS or non-2nd Percentile TOV%','98th Percentile OWS or 2nd Percentile TOV%'], loc=2)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, rotation=40)
    plt.savefig('plots/TOV% vs OWS 60 Games Min.')
    plt.show()

def TS_PctvsOWS(NBA_data):
    player_list=NBA_data[(NBA_data.G >= 60)].Player
    TSPct_list=NBA_data[(NBA_data.G >= 60)].TS_Pct
    OWS_list=NBA_data[(NBA_data.G >= 60)].OWS

    topTSPct=np.quantile(TSPct_list,0.98)
    topOWS=np.quantile(OWS_list, 0.98)
    
    plt.figure(figsize=(10,10))
    ax=plt.subplot()
    ax.set_xlim(0.45, 0.7)
    ax.set_ylim(-2, 12)
    minX = np.min(TSPct_list)
    minY = np.min(OWS_list)
    maxX = np.max(TSPct_list)
    maxY = np.max(OWS_list)
    
    plt.scatter(TSPct_list,OWS_list)

    m, b = np.polyfit(TSPct_list, OWS_list, 1)
    plt.plot(TSPct_list, m*TSPct_list + b, color='red')
    plt.title("TS% vs. OWS (60 Games Min.)") 
    plt.xlabel("TS% (True Shooting Percentage)")
    plt.ylabel("OWS (Offensive Win Shares)")
    
    xticks=[0.45]
    xticklabels= ['0.45']
    yticks=[-2]
    for index, value in player_list.items():
        new_df=NBA_data[(NBA_data.Player==value) & (NBA_data.G>=60)]
        player_row = new_df.iloc[0]
        if (player_row.TS_Pct>=topTSPct or player_row.OWS >=topOWS):
            xticks.append(player_row.TS_Pct)
            yticks.append(player_row.OWS)
            xticklabels.append(player_row.Player)
            annotate = player_row.Player
            plt.annotate(annotate,xy=(player_row.TS_Pct, player_row.OWS), xytext=(player_row.TS_Pct+0.003, player_row.OWS-0.05), size=8)
    xticks.append(0.7)
    xticklabels.append('0.7')
    yticks.append(12)

    i = 1
    while i < len(xticks)-1:
        plt.stem(xticks[i], yticks[i], linefmt=('-.'), markerfmt=('rs'), bottom=-2)
        i += 1
    plt.legend(['Line of Best Fit','non-98th Percentile OWS or TS%','98th Percentile OWS or Percentile TS%'], loc=2)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, rotation=40)
    plt.savefig('plots/TS% vs OWS 60 Games Min.')

    plt.show()

def TRBPctvsWS(NBA_data):
    player_list=NBA_data[(NBA_data.G >= 60)].Player
    TRBPct_list=NBA_data[(NBA_data.G >= 60)].TRB_Pct
    WS_list=NBA_data[(NBA_data.G >= 60)].WS

    topTRBPct=np.quantile(TRBPct_list,0.98)
    topWS=np.quantile(WS_list, 0.98)

    plt.figure(figsize=(10,10))
    ax=plt.subplot()
    ax.set_xlim(0, 30)
    ax.set_ylim(-2.5, 20)
    minX = np.min(TRBPct_list)
    minY = np.min(WS_list)
    maxX = np.max(TRBPct_list)
    maxY = np.max(WS_list)

    plt.scatter(TRBPct_list,WS_list)

    m, b = np.polyfit(TRBPct_list, WS_list, 1)
    plt.plot(TRBPct_list, m*TRBPct_list + b, color='red')
    plt.title("TRB% vs. WS (60 Games Min.)") 
    plt.xlabel("TRB% (Total Rebound Percentage)")
    plt.ylabel("WS (Win Shares)")
    
    xticks=[0]
    xticklabels= ['0']
    yticks=[-2.5]
    for index, value in player_list.items():
        new_df=NBA_data[(NBA_data.Player==value) & (NBA_data.G>=60)]
        player_row = new_df.iloc[0]
        if (player_row.TRB_Pct>=topTRBPct or player_row.WS >=topWS):
            xticks.append(player_row.TRB_Pct)
            yticks.append(player_row.WS)
            xticklabels.append(player_row.Player)
            annotate = player_row.Player
            plt.annotate(annotate,xy=(player_row.TRB_Pct, player_row.WS), xytext=(player_row.TRB_Pct+0.5, player_row.WS+0.1 ), size=8)
    xticks.append(30)
    xticklabels.append('30')
    yticks.append(20)

    i = 1
    while i < len(xticks)-1:
        plt.stem(xticks[i], yticks[i], linefmt=('-.'), markerfmt=('rs'), bottom=-2)
        i += 1
    plt.legend(['Line of Best Fit','non-98th Percentile OWS or TS%','98th Percentile WS or  Percentile TRB%'], loc=2)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, rotation=40)
    plt.savefig('plots/TRB% vs WS 60 Games Min.')
    plt.show()

def StatXvsStatY(statx,staty,NBA_data):
    player_list = NBA_data[NBA_data.G>=60].Player
    statX_list = NBA_data[NBA_data.G>=60][statx]
    statY_list = NBA_data[NBA_data.G>=60][staty]

    topStatX = np.quantile(statX_list,0.98)
    topStatY = np.quantile(statY_list,0.98)

    plt.figure(figsize=(10,10))
    ax=plt.subplot()

    minX = np.min(statX_list)
    maxX = np.max(statX_list)
    minY = np.min(statY_list)
    maxY = np.max(statY_list)
    print (maxX)
    print (minX)
    maxPlotX = maxX + ((maxX-minX)/70)
    minPlotX = minX - ((maxX-minX)/70)
    maxPlotY = maxY + ((maxY-minY)/70)
    minPlotY = minY - ((maxY-minY)/70)
    ax.set_xlim(minPlotX, maxPlotX)
    ax.set_ylim(minPlotY, maxPlotY)

    plt.scatter(statX_list, statY_list)
    m,b=np.polyfit(statX_list, statY_list, 1)
    plt.plot(statX_list, m*statX_list+b, color='red')
    plt.title(statx + " vs. " + staty + " (60 Games Min.)")
    plt.xlabel(statx)
    plt.ylabel(staty)

    for index, value in player_list.items():
        new_df=NBA_data[(NBA_data.Player==value) & (NBA_data.G>=60)]
        player_row=new_df.iloc[0]
        if (player_row[statx]>=topStatX or player_row[staty]>=topStatY):
            annotate=player_row.Player
            plt.annotate(annotate,xy=(player_row[statx],player_row[staty]),xytext=(player_row[statx]+(maxX-minX)/80,player_row[staty]), size=5)
            plt.scatter(player_row[statx],player_row[staty], color='green')
    plt.legend(['Line of Best Fit','non-98th Percentile '+statx+' or '+staty,'98th Percentile '+statx+' or '+staty], loc=2)
    plt.savefig('plots/'+statx+' vs '+ staty + ' 60 Games Min.')

def PlayerOnevsPlayerTwo(playerOne, playerTwo, NBA_data):
    playerOne_row=NBA_data[NBA_data.Player == playerOne]
    playerTwo_row=NBA_data[NBA_data.Player == playerTwo]
    stat_list = (playerOne_row.columns.values).tolist()
    playerOne_plot=[]
    playerTwo_plot=[]
    stat_plot=[]
    for i in stat_list:
        if (i == 'Pos' or i == 'Tm' or i == 'MP' or i == 'Player' or i == 'G' or i=='OWS' or i == 'DWS' or i == 'WS/48' or i == 'OBPM' or i == 'DBPM' or i == 'Season' or i == '3PAr' or i == 'FTr' or i == 'Age' or i == 'ORB_Pct' or i == 'DRB_Pct'):
            pass
        else:
            stat_plot.append(i)
            playerOne_plot.append(playerOne_row[i].tolist()[0])
            playerTwo_plot.append(playerTwo_row[i].tolist()[0])
    
    print (stat_plot)
    print (playerOne_plot)
    print (playerTwo_plot)

    plt.figure(figsize=(10,10))
    n=1
    t=2
    d=11
    w=0.8
    x_values = [t*element + w*n for element
                in range(d)]
    playerOneX = x_values
    plt.bar(playerOneX, playerOne_plot)

    n=2
    t=2
    d=11
    w=0.8
    x_values = [t*element + w*n for element 
                in range(d)]
    playerTwoX = x_values
    plt.bar(playerTwoX, playerTwo_plot)
    ax = plt.subplot()
    xpos=[]
    i = 0
    while i < len(playerOneX):
        xpos.append((playerOneX[i]+playerTwoX[i])/2)
        i+=1
    ax.set_xticks(xpos)
    ax.set_xticklabels(stat_plot)
    plt.xlabel("Advanced Statistics")
    plt.ylabel("Value")
    plt.title(playerOne + ' vs. ' + playerTwo)  
    plt.legend([playerOne, playerTwo])
    plt.savefig('plots/'+playerOne +' vs '+ playerTwo + ' Bar')
    plt.show()

def StatXvsStatY_WebApp(statx,staty,NBA_data):
    player_list = NBA_data[NBA_data.G>=60].Player
    statX_list = NBA_data[NBA_data.G>=60][statx]
    statY_list = NBA_data[NBA_data.G>=60][staty]
    
    topStatX = np.quantile(statX_list,0.98)
    topStatY = np.quantile(statY_list,0.98)

    plt.figure(figsize=(10,10))
    ax=plt.subplot()

    minX = np.min(statX_list)
    maxX = np.max(statX_list)
    minY = np.min(statY_list)
    maxY = np.max(statY_list)
    maxPlotX = maxX + ((maxX-minX)/70)
    minPlotX = minX - ((maxX-minX)/70)
    maxPlotY = maxY + ((maxY-minY)/70)
    minPlotY = minY - ((maxY-minY)/70)
    ax.set_xlim(minPlotX, maxPlotX)
    ax.set_ylim(minPlotY, maxPlotY)

    plt.scatter(statX_list, statY_list)
    m,b=np.polyfit(statX_list, statY_list, 1)
    plt.plot(statX_list, m*statX_list+b, color='red')
    plt.title(statx + " vs. " + staty + " (60 Games Min.)")
    plt.xlabel(statx)
    plt.ylabel(staty)

    for index, value in player_list.items():
        new_df=NBA_data[(NBA_data.Player==value) & (NBA_data.G>=60)]
        player_row=new_df.iloc[0]
        if (player_row[statx]>=topStatX or player_row[staty]>=topStatY):
            annotate=player_row.Player
            plt.annotate(annotate,xy=(player_row[statx],player_row[staty]),xytext=(player_row[statx]+(maxX-minX)/80,player_row[staty]), size=5)
            plt.scatter(player_row[statx],player_row[staty], color='green')
    plt.legend(['Line of Best Fit','non-98th Percentile '+statx+' or '+staty,'98th Percentile '+statx+' or '+staty], loc=2)
    plt.savefig('static/'+statx+' vs '+ staty + ' 60 Games Min. Web App.png')


StatXvsStatY_WebApp('TS%', 'OWS', df_advanced)
StatXvsStatY_WebApp('TOV%', 'OWS', df_advanced)
StatXvsStatY_WebApp('TRB%', 'WS', df_advanced)
StatXvsStatY_WebApp('FTr', 'OWS', df_advanced)

#PlayerOnevsPlayerTwo('Stephen Curry', 'Kevin Durant', df_2018_19_advanced)
#PlayerOnevsPlayerTwo('James Harden', 'Russell Westbrook', df_2018_19_advanced)
