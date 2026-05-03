import os 
import pandas as pd
input_file = "D:\\Docker\\project\\ADMISSIONS.csv"
output_dir = "D:\\Docker\\project\\cleaned"

os.makedirs(output_dir, exist_ok= True)
df= pd.read_csv(input_file)

df = df.dropna()
df.to_parquet(f"{output_dir}/Admissions.parquet")
print("successfully transformed")


