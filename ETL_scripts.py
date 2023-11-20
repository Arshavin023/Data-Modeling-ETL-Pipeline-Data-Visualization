# Importing Libraries
import pandas as pd
import numpy as np
import datetime as dt
from pandas import DataFrame


# Extraction of data 

yellow_taxi = pd.read_csv('CLOUD_STORAGE_URL')



# Transforming data
#### cleaning functions
def clean_ratecodeid(x):
    if x >= 6:
        value=6
    else:
        value=x
    return value

def evaluate_period(x):
    if x >= 4 and x < 6:
        period = 1
    elif x >= 6 and x < 12:
        period = 2
    elif x >= 12 and x < 16:
        period = 3
    elif x >= 16 and x < 20:
        period = 4
    elif x >= 20 and x < 24:
        period = 5
    else:
        period=6
    return period

ratecode=pd.DataFrame(np.array([[1,"Standard rate"],[2,"JFK"],
                                [3,"Newark"],[4,"Nassau or Westchester"],
                                [5,"Negotiated fare"],[6,"Group ride"]]),
                        columns=['ratecode_id','ratecode_name'])
ratecode.ratecode_id=(ratecode.ratecode_id).astype('int')

payment_type = pd.DataFrame(np.array([[0,"Credit card"],[1,"Cash"],[2,"No charge"],
                                [3,"Dispute"],[4,"Unknown"]]),
                        columns=['payment_type_id','payment_type_name'])
payment_type.payment_type_id=(payment_type.payment_type_id).astype('int')


store_and_fwd_flag = pd.DataFrame(np.array([[1,"Y"],[2,"N"]]),
                        columns=['store_and_fwd_flag_id','store_and_fwd_flag_name'])
store_and_fwd_flag.store_and_fwd_flag_id=(store_and_fwd_flag.store_and_fwd_flag_id).astype('int')


month = pd.DataFrame(np.array([[1,"January"],[2,"Febuary"],[3,"March"],[4, "April"],
                            [5, "May"],[6, "June"],[7, "July"],[8, "August"],
                            [9, "September"],[10, "October"],[11, "Novemver"],[12, "December"]]),
                        columns=['month_id','month'])
month.month_id=(month.month_id).astype('int')


weekday = pd.DataFrame(np.array([[0,"Monday"],[1,"Tuesday"],[2,"Wednesday"],[3, "Thursday"],
                            [4, "Friday"],[5, "Saturday"],[6, "Sunday"]]),
                        columns=['weekday_id','weekday'])
weekday.weekday_id=(weekday.weekday_id).astype('int')


period = pd.DataFrame(np.array([[1,"Early Morning"],[2,"Morning"],[3,"Afternoon"],
                            [4, "Evening"],[5, "Night"],[6, "Midnight"]]),
                        columns=['period_id','period'])
period.period_id=(period.period_id).astype('int')

yellow_taxi.tpep_pickup_datetime = (yellow_taxi.tpep_pickup_datetime).astype('datetime64[ns]')
yellow_taxi.tpep_pickup_datetime = (yellow_taxi.tpep_dropoff_datetime).astype('datetime64[ns]')

yellow_taxi['trip_duration_in_minutes'] = ((yellow_taxi.tpep_dropoff_datetime-yellow_taxi.tpep_pickup_datetime).astype('timedelta64[m]')).astype('int')
yellow_taxi['passenger_count'] = yellow_taxi['passenger_count'].fillna(1)
yellow_taxi['RatecodeID'] = yellow_taxi['RatecodeID'].fillna(1)
yellow_taxi['store_and_fwd_flag'] = yellow_taxi['store_and_fwd_flag'].fillna("N")
yellow_taxi['congestion_surcharge'] = yellow_taxi['congestion_surcharge'].fillna(0)
yellow_taxi['Airport_fee'] = yellow_taxi['Airport_fee'].fillna(0)
yellow_taxi['RatecodeID'] = yellow_taxi['RatecodeID'].apply(clean_ratecodeid)

### rename RatecodeID to ratecode_id
yellow_taxi.rename(columns={"RatecodeID":"ratecode_id"},inplace=True)

### rename payment_type column to payment_type_id
yellow_taxi.rename(columns={"payment_type":"payment_type_id"},inplace=True)

### Convert payment_type_id column to integer
yellow_taxi.payment_type_id = (yellow_taxi.payment_type_id).astype('int')

### Rename store_and_fwd_flag table to store_and_fwd_flag_id and replace "N" with 2 and "Y" with 1
yellow_taxi.rename(columns={"store_and_fwd_flag":"store_and_fwd_flag_id"},inplace=True)
store_and_fwd_flag_map = {"N":2,"Y":1}
yellow_taxi.store_and_fwd_flag_id=yellow_taxi.store_and_fwd_flag_id.map(store_and_fwd_flag_map)

# Create foreign keys
yellow_taxi['month_id']=yellow_taxi.tpep_dropoff_datetime.dt.month
yellow_taxi['weekday_id']=yellow_taxi.tpep_dropoff_datetime.dt.dayofweek
yellow_taxi['monthday_id']=yellow_taxi.tpep_dropoff_datetime.dt.day
yellow_taxi['period_id']=(yellow_taxi.tpep_dropoff_datetime.dt.hour).apply(evaluate_period)

result_dict = {"fact_table":yellow_taxi.to_dict(orient='dict'),
                "ratecode":ratecode.to_dict(orient='dict'),
                "payment_type":payment_type.to_dict(orient='dict'),
                "store_and_fwd_flag":store_and_fwd_flag.to_dict(orient='dict'),
                "month":month.to_dict(orient='dict'),
                "weekday":weekday.to_dict(orient='dict'),
                "period":period.to_dict(orient='dict')}


# Loading data

for key,value in result_dict.items():
    value.to_csv('{key}.csv')
