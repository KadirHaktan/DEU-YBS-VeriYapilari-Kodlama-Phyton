
#Liste veri yapısı,For Döngüsü ve Bazı Fonksiyonları

#Liste veri yapısı=>RAM 'de ya da hafıza da birden fazla veriyi tek bir yerde saklamak için kullanılabilen bir veri yapısıdır.
#Liste içinde farklı tipteki veri tipleri tutabilmektedir.İster int(sayi),ister string(karakter dizisi ya da metin),ister boolean ve isterseniz de
#double vb.değişkenlerde liste içinde tutabilirsiniz

#Aşağıdaki örnek kodda bir liste tanımlanmış ve liste içinde farklı tipte veri tipleri tutulmuştur
liste1=[102,45,"Mehmet",55.5,True,False,67.2]

print(type(liste1))#liste1 değişkenimizin ne tür bir değişken olduğunu bakmak için type fonksiyonunu kullandık ve çıktımız < class 'list'> olacaktır.
                   #Yani bir değişkenimizin bir liste olduğunu söyleyecektir
print()

#Listelerdeki herhangi bir elemana erişmek için indekslerden faydalanırız.İndeksleri şöyle düşünebilirsiniz:Liste içindeki her bir değerin adresi belirten yer diye
#düşünebilirsiniz.Örnekle açıklarsak

#liste1        =   [102,45,"Mehmet",55.5,True,False,67.2]
#liste1 indeks =   [ 0, 1 ,   2    ,  3 , 4  , 5   , 6]

#Mesela listedeki birinci elemanın yerini gösteren adres değişken yeri liste1 in 0.indekstir veya üçüncü elemanın indeksi 2.indekstir.

#İndekslerin başlangıç değeri 0'dır ve bitişi de listenin uzunluğunun 1 eksiğidir.Birinci elemanın indeksinin sıfır deme sebebimiz bu.

#İndeks ile elemana erişmek örneği

print(liste1[0])#Output=102
print(liste1[2])#Output=""Mehmet""

print()

#*****Küçük iki soru*******#

#print(liste1[4])=>Output nedir??
#print(liste1[6])=>Output nedir??

#***************************#


#Listelerle for Döngüsü kullanım

#Döngü nedir??
#İstediğimiz uzunlukta uzunluğumuz bitene kadar istediğimiz bir işlemi yapmak diyebiliriz.
#Bir senaryo örneği ile açıklacak olursam

#Bir okulda bir sınıfta derse başlamadan önce hocanın yoklama aldığını varsayalım ve sınıftaki öğrenci sayısı da 30 kişi olduğunu varsayalım.
#Şimdi hocanın öğrencileri belli bir sıraya göre isimleri ile beraber elinde yer alan bir listesi vardır ve liste içindeki her bir ismi okumaya başlayacaktır.
#Listedeki öğrenci derste var mı yok mu diye kontrol eder eğer varsa derste varsa var diye işaretlenir yoksa da yok diye işaretlenir.İşte bu işaretleme
#işlemini sınıftaki öğrenci sayısı kadar 30.öğrenci içinde bu işlem yapılıp bitene kadar bu işlem sürekli tekrar edecektir.

#İşte bu tekrarlama 30.'u da bitene kadar devam ettiği için **döngü** vardır.Aynı yere dönüp işleme devam ediyor ta ki otuzuncu işlem de bitene kadar.


#For 'u da belirlediğimiz uzunluğu geçene kadar istediğimiz işlemi yapmaya devam eden bir yapıdır

#**Yukarıdaki senaryo ile ilgili olarak daha sonra örnek paylaşacam**

#Örnek kullanım

for i in liste1:
    print(i)

#burdaki kodda yukarıda tanımladığımız liste1 içindeki her bir elemana erişmek için her bir elemanı i denilen değişkene atıyoruz ,liste içindeki
#her bir değeri i sayesinde geziniyoruz ve döngü içindeki istediğimiz işlemi gerçekleştiriyoruz.Buradaki işlem de liste1 içindeki her bir değeri yazdırıyoruz

#Bu döngü liste1'in uzunluğu neyse uzunluğu bitene kadar devam edecektir


#Aslında kısacası bu örnekte liste içindeki her bir değer üzerinde gezinmezi sağlayıp ve o gezindiğimiz değeri yazdırmamıza yaramıştır.

print()

#Başka for döngü örnek

for i in range(1,10):
    print(i)

