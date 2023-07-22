import os
import streamlit as st
from connection import KaggleConnection

def main():
    st.title("Kaggle Dataset Downloader")

    # Create a connection to Kaggle using the custom KaggleConnection class
    with KaggleConnection() as kaggle_conn:
        # Check if the user has provided Kaggle API key
        if not kaggle_conn._instance:
            st.warning("Please provide your Kaggle username and API key to access Kaggle datasets.")
            return

        # Get the dataset name from the user
        dataset_name = st.text_input("Enter Kaggle dataset name:")

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
