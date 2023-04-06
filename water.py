import pandas as pd

df = pd.read_excel('assets/water.xlsx')

#percentage of usable or deployable capacity in the Lower Lee Group and Lower Thames Group reservoirs
lower_lee_index = df['Lower Lee Group'].mean()/10
lower_thames_index = df['Lower Thames Group'].mean()/10