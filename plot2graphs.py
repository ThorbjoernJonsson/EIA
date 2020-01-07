import eia
import pandas as pd
import numpy as np
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#Sapp.run(args, host=0.0.0.0)

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

def plot_time_series(df1, df2):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=df1.Date, y=df1['Inventories'], name="Inventory level"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df2.Date, y=df2['Inventories'], name="Crude prices"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text="USA Crude Inventory Level and crude prices"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>primary</b> Barrels", secondary_y=False)
    fig.update_yaxes(title_text="<b>secondary</b> USD/barrel", secondary_y=True)

    fig.show()

    return 1

def main():
    api_key = "YOUR_API_KEY_HERE"
    api = eia.API(api_key)
    #Total US inventories
    #series_ID1='http://api.eia.gov/series/?api_key=YOUR_API_KEY_HER&series_id=PET.WCESTUS1.W'
    series_ID1 = 'http://api.eia.gov/series/?YOUR_API_KEY_HER&series_id=PET.W_EPC0_SAX_YCUOK_MBBL.W'
    series_ID2 = 'http://api.eia.gov/series/?api_key=YOUR_API_KEY_HER&series_id=PET.RWTC.D'
    df1 = retrieve_time_series(api, series_ID1)
    df2 = retrieve_time_series(api, series_ID2)
    plot_time_series(df1, df2)

if __name__== "__main__":
    main()
