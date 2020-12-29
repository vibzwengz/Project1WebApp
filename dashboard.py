import streamlit as st
import io
import requests
import matplotlib.pyplot as plt
import pandas as pd
import folium
import streamlit.components.v1 as components
from streamlit_folium import folium_static
import branca

#folium_static(m)
st.title("Dashboard for Project")
st.sidebar.title("Menu")

st.sidebar.subheader("Features of State Specific EV Policy")
option = st.sidebar.selectbox('Select State Specific Policy', ('--','Central Policy', 'Delhi'))
if option is not "--":
    st.subheader("Main features")


def return_html(option):
    html_string = ''
    if option == 'Central Policy':
        html_string = '<ul>\
              <li>Faster Adoption and Manufacturing of Hybrid and Electric Vehicles(FAME)-1\
                <ul>\
                  <li>Initially launched for a two-year period, but extended till September 2018 at an aprroved outlay of INR 795 Cr in 2015</li>\
                  <li>Focussed on technology development, demand creation, pilot projects and charging infrastructure</li>\
                </ul>\
            </li>\
              <li>FAME-2\
                <ul>\
                  <li>Under phase two extend financial support of INR 8,730 Cr for three years</li>\
                  <li>The fund support includes INR 2,500 Cr for buses, INR 1,000 Cr for four-wheelers,  \
                INR 600 Cr for two-wheelers and INR 750 Cr for high speed three-wheelers</li>\
                </ul>\
            </li>\
            </ul>'
    elif option == "Delhi":
        html_string = '<ul>\
        <li>It envisions the replacement of the existing auto rickshaws and State-run buses with E-Autos and E-Buses respectively\
                      It will also ensure that delivery based services operating in the city are powered by E-Mobility.</li>\
        <li>It talks about increasing road tax for fuel-based vehicles, at least in the luxury segment and imposing in certain parts of the city\
                      a congestion fee that EVs will be exempt from.</li>\
        </ul>'
    return html_string


st.markdown(return_html(option), unsafe_allow_html=True)

data_battery = pd.read_csv("Battery.csv")
def chart_return(option2):
    if option2 =='Range(km) Bar Chart':
        plt.barh(data_battery['Model'], data_battery['Vehicle Range(km)'])
        plt.ylabel("Model")
        plt.xlabel("Range in Kilometres")
        st.pyplot(plt)
    elif option2 == 'Range(mi) Bar Chart':
        plt.barh(data_battery['Model'], data_battery['Vehicle Range(mi)'])
        plt.ylabel("Model")
        plt.xlabel("Range in Miles")
        st.pyplot(plt)


st.sidebar.subheader('Comparision of Present Battery Electric Vehicles sold in the US')
option2 = st.sidebar.selectbox("Select type of visualization",("--","Range(km) Bar Chart",'Range(mi) Bar Chart'))
if option2 is not '--':
    st.subheader("Present Battery Electric Vehicles sold in the US")
    chart_return(option2)

#def car_list()

more_info = st.sidebar.checkbox('More Information')
if more_info:
    cars = []
    for i in range(len(data_battery)):
        string_company = data_battery.iloc[i]['Manufacturer']
        string_model = data_battery.iloc[i]['Model']
        string_car = string_company + " " + string_model
        cars.append(string_car)
    cars = tuple(cars)
    option3 = st.sidebar.radio("Select Brand 🚗",cars)
    for i in range(len(data_battery)):
        string_company = data_battery.iloc[i]['Manufacturer']
        string_model = data_battery.iloc[i]['Model']
        string_car = string_company + " " + string_model
        if string_car == option3:
            st.subheader(string_car)
            st.write(data_battery.iloc[i])

st.sidebar.subheader('Comparision of Present Hybrid Electric Vehicles sold in the US')

    #st.write("You selected " + option3)
#url = "https://github.com/vibzwengz/Project1WebApp/raw/main/test.csv"
#read_data = requests.get(url).content
st.sidebar.subheader("Lithium Reserves,Resources & Production Details")
show_map = st.sidebar.checkbox("Show map of lithium reserves and resources")
show_map_two = st.sidebar.checkbox("Show map of lithium production")

@st.cache
def get_map_data():
    return pd.read_csv("Table4.16.csv")

