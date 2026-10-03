import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure(figsize=(15,10))
df = pd.read_csv('iris_data.csv')

plt.subplot(2,3,1)
plt.scatter(df['SepalLengthCm'],df['SepalWidthCm'], color = 'blue')
k1,b1 = np.polyfit(df['SepalLengthCm'],df['SepalWidthCm'],1)
plt.plot(df['SepalLengthCm'],k1*df['SepalLengthCm']+b1,color = 'red')
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')


plt.subplot(2,3,2)
plt.scatter(df['SepalLengthCm'],df['PetalLengthCm'], color = 'blue')
k2,b2 = np.polyfit(df['SepalLengthCm'],df['PetalLengthCm'],1)
plt.plot(df['SepalLengthCm'],k2*df['SepalLengthCm']+b2,color = 'red')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')


plt.subplot(2,3,3)
plt.scatter(df['SepalLengthCm'],df['PetalWidthCm'], color = 'blue')
k3,b3 = np.polyfit(df['SepalLengthCm'],df['PetalWidthCm'],1)
plt.plot(df['SepalLengthCm'],k3*df['SepalLengthCm']+b3,color = 'red')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalWidthCm')


plt.subplot(2,3,4)
plt.scatter(df['SepalWidthCm'],df['PetalLengthCm'], color = 'blue')
k4,b4 = np.polyfit(df['SepalWidthCm'],df['PetalLengthCm'],1)
plt.plot(df['SepalWidthCm'],k4*df['SepalWidthCm']+b4,color = 'red')
plt.xlabel('SepalWidthCm')
plt.ylabel('PetalLengthCm')


plt.subplot(2,3,5)
plt.scatter(df['SepalWidthCm'],df['PetalWidthCm'], color = 'blue')
k5,b5 = np.polyfit(df['SepalWidthCm'],df['PetalWidthCm'],1)
plt.plot(df['SepalWidthCm'],k5*df['SepalWidthCm']+b5,color = 'red')
plt.xlabel('SepalWidthCm')
plt.ylabel('PetalWidthCm')


plt.subplot(2,3,6)
plt.scatter(df['PetalLengthCm'],df['PetalWidthCm'], color = 'blue')
k6,b6 = np.polyfit(df['PetalLengthCm'],df['PetalWidthCm'],1)
plt.plot(df['PetalLengthCm'],k6*df['PetalLengthCm']+b6,color = 'red')
plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')
plt.show()