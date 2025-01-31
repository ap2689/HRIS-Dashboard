import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv('hr_employee_data.csv')  # Ensure the file path is correct

# Create a simple dashboard
st.title("HRIS Dashboard")
st.write("Here is your employee data:")
st.dataframe(df)

# Create a pie chart for department distribution
department_data = df['Department'].value_counts()

fig = px.pie(names=department_data.index, values=department_data.values, title="Department Distribution")
st.plotly_chart(fig)

# Add a dropdown to filter by department
department_filter = st.selectbox("Select Department", options=df['Department'].unique())
filtered_df = df[df['Department'] == department_filter]
st.write(filtered_df)

# Add a search bar to search for employees by name or ID
search_query = st.text_input("Search Employee by Name or ID")

if search_query:
    search_results = df[df['EmployeeName'].str.contains(search_query, case=False)]
    st.write(search_results)

# Add a reset button to clear filters
if st.button("Reset Filters"):
    st.experimental_rerun()  # Resets the entire dashboard
