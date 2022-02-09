# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:28:49 2022

@author: Sarah
"""

import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px


st.sidebar.image(r"/Users/Sarah/Pictures/criteo-map.jpg")


st.title('Criteo employees departure analysis')

st.header('Current employees')
emp = pd.read_csv(r"C:\Users\Sarah\Documents\Final_project_HR_Analytics\Datasets\emp_with_pred.csv")
emp.drop(['Unnamed: 0.1'],axis=1, inplace=True)

emp.hierarchy_level = np.where((emp.hierarchy_level=='Vice'),
                              'VP', emp.hierarchy_level)
emp.hierarchy_level = np.where((emp.hierarchy_level=='Stagiaire')|(emp.hierarchy_level=='Internship'),
                              'Intern', emp.hierarchy_level)
emp.drop(['Unnamed: 0'], axis=1,inplace=True)

hierarch = emp.groupby('hierarchy_level',as_index=False)['job_field'].count()
hierarch.sort_values(by='job_field', ascending=False, inplace=True)

## MULTISELECT - HIERARCHICAL LEVEL 
x_axis = st.multiselect(label='Chose hierarchical level here', options=hierarch.hierarchy_level.tolist(), default=['Employee','Manager','Intern','Lead','Director','Senior','Head'])

## BAR CHART 1
if x_axis:
    for element in x_axis:
        hierarch2 = hierarch[hierarch['hierarchy_level'].isin (x_axis)]

    fig = go.Figure(
        data=[go.Bar(x=hierarch2['hierarchy_level'],y=hierarch2.job_field, text=hierarch2['job_field'],
            textposition='auto')],
        layout_title_text="Frequency distribution of hierarchical level",
        
    )
    fig

## SLIDER SELECT - YEARS OT JOB
start_year, end_year = st.select_slider(
 'Select a range of years',
 options=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
 value=(3,10))
st.write('You selected years at Criteo between', start_year, 'and', end_year)


    
years = emp.groupby('years_at_job',as_index=False)['job_field'].count()
years.sort_values(by='years_at_job', ascending=False, inplace=True)

years2 = years[(years.years_at_job >= start_year) & (years.years_at_job <= end_year)]

## BAR CHART 2
fig2 = go.Figure(
    data=[go.Bar(x=years2.years_at_job, y=years2.job_field, text=hierarch2['job_field'],
        textposition='auto')],
    layout_title_text="Frequency distribution of number of years in current job",
    
)
fig2

## PIE CHART - YEAR AT CURRENT JOB
emp['approx_work_xp']= np.where(emp['approx_work_xp']==-1, 0,emp['approx_work_xp'])
xp = emp.groupby('approx_work_xp', as_index=False)['job_field'].count()

fig3 = px.pie(xp, values='job_field', names='approx_work_xp', title='Number of years of experience')
fig3

## ML PART STARTS HERE
st.header('Machine learning model')
st.subheader('Features selection')

features = emp[['hierarchy_level', 'years_at_job', 'company2', 'hierarchy_level2',
       'approx_work_xp']].head(5)
features

st.subheader('Decision Tree Classifier')
col1, col2 , col3 = st.columns(3)
with col1:
    st.text('Decision tree with \nmax_depth 3 ')
    st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs/decision_tree.png")
with col2:
    st.text('Confusion matrix')
    st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs/dt_confusion_matrix.png")
with col3:
    st.text('Roc-Auc')
    st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs/dt_roc_auc.png")