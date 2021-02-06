import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ori_data = pd.read_csv('covid_data.csv')
# print(ori_data.info())
ori_data['date'] = pd.to_datetime(ori_data.date)
ori_data['year'] = pd.DatetimeIndex(ori_data.date).year
ori_data['month'] = pd.DatetimeIndex(ori_data.date).month
ori_data['weekday'] = pd.DatetimeIndex(ori_data.date).weekday
ori_data['day'] = pd.DatetimeIndex(ori_data.date).day
for_comparison = ori_data.query("iso_code==['USA', 'IND', 'BRA', 'RUS', 'GBR']")
final_data = for_comparison[
    ['date', 'total_cases', 'total_deaths', 'new_deaths', 'new_cases', 'positive_rate', 'female_smokers',
     'male_smokers', 'month', 'weekday', 'day', 'year', 'location', 'iso_code']]

sns.set_style('darkgrid')
# plt.hist(x='new_cases', data=final_data, stacked=True)
# plt.xlabel('Cases')
# plt.ylabel('Count')
plt.title('New Cases In India Vs USA')
#sns.histplot(x='positive_rate', data=final_data.query("iso_code==['IND', 'USA']"), hue='location', log_scale=True,fill=False)
sns.histplot(final_data, x='month', y='female_smokers',  bins=30, discrete=(True, False), log_scale=(False, True),
             cbar=True, cbar_kws=dict(shrink=.75))
plt.show()
