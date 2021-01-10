import pandas as pd;
import plotly.express as px;

dataframe = pd.read_csv("coviddata.csv")
visualize_data = px.scatter(dataframe,x="date",y="cases",size="cases",color="country",size_max=20)
visualize_data.show()