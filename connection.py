from streamlit.connections import ExperimentalBaseConnection
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleConnection(ExperimentalBaseConnection[KaggleApi]):
    """st.experimental_connection implementation for Kaggle"""

    def _connect(self, **kwargs) -> KaggleApi:
        # Get the Kaggle API key from the user
        kaggle_username = st.text_input("Enter your Kaggle username:")
        kaggle_key = st.text_input("Enter your Kaggle API key:", type="password")

        if not kaggle_username or not kaggle_key:
            st.warning("Please provide your Kaggle username and API key.")
            return None

        # Connect to Kaggle API using the provided key
        api = KaggleApi()
        api.authenticate(username=kaggle_username, key=kaggle_key)

        return api

    def dataset_download_files(self, dataset: str, path: str) -> None:
        self._instance.dataset_download_files(dataset, path=path)
