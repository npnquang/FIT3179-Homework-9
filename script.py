import pandas as pd

# Load the IBTrACS CSV file
file_path = "data/ibtracs_all_list_v04r01.csv"  # adjust if path is different
df = pd.read_csv(file_path, low_memory=False)

# Preview to identify key columns
print(df.columns[:30])  # show first 30 columns to locate IDs and coords

# Common IBTrACS columns:
# 'SID' (storm ID), 'NAME', 'SEASON', 'ISO_TIME', 'LAT', 'LON'

# Sort by time to ensure earliest record is first
df_sorted = df.sort_values(by=["SID", "NUMBER", "ISO_TIME"])

# Drop duplicates, keeping only the first row per storm ID
first_points = df_sorted.drop_duplicates(subset=["SID", "NUMBER"], keep="first")


# Save to new CSV
output_path = "data/ibtracs_first_locations.csv"
first_points.to_csv(output_path, index=False)

print(f"Saved {len(first_points)} first storm locations to {output_path}")
