import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import os


def helpfile():
    DIR = os.path.dirname(os.path.abspath(__file__))
    f = open(DIR + '/plot_help.txt', mode='r')
    print(f.read())
    return


# Desired functions:
# DF to line/scatter
# DF to multiple line/scatter in 1 plot
# DF to multiple line/scatter plots
# ...

def df_col_plot(df=None, x_name=None, y_name=None, help=False):
    if help:
        print('Plots two df columns. Arguments: df, x_name (df.index for index), y_name')
        return

    fig = px.scatter(df, x_name, y_name)
    return fig

def df_3d_plot(
        df=None,
        x_name= 'X',
        y_name= 'Y',
        z_name = 'Z',
        title = 'Title',
        size = None,
        margins = None,
        help=False):

    if help:
        print('3D surface. x-axis is df.index. y-axis is df.columns. Arguments: df, x_label, \
        y_label, z_label, title, size (width, height tuple), margins (l,r,b,t tuple)')
        return

    z = df.values
    fig = go.Figure(data=[go.Surface(z=z)])

    fig.update_scenes(xaxis_title_text = x_name,
                      yaxis_title_text = y_name,
                      zaxis_title_text = z_name)
    fig.update_layout(title = title)

    if size != None:
        width, height = size
        fig.update_layout(autosize=False, width=width, height=height)
    if margins != None:
        l, r, b, t = margins
        fig.update_layout(autosize=False, margin=dict(l=l, r=r, b=b, t=t))

    return fig
