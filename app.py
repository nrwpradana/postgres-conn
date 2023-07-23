import streamlit as st
import pandas as pd
from connection import PostgresConnection

# Assuming you have already uploaded the 'postgres_connection.py' file to the Colab environment.

# Upload the SQL file
uploaded = st.file_uploader("Upload SQL file", type=["sql"])

if uploaded:
    # Read the SQL file content
    sql_content = uploaded.read().decode()

    # Create the connection
    conn = st.experimental_connection("postgres", type=PostgresConnection)

    # Execute the SQL query to fetch the top 10 records
    query = sql_content + " LIMIT 10;"
    result = conn.query(query)

    # Display the query result
    if result is not None:
        df = pd.DataFrame(result, columns=result[0].keys())
        st.write("Top 10 records:")
        st.write(df)
    else:
        st.write("No data retrieved from the SQL file.")
