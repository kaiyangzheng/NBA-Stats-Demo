#all the necessary imports
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from NBA_Stats_web_helper import stats_description
from NBA_Stats_web_helper import stats_expansion
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.max_colwidth', None)

#instantiates Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

def getImage(player):
    first_part=''
    second_part=''
    player=player.split(' ')
    first_part=player[1][0:5]
    first_part=first_part.lower()
    second_part=player[0][0:2]
    second_part=second_part.lower()
    link='https://www.basketball-reference.com/req/202106291/images/players/'+first_part+second_part+'01.jpg'
    return link

class PlayerForm(FlaskForm):
    player_input=StringField("Player:", validators=[DataRequired()])
    submit=SubmitField("Submit")

#reads in nba stats data
player = ''
string = ''
df=pd.read_csv('NBA_stats.csv')
df_advanced = pd.read_csv('NBA_Advanced_Current')
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
    player_form=PlayerForm()
    if player_form.validate_on_submit():
        player=player_form.player_input.data
        return redirect(url_for("home", player = player))
    return render_template("form.html", player=player, template_form=player_form)


#navigation page to different stats
@app.route('/<string:player>')
def home(player):
    img_href=getImage(player)
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    return render_template("home.html", player=player,img_href=img_href, player_row=player_row)

#display all stats
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
#display stats
@app.route('/<string:player>/<string:stat>')
def stats(stat, player):
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    return render_template("stats.html", player=player,
                           stats_expansion = stats_expansion,
                           stat = stat,
                           player_row = player_row,
                           stats_description = stats_description)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
