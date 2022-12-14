import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Racquet Sport Statistics',
                   page_icon=':bar_chart:',
                   layout='wide')
st.title('Pickleball Playerbase Analysis')
st.write('Data Visualization Project by Justin Frandsen')


#player count by year
ppdf = pd.DataFrame({
    'Year':['2017','2018','2019','2020','2021'],
    'Players':[3132000,3301000,3460000,4200000,4820000]})

ppdf=ppdf.set_index('Year')
ppdf = ppdf.replace(',','',regex=True)
if st.checkbox('View Dataset'):
    st.subheader('Yearly Growth')
    st.write(ppdf)

st.bar_chart(ppdf)
    
#sidebar
st.sidebar.header('Pickleball vs. Tennis')
st.sidebar.write('Since 2017, Pickleball has seen an increase of over 1 million players. The goal of showing this data is to answer the question: how big is the sport?')
st.sidebar.markdown('---')
st.sidebar.write('The growth of pickleball is best represented when compared to that of a similar sport such as tennis. It is also a mission to see if the playerbase of tennis has shrunk at all from pickleball stealing the spotlight')
st.sidebar.markdown('---')
st.sidebar.subheader('Ruleset Comparison')
rules=pd.DataFrame({
    'Pickleball':['The serve must be an underhand motion', 'Contact with the ball can only be made below the hips', 'Server must stand behind the baseline; no foot faults are acceptable', 'If the ball touches the net and goes in, it is a let and the point is to be replayed', 'There is only one serve per point', 'The reciever must play the first shot off-the-bounce', 'There is a no-volley zone(called kitchen)', 'Points are scored only on serve'],
    'Tennis':['The serve can be an overhand action', 'Contact with the ball can be made from anywhere', 'Server must stand behind the baseline; no foot faults are acceptable', 'If the ball touches the net and goes in, it is a let and the point is replayed', 'If the first serve goes out it is a fault and the server has another serve', 'The reciever can return the serve without a bounce', 'Players can volley from anywhere on their side of the court', 'Points can be scored on serve and return']},)
hide_table_row_index="""
    <style>
    thead tr th:first-child {display:none}
    tbody th {display:none}
    </style>
    """
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.sidebar.table(rules)
