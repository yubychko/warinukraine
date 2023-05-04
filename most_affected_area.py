#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:04:38 2023

@author: yuliabychkovska
"""

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

political_violence = pd.read_csv('political_violence_ukraine.csv')
# will read cleaned csv
plt.rcParams['figure.dpi'] = 300 #setting dpi for higher quality 

#%% selecting dates of the war
war = political_violence.query("War==True")

#%%
ukraine_map = gpd.read_file('stanford-gg870xt4706-shapefile.zip')

for col in ukraine_map.columns:
    print(col)

print(ukraine_map['name_1'])

#%% Opening a CSV file with standardized regions
region_names = pd.read_csv('region_names.csv')

#%% Merging original names with standard names
ukraine_map = ukraine_map.merge(region_names, on='name_1', how = 'outer', validate='1:1')

#%% Creating a DataFrame to count attacks by region and civilian targeting
attacks = pd.DataFrame()
# Group the war dataframe by region
groupped = war.groupby('ADMIN1')
# Count the total number of attacks in each region
attacks['count'] = groupped.size()
# Count the number of attacks that targeted civilians in each region
attacks['civilian_targeting'] = groupped['CIVILIAN_TARGETING'].count()

#%% Merging war information onto ukraine map
ukraine_map = ukraine_map.merge(attacks, left_on='std_name', right_on='ADMIN1', how='left', validate='1:1')

#%% Saving a new merged map
ukraine_map.to_file('ukraine_map_std.shp')

#%% Making a map that reflects the most affected areas based on number of attacks
# Absolute counts - there is a very big difference between the regions abd the result is not very visible - intermediary map
fig,ax = plt.subplots()
ukraine_map.plot('count', ax=ax, legend=True, cmap='Reds',edgecolor='black', linewidth=0.25)
ax.axis('off')
fig.suptitle('Most Affected Areas: Number of Attacks')
fig.tight_layout()
fig.savefig('number_of_attacks.png')

#%% Making a map that reflects the most affected areas using log scale - powers of 10
from math import log10
# Take the log base 10 of the count column
ukraine_map['log_count'] = ukraine_map['count'].apply(log10)
# Plot the log counts with a color map and legend
fig,ax = plt.subplots()
ukraine_map.plot('log_count', ax=ax, legend=True, cmap='YlOrRd',edgecolor='black', linewidth=0.25)
ax.axis('off')
fig.suptitle('Most Affected Areas: Log 10')
fig.tight_layout()
fig.savefig('log10_of_attacks.png')

# Each region is colored based on the log10 of the number of political violence incidents that occurred in that region. 
# The darker the color of a region, the higher the number of incidents.
# The log10 transformation is used to better visualize the differences in magnitude between the regions, 
# as the number of incidents can vary greatly between regions. 

#%% Makinng a map of civilian targetting based on number of attacks
fig,ax = plt.subplots()
ukraine_map.plot('civilian_targeting', ax=ax, legend=True, cmap='Reds',edgecolor='black', linewidth=0.25)
ax.axis('off')
fig.suptitle('Civilian Targeting: Number of Attacks')
fig.tight_layout()
fig.savefig('civilian_targeting.png')

#Shows that civilian targetting increases when Russia's not successful on the battlefield



