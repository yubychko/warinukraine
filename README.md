# Analysis of Russia's Invasion of Ukraine
## Summary
This project examines political violence in Ukraine from 2018 to the present day and focuses on civilian targeting during Russia’s full-scale invasion starting in 2022. The analysis shows that Russia’s civilian targeting increases in the areas tthey lose in the battle. The regions with only remote violence  experience higher percentages of civilian targeting than the ones engaged in the battles. The project concludes that Russia delibertely targets civilians in Ukraine. 
## Input Data
There are two input files for this project. The data for the project was taken from The Armed Conflict Location & Event Data (ACLED’s) Ukraine Conflict Monitor that provides near real-time data on the war (https://acleddata.com/ukraine-conflict-monitor/#data). 
The dataset **“Ukraine_Black_Sea_2020_2023_Mar24.xlsx”** includes information of event types from 2018 to present day in Ukraine and near Black Sea. 
This project is based on a dataset downloaded on March 24, 2023. 
The second input file is a shapefile of Ukraine **“stanford-gg870xt4706-shapefile.zip”** taken from the University of Texas at Austin and is used to create maps (https://geodata.lib.utexas.edu/catalog/stanford-gg870xt4706). 
## Outputs
1.	Three scripts that should be run in the following order:
  - The first script, called **ukraine_fulldata.py** that reads data from the first input file (“Ukraine_Black_Sea_2020_2023_Mar24.xlsx”). The script cleans the data to include only events related to political violence in Ukraine, without riots, and filters the data to include events occurring on or after February 24, 2022. The script then saves the cleaned data to a CSV file and creates several visualizations, including a time series graph showing political violence over the years in the most affected regions, a time series graph showing political violence for months, and a stacked bar graph of event types during the full-scale war in Ukraine.

  - The second script, called **most_affected_area.py** reads a cleaned CSV file *'political_violence_ukraine.csv'*, selects data for the period of war in Ukraine, reads a shapefile of Ukraine. 
The script then merges standardized region names onto the shapefile, creates a data frame to count the number of attacks and civilian targeting in each region during the war, and merges this information onto the shapefile. Finally, the script generates three maps: the first map shows the number of attacks in each region, the second map shows the number of attacks using a log-10 scale, and the third map shows the number of attacks targeting civilians in each region.

  - The third script, called **civilian_percents.py** reads a CSV file *'political_violence_ukraine.csv'* and a shapefile of Ukraine's administrative boundaries, calculates, and visualizes the percentage of attacks targeting civilians. 
The script defines a function that calculates the percentage of civilian targeting for each region, and the results are merged with the shapefile. 
Then, it creates a new data frame that that contains the percentage of civilian targeting for each administrative region. 
The resulting map shows the percentage of civilian targeting for each region, with a gray region indicating missing data.

2.	Two CSV files: political_violence.csv and region_names.csv. 
  - **political_violence.csv** is a cleaned version of the input file that include only events related to political violence in Ukraine, without riots. 
  - **region_names.csv** is a list of standardized names of regions in Ukraine that will be used to graph maps. 

## Results
