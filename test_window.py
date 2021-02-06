import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('fmri')

print(data, '\n\n', data.info(), '\n\n', data.nunique(), '\n\n', data.region.unique(), '\n\n', data.describe())
sns.lineplot(data=data, x="timepoint", y="signal", hue="region", style="event")
#sns.relplot(
   # data=data, x="timepoint", y="signal",
  #  col="region", hue="event", style="event",
 #   kind="line"
#)
plt.show()
