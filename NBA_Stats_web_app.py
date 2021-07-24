import os
from re import S
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from NBA_Stats_web_helper import basic_stats_description, basic_stats_expansion, basic_stats_calculation, adv_stats_description, adv_stats_expansion,adv_stats_calculation, PlayerOnevsPlayerTwo_WebApp, StatBoxPlot_WebApp
from flask import send_from_directory 
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

player = ''
comparison_player=''
string = ''
df=pd.read_csv('NBA_Basic_Current.csv')
df_advanced = pd.read_csv('NBA_Advanced_Current.csv')
#alters the name list for df
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

#alters the name list for dv_advanced
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
player_row_adv=df_advanced[df_advanced.Player == player]
stat_list_adv = (player_row_adv.columns.values)

print (df.head())
@app.route('/', methods=['GET', 'POST'])
def form():
    global player
    player_form=PlayerForm()
    if player_form.validate_on_submit():
        player=player_form.player_input.data
        return redirect(url_for("home", player = player))
    return render_template("form.html", player=player, template_form=player_form)


@app.route('/<string:player>')
def home(player):
    img_href=getImage(player)
    player_row=df[df.Player == player]
    stat_list = (player_row.columns.values)
    return render_template("home.html", player=player,img_href=img_href, player_row=player_row,basic_stats_expansion = basic_stats_expansion,adv_stats_expansion= adv_stats_expansion)

@app.route('/<string:player>/<string:stat>')
def stats(stat, player):
    basic_row = df[df.Player == player]
    if stat in adv_stats_expansion:
        player_row=df_advanced[df_advanced.Player == player]
        stat_list = (player_row.columns.values)
        stat_calculation = adv_stats_calculation
        stat_description = adv_stats_description
        stat_expansion = adv_stats_expansion
        print ('adv')
        StatBoxPlot_WebApp(player, stat, df_advanced)
    else:
        player_row=df[df.Player == player]
        stat_list = (player_row.columns.values)
        stat_calculation = basic_stats_calculation
        stat_description = basic_stats_description
        stat_expansion = basic_stats_expansion
        print ('basic')
        StatBoxPlot_WebApp(player, stat, df)

    return render_template("stats.html", player=player, 
                           stat_calculation = stat_calculation,
                           stat_description = stat_description,
                           stat_expansion=stat_expansion,
                           stat = stat,
                           player_row = player_row)

@app.route('/<string:player>/FourFactors')
def FourFactors(player):
    return render_template("FourFactors.html", player=player)

@app.route('/<string:player>/ComparisonForm', methods=['GET', 'POST'])
def ComparisonForm(player):
    global comparison_player
    comparison_player_form=PlayerForm()
    if comparison_player_form.validate_on_submit():
        comparison_player=comparison_player_form.player_input.data
        return redirect(url_for("comparison_plot", player=player, comparison_player=comparison_player))
    return render_template("comparison_form.html", comparison_player=comparison_player, player=player, template_form=comparison_player_form)

@app.route('/<string:player>/ComparisonForm/<string:comparison_player>')
def comparison_plot(player, comparison_player):
    href = player + " vs " + comparison_player + " Bar Web App.png"
    return render_template("comparison_plot.html", player=player, comparison_player=comparison_player, href=href)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
