import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins').sort_values("flipper_length_mm", ascending=False)
print(penguins.info())
plt.figure(figsize=(8, 4.5))
plt.title('Penguins Data')
f, ax = plt.subplots(figsize=(6, 15))
# sns.lineplot(x='flipper_length_mm', y='body_mass_g', data=penguins, hue='sex')
sns.barplot(x='flipper_length_mm', y='body_mass_g', data=penguins.loc[100:200], label="flipper_length_mm", color="b")
sns.barplot(x='bill_length_mm', y='body_mass_g', data=penguins.loc[100:200], label="bill_length_mm", color="b")
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)

plt.show()
