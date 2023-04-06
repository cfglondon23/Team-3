import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_excel('assets/traffic.xlsx')
df = df.rename({'Unnamed: 0': 'date'}, axis=1)

pd.options.plotting.backend = "plotly"
df.plot(x='date', y=['Cars','Motorbikes', 'Buses', 'Trucks', 'Vans', 'Pedestrians & cyclists'])
df_melt = df.melt(id_vars='date', value_vars=['Cars','Motorbikes', 'Buses', 'Trucks', 'Vans', 'Pedestrians & cyclists'])
fig = px.line(df_melt, x='date' , y='value' , color='variable')
fig.update_xaxes(rangeslider_visible=True)

#change to html file
pyo.plot(fig, filename='traffic.html')
iframe_html = '<iframe src="https://your-website.com/traffic.html" width="600" height="400"></iframe>'

traffic_index = 5.63
