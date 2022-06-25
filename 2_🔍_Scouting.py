from ast import For
from numpy import full
import pandas as pd
import sys

from PIL import Image

sys.path.append('Functions')
#############################################################################################################################################################

import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = 'Fonts/Gagalin-Regular.otf'
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

#Courier New

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = prop.get_name()

##################################################################################################################################################

import streamlit as st

##################################################################################################################################################

wyscout = pd.read_csv('Data/WyScout.csv')

wyscout.drop_duplicates(subset=['Player'], keep='first', inplace=True)

wyscout.drop(['Team within selected timeframe', 'On loan'], axis=1, inplace=True)

##################################################################################################################################################

from Functions import radar as rd

# add an image to the sidebar
logo = Image.open('SWP LOGO.png')
st.sidebar.image(logo)

##################################################################################################################################################

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
           'Offensive duels/90', 'PAdj Interceptions', 'Aerial duels/90', 'Aerial duels %']

##################################################################################################################################################

scouting_choice = st.sidebar.selectbox('Choose what you want to assess:', ['Pizza Chart', 'Radar Chart Compare', 'Beeswarm'])

##################################################################################################################################################

if scouting_choice == 'Pizza Chart':

    st.title('Pizza Chart')

    first, second, third, fourth = st.columns(4)

    leagues = wyscout.Comp.unique()
    leagues = leagues.tolist()

    leagues_choice = first.selectbox('Choose League:', leagues)

    club = wyscout.loc[wyscout.Comp == leagues_choice]
    club = club.Team.unique()
    club = club.tolist()

    club_choice = second.selectbox('Choose Team:', club)

    players = wyscout.loc[wyscout.Team == club_choice]
    players = players.Player.tolist()

    players_choice = third.selectbox('Choose Player:', players)

    position = ['Center Back', 'Full Back', 'Defensive Midfield', 'Midfield', 'Offensive Midfield', 'Forward']

    position_choice = fourth.selectbox('Choose Position to evaluate:', position)

    if position_choice == 'Center Back':

        fig = rd.PizzaChartSWP(wyscout, center_Back, players_choice, leagues_choice, True)

        st.pyplot(fig)

    elif position_choice == 'Full Back':

        fig = rd.PizzaChartSWP(wyscout, full_Back, players_choice, leagues_choice, True)

        st.pyplot(fig)

    elif position_choice == 'Defensive Midfield':

        fig = rd.PizzaChartSWP(wyscout, defensive_Midfield, players_choice, leagues_choice, True)

        st.pyplot(fig)

    elif position_choice == 'Midfield':

        fig = rd.PizzaChartSWP(wyscout, Midfield, players_choice, leagues_choice, True)

        st.pyplot(fig)

    elif position_choice == 'Offensive Midfield':

        fig = rd.PizzaChartSWP(wyscout, offensive_Midfield, players_choice, leagues_choice, True)

        st.pyplot(fig)

    elif position_choice == 'Winger':

        fig = rd.PizzaChartSWP(wyscout, Winger, players_choice, leagues_choice, True)

        st.pyplot(fig)

    elif position_choice == 'Forward':

        fig = rd.PizzaChartSWP(wyscout, Forward, players_choice, leagues_choice, True)

        st.pyplot(fig)

    ############################################################################################################

elif scouting_choice == 'Radar Chart Compare':

    st.title('Radar Chart Compare')

    first, second, third, fourth = st.columns(4)

    leagues = wyscout.Comp.unique()
    leagues = leagues.tolist()

    leagues_choice = first.selectbox('Choose League:', leagues)

    club = wyscout.loc[wyscout.Comp == leagues_choice]
    club = club.Team.unique()
    club = club.tolist()

    club_choice = second.selectbox('Choose Team:', club)

    players = wyscout.loc[wyscout.Team == club_choice]
    players = players.Player.tolist()

    players_choice = third.selectbox('Choose Player:', players)

    ############################################################################################################

    leaguesCompare = wyscout.Comp.unique()
    leaguesCompare = leaguesCompare.tolist()

    leaguesCompare_choice = first.selectbox('Choose League to compare:', leaguesCompare)

    clubCompare = wyscout.loc[wyscout.Comp == leaguesCompare_choice]
    clubCompare = clubCompare.Team.unique()
    clubCompare = clubCompare.tolist()

    clubCompare_choice = second.selectbox('Choose Team to compare:', clubCompare)

    playersCompare = wyscout.loc[wyscout.Team == clubCompare_choice]
    playersCompare = playersCompare.Player.tolist()
    playersCompare.insert(0, playersCompare[1])

    playersCompare_choice = third.selectbox('Choose Player to compare:', playersCompare)

    position = ['Forward', 'Full Back', 'Defensive Midfield', 'Midfield', 'Offensive Midfield', 'Center Back']

    position_choice = fourth.selectbox('Choose Position to evaluate:', position)

    if position_choice == 'Center Back':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, center_Back)

        st.pyplot(fig)

    elif position_choice == 'Full Back':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, full_Back)

        st.pyplot(fig)

    elif position_choice == 'Defensive Midfield':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, defensive_Midfield)

        st.pyplot(fig)

    elif position_choice == 'Midfield':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, Midfield)

        st.pyplot(fig)

    elif position_choice == 'Offensive Midfield':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, offensive_Midfield)

        st.pyplot(fig)

    elif position_choice == 'Winger':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, Winger)

        st.pyplot(fig)

    elif position_choice == 'Forward':

        fig = rd.radar_chart_compare(wyscout, players_choice, playersCompare_choice, Forward)

        st.pyplot(fig)


