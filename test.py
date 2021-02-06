import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('planets')
sns.histplot(
    df, x="year", y="distance",
    bins=30, discrete=(True, False), log_scale=(False, True),
    cbar=True, cbar_kws=dict(shrink=1),
)
plt.show()
