import seaborn as sns
import matplotlib.pyplot as plt

marks=[76,98.75,89,80]

sns.set_style("whitegrid")
sns.histplot(marks,bins=5)
plt.title("Marks")
plt.show()