elif scouting_choice == 'Beeswarm':

    st.title('Beeswarm')

    compare_choice = st.sidebar.selectbox('Do you want to compare Players?:', ['No', 'Yes'])

    if compare_choice == 'No':

        first, second, third, fourth = st.columns(4)

        leagues = wyscout.Comp.unique()
        leagues = leagues.tolist()

        leagues_choice = first.selectbox('Choose League:', leagues)

        club = wyscout.loc[wyscout.Comp == leagues_choice]
        club = club.Team.unique()
        club = club.tolist()

        club_choice = second.selectbox('Choose Team:', club)

        players = wyscout.loc[wyscout.Team == club_choice]
        players = players.Player.tolist()

        players_choice = third.selectbox('Choose Player:', players)

        position = ['Center Back', 'Full Back', 'Defensive Midfield', 'Midfield', 'Offensive Midfield', 'Forward']

        position_choice = fourth.selectbox('Choose Position to evaluate:', position)

        if position_choice == 'Center Back':

            fig = rd.beeswarmSWP(wyscout, players_choice, center_Back)

            st.pyplot(fig)

        elif position_choice == 'Full Back':

            fig = rd.beeswarmSWP(wyscout, players_choice, full_Back)

            st.pyplot(fig)

        elif position_choice == 'Defensive Midfield':

            fig = rd.beeswarmSWP(wyscout, players_choice, defensive_Midfield)

            st.pyplot(fig)

        elif position_choice == 'Midfield':

            fig = rd.beeswarmSWP(wyscout, players_choice, Midfield)

            st.pyplot(fig)

        elif position_choice == 'Offensive Midfield':

            fig = rd.beeswarmSWP(wyscout, players_choice, offensive_Midfield)

            st.pyplot(fig)

        elif position_choice == 'Winger':

            fig = rd.beeswarmSWP(wyscout, players_choice, Winger)

            st.pyplot(fig)

        elif position_choice == 'Forward':

            fig = rd.beeswarmSWP(wyscout, players_choice, Forward)

            st.pyplot(fig)
    ############################################################################################################

    elif compare_choice == 'Yes':

        first, second, third, fourth = st.columns(4)

        leagues = wyscout.Comp.unique()
        leagues = leagues.tolist()

        leagues_choice = first.selectbox('Choose League:', leagues)

        club = wyscout.loc[wyscout.Comp == leagues_choice]
        club = club.Team.unique()
        club = club.tolist()

        club_choice = second.selectbox('Choose Team:', club)

        players = wyscout.loc[wyscout.Team == club_choice]
        players = players.Player.tolist()

        players_choice = third.selectbox('Choose Player:', players)

        leaguesCompare = wyscout.Comp.unique()
        leaguesCompare = leaguesCompare.tolist()

        leaguesCompare_choice = first.selectbox('Choose League to compare:', leaguesCompare)

        clubCompare = wyscout.loc[wyscout.Comp == leaguesCompare_choice]
        clubCompare = clubCompare.Team.unique()
        clubCompare = clubCompare.tolist()

        clubCompare_choice = second.selectbox('Choose Team to compare:', clubCompare)

        playersCompare = wyscout.loc[wyscout.Team == clubCompare_choice]
        playersCompare = playersCompare.Player.tolist()

        playersCompare_choice = third.selectbox('Choose Player to compare:', playersCompare)

        position = ['Center Back', 'Full Back', 'Defensive Midfield', 'Midfield', 'Offensive Midfield', 'Forward']

        position_choice = fourth.selectbox('Choose Position to evaluate:', position)

        if position_choice == 'Center Back':

            fig = rd.beeswarmSWP(wyscout, players_choice, center_Back, playersCompare_choice)

            st.pyplot(fig)

        elif position_choice == 'Full Back':

            fig = rd.beeswarmSWP(wyscout, players_choice, full_Back, playersCompare_choice)

            st.pyplot(fig)

        elif position_choice == 'Defensive Midfield':

            fig = rd.beeswarmSWP(wyscout, players_choice, defensive_Midfield, playersCompare_choice)

            st.pyplot(fig)

        elif position_choice == 'Midfield':

            fig = rd.beeswarmSWP(wyscout, players_choice, Midfield, playersCompare_choice)

            st.pyplot(fig)

        elif position_choice == 'Offensive Midfield':

            fig = rd.beeswarmSWP(wyscout, players_choice, offensive_Midfield, playersCompare_choice)

            st.pyplot(fig)

        elif position_choice == 'Winger':

            fig = rd.beeswarmSWP(wyscout, players_choice, Winger, playersCompare_choice)

            st.pyplot(fig)

        elif position_choice == 'Forward':

            fig = rd.beeswarmSWP(wyscout, players_choice, Forward, playersCompare_choice)

            st.pyplot(fig)