# -*- coding: utf-8 -*-


# Basit Lineer Regresyon
# Kütüphanelerin eklenmesi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# Veri setinin okunarak bağımlı ve bağımsız değişkenlere ayrılması
dataset = pd.read_csv('AracVeriSeti2.csv', encoding = 'iso-8859-9')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 8].values #4.sutun
y = y.reshape(-1, 1) #bir boyutlu array olması ölçekleme sırasında problem oluşturduğundan bu değişiklik yapıldı

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,1,2,3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)


# Veri setinin eğitim ve test olarak bölünmesi
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)



# Eğitim verileri ile modelin eğitilmesi
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Test verileri kullanılarak tahmin yapılması
y_pred = regressor.predict(X_test)

#Test değerleri ile tahmin değerleri arasındaki hata farkının hesaplanması
#Modelin başarısının ölçüldüğü kısım.
from sklearn.metrics import r2_score
Rkare= r2_score(y_test, y_pred)

