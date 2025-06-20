'''Box Plot
Box plots are useful for visualizing the distribution of data and identifying outliers.'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random data
data = np.random.randn(100)

# Create box plot
sns.boxplot(data=data)
plt.title('Box Plot')
plt.show()

# Using toyota dataset
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./ToyotaCorolla.csv')

plt.boxplot([data["Price"],data["HP"],data["KM"]])

plt.xticks([1,2,3],["Price","HP","KM"])

plt.show()
