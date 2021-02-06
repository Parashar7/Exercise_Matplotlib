import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_df = pd.read_csv('new_data.csv')
data_df['month'] = pd.to_datetime(data_df.date)
data_df['month'] = pd.DatetimeIndex(data_df.date).month
data_df['weekday'] = pd.DatetimeIndex(data_df.date).week
data_df['day'] = pd.DatetimeIndex(data_df.date).day
print(data_df.info(), '\n\n', data_df.nunique())

plt.figure(figsize=(8, 4.5))
sns.set_style('darkgrid')
sns.lineplot('month', 'new_cases', data=data_df)
#sns.lineplot('month', 'new_cases', data=data_df)
plt.show()
