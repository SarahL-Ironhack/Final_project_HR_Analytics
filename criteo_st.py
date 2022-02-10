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

st.sidebar.markdown("**Sarah Léouffre**")
st.sidebar.markdown("**Date**: February 11th, 2021")
st.sidebar.markdown("Paris | DAFT Nov2021")

st.sidebar.image(r"/Users/Sarah/Pictures/criteo-map.jpg")

st.sidebar.markdown('**Summary**')
st.sidebar.markdown('**1. About the data**')
st.sidebar.markdown('**2. Data processing and cleaning**')
st.sidebar.markdown('**3. Exploratory data analysis**')
st.sidebar.markdown('**4. Models implementation and choice**')
st.sidebar.markdown('**5. Main results**')

st.sidebar.image(r"/Users/Sarah/Pictures/ironhack_logo.png")




st.title('Criteo employees departure analysis')

st.header('Business problem')
business_pb = '<p style="font-family:sans-serif; color:Orange; font-size: 28px;"><b>Prediction of which employees are at risk of quitting/leaving from Criteo.</b></p>'
st.markdown(business_pb, unsafe_allow_html=True)
st.header('About Criteo')
about_criteo = '<p style="font-family:sans-serif; color:Orange; font-size: 28px;">Criteo is a Tech company who provides personalised retargeting to Internet retailers to serve online display advertisements to consumers.</p>'
st.markdown(about_criteo, unsafe_allow_html=True)


st.header('1. About the data')
expander1 = st.expander('Click here to see details!', expanded = False)
with expander1:
    col1, col2 = st.columns(2)
    with col1: 
        st.image(r"/Users/Sarah/Pictures/phantom_logo.png",use_column_width='auto')
    with col2:
        st.markdown('- The data was collected by scrapping **LinkedIn** profiles thanks to **PhantomBuster**')
        st.markdown('- Initially scrapped **220 profiles of current employees** + **231 profiles who marked Criteo as their former employer**')
        st.markdown('- Raw datasets included **60 columns** of various information (profileUrl, imageUrl, School, skills etc.)')
        st.markdown(' - All data imported as **object type**')
    st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs_screenshots/raw_columns.png")



## PART 2
st.header('2. Data processing and cleaning')
expander2 = st.expander('Click here to see details!', expanded = False)
with expander2:
    st.markdown('**Main issues**')
    st.markdown(' - All data was categorical and object type')
    st.markdown(' - Filter usefull and useless information among the 60 columns')
    st.markdown(' - Group categorical data (eg: School, Job title, company, job field )')
    st.markdown(' - Convert to integer type')
    st.markdown(' - Calculate approximate work experience')
    st.markdown(' - Finish by encoding the categorical data')
    st.markdown(' - Concat both current and former employees datasets for Machine Learning')
    st.markdown(' - Data was already balanced + no need to scale (exact same results)')



    st.image(r"/Users/Sarah/Pictures/data_clean.jpg",use_column_width='auto')

## PART 3
st.header('3. Exploratory data analysis')

st.subheader('Current employees dataset')

emp = pd.read_csv(r"C:\Users\Sarah\Documents\Final_project_HR_Analytics\Datasets\emp_with_pred.csv")
emp.drop(['Unnamed: 0.1'],axis=1, inplace=True)

emp.hierarchy_level = np.where((emp.hierarchy_level=='Vice'),
                              'VP', emp.hierarchy_level)
emp.hierarchy_level = np.where((emp.hierarchy_level=='Stagiaire')|(emp.hierarchy_level=='Internship'),
                              'Intern', emp.hierarchy_level)
emp.drop(['Unnamed: 0'], axis=1,inplace=True)

hierarch = emp.groupby('hierarchy_level',as_index=False)['job_field'].count()
hierarch.sort_values(by='job_field', ascending=False, inplace=True)


## BAR CHART 1

tree = emp.groupby(['hierarchy_level','job_field'], as_index=False).size()
tree['job_field'] = np.where(tree.job_field == ' ', 'unknown', tree.job_field)

fig = px.treemap(tree, path=[px.Constant("all employees"), 'hierarchy_level','job_field'], values='size',color_continuous_scale='RdBu')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
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
    data=[go.Bar(x=years2.years_at_job, y=years2.job_field, text=hierarch['job_field'],
                 marker_color=px.colors.sequential.Oranges,
        textposition='auto')],
    layout_title_text="Frequency distribution of number of years in current job",
    
)
fig2.update_layout(
xaxis_title="Number of years at current job",
yaxis_title="Number of employees")
fig2

