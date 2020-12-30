import pandas as pd
import matplotlib.pyplot as plt
#first function
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


#second function
'''def chart_return(data,option,type):
    plt.close()
    if type == "electric":
        if option =='Range(km) Bar Chart':
            plt.barh(data['Model'], data['Vehicle Range(km)'])
            plt.ylabel("Model")
            plt.xlabel("Range in Kilometres")
            #st.pyplot(plt)
        elif option == 'Range(mi) Bar Chart':
            plt.barh(data['Model'], data['Vehicle Range(mi)'])
            plt.ylabel("Model")
            plt.xlabel("Range in Miles")
            #st.pyplot(plt)
    if type == "hybrid":
        if option =='Range(km) Bar Chart':
            print('here')
            plt.barh(data['Model'], data['Electric Range(km)'])
            plt.ylabel("Model")
            plt.xlabel("Range in Kilometres")
            #st.pyplot(plt)
        elif option == 'Range(mi) Bar Chart':
            plt.barh(data['Model'], data['Electric Range(mi)'])
            plt.ylabel("Model")
            plt.xlabel("Range in Miles")
            #st.pyplot(plt)
    return plt'''

def chart_return(data,column):
    plt.close()
    plt.barh(data['Model'], data[column])
    plt.ylabel("Model")
    plt.xlabel(column)
    # st.pyplot(plt)
    return plt


#third function
def car_list(data):
    cars = []
    for i in range(len(data)):
        string_company = data.iloc[i]['Manufacturer']
        string_model = data.iloc[i]['Model']
        string_car = string_company + " " + string_model
        cars.append(string_car)
    return tuple(cars)


#fourth function
def display_car_info(data,option):
    for i in range(len(data)):
        string_company = data.iloc[i]['Manufacturer']
        string_model = data.iloc[i]['Model']
        string_car = string_company + " " + string_model
        if string_car == option:
            #st.subheader(string_car)
            return data.iloc[i]


#fifth function
def fancy_html2(map_data,row):
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

def fancy_html1(map_data,row):
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