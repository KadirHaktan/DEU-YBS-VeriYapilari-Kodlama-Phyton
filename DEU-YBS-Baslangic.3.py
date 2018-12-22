#Tuple(Demet) ve Dictionary(Sözlük) veri yapısı

#Tuple(demet)

#Tuple veri yapısı liste gibi hafıza da birden fazla veriyi bir yerde saklamak için kullanılan bir veri yapısıdır.Fakat şöyle
#farkı vardır Tuple içindeki herhangi bir veriye erişip üzerinde değişiklik yapılamaz.

#Tuple veri yapısı tanımlama Örnek

tuple1=("Haktan",11.5,55,True,False,"Veli",44,108.109)
#Demet tanımlarken demetin elemanları içine alması için (..,..,..,..) gibi bir kullanım yaptık
#tuple_type1=(..,..,..,..)

print(type(tuple1))
#Çıktısı <class 'tuple'>  verecektir.Yani bu değişkenin bir demet veri yapısı olduğunu söylüyor

for i in tuple1:
    print(i)
#Listelerle bir ortak yönü de listelerdeki gibi demet içinde de her bir eleman üzerinden geçerek dolaşmak
#için for döngüsü kullanabilmekteyiz

print()

print(tuple1[0]) ##Çıktısı ""Haktan""
#Yine listelerdeki herhangi bir elemana erişmek kullanılan index yapısını demet veri yapısında da kullanabilmekteyiz.

print()

##Tuple veri yapısında yapılmaması gereken bir hata

#Tuple için dediğimiz gibi tuple içindeki herhangi bir elemana erişip eleman üzerinde değişiklik ya da manipülasyon yapamayız
#Hatamızı bir örnekle görelim


#tuple1[0]=114
#Kodumuzu derlediğimiz de şu şekilde bir hata mesajı bize dönecektir:' TypeError: 'tuple' object does not support item assignment '
#Yani bu hata mesajın demek istediği şey şu: **Tip Hatası:Tuple objesi  değer atamasını desteklemez**.
#Değer atamaktan kastımız da bir tuple'daki elemanı yeni bir değerle eşitlemektir

#Bunu bir kanıtta yapmak istediğimiz de Phyton'daki Hata Yönetimi ile gösterecek olursak

print("Tuple içindeki birinci elemanı değiştirirsem ne olur??")
try:
    tuple1[0]=114
except TypeError:
    print("Cevap:Tuple içindeki herhangi bir eleman üzerinde değişiklik yapmak için uygun bir veri tipi değildir.!!Tip hatasıdır!!")


##Gördüğünüz gibi bu bir tip hatasıdır.Eğer except'in yanına başka bir tür Hata tipi(ZeroDivisionError,ValueError...) yazarsak
##Phyton'da kodu derlediğimizde Phyton hata ile ilgili kendi ingilizce olarak:
#TypeError: 'tuple' object does not support item assignment ' hatasını döndürecektir

#********************************************************************************************************************************#
##Peki biz neden try ve except gibi bloklarından faydalandık?
#Biliyorum bunlar biraz ileri konular ama yine de okumak isterseniz diye biraz açıklama yapalım

##Programlarımızı derleyip çalıştırdığımız da çalışma anında oluşabilecek hatalar olabiliyor ve
##bu hatalar da programızın kısmi ya da tamamen akışının ilerlemesini engel olabilmektedir.

##İşte çalışma esnasında oluşabilecek hataları yakalayıp programız çalışırken yapılması gereken diğer işlemler engel olmaması için
#Phyton'da hata yönetiminden faydalanırız.
#Bu hata yönetiminde önce try ile hatayı bulmaya çalışırız eğer try bloğu içinde bir hata görürse
#except'te hata var olduğunu bilir ama hatanın çıkmasını engelleyerek yapmak istediğimiz işlemleri devam etmemizi sağlar.


try:
    tuple1[0]=114
except:
    print("Cevap:Tuple içindeki herhangi bir eleman üzerinde değişiklik yapmak için uygun bir veri tipi değildir.!!Tip hatasıdır!!")

##Yukarıdak gibi exceptin yanına hatanın tipini belirleyeceğimiz gibi
#except diyip direk bloğumuzu açarak yapmak istediğimiz işlemleri kodlayabiliriz

#Output=>"Cevap:Tuple içindeki herhangi bir eleman üzerinde değişiklik yapmak için uygun bir veri tipi değildir.!!Tip hatasıdır!!"

#Görüldüğü Phyton try içindeki hatayı anlayıp except'e hatayı aktarabiliyor.

