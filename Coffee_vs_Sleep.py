import plotly.express as px
import csv
with open('cupsofcoffeevshoursofsleep.csv') as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()
