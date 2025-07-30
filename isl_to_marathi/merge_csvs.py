import os
import pandas as pd

# Define source folder and output file
source_folder = "collected_csvs"
output_file = "merged_dataset.csv"

# Initialize list to hold dataframes
all_data = []

# Loop through each file in the folder
for filename in os.listdir(source_folder):
    if filename.startswith("gesture_") and filename.endswith(".csv"):
        file_path = os.path.join(source_folder, filename)
        print(f"🔄 Merging: {filename}")
        df = pd.read_csv(file_path)

        # Optional: drop empty or corrupt rows
        df.dropna(inplace=True)
        all_data.append(df)

# Concatenate all
if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"\n✅ Merged dataset saved as: {output_file}")
else:
    print("⚠️ No CSV files found to merge.")
