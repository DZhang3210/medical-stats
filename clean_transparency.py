import pandas as pd
import numpy as np

def clean_transparency_data(input_file, output_file):
    # Read CSV, skipping the legend rows
    df = pd.read_csv(input_file, skiprows=2)
    
    # Select essential columns
    essential_cols = [
        'Individual/SHOP',
        'State',
        'Issuer_Name',
        'Plan_ID',
        'Plan_Type',
        'Metal_Level',
        'Plan_Number_Claims_Received_In_Network',
        'Plan_Number_Claims_Denied_In_Network',
        'Issuer_Percent_Internal_Appeals_Overturned'
    ]
    
    df = df[essential_cols]
    
    # Remove rows where plan is new (contains N/A)
    df = df[df['Plan_Number_Claims_Received_In_Network'] != 'N/A']
    
    # Convert numeric columns to float and handle NaN values
    numeric_cols = [
        'Plan_Number_Claims_Received_In_Network',
        'Plan_Number_Claims_Denied_In_Network',
        'Issuer_Percent_Internal_Appeals_Overturned'
    ]
    
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Remove rows with NaN values in claims columns
    df = df.dropna(subset=['Plan_Number_Claims_Received_In_Network', 
                          'Plan_Number_Claims_Denied_In_Network'])
    
    # Calculate denial rate
    df['Denial_Rate'] = (df['Plan_Number_Claims_Denied_In_Network'] / 
                        df['Plan_Number_Claims_Received_In_Network'] * 100)
    
    # Rename columns for clarity
    df = df.rename(columns={
        'Individual/SHOP': 'Market',
        'Plan_Number_Claims_Received_In_Network': 'Claims_Received',
        'Plan_Number_Claims_Denied_In_Network': 'Claims_Denied',
        'Issuer_Percent_Internal_Appeals_Overturned': 'Appeals_Overturned_Rate'
    })
    
    # Format numeric columns with NaN handling
    df['Claims_Received'] = df['Claims_Received'].fillna(0).astype(int)
    df['Claims_Denied'] = df['Claims_Denied'].fillna(0).astype(int)
    df['Denial_Rate'] = df['Denial_Rate'].fillna(0).round(1)
    df['Appeals_Overturned_Rate'] = df['Appeals_Overturned_Rate'].fillna(0).round(1)
    
    # Add % symbol to rate columns
    df['Denial_Rate'] = df['Denial_Rate'].astype(str) + '%'
    df['Appeals_Overturned_Rate'] = df['Appeals_Overturned_Rate'].astype(str) + '%'
    
    # Sort by state, issuer, and metal level
    df = df.sort_values(['State', 'Issuer_Name', 'Metal_Level'])
    
    # Write to CSV
    df.to_csv(output_file, index=False)
    
    # Print summary statistics
    print(f"Processed {len(df)} plans")
    print("\nSample of cleaned data:")
    print(df.head().to_string())
    
    return df

# Usage
input_file = "Medical_Files/Transparency-2025-SHOP.csv"
output_file = "Medical_Files/Transparency-2025-SHOP-Clean.csv"

cleaned_df = clean_transparency_data(input_file, output_file)