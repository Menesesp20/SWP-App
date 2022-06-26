import pandas as pd
import sys

import streamlit as st

import matplotlib.pyplot as plt
import matplotlib as mpl

import plotly.express as px
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from mplsoccer import Pitch, PyPizza, add_image

from highlight_text import  ax_text, fig_text

from soccerplots.utils import add_image
from soccerplots.radar_chart import Radar

from scipy import stats

import math
import ipywidgets as widgets

from pandas.core.common import SettingWithCopyWarning
from IPython.display import display, Math, Latex

import warnings
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

plt.rcParams["figure.dpi"] = 300

sys.path.append('Data Hub/Functions')

###############################################################################################################################################################

from matplotlib import font_manager

font_path = 'Fonts/Gagalin-Regular.otf'
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

#Courier New

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = prop.get_name()

###############################################################################################################################################################

wyscout = pd.read_csv('Data/WyScout.csv')

wyscout.drop_duplicates(subset=['Player'], keep='first', inplace=True)

wyscout.drop(['Team within selected timeframe', 'On loan'], axis=1, inplace=True)

###############################################################################################################################################################

center_Back = ['Non-penalty goals/90', 'Offensive duels %', 'Progressive runs/90',
                'Passes %', 'Forward passes %', 'Forward passes/90', 'Progressive passes/90',
               'PAdj Interceptions', 'PAdj Sliding tackles', 'Defensive duels/90', 'Defensive duels %',
               'Aerial duels/90', 'Aerial duels %', 'Shots blocked/90']

full_Back = ['Successful dribbles %', 'Touches in box/90', 'Offensive duels %', 'Progressive runs/90', 'Crosses/90', 'Deep completed crosses/90',
            'Passes %', 'Deep completions/90', 'Progressive passes/90', 'Key passes/90', 'Third assists/90',
             'PAdj Interceptions', 'Defensive duels %', 'Aerial duels/90', 'Aerial duels %']

defensive_Midfield  = ['xG/90', 'Shots', 'Progressive runs/90', 'Successful dribbles %',
                       'Passes %', 'Forward passes %', 'Forward passes/90', 'Progressive passes/90','PAdj Sliding tackles',
                       'PAdj Interceptions', 'Aerial duels %', 'Defensive duels %', 'Offensive duels %']

Midfield  = ['xG/90', 'Shots', 'Progressive runs/90', 'Successful dribbles %',
             'Passes %', 'Forward passes %', 'Forward passes/90', 'Progressive passes/90',
             'Key passes/90', 'Second assists/90', 'Assists', 'xA',
             'PAdj Interceptions', 'Aerial duels %', 'Defensive duels %',]

offensive_Midfield = ['xG/90', 'Goals/90', 'Progressive runs/90', 'Successful dribbles %',
                      'xA/90', 'Deep completions/90', 'Passes to penalty area/90',
                      'Touches in box/90', 'Key passes/90', 'Passes final 1/3 %',
                      'Passes penalty area %', 'Progressive passes/90',
                      'Succ defensive actions/90', 'PAdj Interceptions', 'Aerial duels %', 'Defensive duels %', 'Pass Ability']

offensive_Midfield_BS = ['Successful dribbles %', 'xA/90', 'Deep completions/90', 'Passes to penalty area/90',
                      'Key passes/90', 'Passes final 1/3 %']

Winger = ['Successful dribbles %', 'Goals', 'xG/90',
          'xA/90', 'Touches in box/90', 'Dribbles/90', 'Passes to penalty area/90', 'Key passes/90',
          'Progressive runs/90', 'Crosses/90', 'Deep completed crosses/90',
          'Offensive duels/90', 'PAdj Interceptions']

Forward = ['Goals', 'xG/90', 'Shots on target, %', 'Goal conversion, %',
           'Successful dribbles %', 'xA/90', 'Touches in box/90', 'Dribbles/90',
           'Offensive duels/90', 'PAdj Interceptions', 'Aerial duels/90', 'Aerial duels %',]

###############################################################################################################################################################

