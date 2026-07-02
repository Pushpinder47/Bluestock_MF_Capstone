import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        try:
            df = pd.read_csv(path)

            print("\n" + "="*50)
            print("File:", file)
            print("Shape:", df.shape)
            print("\nColumns:")
            print(df.columns.tolist())
            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")