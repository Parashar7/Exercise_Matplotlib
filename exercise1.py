import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# data = sns.load_dataset('penguins')
data1 = sns.load_dataset('flights').pivot(index='month', columns='year', values='passengers')
# print('Data of Penguins')
# print(data)
# print(data.shape)
# print(data.info())
# print('Data of Flights')
print(data1)
# print(data1.shape)
# print(data1.nunique())
# rint(data1.passengers.unique())#DO NOT INCLUDE INFO, GIVES ERROR FOR HEATMAP
# print(data1.month.unique())
# print(data1.year.unique())
# print(data1.info())  #DO NOT INCLUDE INFO, GIVES ERROR FOR HEATMAP
# plt.figure(figsize=(8, 4.5))
# plt.title('Passengers Footfall')
# sns.barplot('month', 'passengers', data=flights_df, hue='year')
# sns.heatmap(data1, fmt='d', annot=True, cmap='Blues')
# plt.show()
