![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# FINAL PROJECT - CRITEO HR ANALYTICS

## What you can find in this repository 
* __Code__ : different sets of code 
 * Part 1 of cleaning (essentially reducing the number of columns)
 * The whole encoding part 
 * Supervised machine learning implementation 
* __Datasets__ : Data sets for employees (current) and former employees
 * initial_datasets to find very first csv files that were scrapped
 * csv files with data at different stages (cleaned but not encoded, encoded, with prediction) 
 * the Data map with explanation of all data types and encoding choices
* __Graphs_screenshots__ : pictures loaded from jupyter to be implemented in Spyder for the streamlit
* __criteo_st__ : the whole streamlit code (presentation with graphs)


## SUMMARY 

- [x] Business Problem 
- [x] Data collection
- [x] Data cleaning
- [x] Data map 
- [x] Insights
- [x] Presentation 

### 1. Business problem
 
__*Criteo, What do they do ?*__  
Criteo is a Tech company who provides personalised retargeting to Internet retailers to serve online display advertisements to consumers.

__*Aim of this case*__  
Prediction of which employees are at risk of quitting/leaving from Criteo.
 
### 2. Data collection 
 
**Data source** : LinkedIn  
**Data collection method** : webscrapping thanks to Phantombuster.

In order to be able to do a comparison and anticipate future departures from Criteo France, it is required to have:
- Profiles from people currently working at Criteo France
- Profiles from people who have indicated Criteo as their former employer

**What has been scrapped**  
- 200 profiles of current employees
- 200 profiles of former employees
   * 60 employees whose last employer was Criteo
   * 140 employees who have worked for Criteo longer ago

 ### 3. Data cleaning 

1. Concatenate the different datasets 
2. Drop useless columns to keep only relevant information (Scrapper provides 60 different columns of information)
3. Group some of the categorical data to make them usable (ie: Schools or hierarchy level)
4. Encode categorical data

### 4. Data map

Please check excel file.
