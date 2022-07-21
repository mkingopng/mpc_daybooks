"""
basic visualisation in web browser
"""
import plotly.express as px
import pandas as pd
from variables import *

# read the csv
df = pd.read_csv(f'{MONTH}.csv')

# fix date format
df['TRANSDAT'] = pd.to_datetime(df['TRANSDAT'], dayfirst=True)

# filter by cc
filtered_df = df.loc[df['CC'] == CC]

# plot
fig = px.scatter(filtered_df,
                 x='TRANSDAT',
                 y='AMOUNT',
                 title=f'Transaction Summary for CC {CC}, {MONTH}',
                 hover_data=['TRANSDAT', 'WO-NO', 'AMOUNT'])
fig.show()


# TODO: #1 use openpyxl and xlwings to improve the excel export to include:
#  - the cleaned data on one page,
#  - the pivot on another sheet
#  - scatter plot on 3rd sheet
#  - export to excel. cleaned data to sheet 'data', pivoted data to 'pivot', plot to 'plot'

# TODO #2: write data to mariadb so that there is a single data source with ALL data
#  - query the data

# TODO: #3:
#  - convert visualisation to dashboard with
#  - selector for cc
#  - slider for start and end date

