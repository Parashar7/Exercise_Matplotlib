import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

covid_df = pd.read_csv('covid_data.csv')
covid_df['date'] = pd.to_datetime(covid_df.date)
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).week
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
print(covid_df.info())

new_df = covid_df[
    ['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'positive_rate', 'female_smokers', 'male_smokers',
     'month', 'weekday', 'day', 'new_deaths', 'year']]
print(new_df.info())
final_df = new_df.query("iso_code==['IND', 'USA', 'NZL', 'BRA']")
print(final_df.nunique())
plt.figure(figsize=(12, 6))
sns.set_style('darkgrid')
plt.title('Covid Cases of India')
plt.xlabel('Month', size=14)
plt.ylabel('New Cases', size=14)
# plt.bar('month', 'new_cases', data=final_df)


# sns.barplot(x='month', y='new_deaths', data=final_df, hue='iso_code', ci=68, palette='Blues_d', dodge=True,
#           saturation=60)


# 1.Catplot
# sns.catplot(x='month', y='new_deaths', data=final_df, ci=68, palette='Blues_d', dodge=True,
#            saturation=60, col='iso_code', kind='bar')


# 2.Countplot
# sns.countplot(x='iso_code', data=final_df, palette='Set3')


# 3.Pointplot
# sns.pointplot(x='month', y='new_cases', data=final_df.query("year==2020"), hue='iso_code', palette='Set2',
#     linestyles=['-', '--', '-.'],dodge=False, join=True)


sns.catplot(x='month', y='new_cases', data=final_df.query("year==2020"), dodge=True,
            col='iso_code', height=5, aspect=0.4, kind='point', hue='day')
plt.show()
