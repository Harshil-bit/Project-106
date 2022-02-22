import plotly.express as px
import csv
import numpy as np

def setup():
    data_path="py/cupsofcoffeevshoursofsleep.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

def getDataSource(data_path):
    coffee_in_ml=[]
    hours=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            hours.append(float(row["hours of sleep"]))
    return {"x":coffee_in_ml,"y":hours}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between coffee and hours of sleep ",correlation[0,1])