def fancy_html2(row):
    i = row
    string_1 = map_data.iloc[i]['Country']
    if pd.notna(map_data.iloc[i]['Reserve(Tonnes)']):
        string_3 = int(map_data.iloc[i]['Reserve(Tonnes)'])
    else:
        string_3 = "-"
    if pd.notna(map_data.iloc[i]['Resources(Tonnes)']):
        string_4 = int(map_data.iloc[i]['Resources(Tonnes)'])
    else:
        string_4 = "-"
    left_col_colour = "#CCFFCC"
    right_col_colour = "#CCFFCC"

    html = """<!DOCTYPE html>
<html>

<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
    <table style="width: 350px">
<tbody>
<tr>
<td style="background-color: """ + left_col_colour + """;"><span style="color: #000000;">Country</span></td>
<td style="width: 150px;background-color: """ + right_col_colour + """;">{}</td>""".format(string_1) + """
</tr>
<tr>
<td style="background-color: """ + left_col_colour + """;"><span style="color: #000000;">Reserve(Tonnes)</span></td>
<td style="width: 150px;background-color: """ + right_col_colour + """;">{}</td>""".format(string_3) + """
</tr>
<tr>
<td style="background-color: """ + left_col_colour + """;"><span style="color: #000000;">Resources(Tonnes)</span></td>
<td style="width: 150px;background-color: """ + right_col_colour + """;">{}</td>""".format(string_4) + """
</tr>
</tbody>
</table>
</html>
"""
    return html

if show_map:
    st.subheader("Lithium Reserves & Resources")
    map_data = get_map_data()
    m = folium.Map(tiles="Stamen Watercolor", zoom_start=3, max_zoom=6, min_zoom=2, zoom_Animation=False)
    for i in range(0, len(map_data)):
        html = fancy_html2(i)
        iframe = branca.element.IFrame(html=html, width=350, height=150)
        popup = folium.Popup(iframe, parse_html=True)
        marker = folium.Marker([map_data.iloc[i]['latitude'], map_data.iloc[i]['longitude']],
                                popup=popup, icon=folium.Icon(color='green', icon='info-sign')).add_to(m)

    folium_static(m)

def fancy_html1(row):
    i = row
    string_1 = map_data.iloc[i]['Country']
    string_2 = int(map_data.iloc[i]['Production(tonnes)(2018)'])
    string_5 = int(map_data.iloc[i]['Production(tonnes)(2019)'])
    left_col_colour = "#CCFFCC"
    right_col_colour = "#CCFFCC"

    html = """<!DOCTYPE html>
<html>

<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
    <table style="width: 350px">
<tbody>
<tr>
<td style="background-color: """ + left_col_colour + """;"><span style="color: #000000;">Country</span></td>
<td style="width: 150px;background-color: """ + right_col_colour + """;">{}</td>""".format(string_1) + """
</tr>
<tr>
<td style="background-color: """ + left_col_colour + """;"><span style="color: #000000;">Production(tonnes)(2018)</span></td>
<td style="width: 150px;background-color: """ + right_col_colour + """;">{}</td>""".format(string_2) + """
</tr>
<tr>
<td style="background-color: """ + left_col_colour + """;"><span style="color: #000000;">Production(tonnes)(2019)</span></td>
<td style="width: 150px;background-color: """ + right_col_colour + """;">{}</td>""".format(string_5) + """
</tr>
</tbody>
</table>
</html>
"""
    return html

if show_map_two:
    st.subheader("Lithium Production")
    map_data = get_map_data()
    m = folium.Map(tiles="Stamen Watercolor", zoom_start=3, max_zoom=6, min_zoom=2, zoom_Animation=False)
    for i in range(0, len(map_data)):
        if pd.notna(map_data.iloc[i]['Production(tonnes)(2018)']):
            html = fancy_html1(i)
            iframe = branca.element.IFrame(html=html, width=350, height=150)
            popup = folium.Popup(iframe, parse_html=True)
            marker = folium.Marker([map_data.iloc[i]['latitude'], map_data.iloc[i]['longitude']],
                                   popup=popup, icon=folium.Icon(color='green', icon='info-sign')).add_to(m)

    folium_static(m)


