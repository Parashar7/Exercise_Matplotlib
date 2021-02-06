import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ori_data = pd.read_csv('covid_data.csv')
ori_data['date'] = pd.to_datetime(ori_data.date)
ori_data['year'] = pd.DatetimeIndex(ori_data.date).year
ori_data['month'] = pd.DatetimeIndex(ori_data.date).month
ori_data['weekday'] = pd.DatetimeIndex(ori_data.date).weekday
ori_data['day'] = pd.DatetimeIndex(ori_data.date).day

# print(ori_data.iso_code.unique(), ori_data.info())

for_comparison = ori_data.query("iso_code==['USA', 'IND', 'BRA', 'RUS', 'GBR']")
# print(for_comparison.info())

final_data = for_comparison[
    ['date', 'total_cases', 'total_deaths', 'new_deaths', 'new_cases', 'positive_rate', 'female_smokers',
     'male_smokers', 'month', 'weekday', 'day', 'year', 'location', 'iso_code']]

print(final_data.info(), final_data.nunique())
sns.set_style('darkgrid')
# palette = sns.color_palette("twilight_r", 6)  # number of colors is equal to hue

fig, axes = plt.subplots(3, 2, figsize=(8, 4.5))
# axes[0, 0].plot('month', 'new_cases', 's-b', data=final_data.query("location=='India'"))
# plt.tight_layout(pad=2)
sns.lineplot('month', 'new_deaths', hue='location', style='year', data=final_data.query("iso_code=='IND'"),
             ax=axes[0, 0])
sns.lineplot('month', 'new_cases', hue='location', style='year', data=final_data.query("iso_code=='IND'"),
             ax=axes[0, 1])
sns.lineplot('month', 'total_cases', hue='location', style='year', data=final_data.query("iso_code=='IND'"),
             ax=axes[1, 0])
sns.lineplot('month', 'total_deaths', hue='location', style='year', data=final_data.query("iso_code=='IND'"),
             ax=axes[1, 1])
sns.lineplot('month', 'positive_rate', hue='location', style='year', data=final_data.query("iso_code=='IND'"),
             ax=axes[2, 0])

# sns.lineplot('month', 'new_cases', hue='location', style='year', data=final_data, ax=axes[0, 1])

# sns.relplot('month', 'new_deaths', col='location', hue='year', style='year', size='male_smokers', palette=palette,
#        data=final_data,
#        kind='line')


plt.show()
