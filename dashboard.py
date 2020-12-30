import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import folium
import streamlit.components.v1 as components
from streamlit_folium import folium_static
import branca
from functions import *

st.title("Dashboard for Project")
st.sidebar.title("Menu")

@st.cache
def load_data_1():
    data = pd.read_csv("https://raw.githubusercontent.com/vibzwengz/Project1WebApp/main/Battery.csv")
    return data

@st.cache
def load_data_2():
    data = pd.read_csv("https://raw.githubusercontent.com/vibzwengz/Project1WebApp/main/Table4.16.csv")
    return data

@st.cache
def load_data_3():
    data = pd.read_csv("https://raw.githubusercontent.com/vibzwengz/Project1WebApp/main/Table4.4.csv")
    return data

@st.cache
def get_map_data():
    data = pd.read_csv('https://raw.githubusercontent.com/vibzwengz/Project1WebApp/main/Table4.16.csv')
    return data

st.sidebar.subheader("Features of State Specific EV Policy")
option = st.sidebar.selectbox('Select State Specific Policy', ('--','Central Policy', 'Delhi'))
if option is not "--":
    st.subheader("Main features")


st.markdown(return_html(option), unsafe_allow_html=True)

col1, col2 = st.beta_columns(2)
st.sidebar.subheader('Comparision of Present Battery Electric Vehicles sold in the US')
option2 = st.sidebar.selectbox("Select type of visualization",("--","Vehicle Range(km)",'Vehicle Range(mi)','Battery Size(kWh)'))
if option2 is not '--':
    data = load_data_1()
    st.subheader("Present Battery Electric Vehicles sold in the US")
    st.pyplot(chart_return(data,option2))


more_info = st.sidebar.checkbox('More Information')
if more_info:
    data = load_data_1()
    cars = car_list(data)
    option3 = st.sidebar.radio("Select Car",cars)
    st.subheader(option3)
    st.write(display_car_info(data,option3))


st.sidebar.subheader('Comparision of Present Hybrid Electric Vehicles sold in the US')
option4 = st.sidebar.selectbox("Select type of visualization",("--","Electric Range(km)",'Electric Range(mi)','Battery Size(kWh)'),key = "option4")
if option4 is not '--':
    data = load_data_3()
    st.subheader("Present Hybrid Vehicles sold in the US")
    st.pyplot(chart_return(data,option4))


more_info_2 = st.sidebar.checkbox('More Information',key = "more_info_2")
if more_info_2:
    data = load_data_3()
    cars = car_list(data)
    option5 = st.sidebar.radio("Select Car",cars)
    st.write(display_car_info(data,option5))


st.sidebar.subheader("Lithium Reserves,Resources & Production Details")
show_map = st.sidebar.checkbox("Show map of lithium reserves and resources")
show_map_two = st.sidebar.checkbox("Show map of lithium production")


if show_map:
    st.subheader("Lithium Reserves & Resources")
    map_data = get_map_data()
    m = folium.Map(tiles="Stamen Watercolor", zoom_start=3, max_zoom=6, min_zoom=2, zoom_Animation=False)
    for i in range(0, len(map_data)):
        html = fancy_html2(map_data,i)
        iframe = branca.element.IFrame(html=html, width=350, height=150)
        popup = folium.Popup(iframe, parse_html=True)
        marker = folium.Marker([map_data.iloc[i]['latitude'], map_data.iloc[i]['longitude']],
                                popup=popup, icon=folium.Icon(color='green', icon='info-sign')).add_to(m)

    folium_static(m)



if show_map_two:
    st.subheader("Lithium Production")
    map_data = get_map_data()
    m = folium.Map(tiles="Stamen Watercolor", zoom_start=3, max_zoom=6, min_zoom=2, zoom_Animation=False)
    for i in range(0, len(map_data)):
        if pd.notna(map_data.iloc[i]['Production(tonnes)(2018)']):
            html = fancy_html1(map_data,i)
            iframe = branca.element.IFrame(html=html, width=350, height=150)
            popup = folium.Popup(iframe, parse_html=True)
            marker = folium.Marker([map_data.iloc[i]['latitude'], map_data.iloc[i]['longitude']],
                                   popup=popup, icon=folium.Icon(color='green', icon='info-sign')).add_to(m)

    folium_static(m)