def PizzaChartSWP(df, cols, playerName, league, samePosition=None):
    # parameter list
    params = cols

    playerDF = df.loc[(df.Player == playerName) & (df.Comp == league)]

    league = playerDF.Comp.unique()

    league = league.tolist()

    league = league[0]

    position = playerDF['Position'].unique()

    position = position.tolist()

    position = position[0]

    marketValue = playerDF['Market value'].unique()

    marketValue = marketValue.tolist()
    
    marketValue = marketValue[0]

    if samePosition != None:
        df = df.loc[df['Position'] == position].reset_index()

        player = df.loc[(df['Player'] == playerName) & (df['Comp'] == league) & (df['Position'] == position)][cols].reset_index()
        player = list(player.loc[0])
        player = player[1:]
        
    elif samePosition == None:
        df = df.copy()

        player = df.loc[(df['Player'] == playerName) & (df['Comp'] == league)][cols].reset_index()
        player = list(player.loc[0])
        player = player[1:]

    values = []
    for x in range(len(params)):   
        values.append(math.floor(stats.percentileofscore(df[params[x]], player[x])))

    for n,i in enumerate(values):
        if i == 100:
            values[n] = 99

    if cols == Forward:
        # color for the slices and text
        slice_colors = ["#043484"] * 4 + ["#043484"] * 4 + ["#043484"] * 4
        text_colors = ["#F2F2F2"] * 12

    elif cols == Winger:
        # color for the slices and text
        slice_colors = ["#043484"] * 3 + ["#043484"] * 8 + ["#043484"] * 2
        text_colors = ["#F2F2F2"] * 13

    elif cols == defensive_Midfield:
        # color for the slices and text
        slice_colors = ["#043484"] * 4 + ["#043484"] * 4 + ["#043484"] * 5
        text_colors = ["#F2F2F2"] * 13
        
    elif cols == Midfield:
        # color for the slices and text
        slice_colors = ["#043484"] * 4 + ["#043484"] * 8 + ["#043484"] * 3
        text_colors = ["#F2F2F2"] * 15

    elif cols == full_Back:
        # color for the slices and text
        slice_colors = ["#043484"] * 6 + ["#043484"] * 5 + ["#043484"] * 4
        text_colors = ["#F2F2F2"] * 15

    elif cols == center_Back:
        # color for the slices and text
        slice_colors = ["#043484"] * 3 + ["#043484"] * 4 + ["#043484"] * 7
        text_colors = ["#F2F2F2"] * 14

    elif cols == offensive_Midfield:
        # color for the slices and text
        slice_colors = ["#043484"] * 4 + ["#043484"] * 8 + ["#043484"] * 4
        text_colors = ["#F2F2F2"] * 16

    # instantiate PyPizza class
    baker = PyPizza(
        params=params,                  # list of parameters
        background_color="#181818",     # background color
        straight_line_color="#000000",  # color for straight lines
        straight_line_lw=1,             # linewidth for straight lines
        last_circle_color="#000000",    # color for last line
        last_circle_lw=1,               # linewidth of last circle
        other_circle_lw=0,              # linewidth for other circles
        inner_circle_size=20            # size of inner circle
    )

    # plot pizza
    fig, ax = baker.make_pizza(
        values,                          # list of values
        figsize=(15, 10),                # adjust the figsize according to your need
        color_blank_space="same",        # use the same color to fill blank space
        slice_colors=slice_colors,       # color for individual slices
        value_colors=text_colors,        # color for the value-text
        value_bck_colors=slice_colors,   # color for the blank spaces
        blank_alpha=0.4,                 # alpha for blank-space colors
        kwargs_slices=dict(
            edgecolor="#000000", zorder=2, linewidth=1
        ),                               # values to be used when plotting slices
        kwargs_params=dict(
            color="#F2F2F2", fontsize=10,
            va="center"
        ),                               # values to be used when adding parameter labels
        kwargs_values=dict(
            color="#F2F2F2", fontsize=11,
            zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="cornflowerblue",
                boxstyle="round,pad=0.2", lw=1
            )
        )                                # values to be used when adding parameter-values labels
    )

    if cols == Forward:

        fig_text(s =  'Forward Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)

    elif cols == Winger:

        fig_text(s =  'Winger Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)

    elif cols == defensive_Midfield:

        fig_text(s =  'Defensive Midfield Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)

    elif cols == Midfield:

        fig_text(s =  'Midfield Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)

    elif cols == full_Back:

        fig_text(s =  'Full Back Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)
    elif cols == center_Back:

        fig_text(s =  'Center Back Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)

    elif cols == offensive_Midfield:

        fig_text(s =  'Offensive Midfield Template',
             x = 0.253, y = 0.035,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8)

    ###########################################################################################################

    fig_text(s =  playerName,
             x = 0.5, y = 1.12,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=50);

    if playerName != 'David Neres':

        fig_text(s =  'Percentile Rank | ' + league + ' | Pizza Chart | Season 2021-22',
                x = 0.5, y = 1.03,
                color='#F2F2F2',
                fontweight='bold', ha='center',
                fontsize=14);

    elif playerName == 'David Neres':

        fig_text(s =  'Percentile Rank | ' + league + ' | Pizza Chart | Calendar Year 2021',
                x = 0.5, y = 1.03,
                color='#F2F2F2',
                fontweight='bold', ha='center',
                fontsize=14);

    #fig_text(s =  str(marketValue),
    #         x = 0.5, y = 1.02,
    #         color='#F2F2F2',
    #         fontweight='bold', ha='center',
    #         fontsize=18);

    # add credits
    CREDIT_1 = "data: WyScout"
    CREDIT_2 = "made by: @menesesp20"
    CREDIT_3 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"


    # CREDITS
    fig_text(s =  f"{CREDIT_1}\n{CREDIT_2}\n{CREDIT_3}",
             x = 0.35, y = 0.02,
             color='#F2F2F2',
             fontweight='bold', ha='center',
             fontsize=8);

    # add image
    add_image('Images/SWL LOGO.png', fig, left=0.4578, bottom=0.429, width=0.11, height=0.134)


def beeswarmSWP(df, playerName, cols, playerName2=None):
    
    if playerName2 != None:
        player = df.loc[(df['Player'] == playerName)]

        league = player.Comp.unique()

        league = league[0]

        position = player.Position.unique()

        position = position.tolist()

        position = position[0]

        player2 = df.loc[(df['Player'] == playerName2)]

        league2 = player2.Comp.unique()

        league2 = league2[0]

        minute = player['Minutes played'].max()

        minute2 = player2['Minutes played'].max()

        if minute > minute2:
            minute = minute
        elif minute2 > minute2:
            minute = minute2
        else:
            minute = minute

        df = df.loc[(df['Minutes played'] >= minute) & (df['Comp'] == league) | (df['Comp'] == league2)].reset_index()

    elif playerName2 == None:
        player = df.loc[(df['Player'] == playerName)]

        position = player.Position.unique()

        position = position.tolist()

        position = position[0]

        minute = player['Minutes played'].max()

        league = player.Comp.unique()

        league = league[0]

        df = df.loc[(df['Minutes played'] >= minute) & (df['Comp'] == league)].reset_index()

    fig,axes = plt.subplots(3,2,figsize=(14,10))
    fig.set_facecolor('#1b1b1b')

    metrics = cols

    #set default colors
    text_color = 'white'
    background = '#1b1b1b'

    #set up our base layer
    mpl.rcParams['xtick.color'] = text_color
    mpl.rcParams['ytick.color'] = text_color

    #create a list of comparisons
    counter=0
    counter2=0
    met_counter = 0

    for i,ax in zip(df['Player'],axes.flatten()):
        ax.set_facecolor(background)
        ax.grid(ls='dotted',lw=.5,color='#043484',axis='y',zorder=1)
        
        spines = ['top','bottom','left','right']
        for x in spines:
            if x in spines:
                ax.spines[x].set_visible(False)
                
        sns.swarmplot(x=metrics[met_counter],data=df,ax=axes[counter,counter2], zorder=1,color='white')
        ax.set_xlabel(f'{metrics[met_counter]}',c='white')
        
        if playerName2 != None:
            for x in range(len(df['Player'])):
                if playerName in df['Player'][x]:
                    ax.scatter(x=df[metrics[met_counter]][x], y=0, s=200, c='#043484', zorder=2)

                if playerName2 in df['Player'][x]:
                    ax.scatter(x=df[metrics[met_counter]][x], y=0, s=200, c='#ea04dc', zorder=2)

        if playerName2 == None:
            for x in range(len(df['Player'])):
                if playerName in df['Player'][x]:
                    ax.scatter(x=df[metrics[met_counter]][x], y=0, s=200, c='#043484', zorder=2)            

        met_counter+=1
        if counter2 == 0:
            counter2 = 1
            continue
        if counter2 == 1:
            counter2 = 0
            counter+=1

            
    if playerName2 == None:
        highlight_textprops =\
        [{"color": '#043484',"fontweight": 'bold'}]

        fig_text(s=f'<{playerName}>' + ' ' + 'Stats',
                x=0.4, y=.93,
                #highlight_weights = ['bold'],
                fontsize=30,
                highlight_textprops = highlight_textprops,
                color = text_color,
                va='center'
                    )

        fig_text(s='Made in <SWP APP>',
                x=0.45, y=.89,
                #highlight_weights = ['bold'],
                fontsize=15,
                highlight_textprops = highlight_textprops,
                color = text_color,
                va='center'
                    )

    elif playerName2 != None:
        highlight_textprops =\
            [{"color": '#043484',"fontweight": 'bold'},
            {"color": '#ea04dc',"fontweight": 'bold'}]

        fig_text(s=f'<{playerName}>' + ' ' +  'and' + ' ' + f'<{playerName2}>' + ' ' + 'Stats',
                x=0.3, y=.90,
                #highlight_weights = ['bold'],
                fontsize=30,
                highlight_textprops = highlight_textprops,
                color = text_color,
                va='center'
                    )

    fig.text(.12,.05,"all stats/90", fontsize=11, color=text_color)
    fig.text(.12,.03,"@menesesp20 / data via wyscout", fontstyle='italic', fontsize=11,color=text_color)

    # add image
    add_image('Images/SWL LOGO.png', fig, left=0.80, bottom=0.01, width=0.11, height=0.05)

def radar_chart_compare(df, player, player2, cols):

  #Obtenção dos dois jogadores que pretendemos
  pl1 = df[(df['Player'] == player)]

  position = pl1['Position'].unique()
  position = position.tolist()
  position = position[0]

  val1 = pl1[cols].values[0]

  club = pl1['Team'].values[0]
  league = pl1['Comp'].values[0]

  #Obtenção dos dois jogadores que pretendemos
  pl2 = df[(df['Player'] == player2)]
  val2 = pl2[cols].values[0]

  position2 = pl2['Position'].unique()
  position2 = position2.tolist()
  position2 = position2[0]

  club2 = pl2['Team'].values[0]
  league2 = pl2['Comp'].values[0]


  df = df.loc[(df.Comp == league)| (df.Comp == league2)]

  #Obtenção dos valores das colunas que pretendemos colocar no radar chart, não precisamos aceder ao index porque só iriamos aceder aos valores de um dos jogadores
  values = [val1, val2]

  #Obtençaõ dos valores min e max das colunas selecionadas
  ranges = [(df[col].min(), df[col].max()) for col in cols] 

  #Atribuição dos valores aos titulos e respetivos tamanhos e cores
  title = dict(
      #Jogador 1
      title_name = player,
      title_color = '#ea04dc',
      
      #Jogador 2
      title_name_2 = player2,
      title_color_2 = '#2d92df',

      #Tamnhos gerais do radar chart
      title_fontsize = 20,
      subtitle_fontsize = 15
  )

  #team_player = df[col_name_team].to_list()

  #dict_team ={'Dortmund':['#ffe011', '#000000'],
              #'Nice':['#cc0000', '#000000'],
              #'Nice':['#cc0000', '#000000']}

  #color = dict_team.get(team_player[0])

  ## endnote 
  endnote = "Visualization made by: Pedro Meneses(@menesesp20)"

  #Criação do radar chart
  fig, ax = plt.subplots(figsize=(18,15), dpi=200)
  radar = Radar(background_color="#1b1b1b", patch_color="#e8e8e8", range_color="white", label_color="white", label_fontsize=11, range_fontsize=12)
  fig, ax = radar.plot_radar(ranges=ranges, 
                             params=cols, 
                             values=values, 
                             radar_color=['#ea04dc','#043484'], 
                             figax=(fig, ax),
                             image_coord=[0.40, 0.81, 0.1, 0.075],
                             title=title,
                             endnote=endnote, end_size=0, end_color="#1b1b1b",
                             compare=True)
  
  fig.set_facecolor('#1b1b1b')

  # add image
  add_image('Images/SWL LOGO.png', fig, left=0.458, bottom=0.445, width=0.11, height=0.07)

def radar_chart(df, player, col_name_player, col_name_team, cols, league, club, player2=None, player3=None):

  if player2 == None:
    #Atribuição do jogador a colocar no gráfico
    players = df[df[col_name_player] == player]
    #Valores que pretendemos visualizar no radar chart, acedemos ao index 0 para obtermos os valores dentro da lista correta
    values = players[cols].values[0]
    #Obtenção do alcance minimo e máximo dos valores
    ranges = [(df[col].min(), df[col].max()) for col in cols]

    #Atribuição dos valores aos titulos e respetivos tamanhos e cores
    title = dict(
      title_name = player,
      title_color = '#043484',
      title_fontsize = 25,
    )

    #team_player = df[col_name_team].to_list()

    #dict_team ={'Dortmund':['#ffe011', '#000000'],
              #'Nice':['#cc0000', '#000000'],}

    #color = dict_team.get(team_player[0])

    ## endnote 
    endnote = "Visualization made by: Pedro Meneses(@menesesp20)"

    #Criação do radar chart
    fig, ax = plt.subplots(figsize=(18,15))
    radar = Radar(background_color="#181818", patch_color="white", range_color="white", label_color="white", label_fontsize=12, range_fontsize=12)
    fig, ax = radar.plot_radar(ranges=ranges, 
                               params=cols, 
                               values=values, 
                               radar_color='#043484',
                               figax=(fig, ax),
                               image_coord=[0.464, 0.81, 0.1, 0.075],
                               title=title,
                               endnote=endnote)

    fig.set_facecolor('#181818')

  else:
    radar_chart_compare(df, player, player2, col_name_player, col_name_team, cols, league)


