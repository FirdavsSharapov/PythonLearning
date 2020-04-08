# In python we have 2 options to import and work with CSV
import csv
from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'scr dest convert')


def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')


columns = [
    Column('vendorID', 'vendor_id', int),
    Column('passenger_info', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'tpeppickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float)
]
