import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')
sns.catplot(x="sex", y="total_bill",
            hue="smoker", col="time",
            data=df, kind="point",
            dodge=True,
            height=4, aspect=1)
plt.show()
