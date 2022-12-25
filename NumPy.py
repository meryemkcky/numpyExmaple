#matris yapıyoruz. liste 2 index li 3 satır ve 4 sütun
#kaça kaç array olduğunu belirleyerek içerisine kaçarlı sayı olduğunu yazıyoruz.
#çıktılar float olarak alıyor.
import numpy as np
data= np.random.rand (5,3,4)
zeroe= np.zeros ((2,3,2))
full=np.full((2,2,2),7) #2 indexli 2 satırlı ve 2 sütunlu matriksin içerisini 7 olarak dolduruyor.
ones= np.ones((2,2,2))  #2 indexli 2 satırlı ve 2 sütunlu matriksin içerisini 1 olarak dolduruyor.
print(data)
print(zeroe)
print(full)
print(ones)

arr = np.array([[1,2,3,4], [1,2,3,4]])
print(arr)

#4 elamnlı bir liste yaptıysan her iki index de 4 elemanlı olamalı, yazdırıyor üç elemanlı vs fakat bir hata da veriyor.

arr_two = np.array([[5,6,7,8], [1,2,3,4]])
print(arr_two)
print(type(arr))

shape = data.shape #matriksin kaça kaç olduğunu gösterir.
size = data.size #eleman sayısını belirtiyor.
types = data.dtype #tipini belirliyor.

print(shape)
print(size)
print(types)

arr=data[0] #array listesinde kaçıncı indexi görüntüleme
print(arr)
slicer = data[0:4] #birden fazla indexe sahip olduğunda kaçıncı indexe kadar göstereceğini belirtiyor.
print(slicer)

slicer_two= data [0][0:2] #Sıfırıncı indexin içerisindeki sıfırıncı satırdan ikinci satıra kadar alıyor.
print(slicer_two)

reverse = data[-1]
print(reverse)

singleval = data[0][0][0]
print(singleval)

range_array = np.arange (0, 10, 2)  #0 ile 10 arasında olacak 2 şer arttırma
print(range_array)

random_array = np.random.randint(0, 10, size=(3,5)) #0 ile 10 arasında 3 satırlık 5 sütunluk bir dizi oluşturma
print(random_array)

random_array.shape #satır ve sütun sayısı
random_array.size #eleman sayısı


# seed içerisine yazdığın sayılar hazır listeler onları yazarsan onu kullanıyor.
# Fakat seed kullanmadan yazarsan her seferinde farklı liste çıkarıyor karışına
np.random.seed(seed=99999)
random_array_4 = np.random.randint(10, size=(5,3))
print(random_array_4 )

np.random.seed(seed=7)
random_array_5 = np.random.randint(10, size=(5,3))
print(random_array_5 )

#Random listede görünen elemanları yazdırıyor, random listende hangi rakam yoksa onu yazmıyor.
np.unique (random_array_4)
print(np.unique (random_array_4))

print("-------")
np.random.seed(seed=3)
a4= np.random.randint(10, size=(2,3,4,5)) #sağdan sola doğru görüntüleme yapılıyor. En sağdaki 5 elemanlı satırı oluşturuyor.
#4 bir diamention da kaç satır olduğunu gösteriyor, 3 kaç boyutlu olduğunu gösteriyor. 2 ise aynı şeylerden iki tane olacağını gösteriyor.
print(a4)

print("-----")
print(a4.shape)#matriksin içerisindeki kaça kaç olduğu
print(a4.ndim) # 4 boyutlu ndim n kadar diamention

print("-------")

#git init -> Her proje oluşturduğumuzda bu komutu terminal üzerinden yazmamız gerekli ki git bizim dosyalarımızı takip edebilsin ve git üzerinden işlemler yapabilelim.
