## Online Food Delivery Analysis 

End-to-end data analysis of online food delivery data — from raw CSV cleaning in Python to a cloud PostgreSQL database (Railway) and an interactive Power BI dashboard exploring customer demographics, income, and ordering behaviour.

## Project Goal

Understand who orders food online, from where, and why — and visualize the patterns behind customer reordering behaviour in Bangalore.


## Tech Stack

Layer - Tool
Data cleaning - Python (pandas) 
Database - PostgreSQL (Railway) 
Connection - Railway CLI SSH tunnel 
Visualization - Power BI Desktop 
Environment - GitHub Codespaces 


## Project Structure

online-food-delivery-analysis/
├── raw/ # Original + cleaned CSV
├── notebooks/ # Jupyter notebooks
├── powerbi/ # .pbix file + screenshots
│ └── screenshots/
├── clean.py # Data cleaning script
├── explore.py # Quick EDA script
├── upload.py # Upload CSV → Postgres
├── requirements.txt
└── README.md

Pipeline

1. Clean — drop junk columns, strip whitespace, standardize categories
2. Store— push cleaned data to a cloud PostgreSQL database on Railway
3. Visualize — connect Power BI via ODBC and build a 4-page interactive dashboard


## Dashboard Pages - Page What it shows

Overview -  Total customers, Yes/No reorder split, customer type, gender 
Demographics - Age distribution, marital status, occupation, gender × output 
Income & Education -  Income brackets, education levels, income × output, education × customer type
Feedback - Positive vs negative feedback, feedback × output, feedback by customer type 

## Key Insights

- 388 customers analysed; 78% reordered (Yes), 22% did not
- Majority are students (207) and young adults (avg age 24.6)
- 187 customers report "No Income" — consistent with the student skew
- Feedback is mostly positive (317 vs 71), but doesn't strongly predict reordering
- Orders cluster heavily around a handful of Bangalore pincodes

