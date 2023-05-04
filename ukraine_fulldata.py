#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:08:40 2023

@author: yuliabychkovska
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw_ukraine = pd.read_excel('Ukraine_Black_Sea_2020_2023_Mar24.xlsx')
plt.rcParams['figure.dpi'] = 300

#%% Keeping only Ukraine in the dataset
raw_ukraine = raw_ukraine[raw_ukraine['COUNTRY'] == 'Ukraine']

print(raw_ukraine['DISORDER_TYPE'].value_counts())

#%% Creating a subset of data of political violence without riots for all years (2018-2023) to be used as denominator
political_violence = raw_ukraine.query('DISORDER_TYPE=="Political violence"')
political_violence = political_violence.query('EVENT_TYPE!="Riots"')

print(political_violence['EVENT_TYPE'].value_counts())

#%% Creating series and dataframe for full-scale war
from datetime import datetime

# Filter political_violence dataframe to only include events on or after February 24, 2022
war = political_violence['EVENT_DATE'] >= datetime(2022,4,24)

# Add war column to the dataframe 
political_violence['War'] = war #adding war column to the dataframe 

#%% Saving the cleaned data to csv
political_violence.to_csv('political_violence_ukraine.csv')

#%% Creating data frame for affected regions
regions = political_violence.query("ADMIN1=='Kyiv' or ADMIN1=='Kharkiv' or ADMIN1=='Zaporizhia' or ADMIN1=='Kherson' or ADMIN1=='Luhansk' or ADMIN1=='Donetsk'")
print(regions['EVENT_TYPE'].value_counts())

#%% Creating a time series graph to show political violence over the years in the most affected regions - intermediary graph

# Count the number of attacks by year and administrative region
size_violence = regions.groupby(['YEAR','ADMIN1']).size()
# Reset the index and rename the count column
size_violence = size_violence.reset_index()
size_violence = size_violence.rename(columns={0:'count'})

# Plot a figure
fig, ax1 = plt.subplots() 
sns.lineplot(data=size_violence, x='YEAR', y='count', hue='ADMIN1', ax=ax1)
fig.tight_layout()
fig.savefig('violence_timeseries.png')

#%% Creating a data frame for political violence for months 

# Count records by date and location
event_violence = regions.groupby(['EVENT_DATE','ADMIN1']).size() 
# Convert the data from long to wide format, with one column per region, and fill in missing values with zeros
violence1 = event_violence.unstack().fillna(0) 
# Resample the data to group it by month, and produce a new dataframe with one record for the last day of each month
violence_m = violence1.resample('M').sum() 

#%% Creating a time series graph to show political violence for months 

# Create a new dataframe to show political violence count for each month
violence_months = violence_m.stack().reset_index()
# Rename the count column to 'count'
violence_months = violence_months.rename(columns={0:'count'})

#Plot a figure
fig, ax1 = plt.subplots() 
sns.lineplot(data=violence_months,x='EVENT_DATE',y='count',hue='ADMIN1')
fig.suptitle('Political Violence for Months')
fig.tight_layout()
fig.savefig('violence_timeseries_months.png')

#%% Selecting dates of the war
fullscale_war = political_violence.query("War==True") 

#%% Making stacked bar graph for event types that shows civilian targeting and other

# Filter the data to include the relevant columns with event types and civilian targeting
relevant_data = fullscale_war[['EVENT_TYPE', 'CIVILIAN_TARGETING']]

# Replace empty values in 'CIVILIAN_TARGETING' with 'Other'
relevant_data['CIVILIAN_TARGETING'].fillna(value='Other', inplace=True)

# Create a new column that maps "Civilian targeting" to True and everything else to False
relevant_data['Is Civilian Targeting'] = relevant_data['CIVILIAN_TARGETING'] == "Civilian targeting"

# Group the data by event type and target category and count the number of occurrences of each
grouped_data = relevant_data.groupby(['EVENT_TYPE', 'Is Civilian Targeting'])['Is Civilian Targeting'].count().unstack()

#%% Plotting the stacked bar graph
fig1, ax1 = plt.subplots()
grouped_data.plot.barh(ax=ax1, stacked=True)
ax1.set_xlabel("")
ax1.set_ylabel("")
fig1.suptitle("Event Types during the Full-Scale War in Ukraine")
ax1.legend(['Other', 'Civilian Targeting'])

# Add labels with numbers to each bar
for i, v in enumerate(grouped_data.sum(axis=1)):
  ax1.text(v + 0.1, i - 0.1, str(int(v)), color='black')

fig1.tight_layout()
fig1.savefig("event_types_bar_graph.png")





