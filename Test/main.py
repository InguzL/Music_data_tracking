# import streamlit as st
import requests
import plotly.express as px
import pandas as pd


df = pd.read_csv("/Users/Jakemanns/Documents/Terraform_project_files/Music_data_tracking/Test/gig_import_sheet.csv")

df['merch_income'].replace(" ", "")
df['tickets_income'].replace(" ", "")

df = df.astype({'merch_income':'float', 'tickets_income':'float', 'expenses':'float', 'venue_rating':'float', 'audience_rating':'float'})
df.info(verbose=True)
df[['latitude','longitude']] = df['venue_latitude, venue_longitude'].str.split(', ', expand=True)
df = df.astype({'latitude':'float', 'longitude':'float'})
df['net_income'] = df['merch_income'] + df['tickets_income']
df['profit_percentage'] = (df['net_income'] - df['expenses']) / df['expenses'] * 100
df['overall_rating'] = df[['venue_rating', 'audience_rating']].mean(axis=1)

# df = px.data.[imported from dynamodb]
print(df)
fig = px.scatter_mapbox(df,
                        lon = df['longitude'],
                        lat = df['latitude'],
                        zoom = 10,
                        color = df['overall_rating'],
                        size = df['profit_percentage'],
                        width = 1920,
                        height = 1020,
                        title = 'Venue map'
                        )

fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={'r':0,
                          't':50,
                          'l':0,
                          'b':10})

fig.show()



# response = requests.get(url="")