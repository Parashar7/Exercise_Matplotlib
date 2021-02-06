import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

original_data = pd.read_csv('covid_data.csv')
# print(original_data.info())

# Extract data of India
new_data_of_IND = original_data.query("iso_code=='IND'")
# print(new_data_of_IND.info())

final_data_IND = new_data_of_IND[['date', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'positive_rate']]
final_data_IND['date'] = pd.to_datetime(final_data_IND.date)
final_data_IND['year'] = pd.DatetimeIndex(final_data_IND.date).year
final_data_IND['month'] = pd.DatetimeIndex(final_data_IND.date).month
final_data_IND['weekday'] = pd.DatetimeIndex(final_data_IND.date).week
final_data_IND['day'] = pd.DatetimeIndex(final_data_IND.date).day
print(final_data_IND.info())
# extract data of USA and Europe
new_data_of_USA = original_data.query("iso_code==['USA', 'GBR']")
final_data_USA = new_data_of_USA[
    ['date', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'positive_rate', 'location']]
print(final_data_USA.location.unique())
final_data_USA['date'] = pd.to_datetime(final_data_USA.date)
final_data_USA['year'] = pd.DatetimeIndex(final_data_USA.date).year
final_data_USA['month'] = pd.DatetimeIndex(final_data_USA.date).month
final_data_USA['weekday'] = pd.DatetimeIndex(final_data_USA.date).weekday
#final_data_IND['day'] = pd.DatetimeIndex(final_data_USA.date).day
print(final_data_USA.info())
#sns.lineplot('month', 'new_cases', data=final_data_USA, hue='location', style='year')
sns.relplot('month', 'new_cases', col='location', data=final_data_USA, kind='line', hue='year')
# print(final_data_IND.nunique())
#sns.lineplot('month', 'new_cases', data=final_data_IND, hue='year')
plt.show()
