import pandas as pd

data = pd.read_csv('covid_data.csv')
print(data)
print(data.query('new_cases < 0'))

data[data.new_cases < 0] = 0
print(data)

df = data.fillna(0)  # fills nan value with 0 to whole file
#print(df)
df.to_csv('df.csv', index=None)
df.to_csv('df_with_index.csv')
# data['iso_code'] = data['iso_code'].fillna(0)  # fills nan value with 0 in a particular column
# print(data)
# print(data.info())

# final_df = df[['iso_code', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'positive_rate']]
# print(final_df)
