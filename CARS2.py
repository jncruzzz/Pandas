import pandas as pd

cars=pd.read_csv('.spyder-py3/cars.csv')
#a.
cars.ix[:5,0:12:2]

#b.
cars[cars['Model']== 'Mazda RX4']

#c.
cars.loc[23, ['Model','cyl']]

#d.
cars.loc[[1, 18, 28], ['Model','cyl', 'gear']] 
