    #all the necessary imports
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from NBA_Stats_web_helper import stats_description
from NBA_Stats_web_helper import stats_expansion
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.max_colwidth', None)

#instantiates Flask app
app = Flask(__name__)

#reads in nba stats data
player = 'Stephen Curry'
df=pd.read_csv('NBA_stats.csv')
string = ''
#alters the name list to names only
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
#initializes row of stats and a list of stats
player_row=df[df.Player == player]
stat_list = (player_row.columns.values)

#player input form
@app.route('/', methods=['GET', 'POST'])
def form():
    global player
    if (len(request.form)>0):
        player=request.form['player']
    else:
        player='Stephen Curry'
    return render_template("form.html", player=player)


#navigation page to different stats
@app.route('/<string:player>')
def home(player):
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    return render_template("home.html", player=player)

#display stats
@app.route('/<string:player>/ALL')
def all(player):
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    string = ''
    i = 0
    while i < len(stat_list):
        string += f'<p>{stat_list[i]}: {str(player_row[stat_list[i]].tolist()[0])}</p> '
        i += 1
    return f'''
             <h1 style="text-decoration: underline;">ALL STATISTICS</h1>
             {string}
             <a href='/{player}'>Home</a>
    '''

@app.route('/<string:player>/<string:stat>')
def stats(stat, player):
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    return render_template("stats.html", player=player,
                           stats_expansion = stats_expansion,
                           stat = stat,
                           player_row = player_row,
                           stats_description = stats_description)
