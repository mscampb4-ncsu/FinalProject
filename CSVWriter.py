#Import necessary modules
import pandas as pd
import time

#Import streaming data
power = pd.read_csv("power_streaming_data.csv")


#Randonly sample 5 rows of data, then write those 5 rows to a csv file
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html

for i in range(10):
    current = power.sample(n = 5, axis = 0) #axis = 0 corresponds to rows
    fileName = f"streamdata/power_stream_{i}.csv"
    current.to_csv(fileName, index = False) #Setting index to false removes row numbers from the output.
    time.sleep(10) #Pause for 10 seconds before iterating again.

