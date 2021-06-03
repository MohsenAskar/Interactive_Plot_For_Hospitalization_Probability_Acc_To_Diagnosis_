# aim is to make interactive plots which can both used locally and in html 
import pandas as pd
import numpy as np
import plotly.express as px
import openpyxl # to read .xlsx files
data = pd.read_excel(r'C:\Users\mas082\OneDrive - UiT Office 365\Desktop\VS_Code\Real_Data_NPR\Book2.xlsx', engine='openpyxl')

data.head()
# data["color"] = data["color"].astype(str) # use this if you have a numeric variable and want to categorise it
fig = px.scatter(data, x="hovedtilstand", y="Probability for hospitalization if you have this diagnosis", size="Probability for hospitalization if you have this diagnosis", color="color"
                 , size_max=10) #use hover_name="ICD names" when you attach ICD names to ICD codes
fig.show()

