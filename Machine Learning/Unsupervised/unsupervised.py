from sklearn.cluster import KMeans
import numpy as np

data=np.random.rand(100,2)

kmeans= KMeans(n_clusters=3)
kmeans.fit(data)

labels = kmeans.predict(data)

import matplotlib.pyplot as plt
plt.scatter(data[:,0], data[:,1], c=labels)
plt.title("Scatter chart")
plt.show()