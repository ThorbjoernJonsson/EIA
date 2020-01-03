import eia
import pandas as pd
import numpy as np
import datetime as dt
import plotly.graph_objects as go

def retrieve_time_series(api, series_ID):
    series_search = api.data_by_series(series=series_ID)
    df = pd.DataFrame(series_search)

    #clean data frame
    len_dat = len(df.index)
    dates = [0]*len_dat
    inv = [0]*len_dat
    for i in range(0, len_dat):
        temp = (df.index[i].split(" "))
        dates[i] = dt.date(int(temp[0]), int(temp[1][0:2]), int(temp[-1]))
        inv[i] = df.values[i][0]

    upd_df = pd.DataFrame({"Date":dates, "Inventories": inv})
    return upd_df

def plot_time_series(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date, y=df['Inventories'], name="Inventory level",
                             line_color='deepskyblue'))

    fig.update_layout(title_text='USA Crude Inventory Level',
                      xaxis_rangeslider_visible=True)
    fig.show()
    return 1

def main():
    api_key = "YOUR_API_KEY_HERE"
    api = eia.API(api_key)
    series_ID='http://api.eia.gov/series/?api_key=6569647505cfb6f73e1aa9363045abc3&series_id=PET.WCESTUS1.W'
    df = retrieve_time_series(api, series_ID)
    plot_time_series(df)
