import pandas as pd

# Read the three files
ind_qhp = pd.read_csv('Medical_Files/Clean/Transparency-2025-Ind-QHP-Clean.csv')
shop = pd.read_csv('Medical_Files/Clean/Transparency-2025-SHOP-Clean.csv')
ind_sadp = pd.read_csv('Medical_Files/Clean/Transparency-2025-Ind-SADP-Clean.csv')

# Concatenate all dataframes
merged_df = pd.concat([ind_qhp, shop, ind_sadp], ignore_index=True)

# Save the merged file
merged_df.to_csv('Medical_Files/Clean/Transparency-2025-All-Plans-Clean.csv', index=False)