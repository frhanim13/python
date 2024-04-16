
# Import pandas into the environment
import pandas as pd

# Import marketing.csv 
marketing = pd.read_csv('marketing.csv')

# Print the first five rows of the DataFrame
print(marketing.head(5))

# Print the statistics of all columns
print(marketing.describe())

# Check column data types and non-missing values
print(marketing.info())

# Check the data type of is_retained
print(marketing['is_retained'].dtype)

# Convert is_retained to a boolean
marketing['is_retained'] = marketing['is_retained'].astype(bool)

# Check the data type of is_retained, again
print(marketing['is_retained'].dtype)

# Mapping for channels
channel_dict = {"House Ads": 1, "Instagram": 2, 
                "Facebook": 3, "Email": 4, "Push": 5}

# Map the channel to a channel code
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)

# Import numpy
numpy as np

# Add the new column is_correct_lang
marketing['is_correct_lang'] = np.where(marketing['language'] == 'English', True, False)

# Import pandas into the environment
import pandas  as pd 

# Import marketing.csv with date columns
marketing = pd.read_csv('marketing.csv', parse_dates=['date_served', 'date_subscribed','date_canceled'])

# Add a DoW column
marketing['DoW'] = marketing['date_subscribed'].dt.dayofweek

#determine how many users are seeing the marketing assets each day

daily_users = marketing.groupby('date_served')['user_id'].nunique()

# Print head of daily_users
print(daily_users.head())








