import numpy as np

data= np.random.rand (2,2,2)
print("birinci:",data)
np.delete(data, 0, axis=1) #sıfırıncı axin birincisini sil
print("ikinci:",data)

#kaydetmeyi-dışa aktarmaya yarıyor.
np.save("new array.npy",data)
test=np.load("new array.npy")
print(test)