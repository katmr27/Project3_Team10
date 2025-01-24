import pandas as pd
import numpy as np

def display_trails_info():
    # Read the DataFrame
    df = pd.read_csv('merged_trails.csv')
    
    # Clear formatting for better display
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    # 1. Basic Dataset Information
    print("\n=== TRAILS DATASET OVERVIEW ===")
    print(f"Total number of trails: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    
    # 2. Display column names and data types
    print("\n=== COLUMNS AND DATA TYPES ===")
    for col, dtype in df.dtypes.items():
        print(f"{col:<25} {dtype}")
    
    # 3. Sample of the data
    print("\n=== FIRST 5 TRAILS ===")
    print(df.head().to_string())
    
    # 4. Basic statistics for numerical columns
    print("\n=== NUMERICAL STATISTICS ===")
    print("Distance (miles):")
    print(f"Average: {df['distance(miles)'].mean():.2f}")
    print(f"Minimum: {df['distance(miles)'].min():.2f}")
    print(f"Maximum: {df['distance(miles)'].max():.2f}")
    
    print("\nElevation Gain (feet):")
    print(f"Average: {df['elevation_gain(feet)'].mean():.2f}")
    print(f"Minimum: {df['elevation_gain(feet)'].min():.2f}")
    print(f"Maximum: {df['elevation_gain(feet)'].max():.2f}")
    
    # 5. Categorical breakdowns
    print("\n=== TRAIL CHARACTERISTICS ===")
    print("\nDifficulty Distribution:")
    print(df['difficulty'].value_counts())
    
    print("\nTrail Type Distribution:")
    print(df['trail_type'].value_counts())
    
    print("\nCrowded Status Distribution:")
    print(df['crowded'].value_counts())
    
    print("\nFamily Friendly Distribution:")
    print(df['family_friendly'].value_counts())
    
    return df  # Return the DataFrame for further use if needed

# Run the analysis
trails_df = display_trails_info()