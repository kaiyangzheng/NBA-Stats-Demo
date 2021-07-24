import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

basic_stats_description={"PTS" : "1 point is awarded to a player whenever he makes a free throw; 2 points are awarded to a player whenever he makes a 2 point field goal; 3 points are awarded to a player whenever he makes a 3 point field goal",
                         "AST" : "An assist is awarded to a player whenever he makes a pass that directly leads to a score, excluding free throws",
                         "TRB" : "A rebound is awarded to a player whenever he gains possession of a ball off a missed field goal or free throw",
                         "TOV" : "A turnover is awarded to a player whenever he loses possession of the ball in a manner that does not involve missing a field goal or free throw",
                         "STL" : "A steal is awarded to a player whenever he causes a turnover by deflecting the ball or intercepting a pass",
                         "BLK" : "A block is awarded to a player whenever he deflects a field goal attempt from the opposing team, causing it to miss",
                         "PF" : "A personal foul is awarded to a player whenever he commits illegal personal contact to an opposing player. A player can have a maximum of 6 fouls before he is forced to leave the game",
                         "FGA" : "A field goal attempt is awarded to a player whenever he attempts any shot other than a free throw",
                         "FTA" : "A free throw attempt is awarded to a player whenever he attempts a free throw as a result of being fouled while shooting, or being fouled while the opposing team has more than 4 fouls in the current quarter",
                         "FT" : "A free throw make is awarded to a player whenever he makes a free throw as a result of being fouled while shooting, or being fouled while the opposing team has more than 4 fouls in the current quarter",
                         "2PA" : "A 2 point attempt is awarded to a player whenever he attempts a shot inside the three point line, excluding free throws",
                         "3PA" : "A 3 point attempt is awarded to a player whenever he attempts a shot outside the three point line",
                         "FG" : "A field goal is awarded to a player whenver he makes any shot other than a free throw",
                         "2P" : "A 2 point field goal is awarded to a player whenever he makes a shot inside the three point line, excluding free throws",
                         "3P" : "A 3 point field goal is awarded to a player whenever he makes a shot outside the three point line",
                         "FG%" : "The efficiency at which a player makes field goals",
                         "FT%" : "The efficiency at whih a player makes free throws",
                         "2P%" : "The efficiency at which a player makes two point field goals",
                         "3P%" : "The efficiency at which a player makes three point field goals",
                         "eFG%" : "A modification of FG% which considers 3 point makes to be worth 1.5 times more than 2 point makes"
                         }

basic_stats_expansion={"PTS": "Points Per Game",
                       "AST" : "Assists Per Game",
                       "TRB" : "Total Rebounds Per Game",
                       "TOV" : "Turnovers Per Game",
                       "STL" : "Steals Per Game",
                       "BLK" : "Blocks Per Game",
                       "PF" : "Personal Fouls Per Game",
                       "FGA" : "Field Goal Attempts Per Game",
                       "FTA" : "Free Throw Attempts Per Game",
                       "FT" : "Free Throw Makes Per Game",
                       "2PA" : "Two Point Attempts Per Game",
                       "3PA" : "Three Point Attempts Per Game",
                       "FG" : "Field Goal Makes Per Game",
                       "2P" : "Two Point Makes Per Game",
                       "3P" : "Three Point Makes Per Game",
                       "FG%" : "Field Goal Percentage",
                       "FT%" : "Free Throw Percentage",
                       "2P%" : "Two Point Percentage",
                       "3P%" : "Three Point Percentage",
                       "eFG%" : "Effective Field Goal Percentage"}

