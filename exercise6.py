import matplotlib.pyplot as plt
import seaborn as sns

flight = sns.load_dataset('flights')
may_flights = flight.query("month == 'May'")
print(may_flights)
sns.set_style('darkgrid')
plt.title('Passengers in the month of May')
sns.lineplot(data=may_flights, x="year", y="passengers")

plt.show()
