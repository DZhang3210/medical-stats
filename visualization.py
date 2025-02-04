import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import geopandas as gpd

# Read the Excel file - replace 'your_file.xlsx' with your actual filename
df = pd.read_csv('Medical_Files/Merged/Transparency-2025-All-Plans-Clean.csv')

# Print column names to debug
print("Available columns:", df.columns.tolist())

# Calculate denial rate for each plan (using correct column name)
df['Denial_Rate'] = (df['Claims_Denied'] / 
                     df['Claims_Received'] * 100)


# Group by state and calculate mean denial rate
state_denial_rates = df.groupby('State')['Denial_Rate'].agg([
    'mean',
    'count'  # number of plans in each state
]).reset_index()

# Sort by mean denial rate
state_denial_rates = state_denial_rates.sort_values('mean', ascending=True)

# Load US states geometry
states_map = gpd.read_file('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json')

# Merge the geometry with our denial rates data
# Convert state codes to uppercase to match the geometry data
states_map = states_map.merge(state_denial_rates, 
                            how='left',
                            left_on='id',
                            right_on='State')

# Create the visualization
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Create choropleth map
states_map.plot(column='mean',
                ax=ax,
                legend=True,
                legend_kwds={'label': 'Denial Rate (%)',
                            'orientation': 'horizontal'},
                missing_kwds={'color': 'lightgrey'},
                cmap='YlOrRd')

# Add state labels with denial rates
for idx, row in states_map.iterrows():
    # Get the centroid of each state
    centroid = row.geometry.centroid
    # Add text with state name and denial rate
    if not np.isnan(row['mean']):  # Only add label if we have data
        ax.text(centroid.x, centroid.y,
                f"{row['id']}\n{row['mean']:.1f}%",
                ha='center',
                va='center',
                fontsize=8)

# Customize the plot
plt.title('Insurance Claim Denial Rates by State', pad=20)
ax.axis('off')  # Remove axes

# Adjust layout
plt.tight_layout()

plt.show()

# Print summary statistics
print("\nSummary Statistics:")
print(f"States with highest denial rates:")
print(state_denial_rates.nlargest(5, 'mean')[['State', 'mean', 'count']])
print("\nStates with lowest denial rates:")
print(state_denial_rates.nsmallest(5, 'mean')[['State', 'mean', 'count']])