basic_stats_calculation={"PTS" : "See Definition",
                         "AST" : "See Definition",
                         "TRB" : "See Definition",
                         "TOV" : "See Definition",
                         "STL" : "See Definition",
                         "BLK" : "See Definition",
                         "PF" : "See Definition",
                         "FGA" : "See Definition",
                         "FTA" : "See Definition",
                         "FT" : "See Definition",
                         "2PA" : "See Definition",
                         "3PA" : "See Definition",
                         "FG" : "See Definition",
                         "2P" : "See Definition",
                         "3P" : "See Definition",
                         "FG%" : "FG/FGA",
                         "FT%" : "FT/FTA",
                         "2P%" : "2P/2PA",
                         "3P%" : "3P/3PA",
                         "eFG%" : "(2P + 1.5 * 3P)/FGA"
                        }

adv_stats_description={"PER" : "PER is a measure of a player's per-minute productivity",
                       "TS%" : "TS% is a measure of a player's shooting efficiency. TS% takes into account 2 point field goals, 3 point field goals, and free throws, making it more accurate than other shooting efficiency statistics",
                       "TRB%" : "TRB% is an estimate of the percentage of rebounds a player grabs while on the court",
                       "AST%" : "AST% is an estimate of the percentage of field goals a player assists while on the court",
                       "STL%" : "STL% is an estimate of the percentage of opponent possessions ended with a steal by a player while on the court",
                       "BLK%" : "BLK% is an estimate of the percentage of opponent two point field goal attempts blocked by a player while on the court",
                       "TOV%" : "TOV% is an estimate of turnovers committed by a player per 100 plays",
                       "USG%" : "USG% is an estimate of the percentage of plays a player is involved in while on the court",
                       "ORtg" : "ORtg is the points produced by a player per 100 possessions",
                       "DRtg" : "DRtg is the points allowed by a player per 100 possessions",
                       "OWS" : "OWS is an estimate of the number of wins contributed by a player on offense",
                       "DWS" : "DWS is an estimate of the number of wins contributed by a player on defense",
                       "WS" : "WS is an estimate of the number of wins contributed by a player",
                       "WS/48" : "WS/48, or Win Shares Per 48 Minutes, is an estimate of the number of wins contributed by a player per 48 minutes",
                       "OBPM" : "OBPM, or Offensive Box Score Plus/Minus, is an estimate of the number of points a player scores per 100 possessions above the NBA average.",
                       "DBPM" : "DBPM is an estimate of the number of defensive points a player contributes per 100 possessions above the NBA average",
                       "BPM" : "BPM is an estimate of the number of points a player contributes per 100 possessions above the NBA average",
                       "VORP" : "VORP is an estimate of the points per 100 possessions that a player contributes above a replacement player (-2.0 VORP)."
                       }

adv_stats_expansion={"PER": "Player Efficiency Rating",
                     "TS%": "True Shooting Percentage",
                     "TRB%": "Total Rebound Percentage",
                     "AST%": "Assist Percentage",
                     "BLK%" : "Block Percentage",
                     "TOV%" : "Turnover Percentage",
                     "USG%" : "Usage Percentage",
                     "ORtg" : "Offensive Rating",
                     "DRtg" : "Defensive Rating",
                     "OWS" : "Offensive Win Shares",
                     "DWS" : "Defensive Win Shares",
                     "WS" : "Win Shares",
                     "WS/48" : "Win Shares Per 48 Minutes",
                     "OBPM" : "Offensive Box Plus Minus",
                     "DBPM" : "Defensive Box Plus Minus",
                     "BPM" : "Box Plus Minus",
                     "VORP" : "Value OVer Replacement Player"
                     }

adv_stats_calculation={"PER" : "",
                       "TS%" : "PTS/(2*(FGA+(0.44*FTA)))",
                       "TRB%" : "(100*(Tm MP/5))/(MP*(Tm TRB+Opp TRB))",
                       "AST%" : "(100*Ast/(((MP/Tm MP/5)) * Tm FG) - FG)",
                       "BLK%" : "(100*(BLK*(Tm MP/5))/(MP*(Opp FGA - Opp 3PA))",
                       "TOV%" : "(100*(TOV)/FGA+0.44*FTA+TOV)",
                       "USG%" : "(100*((FGA+0.44*FTA+TOV)*(Tm MP/5))/(Tm FGA+0.44*Tm FTA+Tm TOV))",
                       "OWS" : "",
                       "DWS" : "",
                       "WS" : "",
                       "WS/48" : "",
                       "OBPM" : "",
                       "DBPM" : "",
                       "BPM" : "",
                       "VORP" : "",
                    }


            


