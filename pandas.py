import pandas as pd
# Data link ... https://raw.githubusercontent.com/QCaudron/pydata_pandas/master/data/coffees.csv

data = pd.read_csv("https://raw.githubusercontent.com/QCaudron/pydata_pandas/master/data/coffees.csv")

print(data.head())


# Look at string in 3rd Row..
#.loc , .iloc
print(data.loc[2])

# Take a look at NaN Value..

print(data.coffees) # or data["coffees"]
# we see the 4th entry in NaN 

# Indexing on a series.. 
data.coffees[:5]

# How long is the dataset ?
print(len(data))  #671 data points

data.describe()

# Missing values?? .. 

data.isnull().sum()  # for all column variables

#          # Look at dataframe
# this gives us every row where NA appears. 
data[data.coffees.isnull()]

#What type of python objects are the columns?
data.dtypes
# coffee should be numerical not object and timestamp should be timestamp-type.

# print 1st element in the series timestamp (which is a column)
print(data.timestamp[0])

# print its type 
print(type(data.timestamp[0]))  #Its a string.

     # two problems. timestamp is string not datetime.
     # coffees contains NA and 1 string value.
# coerce turns errors into NA.
data.coffees = pd.to_numeric(data.coffees, errors="coerce")
data.dtypes # now coffees is float64.

# you could drop rows that are NA or fill them with the mean.. or interpolate,between dates.

data = data.dropna() # will drop all rows with NA. dropna(inplace=True)
data.head() # check 

data.coffees = data.coffees.astype(int) #Changed them from float to int. 
data.dtypes # Check
#Change timestamps into datetime objects.
data.timestamp = pd.to_datetime(data.timestamp)

data.describe()  #only shows coffees. 
data.describe(include="all") # shows all.. 

data[:5]
data.dtypes

data.coffees.plot()
# plotting against the index, not taking into account distance between data times.
data.plot(x=data.timestamp, style=".-")
# inspect last few points, 

print(data.tail(n=10))
# This part of the data doesnt tell us much.

# get rid of everything after the 1st of march.
data = data[data.timestamp < "2013-03-01"]
data.tail()

data.plot(x=data.timestamp, style=".-",figsize=(15,4))
# Main contributors  .value_counts()
data.contributor.value_counts()
# when plot against a series it plots against index, which are names.
data.contributor.value_counts().plot(kind="bar")


# On which weekdays were contributions made? ...   
#create a series of the weekdays
weekdays = data.timestamp.dt.weekday
weekdays
# assign it to dataframe
data = data.assign(weekdays=weekdays)
data.head() # check .. Good.

         
weekday_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday_dict = {key: weekday_names[key] for key in range(7)}
# 0: 'Monday' 1: 'Tuesday' 2: 'Wednesday' 3: 'Thursday' .. etc.


def day_of_week(idx):
    return weekday_dict[idx]


day_of_week(0)  # Just returns day of week given index 0-6.. 

data.weekdays = data.weekdays.apply(day_of_week)
data.head()

# count by weekdays, so group by weekdays. monday = #, tuesday = #..

weekday_counts = data.groupby("weekdays") # this wont give you any info

weekday_counts = data.groupby("weekdays").count()
print(weekday_counts) #re-order by our weekday_names vv

weekday_counts = weekday_counts.loc[weekday_names]
print(weekday_counts)
# Visualize these weekday counts.. 

weekday_counts.plot(kind="bar") # plots timestamp, coffees, contributor
weekday_counts.coffees.plot(kind="bar")

""" WEEKDAY TRENDS """ # ... 


data.index = data.timestamp
data.head()
# double timestamp  , drop it.
#axis =1 . look for columns to drop dont drop rows., inplace=True
data.drop(["timestamp"],axis=1, inplace=True)
data.head()

# Let's add some rows at midnight 

midnights = pd.date_range(data.index[0], data.index[-1], fred="D", normalize=True)
midnights  # 
# Take union of existing and new indices.
new_index = midnights.union(data.index)
# No repeats, because no one had coffee exactly at midnight.

# reindex our dataframe.. 
unsampled_data = data.reindex(new_index)
unsampled_data.head(10)  # we need to fill NaN's ..
# interpolate... # using time as index.
unsampled_data = unsampled_data.interpolate(method="time")
