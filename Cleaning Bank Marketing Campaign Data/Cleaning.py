import pandas as pd
import numpy as np

# Start coding here...

file_path = "bank_marketing.csv"
data = pd.read_csv(file_path)


# ================== CLIENT DATAFRAME ==================
client_columns = ['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']
client = data[client_columns].copy()


# Cleaning and formatting

#Change "." to "_"
client['job']=client['job'].str.replace('.','-',regex=False) 

#Change "." to "_" and "unknown" to np.NaN
client['education']=client['education'].str.replace('.','-',regex=False).replace('unknown',np.NaN) 

#Convert to boolean data type:1 if "yes", otherwise 0

client['credit_default']=client['credit_default'].apply(lambda x: 1 if x == "yes" else 0).astype(bool)

client['mortgage']=client['mortgage'].apply(lambda x: 1 if x == "yes" else 0).astype(bool)


client.to_csv("client.csv", index=False)

# ================== CAMPAIGN DATAFRAME ==================
campaign_columns = [
    'client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts',
    'previous_outcome', 'campaign_outcome', 'day', 'month'
]
campaign = data[campaign_columns].copy()

# Add and format the last_contact_date
month_mapping = {
    'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05',
    'jun': '06', 'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10',
    'nov': '11', 'dec': '12'
}
campaign['month'] = campaign['month'].map(month_mapping)
campaign['year'] = 2022
campaign['last_contact_date'] = pd.to_datetime(campaign[['year', 'month', 'day']].astype(str).agg('-'.join, axis=1))

# Cleaning and formatting
campaign['previous_outcome'] = campaign['previous_outcome'].apply(lambda x: 1 if x == "success" else 0).astype(bool)
campaign['campaign_outcome'] = campaign['campaign_outcome'].apply(lambda x: 1 if x == "yes" else 0).astype(bool)
campaign = campaign.drop(columns=['day', 'month', 'year'])

# Save to campaign.csv
campaign.to_csv("campaign.csv", index=False)

# ================== ECONOMICS DATAFRAME ==================
economics_columns = ['client_id', 'cons_price_idx', 'euribor_three_months']
economics = data[economics_columns].copy()

# Save to economics.csv
economics.to_csv("economics.csv", index=False)

print("Data cleaning and saving completed. Files generated: client.csv, campaign.csv, economics.csv")
