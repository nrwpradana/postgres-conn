import streamlit as st
from connection import PostgresConnection
import json

# Assuming you have already uploaded the 'postgres_connection.py' file to the Colab environment.

# Upload the database credentials file
uploaded = st.file_uploader("Upload PostgreSQL credentials JSON file", type=["json"])

if uploaded:
    db_config = json.load(uploaded)

    # Create the connection
    conn = st.experimental_connection("postgres", type=PostgresConnection, **db_config)

    # Test query to verify the connection
    query = "SELECT version();"
    result = conn.query(query)

    # Display the query result
    st.write("PostgreSQL version:")
    st.write(result)
    
    # Display the PostgreSQL version from the JSON file
    postgres_version = db_config.get("postgres_version")
    if postgres_version:
        st.write("Configured PostgreSQL version:")
        st.write(postgres_version)
    else:
        st.write("PostgreSQL version is not specified in the JSON file.")
