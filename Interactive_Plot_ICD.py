# aim is to make interactive plots which can both used locally and in html 
import pandas as pd
import numpy as np
import plotly.express as px
import openpyxl # to read .xlsx files
data = pd.read_excel(r'C:\Users\mas082\OneDrive - UiT Office 365\Desktop\VS_Code\Real_Data_NPR\Book2.xlsx', engine='openpyxl')

data.head()
# data["color"] = data["color"].astype(str) # use this if you have a numeric variable and want to categorize it
fig = px.scatter(data, x="hovedtilstand", y="Prob. for hosp.", size="Prob. for hosp.", color="color"
                 , size_max=10, title="Probability of staying in a hospital more than 1 day according to diagnosis", hover_name="ICD category") #use hover_name="ICD names" when you attach ICD names to ICD codes
fig.update_layout(template='plotly_white') # or plotly_dark
fig.show()

# create html plot 
import plotly.io as pio
pio.write_html(fig, file='index.html', auto_open=True) #ok

# upload to github repository

