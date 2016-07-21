import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime


def loadHistoricalChart(data):
    
    title = 'Stock Prices'
    colors = 'rgba(67,67,67,1)'
    mode_size = 12
    line_size = 3
       
    dataSet = data.get("results")
    x_data = []
    y_data = []

    for i in dataSet:
        for key, value in i.items():
            if key == "tradingDay":
                date = datetime(year = int(value[0:4]), month = int(value[5:7]), day = int(value[8:10]))
                x_data.append(date)
            elif key == "close":
                y_data.append(value)
    
    trace = [go.Scatter(
            x=x_data,
            y=y_data,
            name = title,
            connectgaps=True,
    )]

    fig = go.Figure(data=trace)

    py.image.save_as(fig, 'historicalPrice.png')
