/Users/jankirenz/code/bike/database/connection.pyfrom sqlalchemy import create_engine
import pandas as pd
import urllib.parse

# Connection settings
server = 'dwh.hdm-server.eu'
database = 'AdventureBikes Sales DataMart'
username = 'mike.farmer'
password = urllib.parse.quote_plus('password123')

# Create connection string for Mac (updated driver path)
conn_str = (
    'mssql+pyodbc://'
    f'{username}:{password}@{server}/{database}'
    '?driver=/opt/homebrew/lib/libmsodbcsql.17.dylib'  # Updated Mac path
)

try:
    # Create engine
    engine = create_engine(conn_str)
    
    # Test connection with a simple query
    df = pd.read_sql('SELECT @@version', engine)
    print("Connection successful!")
    print(f"SQL Server version: {df.iloc[0,0]}")

except Exception as e:
    print(f"Error connecting to database: {e}")

finally:
    # Dispose engine
    engine.dispose()
    print("Connection closed.")