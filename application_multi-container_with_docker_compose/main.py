# Veri setini indiriniz
# wget -O /tmp/dirty_store_transactions.csv \https://github.com/erkansirin78/datasets/raw/master/dirty_store_transactions.csv

######## Kütüphanlerin Import Edilmesi ve Ayarlar ########
import pandas as pd
import re
import warnings
from sqlalchemy import create_engine
import sqlalchemy
import time

warnings.simplefilter(action='ignore', category=Warning)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', None)
time.sleep(30)

username = ''
password = ''
host_name = ''
port = ''
database_name = ''

################## Connecting string ##################

engine = create_engine(f'postgresql://{username}:{password}@{host_name}:{port}/{database_name}')
######## Veri Setini Okuma ########
# df = pd.read_csv("dirty_store_transactions.csv")
url = "https://raw.githubusercontent.com/erkansirin78/datasets/master/dirty_store_transactions.csv"
df = pd.read_csv(url)
print(df.head(10))

######## Veri Setini Yapısal Hale Getirme ########

def clean_store_location(st_loc):
    return re.sub(r'[^\w\s]', '', st_loc).strip()

def clean_product_id(pd_id):
    matches = re.findall(r'\d+', pd_id)
    if matches:return matches[0]
    return pd_id

def remove_dollar(amount):
    return float(amount.replace('$', ''))

df['STORE_LOCATION'] = df['STORE_LOCATION'].map(lambda x: clean_store_location(x))
df['PRODUCT_ID'] = df['PRODUCT_ID'].map(lambda x: clean_product_id(x))

for to_clean in ['MRP', 'CP', 'DISCOUNT', 'SP']:
    df[to_clean] = df[to_clean].map(lambda x: remove_dollar(x)).astype(float)
    



print("\nDataframe clean transaction is succesfully.\n")

df.to_sql(name='cleandata', con=engine, index=False, if_exists='replace')

print('data transfer succesful')


