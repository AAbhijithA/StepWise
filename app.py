'''
Importing necessary libraries for the code
'''
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Footfall Management System")

df = pd.DataFrame({"Day":[1,2,3,4],"Customers": [450,200,321,222]})
st.write("\n\n\nHere is your performance graph for multiple aisles:\n")
st.write("Aisle 1 dataframe\n")
st.write(df)
fig, ax = plt.subplots()
ax.plot(df['Day'], df['Customers'])
ax.set_xlabel('Day')
ax.set_ylabel('Customers')
ax.set_title('Performance graph for Aisle 1')
st.pyplot(fig)

df = pd.DataFrame({"Day":[1,2,3,4],"Customers": [200,200,189,187]})
st.write("Aisle 2 dataframe\n")
st.write(df)

st.write("\n\n")

fig, ax = plt.subplots()
ax.plot(df['Day'], df['Customers'])
ax.set_xlabel('Day')
ax.set_ylabel('Customers')
ax.set_title('Performance graph for Aisle 2')
st.pyplot(fig)

df = pd.DataFrame({"Day":[1,2,3,4],"Customers": [50,69,44,100]})
st.write("Aisle 3 dataframe\n")
st.write(df)

st.write("\n\n")

fig, ax = plt.subplots()
ax.plot(df['Day'], df['Customers'])
ax.set_xlabel('Day')
ax.set_ylabel('Customers')
ax.set_title('Performance graph for Aisle 3')
st.pyplot(fig)

df = pd.DataFrame({"Day":[1,2,3,4],"Customers": [100,100,100,100]})
st.write("Aisle 4 dataframe\n")
st.write(df)

st.write("\n\n")

fig, ax = plt.subplots()
ax.plot(df['Day'], df['Customers'])
ax.set_xlabel('Day')
ax.set_ylabel('Customers')
ax.set_title('Performance graph for Aisle 4')
st.pyplot(fig)