#*********************************************************************************************************************************#


#Not:Tuple'ların oluşturulması listelere göre daha hızlıdır.Çünkü aslında Tuple üzerinden yapılacak işlemler daha azdır diyebiliriz.
#Tuple'ın listelere göre daha az fonksiyonları vardır.

#Bunu görmek için veri yapısına ait tüm fonksiyon ve özelliklerini görmek için dir komutu kullanacaz ayritten.
#Bu dir komutu veri yapısına ait özellikleri ve fonksiyonların isimlerini her birini bir aslında liste içinde tutuyor.

#Dolasıyla liste'ye ait uzunluğa bakmak için de len fonksiyonuna bakabiliriz.Bu len fonksiyonu da veri yapımızın içinde toplamda
#ne kadar fonksiyon ve özellik olduğunu bize söyleyecektir.Bahsettiğim şeyin kodlaması şu şekildeki gibidir.

print("Tuple veri yapısında toplamda kaç fonksiyon ve özellikleri var: ",len(dir(tuple)))
print("Liste veri yapısında toplamda kaç fonksiyon ve özellikleri var: ",len(dir(list)))

##Görüldüğü gibi demetlere ait fonksiyon ve özellik sayısı listelere göre daha azdır.Bu da demek oluyor ki değişiklik ya da üzerinde oynama yapılmadan
##bu tuple'larımızı hafıza da bir seferde oluştarabilecez demektir.Bu da zaman açısından listelere göre oluşturulması daha hızlı olacaktır.


#*******************************************************************************************************************************#


#Dictionary(Sözlük veri yapısı)

#Dictionary ya da Sözlük veri yapısı liste ve demetler gibi hafıza da birden fazla veriyi ve veri türünü tutarız ama sözlüğün ikisinden de
#açık farkı şudur:Sözlük içindeki bir elemanda aslında iki yapı söz konusudur:
#1)Anahtar(Key)
#2)Değer(Value)


#Bunların kullanım örneği ve mantığı ile alakalı bir senaryo ile açıklamak gerekirse:

#Diyelim ki siz Google'un desteklediği mobil uygulama geliştirme yapılabilen Flunter Framework ve Dart programlama dilini öğrenmek istiyorsunuz.
#Fakat Türkçe olarak bir kaynak bulamadığınızı varsayın ve bu yüzden de bu konu hakkında İngilizce bir dokümantasyon ya da makale okuyorsunuz.
#O makalele de hiç daha önce karşınıza çıkmayan bir kelime çıktı ve kelimenin anlamını merak ettiniz.Anlamını araştırmak bir tane İngilizce-Türkçe
#çeviri yapabilen bir siteye girdiniz ve çevirme yapmak istediğiniz kelimeyi yazıyorsanız ve o size bir sonuç dönüyor

#Şimdi burada aslında çeviri yapmak içinde girdiğimiz kelime **anahtardır**
#ve çeviri yaptıktan sonra da bize dönen sonuçta aslında bir **değerdir**

#O çeviri web sitesinde her bir çevirilecek kelime ve sonuç verileri aslında web sitesine ait veritabanındaki bir tabloda ya da
#**veritabanı işlemler için kullanılan katmanda** veriler bir sözlük içinde tutuluyor gibi düşünebiliriz.

#Günümüzde özellikle bir platformdan  başka bir platforma veri gönderebilmek adına
#yani platformlar arası veri aktrarımı,alımı ve haberleşmesi için kullanılan veri format standardı olan JSON formatıdı da aslında verileri bir
#sözlük şeklinde tutmaktadır.İlişkisel olmayan veritabanlarında(MongoDb gibi) bu format kullanılmaktadır.

#Not:JSON'ın açılımı(JavaScript Object Notation(JavaScript Obje Notasyonu))

##Senaryo aslında şöyle işliyor gibi düşünebiliriz:
#Ara yüz katmanda yani web sayfasında biz çevirmek istediğimiz kelimeyi(**anahtar**) Çevir butonuna bastıktan sonra bir istek gönderiyoruz
#Bu isteğimiz gerçekleşme esnasında önce veritabanındaki tabloları erişir yani sözlük şeklinde tutulan verilerin yerine ulaşır
#daha sonra veriler ulaşıldıktan sonra bir kontrol katmana gider ve orada istek gönderdiğimiz verini karşılığı var mı diye kontrol ederiz.
#Eğer karşılığı bulanabiliyorsa şait istek gönderdiğimiz verinin(**anahtarı**) karşılığı(yani **değeri**) arayüzümüz yani web sitemize gösteririz.

