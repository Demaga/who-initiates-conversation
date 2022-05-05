import json
import pandas as pd
import plotly.express as px

f = open("result.json")
data = json.load(f)

data = data["messages"]
# print(data)

df = pd.DataFrame.from_records(data)
print(df.head)

for col in df.columns:
    print(col)

df["date"] = df["date"].transform(lambda x: x.split('T')[0])

print(df.head)

df = df.groupby('date').first()

print(df.head)

df = df.groupby("from").count()
df = df.reset_index()
print(df)

fig = px.pie(df, values='id', names='from', title='Первое сообщение за день')
fig.show()