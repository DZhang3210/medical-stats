Data was provided, in a cleaned csv file format, so that you could test it yourself, and verify the results.
Github link: https://github.com/DZhang3210/medical-stats

# Medical Stats Project Summary

This project analyzes healthcare insurance claim denial rates across different states using transparency data.

## Data Processing Pipeline

### Data Cleaning (`clean_transparency.py`)

- Processes raw transparency data files
- Removes invalid entries and handles missing values
- Calculates denial rates
- Standardizes column names and formats
- Key columns include:
  - Market
  - State
  - Issuer Name
  - Claims Received/Denied
  - Appeals rates

### Data Merging (`merge_transparency_files.py`)

Combines three different plan types:

- Individual Qualified Health Plans (QHP)
- Small Business Health Options Program (SHOP)
- Individual Stand-Alone Dental Plans (SADP)

### Visualization (`visualization.py`)

Creates a comprehensive bar chart showing:

- Average denial rates by state
- Number of plans per state
- Clear labeling and grid lines for readability
- Generates summary statistics focusing on states with highest denial rates

## Key Features

- Handles multiple insurance plan types
- Calculates and visualizes state-level denial rates
- Provides detailed statistics on claims processing
- Includes data on appeals and overturned decisions
- Maintains data quality through thorough cleaning processes

## Data Structure

The cleaned data includes important metrics such as:

- Claims received and denied
- Denial rates as percentages
- Appeals overturned rates
- Plan details (ID, Type, Metal Level)
- Market information
- State and issuer information