#Tabi eğer istek gönderdiğimiz anahtarın karşılığını bulamıyorsak zaten bize bir hata mesajı dönecektir.
#Ama bizim burda ilgilendiğimiz şey aslında dict veri yapısının nasıl bir yerde kullanılabileceği hakkında bir örnektir.
#Tabi bu senaryo da aslında daha çok şey dahil edilebilir hatta dahil edilmesi gereken şeyler de var ama bu bizim konumuzun dışına çıkacaktır.


#************************Not********************************************#
##Yukarıda bahsettiğim senaryo alakalı bazı şeyler birazcık kulağa bir şey girmesi amaçlıdır.
#Bu sözel bahsettiğim şeyler sınavda çıkacaktır demiyorum.Hatta çıkmaz da!!
#************************************************************************#


#Dictionary kullanım

dict1={"Apple":"Elma","Book":"Kitap","Computer":"Bilgisayar"}

#Sözlük veri yapısı tanımlarken süslü parantez açıyoruz ve dediğim gibi her bir eleman gördüğünüz gibi iki yapıdan oluşuyor.

#{"Apple"=>(anahtar(key)):"Elma"=>(değer(value))}

#Sözlük içinde anahtar Apple olmakta değer de Elma olmaktadır.Şöyle de diyebiliriz Apple'ın **değeri** Elmadır,Elma'nın **anahtarı** da Apple'dır.

#şu şekilde de kullanabiliriz.Kodumuzun daha hoş durması açısından

dict2={
    "Apple":"Elma",
    "Book":"Kitap",
    "Computer":"Bilgisayar"
}
##Bu şekilde kullanımı genelde JSON veri formatı oluştururken veya
##JSON veri formatı şeklindeki verilerin tutulduğu yapıda çok görülür

#Başka tarz kullanımlar

dict3={
     (1,2,3,4):(5,6,7,8),
     ((1,2),(3,4)):((5,6),(7,8)),
     "Bir":1,
     "5.5":5.5
}

##Sözlük içindeki elemanlara erişme yolları

print(dict3[(1,2,3,4)])
#sözlük içindeki bir değere ulaşmak için o değere ait anahtar değeri gördüğünüz gibi
#sözlük degiskeni ismi[anahtar] şeklinde sözlük içindeki değere ulaşmak için kullanılır
#Output=>(5,6,7,8)

print(dict3["Bir"])
#Output nedir tahmin edin??

print(dict3[((1,2),(3,4))])
#Output nedir tahmin edin??
#**********************************

print()

#Sözlüklere ait bazı fonksiyonlar

#Fonksiyonları for döngüsü ile kullanarak gösteriyor olacam

print("Dict3' e ait Değerler")
for i in dict3.values():
    print(i)

#dict3.values() ile dict3 sözlüğündeki bütün değerleri(value) bulan ve gerektiğinde gösterebilmezi sağlar.
#for döngüsü aracılığıyla da her bir value üstünde de dolaşarak her bir value'u yukarıdaki kodla yazdırmış oluruz.

print()
print("Dict3'e ait Anahtarlar")
for i in dict3.keys():
    print(i)

#dict3.keys() ile sözlükteki her bir anahtar bulup ve gerektiğinde gerektiğinde gösterebilmemizi sağlar.
#Yine yukarıdaki gibi her bir anahtar  üzerinde dolaşmak için for döngüsünden faydalandık

print()

print("Dict3'e ait Tüm Değerler ve Anahtarlar")
for a,b in dict3.items():
    print(a,"anahtarın karşılığı:","",b)

#dict3.items() ile dict3 sözlüğündeki tüm anahtar ve değerler hafızaya alınır.
#for döngüsü kullanırken dikkat ettiyseniz a ve b diye her bir eleman üzerinden dolaşım için değer kullandık.Peki neden iki değer oluşturduk?
#Aslında a sözlükteki her bir anahtar b ise de sözlükteki her bir anahtarın değeridir ve items() fonksiyonu da her iki yapıyı da hafızaya da aldığı için
#biz yazdırma işlemi yaparken a ve b değişkeninden de faydalanabildik.

#Output
#Dict3'e ait Tüm Değerler ve Anahtarlar
#(1, 2, 3, 4) anahtarın karşılığı:  (5, 6, 7, 8)
#((1, 2), (3, 4)) anahtarın karşılığı:  ((5, 6), (7, 8))
#Bir anahtarın karşılığı:  1
#5.5 anahtarın karşılığı:  5.5
















