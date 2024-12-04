import numpy as np
import pandas as pd 
data=pd.read_csv("AQI_Data.csv")
data.head(8) # to get starting 8 rows
data.tail() #to get the last 5 rows
data.info() # to get the data types and number of non null count 
np.mean('AQI') # to get mean AQI 
np.max('PM2.5') #to get max PM2.5
np.min('PM10') # to get min PM10 

import pandas as pd
data=pd.read_csv('AQI_Data.csv')
group=data.groupby['City'].avg('AQI').max('PM2.5').min('PM10')