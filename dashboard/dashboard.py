import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

# input all of the data needed
customers_df = pd.read_csv('https://raw.githubusercontent.com/adnanalamsyah/Submission/main/dashboard/customers_df_new.csv')
orders_df = pd.read_csv('https://raw.githubusercontent.com/adnanalamsyah/Submission/main/dashboard/orders_df_new.csv')
sellers_df = pd.read_csv('https://raw.githubusercontent.com/adnanalamsyah/Submission/main/dashboard/sellers_df_new.csv')

# describe the data that would be use
customers_df.describe(include="all")
# group the data by the categories
customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)
customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)
# input the sellers data
sellers_df.describe(include="all")
# group the sellers data
sellers_df.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False)
sellers_df.groupby(by="seller_state").seller_id.nunique().sort_values(ascending=False)

# input the header
st.header('Project Data Analysis :stars:')

# input sidebar with image and subheader
with st.sidebar:
    st.image("https://psbhfhunila.org/wp-content/uploads/2022/07/E-commerce-KoinWorks-583x420.jpg")
    st.subheader("Adnan Alamsyah Bangkit Cohort Machine Learning")
    st.write("project akhir ini menggunakan dataset e-commerce yang tersedia pada website dicoding")

st.subheader("Spreadness of seller and customers")

# input the values and labels that you want to use
labels = ['seller SP', 'cust SP', 'seller PR', 'cust PR', 'seller MG', 'cust MG']
values = [1849, 41746, 349, 5045, 244, 11635]

# Create bar chart
fig, ax = plt.subplots()
ax.bar(labels, values)

# Customize plot
ax.set_ylabel('Values')
ax.set_title('Spreadness of seller and customers')

# Show plot
st.pyplot(fig)

# state the explanation by expanding 
with st.expander("explanation"):
        st.write("according to the code and diagram above, it has been known that sau paulo has been chosen as the state that has biggest seller and customer for the e-commerce, but from this diagram it can be seen that the amount of customer is bigger than the seller")

# input the data that you want to choose
labels = ['SP', 'PR', 'MG']
sizes = [1849, 349, 244]

# Create pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Customize plot
ax.set_title('Biggest Seller State')

# Show plot
st.pyplot(fig) 

with st.expander("explanation"):
        st.write("according to the code and pie chart above it can be seen that the state that has biggest amount of seller is SP or Sau Paulo with the total domination of 75 percent rather than other states")