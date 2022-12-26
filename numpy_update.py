import numpy as np
import timeit

list1=np.random.rand(10)
list2=np.random.rand(10)

add = np.add(list1,list2) #toplama
sub=np.subtract(list1,list2)#çıkarma
div=np.divide(list1,list2)#çarpma
mult=np.multiply(list1,list2)#bölme
dot=np.dot(list1,list2) #tek bir değer döndürmeye yarıyor.
print(add)

sqrt = np.sqrt(25) #karekökünü alır
print(sqrt)

ab=np.abs(-2) #mutlak değeri
print(ab)

power=np.power(2,7) #üst sayılar 2 üzeri 7
print(power)
log=np.log(25) #logaritma hesaplama
print(log)
exp=([2,3])
print(exp)
mins=np.min(list1)
print(mins)
maxs=np.max(list1)
print(maxs)

list1.sort()
print(list1.sort())

data= np.random.rand (5,3,4) #shape matrixin kaça kaç olduğunu gösteriyor
print(data.shape)

#matrixini yeniden boyutlandırıyor.

data=data.reshape((2,2,-1)) #5 olanı 2 yapacağım 3 olanı 2 yapacağım -1 önemli değil, çünkü artan elemanları en sona ekleyerek yazdırıyor.
print(data.shape) #sondaki -1 kaç sütun olduğunu bilgisayarın karar vermesini sağlıyor.

zeroes = np.zeros((8))
print(zeroes)
zeroes= np.append(zeroes, [3,4]) #append eklemek komutu.
print(zeroes)

zeroes = np.insert(zeroes,2,1) #belirlediğin yere ekleme yapar.
print(zeroes)

#insert ve append fonksiyonları array de kullanıldığında index,satır ve sütunları tek bir satırda topluyor.

# // kalansız bölmek
# ** üs almak
print("-----------")
#Aggregition

listy_list = [1,2,3]
type (listy_list)

print(listy_list)

sum(listy_list)
print(sum(listy_list))

print("-----")

print(np.sum(listy_list))

#python metodunda ve datatype kısmında (sum()) kullanılıyor. Numpy metodlarında ve arraylerinde (np.sum()) kullanılıyor.

massive_array = np.random.random(100000)
massive_array.size

print(massive_array.size)
np.random.seed(1)

print("%timeit sum(massive_array)")
print("%timeit np.sum(massive_array)") #daha hızlı

listy_listt = [1,2,3,9,6,8]
np.mean(listy_listt)  #tümünün ortalaması
print(np.mean(listy_listt))

print(np.max(listy_listt))
print(np.min(listy_listt))
print(np.std(listy_listt))
print(np.var(listy_listt)) #varyans hesaplar,  higher çıkarsa yakın uzaklık - lower çıkarsa uzaklıkları fazla

#Standart Sapma Hesaplama
np.sqrt(np.var(listy_listt))

#Standart sapma ve varyansın demosu
high_var_array = np.array([1, 100, 200, 300, 4000, 5000])
low_var_array = np.array([2, 4, 6, 8, 10])

print(high_var_array)
print(low_var_array)

print("--")
print(np.var(high_var_array))
print(np.var(low_var_array))

print("--")
print(np.std(high_var_array))
print(np.std(low_var_array))

print("--")
print(np.mean(high_var_array))
print(np.mean(low_var_array))

print("--")

#grafik yapmak için kullanılıyor
import matplotlib.pyplot as plt
print(plt.hist(high_var_array))

print(plt.hist(low_var_array))
plt.show()

print("--")

np.random.seed(0)

mat1 = np.random.randint(10, size=(5,3))
mat2 = np.random.randint(10, size=(5,3))
print(mat1)
print("-")
print(mat2)
print("-")
print(mat1.shape)
print("-")
print(mat1.shape)
print("-")
print(mat1*mat2)

print("---")

#numpy dot product

# 3x2 lik bir tabloda 3 satırlı ve 3 sütunlu tablodaki satırlar ile 2x2 lik tablodaki sütunu çarparak yeni bir parantez oluşturuyor.
#5 0 3      #4 7
#3 7 9      #5 9
            #3 2

# 5*4 0*5 3*3
#3*7 7*9 9*2

#yukarıda anlattığımız olay aşağıda örneği yapılmıştır.
#Transpose Mat1

print(mat1.T)
print(mat1.shape)
print(mat2.T.shape)

mat3 = np.dot(mat1,mat2.T)
print(mat3)
print(mat3.shape)
print(mat2)
print(mat1)
