import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

customers_df = pd.read_csv('https://raw.githubusercontent.com/adnanalamsyah/Submission/main/dashboard/customers_df_new.csv')
orders_df = pd.read_csv('https://raw.githubusercontent.com/adnanalamsyah/Submission/main/dashboard/orders_df_new.csv')
sellers_df = pd.read_csv('https://raw.githubusercontent.com/adnanalamsyah/Submission/main/dashboard/sellers_df_new.csv')

customers_df.describe(include="all")
customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)
customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)
sellers_df.describe(include="all")
sellers_df.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False)
sellers_df.groupby(by="seller_state").seller_id.nunique().sort_values(ascending=False)

st.header('Project Data Analysis :stars:')

with st.sidebar:
    st.image("https://psbhfhunila.org/wp-content/uploads/2022/07/E-commerce-KoinWorks-583x420.jpg")
    st.subheader("Adnan Alamsyah Bangkit Cohort Machine Learning")
    st.write("project akhir ini menggunakan dataset e-commerce yang tersedia pada website dicoding")

st.subheader("Spreadness of seller and customers")


labels = ['seller_state', 'customer_state']
values = [1849, 41746]

# Create bar chart
fig, ax = plt.subplots()
ax.bar(labels, values)

# Customize plot
ax.set_ylabel('Values')
ax.set_title('Spreadness of seller and customers')

# Show plot
st.pyplot(fig)

with st.expander("explanation"):
        st.write("according to the code and diagram above, it has been known that sau paulo has been chosen as the state that has biggest seller and customer for the e-commerce, but from this diagram it can be seen that the amount of customer is bigger than the seller")

# Data
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
        st.write("according to the code and pie chart above it can be seen that the state that has biggest amount of seller is SP or Sau Paulo")