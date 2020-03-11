#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

from bubbly.bubbly import bubbleplot
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot

import plotly.graph_objs as go


# In[ ]:


data = pd.read_csv("europe.csv")
data.info()


# In[ ]:


life_data = {"country":data.country,"prct_yng_adt_pop":data.prct_yng_adt_pop, "good_health":data.good_health, "median_income":data.median_income, "avg_hrs_worked":data.avg_hrs_worked, "avg_temp":data.avg_temp, "prct_low_savings":data.prct_low_savings, "prct_rpt_crime":data.prct_rpt_crime, "prct_life_satis_high":data.prct_life_satis_high}
life = pd.DataFrame(data=life_data)
life


# In[ ]:


final_df = life.sort_values(by=['prct_rpt_crime'], ascending=True)
final_df


# In[ ]:


# l = data.loc[data['country'] == 'Spain']
# l
lst = []
# l = data.loc[data['country'] == 'Germany']
for index, rows in data.iterrows():
    my_lst = [rows.prct_yng_adt_pop, rows.good_health, rows.median_income, rows.avg_hrs_worked, rows.avg_temp, rows.prct_low_savings, rows.prct_rpt_crime, rows.prct_life_satis_high]
    lst.append(my_lst)
lst


# In[ ]:


cty = []
for i in range(32):
    cty.append(data.country[i])
# print(cty)


# In[ ]:


categories = ['Young Population', 'Health', 'Median Income', 'Hours worked', 'Avg temp', 'Low savings', 'Crime', 'Life Satisfaction']

fig = go.Figure()
for i in range(32):    
    fig.add_trace(go.Scatterpolar(
          r=lst[i],
          theta=categories,
          fill='none',
          name=cty[i]
    ))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 100]
    )),
  showlegend=True
)

fig.show()

