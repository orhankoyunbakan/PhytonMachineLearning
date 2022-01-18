# Veri Ön İşleme Kodları

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset import edilir ve x ile y değişkenlerine aktarılır
dataset = pd.read_csv('AracVeriSeti2.csv')
X = dataset.iloc[:, :-1].values #son satır hariç hepsini x'e ata 
y = dataset.iloc[:, -1].values  #son satırı y'e ata
print(X)
print("--------------")
print(y)




#Eksik veriler doldurulur
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 4:6])
X[:, 4:6] = imputer.transform(X[:, 4:6]) #1.ve 2. satıra işlem uygula
print(X)


#Categorisal veriler numerik hale dönüştürülür
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,1,2,3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
print("-----------------")




# Dataset test ve train diye ikiye ayrılır
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)



# Nornalizasyon yapılır
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 4:6] = sc.fit_transform(X_train[:, 4:6])
X_test[:, 4:6] = sc.transform(X_test[:, 4:6])

print(X_train)
print(X_test)