df_2018_19_advanced=pd.read_csv('2018-19 NBA Data.csv')
df = pd.read_csv('NBA_Basic_Current.csv')
df_advanced=pd.read_csv('NBA_Advanced_Current.csv')
i = 0
player_list=[]
while i < len(df['Player']):
    player_list.append(df['Player'][i])
    i+=1
i = 0
while i < len(player_list):
    player_list[i]=player_list[i].split('\\')
    player_list[i]=player_list[i][0]
    i+=1
df.Player=player_list

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
    print (stat_list)
    playerOne_plot=[]
    playerTwo_plot=[]
    stat_plot=[]
    for i in stat_list:
        if (i == 'Rk' or i == 'Pos' or i == 'Tm' or i == 'MP' or i == 'Player' or i == 'G' or i=='OWS' or i == 'DWS' or i == 'WS/48' or i == 'OBPM' or i == 'DBPM' or i == 'Season' or i == '3PAr' or i == 'FTr' or i == 'Age' or i == 'ORB%' or i == 'DRB%' or i == 'ORB_Pct' or i == 'DRB_Pct'):
            pass
        else:
            stat_plot.append(i)
            playerOne_plot.append(playerOne_row[i].tolist()[0])
            playerTwo_plot.append(playerTwo_row[i].tolist()[0])

    plt.figure(figsize=(10,10))
    n=1
    t=2
    d=11
    w=0.8
    x_values = [t*element + w*n for element
                in range(d)]
    playerOneX = x_values
    print (playerOneX)
    print (playerOne_plot)
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

def PlayerOnevsPlayerTwo_WebApp(playerOne, playerTwo, NBA_data):
    playerOne_row=NBA_data[NBA_data.Player == playerOne]
    playerTwo_row=NBA_data[NBA_data.Player == playerTwo]
    stat_list = (playerOne_row.columns.values).tolist()
    print (stat_list)
    playerOne_plot=[]
    playerTwo_plot=[]
    stat_plot=[]
    for i in stat_list:
        if (i == 'Rk' or i == 'Pos' or i == 'Tm' or i == 'MP' or i == 'Player' or i == 'G' or i=='OWS' or i == 'DWS' or i == 'WS/48' or i == 'OBPM' or i == 'DBPM' or i == 'Season' or i == '3PAr' or i == 'FTr' or i == 'Age' or i == 'ORB%' or i == 'DRB%'):
            pass
        else:
            stat_plot.append(i)
            playerOne_plot.append(playerOne_row[i].tolist()[0])
            playerTwo_plot.append(playerTwo_row[i].tolist()[0])

    plt.figure(figsize=(10,10))
    n=1
    t=2
    d=11
    w=0.8
    x_values = [t*element + w*n for element
                in range(d)]
    playerOneX = x_values
    print (playerOneX)
    print (playerOne_plot)
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
    plt.savefig('static/'+playerOne +' vs '+ playerTwo + ' Bar Web App.png')

def BoxPlotPrac(NBA_data):
    PER_list = NBA_data['PER']
    plt.boxplot(PER_list, vert=False)
    plt.annotate('Mean', xy=(np.mean(PER_list), 1), xytext=(np.mean(PER_list)-1, 0.88),size=5)
    plt.annotate('1st Quartile', xy=(np.quantile(PER_list, 0.25), 1), xytext=(np.quantile(PER_list, 0.25)-2, 0.88), size=5)
    plt.annotate('3rd Quartile', xy=(np.quantile(PER_list, 0.75), 1), xytext=(np.quantile(PER_list, 0.75)-2, 0.88), size=5)
    plt.annotate('Max', xy=(np.max(PER_list), 1), xytext=(np.max(PER_list), 0.88), size=5)
    plt.annotate('Min', xy=(np.min(PER_list), 1), xytext=(np.min(PER_list), 0.88), size=5)