## PIE CHART - YEAR AT CURRENT JOB
emp['approx_work_xp']= np.where(emp['approx_work_xp']==-1, 0,emp['approx_work_xp'])
xp = emp.groupby('approx_work_xp', as_index=False)['job_field'].count()

pie1 = px.pie(xp, values='job_field', names='approx_work_xp', title='Number of years of experience',
           color_discrete_sequence=px.colors.sequential.Oranges)
pie1

st.markdown("""---""")


## FORMER EMPLOYEES
st.subheader('Former employees dataset')
former = pd.read_csv(r"C:\Users\Sarah\Documents\Final_project_HR_Analytics\Datasets\former_not_encoded.csv")
former.drop(['Unnamed: 0'],axis=1,inplace=True)

hierarch_form = former.groupby('hierarchy_level',as_index=False)['job_field'].count()
hierarch_form.sort_values(by='job_field', ascending=False, inplace=True)

## MULTISELECT - HIERARCHICAL LEVEL 
x_axis2 = st.multiselect(label='Choose hierarchical level here', options=hierarch_form.hierarchy_level.tolist(), default=['Employee','Manager','Lead','Director','Senior','Head','CXO'])

## BAR CHART 1
if x_axis2:
    for element in x_axis2:
        hierarch3 = hierarch_form[hierarch_form['hierarchy_level'].isin (x_axis2)]

    fig4 = go.Figure(
        data=[go.Bar(x=hierarch3['hierarchy_level'],y=hierarch3.job_field, text=hierarch3['job_field'],
                     marker_color=px.colors.sequential.Oranges,
            textposition='auto')],
        layout_title_text="Frequency distribution of hierarchical level",
        
    )
    fig4.update_layout(
    xaxis_title="Hierarchical level",
    yaxis_title="Number of employees")
    fig4
    
fig = px.scatter(former, x="years_at_job", y="approx_work_xp", color="hierarchy_level",
                 title='Former employees hierarchical level according to work experience at time at current job.',
                 color_discrete_sequence=px.colors.sequential.Oranges,)
fig

## CHART 2
work_xp = former.groupby(['approx_work_xp'], as_index=False)['school'].count()
line1 = px.line(work_xp, x="approx_work_xp", y="school", title='Number of employees with x years of experience',
                color_discrete_sequence=px.colors.qualitative.Vivid,)
line1

## PART 4
## ML PART STARTS HERE
st.header('4. Machine learning model')
expander3 = st.expander('Click here to see the feature selection!', expanded = False)
with expander3:
    st.subheader('Features selection')
    st.markdown('Best results were obtained with features selected with Select From Model')
    
    ## FEATURES
    features = emp[['hierarchy_level', 'years_at_job', 'company2', 'hierarchy_level2',
           'approx_work_xp']].head(5)
    features

expander4 = st.expander('Click here to see the different models!', expanded  =  False)
with expander4:
## MODEL COMPARISON
    st.subheader('Models comparison')
    mod1, mod2, mod3 = st.columns(3)
    with mod1:
        st.markdown('**Random Forest Classifier**')
        st.markdown('With n_estimators = 120')
        st.metric('Accuracy score (%):', value = 74.16)
    with mod2:
        st.markdown('**Logistic Regression**')
        st.metric('Accuracy score (%):', value = 70.7)
    with mod3:
        st.markdown('**K Neighbors Classifier**')
        st.markdown('With k = 4')
        st.metric('Accuracy score (%):', value = 62.9)
    
    mod4, mod5, mod6 = st.columns(3)
    with mod4:
        st.markdown('**Extra trees classifier**')
        st.metric('Accuracy score (%):', value = 68.54)
    with mod5:
        st.markdown('**Support Vector Classification (SVC)**')
        st.metric('Accuracy score (%):', value = 68.54)
    with mod6:
        st.markdown('**Decision Tree**')
        st.markdown('With with max_depth 3 and min_samples_split = 2')
        st.metric('Accuracy score (%):', value = 74.2)

