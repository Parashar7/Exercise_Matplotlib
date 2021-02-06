import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

data1 = sns.load_dataset('dots')
sns.lineplot(
    data=data1.query("coherence > 0"),
    x="time", y="firing_rate", hue="coherence", style="choice",
    palette="flare", hue_norm=mpl.colors.LogNorm(),
)
plt.show()
