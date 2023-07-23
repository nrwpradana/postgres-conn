import streamlit as st
from connection import PostgresConnection
import json

# Assuming you have already uploaded the 'postgres_connection.py' file to the Colab environment.

# Upload the database credentials file
uploaded = st.file_uploader("Upload PostgreSQL credentials JSON file", type=["json"])

if uploaded:
    db_config = json.load(uploaded)

    # Display the database credentials
    st.write("Database Credentials:")
    st.write("Database Name:", db_config.get("dbname"))
    st.write("User:", db_config.get("user"))
    st.write("Password:", db_config.get("password"))
    st.write("Host:", db_config.get("host"))
    st.write("Port:", db_config.get("port"))

    # Create the connection
    conn = st.experimental_connection("postgres", type=PostgresConnection, **db_config)

    # Test query to verify the connection
    query = "SELECT version();"
    result = conn.query(query)

    # Display the query result
    st.write("PostgreSQL version:")
    st.write(result)
