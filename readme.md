![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# FINAL PROJECT - CRITEO HR ANALYTICS


## SUMMARY 

- [x] Business Problem 
- [x] Data collection
- [x] Data cleaning
- [x] Data map 
- [x] Insights
- [x] Presentation 

### 1. Business problem
 
__*Criteo, What do they do ?*__  
 Criteo is a Tech company who provides personalised retargeting that works with Internet retailers to serve online display advertisements to consumers. 

__*Aim of this case*__  
 Understand the reasons that push Criteo's employees to leave the company:
- Their profile (educational background, age range etc.)
- Their current job responsibility level
- Who today is more at risk to leave ?
 
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

## 4. Data map

Please check excel file.
