#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

from bubbly.bubbly import bubbleplot
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot

import plotly.graph_objs as go

import Clean as cl
data = pd.read_csv("europe.csv")


# Following are the codes for various bubbleplot generated using iplot
# The only thing changing is the column names and their values.
figure = bubbleplot(dataset = data, x_column='gdp', y_column='prct_job_satis_high',
    bubble_column='country', size_column='total_pop', color_column='country',
    x_title="GDP", y_title="Job Satisfaction", title='GDP vs Job vs Population',
    x_logscale=True, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='prct_life_satis_high', y_column='prct_env_satis_high',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Life Satisfaction", y_title="Environment Satisfaction", title='Life S vs Env S vs GDP',
    x_logscale=True, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='prct_life_satis_high', y_column='prct_job_satis_high',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Life Satisfaction", y_title="Job Satisfaction", title='Life S vs Job S vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='prct_env_satis_high', y_column='prct_job_satis_high',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Environment Satisfaction", y_title="Job Satisfaction", title='Env S vs Job S vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='political_trust_rating', y_column='legal_trust_rating',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Political trust rating", y_title="Legal trust rating", title='GDP vs Politics vs Legal',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='prct_leisure_satis_high', y_column='prct_job_satis_high',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Leisure Satisfaction", y_title="Job Satisfaction", title='Leisure S vs Job S vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='median_income', y_column='life_expect',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Median Income", y_title="Life Expectancy", title='Median Inc vs Life Exp vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='police_trust_rating', y_column='legal_trust_rating',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Police Trust", y_title="Legal Trust", title='Police trust vs Legal trust vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='hard_budget', y_column='prct_low_savings',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Hard Budget", y_title="Low Savings", title='Hard budget vs Low savings vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='prct_leisure_satis_high', y_column='avg_hrs_worked',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Leisure Satisfaction", y_title="Avg Hours worked", title='Leisure S vs Work hours vs Population',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='unemp_rate', y_column='hard_budget',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Unemployment Rate", y_title="Hard Budget", title='Unemploy rate vs Hard budget vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='police_trust_rating', y_column='Political_trust_rating',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Police Trust", y_title="Political Trust", title='Police trust vs Political trust vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='gdp', y_column='prct_rpt_crime',
    bubble_column='country', size_column='total_pop', color_column='country',
    x_title="GDP", y_title="Reported Crime", title='GDP vs Reported Crime vs Population',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='gdp', y_column='avg_hrs_worked',
    bubble_column='country', size_column='total_pop', color_column='country',
    x_title="GDP", y_title="Avg work hours", title='GDP vs Work hours vs Population',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

figure = bubbleplot(dataset = data, x_column='prct_leisure_satis_high', y_column='median_income',
    bubble_column='country', size_column='gdp', color_column='country',
    x_title="Leisure Satisfaction", y_title="Median Income", title='Leisure Satisfaction vs Median Income vs GDP',
    x_logscale=False, scale_bubble=3, height=650)
iplot(figure)

# Creating a list of columns used for Radar plots
lst = []

for index, rows in data.iterrows():
    my_lst = [rows.prct_yng_adt_pop, rows.good_health, rows.median_income, rows.avg_hrs_worked, rows.avg_temp, rows.prct_low_savings, rows.prct_rpt_crime, rows.prct_life_satis_high]
    lst.append(my_lst)

# List of countries
cty = []
for i in range(32):
    cty.append(data.country[i])
# print(cty)
# Generating Radar plot using plotly on the following categories
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

    # Code for generating Geographically colored map of europe based on given column values
trace = [go.Choropleth(
               colorscale = 'YlOrRd',
               locationmode = 'country names',
               locations = data['country'],
               text = data['country'],
               z = data['avg_temp'],
               )]
layout = go.Layout(title = 'Avg Temperature in European Countries',
                geo = go.layout.Geo(
                       scope = 'europe',
                       showcountries = True,))
fig = go.Figure(data = trace, layout = layout)
iplot(fig)
