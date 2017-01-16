import csv
import pygeocoder
import pandas as pd
from time import sleep

from pygeocoder import Geocoder
df = pd.read_csv('./nec.csv')
address = df.Address


#loop through addresses and print to file
with open('geocoded_nec.csv', 'w') as outfile:
    for a in address:
    	sleep(0.3)
        result = Geocoder.geocode(a)
        if type(a) is str:
            print >>outfile, a + "," + str(result[0].coordinates)
