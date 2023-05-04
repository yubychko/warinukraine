# Analysis of Russia's Invasion of Ukraine
## Summary
This project examines political violence in Ukraine from 2018 to the present day and focuses on civilian targeting during Russia’s full-scale invasion starting in 2022. The analysis shows that Russia’s civilian targeting increases in the areas tthey lose in the battle. The regions with only remote violence  experience higher percentages of civilian targeting than the ones engaged in the battles. The project concludes that Russia delibertely targets civilians in Ukraine. 
## Input Data
There are two input files for this project. The data for the project was taken from [The Armed Conflict Location & Event Data (ACLED’s) Ukraine Conflict Monitor](https://acleddata.com/ukraine-conflict-monitor/#data) that provides near real-time data on the war. 
The dataset **“Ukraine_Black_Sea_2020_2023_Mar24.xlsx”** includes information of event types from 2018 to March 24, 2023 in Ukraine and near Black Sea. 
The second input file is a [shapefile of Ukraine](https://geodata.lib.utexas.edu/catalog/stanford-gg870xt4706) **“stanford-gg870xt4706-shapefile.zip”** taken from the University of Texas at Austin and is used to create maps. 
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

The **time series graph** shows the number of political violence events in the most affected regions from 2018 to the present day by months.
Russia invaded east and south of Ukraine in 2014 which is represented by political violence in Donetsk and Luhansk prior to the full-scale invasion.
The graph shows a rapid increase in political violence with full-scale invasion.
![Violence timeseries months](https://github.com/yubychko/warinukraine/blob/images/violence_timeseries_months.png)

The **event-type bar graph** shows three political violence events which include Violence against civilians, Explosions and Remote violence, and Battles during full-scale war (starting in 2022). 
The bar graph helps to see that while violence against civilians is a low number, Explosions and Remote violence is often targeted at civilians. 
This graph also shows that Explosions and Remote violence are the biggest share of violence by Russia.
![Event type bar graph](https://github.com/yubychko/warinukraine/blob/images/event_types_bar_graph.png)

The **Most Affected Areas: Log 10 map** shows political violence in each region. Each region is colored based on the log10 of the number of political violence incidents that occurred in that region. 
The darker the color of a region, the higher the number of incidents. 
By using the log-10 transformation, the map shows the magnitude of variation between regions with very high and very low numbers of incidents. 
This allows for a more accurate visual representation of the data and makes it easier to identify which regions have the highest levels of political violence incidents.
![Log-10 map](https://github.com/yubychko/warinukraine/blob/images/log10_of_attacks.png)

To conduct more in-depth analysis, the project focused on **civilian targeting**. 
The hypothesis was that civilian targeting increases when Russians fail on the battlefield. 
The hypothesis proved to be true because the number of civilian targeting attacks is higher in the regions that Russians have lost control over than in those they occupy. 
The **Civilian Targeting: Number of Attacks map** shows the number of civilian targeting attacks by region. 
![Number of attacks map](https://github.com/yubychko/warinukraine/blob/images/civilian_targeting.png)

The **Civilian Targeting: Percentage by Region map** shows percentages of civilian targeting by region during the full-scale war.
When calculating civilian targeting precents, the percent of civilian targeting in the whole territory of Ukraine is 6.64 % of all attacks. 
When looking at civilian targeting in a currently occupied region – Luhansk, it decreases to 3.27%. 
In Kherson, the region that Ukrainian Armed Forces liberated in the fall 2022 counteroffensive, the civilian targeting percent reaches 11.45% out of all attacks. 
Moreover, the regions with remote violence only (west) have higher percentage of civilian targeting overall. 
In the regions that do not have active battles, Russia targets civilians more often. 
Kyiv, the region of the capital has almost 64% of civilian targeting, meaning Russians deliberately target civilians.
![Percentage by region map](https://github.com/yubychko/warinukraine/blob/images/civilian_targeting_percentage.png)

In conclusion, this research shows that Russia deliberately targets civilians in its ulawful war in Ukraine. Civilian targeting increases when Russian forces fail on the battlefield. Russia targets civilians in non-combat regions at a disproportionately high rate, as showed by the percentage of such attacks that are directed towards civilian targets.


