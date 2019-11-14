# import package
import pandas as pd
import numpy as np

# import data
data = pd.read_csv('q2.csv')

# Check if shortage
data['shortage'] = 0
data.loc[data['quantity'] == 0, ['shortage']] = 1

# Group up (Shortage)
data_pivot = pd.pivot_table(data, values='shortage', index=['sport','family'], columns=['store'], aggfunc=np.sum)
data_pivot = data_pivot.reset_index()
data_pivot = data_pivot.fillna(0)
data_pivot['all_store'] = data_pivot[1614] + data_pivot[1618] + data_pivot[2350]
data_sum_family = data_pivot.groupby('family', as_index=False).sum()
data_sum_family['sport'] = 'zz_All'
data_sum_sport = data_pivot.groupby('sport', as_index=False).sum()
data_sum_sport['family'] = 'zz_All'
data_sums = data_pivot.select_dtypes(pd.np.number).sum().rename('zz_All')
data_pivot = data_pivot.append(data_sum_family)
data_pivot = data_pivot.append(data_sum_sport).set_index(['sport', 'family']).sort_index()
data_pivot = data_pivot.reset_index()
data_sums['sport'] = 'zz_All'
data_sums['family'] = 'zz_All'
data_pivot = data_pivot.append(data_sums)

# Group Up (Count Shop)
shop_count = pd.pivot_table(data, values='shortage', index=['sport','family'], columns=['store'], aggfunc='count')
shop_count = shop_count.reset_index()
shop_count = shop_count.fillna(0)
shop_count['all_store'] = shop_count[1614] + shop_count[1618] + shop_count[2350]
shop_count_family = shop_count.groupby('family', as_index=False).sum()
shop_count_family['sport'] = 'zz_All'
shop_count_sport = shop_count.groupby('sport', as_index=False).sum()
shop_count_sport['family'] = 'zz_All'
shop_count_sums = shop_count.select_dtypes(pd.np.number).sum().rename('zz_All')
shop_count = shop_count.append(shop_count_family)
shop_count = shop_count.append(shop_count_sport).set_index(['sport', 'family']).sort_index()
shop_count = shop_count.reset_index()
shop_count_sums['sport'] = 'zz_All'
shop_count_sums['family'] = 'zz_All'
shop_count = shop_count.append(shop_count_sums)

# Calculate Shortage Rate
data_pivot = data_pivot.set_index(['sport', 'family'])
shop_count = shop_count.set_index(['sport', 'family'])
shortage = data_pivot / shop_count *100
shortage = shortage.reset_index()
print(shortage)
shortage.to_csv('q2ans.csv', index=False)