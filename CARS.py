import pandas as pd

cars=pd.read_csv('.spyder-py3/cars.csv')

a = cars.iloc[0:5]

b = cars.iloc[27:]

frames = [a, b]

result = pd.concat(frames)
print(result)