print()

#Bu örnekte uzunluğumuz belirlemek için aslında range diye bir fonksiyondan yararlandık.Bu range fonksiyonu şunu yapıyor:1 dahil ama 10 dahil olmayıp
#1'den 9'a kadar olan sayılar üzerinde geziniyor.


###List veri yapısına ait bazı fonksiyonlar

#append =>Listemizin sonuna eleman eklemek için kullanılan bir fonksiyondur.Örnekle görecek olursanız

for i in liste1:
    print(i)
#*********
#First Output Before Used Append Function
#102
#45
#""Mehmet""
#55.5
#True
#False
#67.2
#*********

print()

liste1.append(555.34)
for i in liste1:
    print(i)
#*********
#Second Output After Used Append Function
#102
#45
#""Mehmet""
#55.5
#True
#False
#67.2
#555.34
#*********

#İnsert fonksiyonu
#Bu fonksiyonda da ekleme yaparız ama burada nerede ekleme yapmak istersek ekleme yapabiliriz

#Kullanımı şu şekildedir

print()

liste1.insert(2,"Ali")
#Bu fonksiyon içinde gördüğünüz gibi iki parametre ya da değer alıyor.
#Birinci parametre ekleme yapmak istediğimiz indeks ikinci parametre de belirlediğimiz indekse bir değer atıyoruz

#2.indekste önceden ""Mehmet"" değişkeni vardı.
# Peki o ne oldu?O değişken aslında listede 1 ilerledi ve onla beraber listenin uzunluğu 1 artmış da oluyor.
#Mehmet değişkeni artık 3.indekste yani listenin 4.elemanı oluyor.

for i in liste1:
    print(i)

print()
#Len fonksiyonu

#Len fonksiyonu listemizin uzunluğumuzu kaç olduğunu bulmak için kullanabileceğimiz bir fonksiyon

#Örnek kullanım

print("Listenin uzunluğu:",len(liste1))#Output=9
#Peki diyeceksiniz liste1 'i başta tanımladığımızda 7 elemanlı değil miyim?Sonradan listemize append ile listenin sonuna ve insert ile
# istediğimiz indeks yerine eleman eklediğimiz için listenin uzunluğu 7 değil 9'dur.

#İndeksler için sıfırdan başlayıp listen uzunluğunun bir eksiğine kadar devam eder demiştik
#O zamanlar listemizin son elemanına şu şekilde erişebiliriz demi?

#**print(liste1[len(liste1)-1])** =>Yani listenin uzunluğunu verisini almak için len fonksiyonu kullanıyoruz bunu da 1 ile çıkarıp daha sonra
#listenin uzunluğun 1 eksiğini indeks olarak alıp yazdırıyoruz gördüğünüz gibi.

#Output=>555.34
#Çünkü listenin son elemanına erişiyoruz ve son elemanda 555.34'tür.

print("Listenin son elemanı: ",liste1[len(liste1)-1])

##**Küçük bir soru**##
#Listenin ilk elemanına ulaşmak için liste1[0] yazmak yerine len fonksiyonunu kullanarak kapalı parantez içinde nasıl sıfırıncı indekse elde edebiliriz
#ya da nasıl birinci elemana ulaşabiliriz??
##******************##


#Dipnot:Stringler için aslında karakter dizisidir demiştim.
#Karakter dizisi dediğimiz içinde aslında bir metin içindeki her bir değer liste içinde tutuluyor.O açıdan string veri yapısı bir liste tipi de diyebiliriz.

#Örneke açıklayacak olursak

s1="VeriYapıları ve Algoritmalar"


print(s1[5])#Output=>a
print(s1[0])#Output=>V

print()

#İndeks ile erişim gördüğünüz gibi gerçekleşebiliyor.
#Bu indeks erişim de liste veri yapısına özgüdür.O zaman string veri yapısınında aslında bir çeşit liste olduğunun çıkarımın yapabiliriz.

#İndeks ile erişim sırasında ilk eleman V ile başlıyor o da sıfırıncı indeks son eleman yani 27.indekste r harfi olacaktır.
# Metin içindeki aradaki boşluklar da aslında karakter olduğu için listenin bir elemanıdır aslında.

for i in s1:
    print(i)

#Metin aslında bir liste olduğu için liste içindeki her bir eleman üzerinden de gezinebilecektir.
# O açıdan da for döngüsü ile beraber kullanılabilmektedir.