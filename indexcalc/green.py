import pandas as pd

df = pd.read_excel('assets/green_space.xlsx')

#percentage of greeneries within 1000m radius
greenery_index = df['Average combined size of  Parks, Public Gardens, or Playing Fields within 1,000 m radius (m2)'].mean()/100000