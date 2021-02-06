import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

car_crash = sns.load_dataset('car_crashes')
# print(car_crash)
print(car_crash, car_crash.info(), car_crash.describe(), car_crash.nunique())
plt.figure(figsize=(20, 15))
sns.set_style('darkgrid')
plt.title('Car Crash')
# plt.plot('alcohol', 'o-b', data=car_crash)
# plt.plot('speeding', 'x--r', data=car_crash)
# sns.lineplot('alcohol', 'speeding', data=car_crash)
# plt.legend(['Speeding', 'Alcohol'])
# plt.xlabel('Value')
# plt.ylabel('Instances')


# sns.scatterplot('speeding', 'alcohol', data=car_crash, hue='not_distracted', s=100)
# plt.hist('speeding', data=car_crash)
# plt.hist('alcohol', data=car_crash)
# plt.hist(['speeding', 'alcohol'], bottom='speeding', data=car_crash,stacked=True)
# plt.legend(['Alcohol', 'Speeding'])
# sns.barplot('total', 'alcohol', data=car_crash.loc[20:50+1])
# plt.bar('total', 'alcohol', data=car_crash.loc[20:50+1])
# plt.hist('not_distracted', data=car_crash)
# plt.plot('total', 'alcohol', 's--b', data=car_crash)
#sns.histplot(x='alcohol', kde=True, data=car_crash)
#sns.histplot(data=car_crash, x='total', stat='probability', discrete=True)
#sns.histplot(data=car_crash, x='speeding', log_scale=True, fill=False, element='step')
#sns.histplot(car_crash, x='alcohol', y='speeding')
sns.histplot(car_crash, x='alcohol', element='poly')
#sns.histplot(data=car_crash, x='speeding')
sns.set_color_codes('muted')
sns.barplot(x="abbrev", y="total", data=car_crash,
            label="Total", color="b")

plt.show()
