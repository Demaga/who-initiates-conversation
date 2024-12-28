import json
import pandas as pd
import plotly.express as px

f = open("result.json")
data = json.load(f)

data = data["messages"]

df = pd.DataFrame.from_records(data)
df["date"] = df["date"].transform(lambda x: x.split('T')[0])

df = df.groupby('date').first()
df = df.groupby("from").count()
df = df.reset_index()

fig = px.pie(df, values='id', names='from', title='First to message')
fig.show()
