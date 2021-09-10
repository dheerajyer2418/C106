import plotly.express as px
import csv

with open("Size-of-tv.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Size of TV", y = "Average time spent")
    fig.show()