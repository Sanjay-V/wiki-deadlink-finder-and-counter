import pandas as pd
df = pd.read_csv("output.csv")
count = df.groupby(['Link']).count() 
data = pd.DataFrame(count)
data =data.drop(columns=['status'])
data.rename(columns = {'url':'Dead Link Count'}, inplace = True) 
data.to_csv('Count.csv')
