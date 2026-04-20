import pandas as pd
import numpy as np
import os

file_path = "data/raw/data.csv"

rows = 5_000_000
chunk_size = 500_000

# Ensure fresh start
if os.path.exists(file_path):
    os.remove(file_path)

for i in range(0, rows, chunk_size):
    print(f"Generating rows {i} to {i + chunk_size}")

    df = pd.DataFrame({
        "id": range(i, i + chunk_size),
        "name": np.random.choice(["Alice", "Bob", "Charlie", None], chunk_size),
        "age": np.random.randint(18, 70, chunk_size),
        "salary": np.random.randint(20000, 100000, chunk_size)
    })

    if i == 0:
        df.to_csv(file_path, mode='w', index=False)   # overwrite + header
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

print("Data generated successfully!")
