import streamlit as st
import pandas as pd
import sys

import matplotlib.pyplot as plt

from PIL import Image

import warnings
warnings.filterwarnings("ignore")

from pandas.core.common import SettingWithCopyWarning

import warnings
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

plt.rcParams["figure.dpi"] = 300

sys.path.append('Functions')

##################################################################################################################################################

image = Image.open('SWP LOGO.png')

st.set_page_config(page_title='SWP APP', layout="wide", page_icon=image)

st.set_option('deprecation.showPyplotGlobalUse', False)

# add an image to the sidebar
logo = Image.open('SWP LOGO.png')
st.sidebar.image(logo)

##################################################################################################################################################

from matplotlib import font_manager

font_path = 'Fonts/Gagalin-Regular.otf'
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

#Courier New

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = prop.get_name()

##################################################################################################################################################

new_title = '<p style="font-family:Gagalin regular; color:#043484; font-size: 42px;">Sports With Python App</p>'
st.markdown(new_title, unsafe_allow_html=True)

main_message = '<p style="font-family:Arial; color:white; font-size: 20px;">This is an App developed by Sports With Python with the aim of bringing the sports audience closer to the world of data.<br>In this App you will be able to see your favourite players, the players associated\nwith your teams during the transfer markets and make your own assessments<br>through graphical analysis of the players</p>'
st.markdown(main_message, unsafe_allow_html=True)

league_message_1 = '<p style="font-family:Gagalin regular; color:#043484; font-size: 25px;">Leagues currently available in the SWP App:</p>'
st.markdown(league_message_1, unsafe_allow_html=True)

continent_message = '<p style="font-family:Gagalin regular; color:#043484;; font-size: 22px;">American Continent:</p>'
st.markdown(continent_message, unsafe_allow_html=True)

league_message_2 = '<p style="font-family:Arial; color:white; font-size: 20px;">Argentina<br>Brazil (Brasileirão, Serie B and Serie C)<br>Peru<br>Colombia<br>MLS<br>MLS Pro<br>US League 1<br>USL Championship</p>'
st.markdown(league_message_2, unsafe_allow_html=True)

continent_message = '<p style="font-family:Gagalin regular; color:#043484;; font-size: 22px;">European Continent:</p>'
st.markdown(continent_message, unsafe_allow_html=True)

league_message_3 = '<p style="font-family:Arial; color:white; font-size: 20px;">Portugal<br>Spain<br>France<br>Italy<br>Germany<br>England<br>Scotland<br>Czech<br>Denmark<br>Netherlands<br>Serbia<br>Turkey<br>Belgium<br>Switzerland<br>Sweden</p>'
st.markdown(league_message_3, unsafe_allow_html=True)

continent_message = '<p style="font-family:Gagalin regular; color:#043484;; font-size: 22px;">Asian Continent:</p>'
st.markdown(continent_message, unsafe_allow_html=True)

league_message_4 = '<p style="font-family:Arial; color:white; font-size: 20px;">Japan<br>South Korea</p>'
st.markdown(league_message_4, unsafe_allow_html=True)

data_Message = '<p style="font-family:Gagalin regular; color:#043484; font-size: 18px;">All data from WyScout</p>'
st.markdown(data_Message, unsafe_allow_html=True)