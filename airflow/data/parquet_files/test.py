import pandas as pd

# Path to the Parquet file
file_path = 'openmeteo_data.parquet'

# Read and display the Parquet file
df = pd.read_parquet(file_path)
print(df)