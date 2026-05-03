  
        
"""import pandas as pd
import os

output_dir = "cleaned_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List of files to process
target_files = ["CALLOUT.csv", "ICUSTAYS.csv", "LABEVENTS.csv", "PATIENTS.csv", 
                "DIAGNOSES_ICD.csv", "D_ICD_DIAGNOSES.csv", "ADMISSIONS.csv"]

# Get all files in the current folder
current_files = os.listdir('.')

for target in target_files:
    # Match files regardless of case (small or capital)
    match = next((f for f in current_files if f.lower() == target.lower()), None)
    
    if match:
        print(f"Processing: {match}")
        try:
            df = pd.read_csv(match, low_memory=False)
            df = df.dropna()
            output_file = match.replace('.csv', '.parquet').replace('.CSV', '.parquet')
            df.to_parquet(os.path.join(output_dir, output_file))
            print(f"Success: {output_file} saved")
        except Exception as e:
            print(f"Error processing {match}: {e}")
    else:
        print(f"Missing: {target}")
        
        CREATE EXTERNAL TABLE CALLOUT (
    subject_id BIGINT,
    hadm_id BIGINT,
    submit_wardid INT,
    submit_careunit STRING,
    curr_wardid INT,
    curr_careunit STRING,
    callout_wardid INT,
    callout_service STRING,
    request_tele INT,
    request_resp INT,
    request_any INT,
    request_status STRING,
    createtime STRING,
    updatetime STRING,
    acknowledgetime STRING,
    outcometime STRING,
    firstreservationtime STRING,
    currentreservationtime STRING
) STORED AS PARQUET LOCATION '/data/mimic/CALLOUT';
        

    
  
    
    
    docker cp D:\Docker\project\docker-hadoop-spark\cleaned_data\PATIENTS.parquet namenode:/tmp/

    
    
docker cp D:\Docker\project\docker-hadoop-spark\. namenode:/tmp/mimic_data/
Get-ChildItem "D:\Docker\project\docker-hadoop-spark\*.parquet" | ForEach-Object {
    $name = $_.BaseName
    $fullName = $_.FullName
    Write-Host "Uploading $name to HDFS..."
    
    docker exec namenode hdfs dfs -mkdir -p /data/mimic/$name
    
    Get-Content $fullName -Encoding Byte -Raw | docker exec -i namenode hdfs dfs -put - /data/mimic/$name/$($_.Name)
}docker context use default"""














import pandas as pd
import os
from pathlib import Path

# Configuration: Using Relative Paths for Portability
INPUT_DIR = Path("D:\Docker\project\docker-hadoop-spark")  # Looks for CSVs in the current folder
OUTPUT_DIR = Path("cleaned_data")
TARGET_FILES = [
    "ADMISSIONS.csv", "CALLOUT.csv", "ICUSTAYS.csv", 
    "LABEVENTS.csv", "PATIENTS.csv", "DIAGNOSES_ICD.csv", "D_ICD_DIAGNOSES.csv"
]

def clean_and_convert():
    # Create output directory if it doesn't exist [cite: 59]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for file_name in TARGET_FILES:
        # Match files case-insensitively
        input_path = next((p for p in INPUT_DIR.glob('*') if p.name.lower() == file_name.lower()), None)
        
        if not input_path:
            print(f"Status: Missing -> {file_name}")
            continue
            
        print(f"Status: Processing -> {input_path.name}")
        try:
            # Optimized reading [cite: 14, 16]
            df = pd.read_csv(input_path, low_memory=False)
            
            # Cleaning: Dropping rows where critical IDs are missing [cite: 68]
            # This is safer than a blanket dropna()
            df = df.dropna(how='all') 
            
            # Define output path with .parquet extension [cite: 8, 71]
            output_file = OUTPUT_DIR / input_path.with_suffix('.parquet').name
            
            # Save to Parquet format [cite: 71]
            df.to_parquet(output_file, engine='pyarrow', index=False)
            print(f"Status: Success -> {output_file.name} saved in {OUTPUT_DIR}")
            
        except Exception as e:
            print(f"Status: Error in {file_name} -> {e}")

if __name__ == "__main__":
    clean_and_convert()