import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the csv file
df = pd.read_csv('Merged/Transparency-2025-All-Plans-Clean.csv')



# Calculate denial rate for each plan
df['Denial_Rate'] = (df['Claims_Denied'] / 
                     df['Claims_Received'] * 100)

# Group by state and calculate mean denial rate
state_denial_rates = df.groupby('State')['Denial_Rate'].agg([
    'mean',
    'count'  # number of plans in each state
]).reset_index()

# Sort by mean denial rate
state_denial_rates = state_denial_rates.sort_values('mean', ascending=True)

# Create the visualization
plt.figure(figsize=(15, 8))
sns.barplot(data=state_denial_rates, 
            x='State', 
            y='mean',
            color='skyblue')

# Customize the plot
plt.title('Average Insurance Claim Denial Rates by State', pad=20)
plt.xlabel('State')
plt.ylabel('Average Denial Rate (%)')
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Optional: Add data labels on top of each bar
for i, row in state_denial_rates.iterrows():
    plt.text(i, 
             row['mean'] + 0.5,  # Single y-position specification
             f"{row['mean']:.1f}%\n(n={int(row['count'])})", 
             ha='center', 
             va='bottom',
             fontsize=8,
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

plt.show()


# Print summary statistics in a formatted table
print("\nSummary Statistics:")
print("\nStates with highest denial rates:")
print("-" * 50)
print(f"{'State':<15}{'Denial Rate':>15}{'Plans Count':>15}")
print("-" * 50)
for _, row in state_denial_rates.nlargest(5, 'mean').iterrows():
    print(f"{row['State']:<15}{row['mean']:>14.1f}%{row['count']:>15}")

print("\nStates with lowest denial rates:")
print("-" * 50)
print(f"{'State':<15}{'Denial Rate':>15}{'Plans Count':>15}")
print("-" * 50)
for _, row in state_denial_rates.nsmallest(5, 'mean').iterrows():
    print(f"{row['State']:<15}{row['mean']:>14.1f}%{row['count']:>15}")