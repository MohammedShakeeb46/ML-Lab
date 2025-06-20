'''Heat Map
Heat maps are useful for visualizing data in matrix form.'''

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.rand(10, 12)

# Create heat map
sns.heatmap(data, annot=True, cmap='viridis')
plt.title('Heat Map')
plt.show()

# using toyota dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("./ToyotaCorolla.csv")

sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet')
plt.show()
