import pystore
import pandas as pd

# Create a sample DataFrame
data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

df_slice = df.iloc[1:-1].copy()
df_leftout = df.iloc[[0,-1]].copy()

pystore.get_path()

pystore.list_stores()

store = pystore.store('tempstore')

collection = store.collection('test_collection')

store.list_collections()

collection.write('test_item', df_slice, metadata={'source': 'slice'})

collection.list_items()

item = collection.item('test_item')

df_read = item.to_pandas()

collection.append('test_item', df_leftout)

df_read = item.to_pandas()

# collection.list_items(source='Quandl')

collection.delete_item('test_item')
# store.delete_collection('test_collection')
# pystore.delete_store('tempstore')



...


