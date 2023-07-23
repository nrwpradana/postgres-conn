from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

import psycopg2
import pandas as pd

class PostgresConnection(ExperimentalBaseConnection[psycopg2.extensions.connection]):

    def _connect(self, **kwargs) -> psycopg2.extensions.connection:
        if 'dbname' in kwargs:
            dbname = kwargs.pop('dbname')
        else:
            dbname = self._secrets['dbname']
        
        if 'user' in kwargs:
            user = kwargs.pop('user')
        else:
            user = self._secrets['user']
        
        if 'password' in kwargs:
            password = kwargs.pop('password')
        else:
            password = self._secrets['password']
        
        if 'host' in kwargs:
            host = kwargs.pop('host')
        else:
            host = self._secrets['host']
        
        if 'port' in kwargs:
            port = kwargs.pop('port')
        else:
            port = self._secrets['port']

        return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port, **kwargs)

    def cursor(self) -> psycopg2.extensions.cursor:
        return self._instance.cursor()

    def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(query: str, **kwargs) -> pd.DataFrame:
            cursor = self.cursor()
            cursor.execute(query, **kwargs)
            columns = [desc[0] for desc in cursor.description]
            return pd.DataFrame(cursor.fetchall(), columns=columns)

        return _query(query, **kwargs)
