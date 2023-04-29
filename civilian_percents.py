#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:38:41 2023

@author: yuliabychkovska
"""

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Reading needed files and selecting needed data
political_violence = pd.read_csv('political_violence_ukraine.csv')
political_violence = political_violence.query("War==True")

ukraine_map = gpd.read_file('ukraine_map_std.shp')

plt.rcParams['figure.dpi'] = 300

#%% Counting civilian targeting 
civilian = political_violence['CIVILIAN_TARGETING'].value_counts(dropna=False)
print(civilian)

#%% Defining a function for calculating civilian targeting percentage 
def calc_percent_civ_targeting(df):
    # Count the number of instances where the 'CIVILIAN_TARGETING' column value is 'Civilian targeting' in the input dataframe, 
    #and extract the result for the 'Civilian targeting' value
    civilian_targeting = df['CIVILIAN_TARGETING'].value_counts(dropna=False)['Civilian targeting']
    
    # Get the total number of instances in the 'CIVILIAN_TARGETING' column of the input dataframe
    total = len(df['CIVILIAN_TARGETING'])
    
    # Calculate the percentage of instances where the 'CIVILIAN_TARGETING' column value is 'Civilian targeting' 
    # by dividing the number of 'Civilian targeting' instances by the total number of instances and multiplying by 100
    percent_civ = (civilian_targeting/total*100).round(2)
    
    # Return the percentage of civilian targeting
    return percent_civ

#%% Calculating overall civilian targeting percentage 
percent_civ_all = calc_percent_civ_targeting(political_violence)

print("Percentage of Civilian Targeting in all data: ", percent_civ_all)

#%% Selecting the most affected regions
affected_regions = political_violence.query("ADMIN1=='Kyiv' or ADMIN1=='Kharkiv' or ADMIN1=='Zaporizhia' or ADMIN1=='Kherson' or ADMIN1=='Donetsk'")

#%% Calculating civilian targeting percentage in the most affected regions
# Use the `calc_percent_civ_targeting` function to calculate the percentage of civilian targeting in the most affected regions
percent_civ_affect = calc_percent_civ_targeting(affected_regions)

print("Percentage of Civilian Targeting in the most affected regions: ", percent_civ_affect)

#%% Defining a function to calculate percentages for every region

def calc_percent_civ_targeting(data, admin1_col='ADMIN1', targeting_col='CIVILIAN_TARGETING'):
    #Calculates the percentage of attacks that targeted civilians in each region
 
    # Fill missing values with "Not reported"
    data[targeting_col] = data[targeting_col].fillna('Not reported')
    
    # Group the data by administrative region and targeting column, and count the number of attacks
    counts = data.groupby([admin1_col, targeting_col]).size().reset_index(name='count')
    
    # Pivot the data to put the targeting column values in separate columns
    pivoted = counts.pivot(index=admin1_col, columns=targeting_col, values='count').reset_index()
    
    # Calculate the percentage of attacks that targeted civilians
    pivoted['total'] = pivoted['Civilian targeting'] + pivoted['Not reported']
    pivoted['percent_civ_targeting'] = ((pivoted['Civilian targeting'] / pivoted['total']) * 100).round(2)
    
    # Return the result - a dataframe ontaining the percentage of attacks that targeted civilians in each region
    return pivoted[[admin1_col, 'percent_civ_targeting']]


#%%

# Calculate the percentage of attacks that targeted civilians in each region
civ_targeting_by_region = calc_percent_civ_targeting(political_violence)

print(civ_targeting_by_region)


#%% To check the function above, calculating Kherson's percentage of civilian targeting 

# Filter the political_violence dataframe to only include rows where ADMIN1 is 'Kherson'
kherson = political_violence.query("ADMIN1=='Kherson'")

# Use the `calc_percent_civ_targeting` function to calculate the percentage of civilian targeting in Kherson
percent_kherson = calc_percent_civ_targeting(kherson)
print("Percentage of Civilian Targeting in Kherson: ", percent_kherson)

#%% Luhansk's percentage of civilian targeting (expecting a lower percent because occupied)
luhansk = political_violence.query("ADMIN1=='Luhansk'")

percent_luhansk = calc_percent_civ_targeting(luhansk)
print("Percentage of Civilian Targeting in Luhansk: ", percent_luhansk)

#%% Including a blank region on a map (that does not have a percentage)

# Add a row for the blank region
civ_targeting_by_region.loc[-1] = [0, 'Blank Region']
civ_targeting_by_region.index = civ_targeting_by_region.index + 1
civ_targeting_by_region = civ_targeting_by_region.sort_index()

# Merge the percentage data with the shapefile based on the administrative boundary
merged_data = ukraine_map.merge(civ_targeting_by_region, left_on='std_name', right_on='ADMIN1')

# Fill NaN values with 0
merged_data['percent_civ_targeting'] = merged_data['percent_civ_targeting'].fillna(0)

# Set a different color for the blank region
missing_kwds = {'color': 'gray'}


#%% Plot percentage of civilian targeting on a map

fig, ax = plt.subplots()
merged_data.plot(column='percent_civ_targeting', ax=ax, legend=True, cmap='Reds',edgecolor='black', linewidth=0.25)
ax.axis('off')
fig.suptitle('Percentage of Civilian Targeting by Region')
fig.tight_layout()
fig.savefig('civilian_targeting_percentage.png')






