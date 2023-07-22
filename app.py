import os
import pandas as pd
import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleConnection(ExperimentalBaseConnection[KaggleApi]):
    """st.experimental_connection implementation for Kaggle"""

    def _connect(self, **kwargs) -> KaggleApi:
        # Get the Kaggle API key from the uploaded kaggle.json file
        kaggle_json = st.file_uploader("Upload kaggle.json", type=["json"])
        if kaggle_json is not None:
            with open(kaggle_json.name, "wb") as f:
                f.write(kaggle_json.read())

        # Connect to Kaggle API using the provided key
        api = KaggleApi()
        api.authenticate()

        return api

    def dataset_download_files(self, dataset: str, path: str) -> None:
        self._instance.dataset_download_files(dataset, path=path)

def main():
    st.title("Kaggle Dataset Downloader")

    # Create a connection to Kaggle using the custom KaggleConnection class
    with KaggleConnection() as kaggle_conn:
        # Get the dataset name from the user
        dataset_name = st.text_input("Enter Kaggle dataset name:")

        # Check if the user has uploaded kaggle.json
        if not kaggle_conn._instance:
            st.warning("Please upload your kaggle.json file to access Kaggle datasets.")
            return

        # Check if the dataset name is provided
        if dataset_name:
            st.write("Downloading dataset...")
            # Define the download path
            download_path = os.path.join(".", dataset_name)

            try:
                # Download the dataset
                kaggle_conn.dataset_download_files(dataset_name, path=download_path)

                # List the downloaded files
                st.write("Downloaded files:")
                for file in os.listdir(download_path):
                    st.write(file)

            except Exception as e:
                st.error(f"Error downloading dataset: {str(e)}")

if __name__ == "__main__":
    main()
