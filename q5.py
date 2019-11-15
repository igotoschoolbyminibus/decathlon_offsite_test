# Import Package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Import Data
data = pd.read_csv('q5.csv')
data = data.set_index('person_id')

# Descriptive Statistics
summary_data = data.describe()

# Check and remove outliers
top_5_data = data.sort_values(by=['ttl_to'], ascending = False).head()
top_5_person = list(top_5_data.index)
data_remove_outlier = data.drop(top_5_person)
new_summary_data = data_remove_outlier.describe()
data = data_remove_outlier

# Select Feature
selected_features = data[['ttl_txn_off', 'avg_qty_per_txn_off', 'avg_to_per_qty_off', 'ttl_txn_on', 'avg_qty_per_txn_on', 'avg_to_per_qty_on', 'to_share_online', 'to_share_gender_gap', 'to_share_kid', 'to_share_weekday', 'to_share_weekend']]

# Normalization before using K-means
scaler = StandardScaler()
scaled_features = scaler.fit_transform(selected_features)

# Find optimal n
sum_of_square_distances = []
K = range(1, 20)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(scaled_features)
    sum_of_square_distances.append(km.inertia_)
plt.plot(K, sum_of_square_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

# K-means clustering
kmeans = KMeans(n_clusters=7)
kmeans.fit(scaled_features)
labels = kmeans.predict(scaled_features)
centroids = kmeans.cluster_centers_
column_names = list(selected_features.columns)
centroids_df = pd.DataFrame(centroids)
centroids_df.columns = column_names
labels_list = list(labels)
data['labels'] = labels_list

# Analysis
## Check Number of Records for each group
unique, counts = np.unique(labels, return_counts=True)
dict(zip(unique, counts))

## Group Statistics
group_0 = data.loc[data['labels'] == 0]
group_1 = data.loc[data['labels'] == 1]
group_2 = data.loc[data['labels'] == 2]
group_3 = data.loc[data['labels'] == 3]
group_4 = data.loc[data['labels'] == 4]
group_5 = data.loc[data['labels'] == 5]
group_6 = data.loc[data['labels'] == 6]
summary_group_0 = group_0.describe()
summary_group_1 = group_1.describe()
summary_group_2 = group_2.describe()
summary_group_3 = group_3.describe()
summary_group_4 = group_4.describe()
summary_group_5 = group_5.describe()
summary_group_6 = group_6.describe()
writer = pd.ExcelWriter('q5result.xlsx')
summary_group_0.to_excel(writer, 'group_0')
summary_group_1.to_excel(writer, 'group_1')
summary_group_2.to_excel(writer, 'group_2')
summary_group_3.to_excel(writer, 'group_3')
summary_group_4.to_excel(writer, 'group_4')
summary_group_5.to_excel(writer, 'group_5')
summary_group_6.to_excel(writer, 'group_6')
writer.save()