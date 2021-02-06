import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

continent = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
lifeExp = [49, 65, 60, 72, 74]
df = pd.DataFrame({"continent": continent, "lifeExp": lifeExp})

plt.figure(figsize=(8, 6))
splot = sns.barplot(x="continent", y="lifeExp", data=df)
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')
plt.xlabel("Continent", size=14)
plt.ylabel("LifeExp", size=14)
plt.show()
