import matplotlib.pyplot as plt
import numpy
from scipy import stats
from sklearn.metrics import r2_score
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")





# generating random data
#x = numpy.random.normal(5.0, 1.0, 1000)
#y = numpy.random.normal(10.0, 2.0, 1000)

#plt.hist(ages, 100)

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()


#predictedCO2 = regr.predict([[2300, 1300]])
scaledX = scale.fit_transform(X)
#regr.fit(X,y)

# when scaled
regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])

print(predictedCO2)

#print(regr.coef_)

#print(scaledX)