"""
def StatBoxPlot_WebApp(player, stat, NBA_data):
    stat_list = NBA_data[stat]
    new_df = NBA_data[NBA_data.Player == player]
    player_row = new_df.iloc
    print (player_row)
    plt.figure(figsize=(10,10))
    plt.boxplot(stat_list, vert=False)
    plt.stem(np.median(stat_list), 1, linefmt='-.', markerfmt='C1o', label="Median: " + str(np.median(stat_list)))
    plt.stem(np.quantile(stat_list, 0.25), 1, linefmt='-.', markerfmt='C2o', label = "Lower Quartile (Q1): " + str(np.quantile(stat_list, 0.25)))
    plt.stem(np.quantile(stat_list, 0.75), 1, linefmt='-.', markerfmt='C3o', label = "Upper Quartile (Q3): " + str(np.quantile(stat_list, 0.75)))
    plt.stem(np.max(stat_list), 1, linefmt='-.', markerfmt='C4o', label = 'Max: ' + str(np.max(stat_list)))
    plt.stem(np.min(stat_list), 1, linefmt='-.', markerfmt='C5o', label = 'Min: ' + str(np.min(stat_list)))
    plt.stem(player_row[stat], 1, linefmt='-.', markerfmt='C6o')
    plt.annotate(player, xy=(player_row[stat], 1), xytext=(player_row[stat]-0.4, 1.05), size=7)
    plt.legend(loc=2)
    yticks = []
    ax = plt.subplot()
    ax.set_yticks(yticks)
    plt.title(stat)
    plt.ylim(0,2)
    plt.savefig('static/' + player + ' ' + stat + '.png')
"""

def StatBoxPlot_WebApp(player, stat, NBA_data):
    player_row = NBA_data[NBA_data.Player == player]
    player_stat = player_row[stat].tolist()[0]
    stat_list = NBA_data[stat]
    plt.figure(figsize=(10,10))
    plt.boxplot(stat_list, vert=False)
    plt.stem(np.median(stat_list), 1, linefmt='-.', markerfmt='C1o', label="Median: " + str(np.median(stat_list)))
    plt.stem(np.quantile(stat_list, 0.25), 1, linefmt='-.', markerfmt='C2o', label = "Lower Quartile (Q1): " + str(np.quantile(stat_list, 0.25)))
    plt.stem(np.quantile(stat_list, 0.75), 1, linefmt='-.', markerfmt='C3o', label = "Upper Quartile (Q3): " + str(np.quantile(stat_list, 0.75)))
    plt.stem(np.max(stat_list), 1, linefmt='-.', markerfmt='C4o', label = 'Max: ' + str(np.max(stat_list)))
    plt.stem(np.min(stat_list), 1, linefmt='-.', markerfmt='C5o', label = 'Min: ' + str(np.min(stat_list)))
    plt.annotate(player, xy=(player_stat, 1), xytext=(player_stat-np.max(stat_list)/10, 1.1), size=13,  arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
    plt.stem(player_row[stat], 1, linefmt='-.', markerfmt='C6o')
    plt.legend(loc=2)
    yticks = []
    ax = plt.subplot()
    ax.set_yticks(yticks)
    plt.title(stat)
    plt.ylim(0,2)
    plt.savefig('static/' + player + ' ' + stat + '.png')
StatBoxPlot_WebApp('Stephen Curry', 'TOV', df)

StatXvsStatY_WebApp('TS%', 'OWS', df_advanced)
StatXvsStatY_WebApp('TOV%', 'OWS', df_advanced)
StatXvsStatY_WebApp('TRB%', 'WS', df_advanced)
StatXvsStatY_WebApp('FTr', 'OWS', df_advanced)



