from flask import Flask, render_template
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from NBA_Stats_web_helper import stats_description
from NBA_Stats_web_helper import stats_expansion

pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.max_colwidth', None)

player = 'Stephen Curry'
df=pd.read_csv('NBA_stats.csv')
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

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("home.html", player = player)


@app.route('/ALL')
def all():
    string = ''
    i = 0
    while i < len(stat_list):
        string += f'<p>{stat_list[i]}: {str(player_row[stat_list[i]].tolist()[0])}</p> '
        i += 1
    return f'''<a href='/'>Home</a>
             {string}
    '''

@app.route('/<string:stat>')
def stats(stat):
    
    return render_template("stats.html", stats_expansion = stats_expansion,
                           stat = stat,
                           player_row = player_row,
                           stats_description = stats_description)
