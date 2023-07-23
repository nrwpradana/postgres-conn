import streamlit as st
from connection import PostgresConnection
import json

st.markdown("**Make sure the PostgreSQL server is running.**")

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