## FINAL MODEL : DECISION TREE CLASSIFIER
expander5 = st.expander('Click here to see the details of the implemented model', expanded = False)
with expander5:
    st.subheader('Decision Tree Classifier')
    col1, col2 , col3 = st.columns(3)
    with col1:
        st.text('Decision tree with \nmax_depth 3 ')
        st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs_screenshots/decision_tree.png")
    with col2:
        st.text('Confusion matrix')
        st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs_screenshots/dt_confusion_matrix.png")
    with col3:
        st.text('Roc-Auc')
        st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs_screenshots/dt_roc_auc.png")
    st.image(r"/Users/Sarah/Documents/Final_project_HR_Analytics/Graphs_screenshots/nineteen.png")
## PART 5 MAIN RESULTS

st.header('5. Main results')
st.subheader('These are the results after having input the current employees dataset into our machine learning model')

predict = emp.groupby(['prediction'],as_index=False)['school'].count()

pie2 = px.pie(predict, values='school',names=['Possible stayer','Possible quitter'],
              color_discrete_sequence=px.colors.diverging.RdYlGn,
              title='Leaving prediction for current employees',hole=.3)
pie2.update_traces(textinfo='value+percent')
pie2

quit_pred = emp[emp['prediction']==1]

st.subheader('Comparing feature metrics from employees predicted to leave. vs predicted to stay.')

m1, m2 = st.columns((1, 1))
mean_years_at_job = round(emp["years_at_job"].mean(), 1)
mean_approx_work_xp = round(emp["approx_work_xp"].mean(), 1)

pred_mean_years_at_job = round(quit_pred["years_at_job"].mean(), 1)
pred_mean_approx_work_xp = round(quit_pred["approx_work_xp"].mean(), 1)

m1.metric(label="Average years at current job vs. total average", value=pred_mean_years_at_job, delta =pred_mean_years_at_job-mean_years_at_job,delta_color='inverse' )
m2.metric(label="Average work experience vs. total average", value=str(pred_mean_approx_work_xp)+ " Years", delta=round(pred_mean_approx_work_xp-mean_approx_work_xp,1),delta_color='inverse')

st.text('')
st.text('')


f1, f2 = st.columns((1,1))
with f1:
    y_feature = st.selectbox(label='Chose feature to display here', options=['company2','approx_work_xp','years_at_job','hierarchy_level','hierarchy_level2'])
with f2:
    color = st.radio(
         "What group would you like to see ? ",
         ('All', 'Predicted to stay', 'Predicted to leave'))

data = emp.groupby(['prediction', y_feature],as_index=False)['job_field'].count()

if color == 'All':
    stay = data[data['prediction']==0]
    leave = data[data['prediction']==1]
    fig6 = go.Figure()
    
    fig6.add_trace(go.Bar(x=stay[y_feature],y=stay.job_field,
                    text=stay.job_field,
                    marker_color='orange',
                    name='Predicted to stay'))
    fig6.add_trace(go.Bar(x=leave[y_feature],y=leave['job_field'],
                    marker_color='indianred',
                    text=leave.job_field,
                    name='Predicted to leave'))
    fig6.update_layout(xaxis_title=y_feature, yaxis_title="Number of employees",
                   title="Model features comparison between employees predicted to leave and employees predicted to stay")
    fig6
elif color =='Predicted to stay':
    data = data[data['prediction']==0]
    fig6= go.Figure(
        data=[go.Bar(x=data[y_feature],y=data['job_field'],
                     text=data['job_field'],
                     marker_color="Orange")])
    fig6.update_layout(xaxis_title=y_feature, yaxis_title="Number of employees",
                       title="Model features comparison between employees predicted to leave and employees predicted to stay")
    fig6

elif color == 'Predicted to leave':
    data = data[data['prediction']==1]
    fig6= go.Figure(
        data=[go.Bar(x=data[y_feature],y=data['job_field'],
                     text=data['job_field'],
                     marker_color='indianred')])
    fig6.update_layout(xaxis_title=y_feature, yaxis_title="Number of employees",
                       title="Model features comparison between employees predicted to leave and employees predicted to stay")
    fig6
    

st.markdown('---')

## CONCLUSION

st.header('Conclusion')
st.markdown('**Given the information we have:**')
st.markdown("- HR's could set a milestone when employees reach **3 years at the same position** (point at which there are as many resignations as people who stay) ")
st.markdown("- Employees could at that point be offered some **training, a horizontal or vertical career change** ")
st.markdown("- The company can also use this information to **anticipate needed recruitments** and have a smoother turn-over")

st.markdown('---')

## FINAL
st.header('Thank you for your attention !')
st.image(r"/Users/Sarah/Pictures/questions.jpg")
