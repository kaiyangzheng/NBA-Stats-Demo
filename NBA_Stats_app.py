import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.max_colwidth', None)

def display_stats(df, player):
    string = ''
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
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    for i in stat_list:
        string += i + ', '
    string += 'ALL'
    print ('List of statistics: ' + '\n' + string)
    print ('')
    stat = input('Choose a statistic to display: ')
    if stat == 'ALL':
        i = 0
        while i < len(stat_list):
            print (stat_list[i] + ': ' + str(player_row[stat_list[i]].tolist()[0]))
            i += 1
    else:   
        stat_print = player_row[stat].tolist()[0]
        print (stat + ': ' + str(stat_print))
    

nba_df=pd.read_csv('NBA_stats.csv')
player = input('Choose an NBA player: ')
print ('')

display_stats(nba_df, player)
