
#Algoritma,Big-0,Kod Karmaşıklığı

#Algoritma nedir?
#Algoritma:Bir problemin çözümü için çözümleri adımlaştırması ya da çözümleri aşama aşama yapılması diyebiliriz

#Örnek=>Kullanıcıdan alınacak iki sayının toplayarak ekranda göstermek isteyelim.
##Bu problemin algoritması nasıl olacaktır.Adım adım çözümler yapılacak.Aşağıdaki gibi sözde kodu yazılmış gibi yapılabilir.

#Sözde kod(Pousedo-Code)
#1)Kullanıcıdan 1.sayı al ve alınan sayıyı 1.sayı diye değişkene ata(eşitle)
#2)Kullanıcıdan 2.sayı al ve alınan sayıyı 2.sayı diye değişkene ata
#3)Toplam diye bir değişken tanımla
#4)1.sayı ile 2.sayıyı topla ve toplam denilen değişkene eşitle(ata)
#5)Toplama sonucu toplam değişkene atanan değeri yani kısacası toplam değişkeni ekrana yazdır

#**Burdaki söz kod aslında 5 tane aşama gösterilmiş işte bu 5 tane aşama aslında çözümlerdir ve bu çözümler adımlaştırarak
     #sorun çözülmüştür.İşte bu tür problem çözmeye aslında bilgisayar bilimlerinde **algoritma** denir**#


#Peki diyeceksiniz biz bu adımları sözde görerek anlamadık hadi basitçe kodları yazalım.
#İsterseniz aşağıdaki kodları yazmadan önce siz kodları tahmin etmeyi deneyin.
#Yapamazsanız aşağıdaki kodlara bakabilirsiniz.


#birinci_sayi=int(input("Birinci sayı:  "))
#ikinci_sayi=int(input("İkinci sayı      "))
#**Aslında burası sözde kodda adımlarından 1. ve 2. adım diyebiliriz.
#Şöyle ki bir kere dikkat edin input fonksiyonu ile biz kullanıcıdan değer alıyoruz ve aldığımız değeri int(sayı) tipine dönüştürüyoruz
#Çünkü Phyton'da input'tan önce int() şeklinde parantez açılıp bu fonksiyonu kullanmazsanız Phyton bu değeri string olarak bilecektir.
#Değerler alındıktan sonra dikkat edin alınan değerleri birinci_sayı ve ikinci_sayı diye değişkenlere eşitledik ya da atadık.

#**input()=>kullanıcıdan veri almak için kullanılan fonksiyon
#**int()=>parantez içine bir değişken yazıldığında o değişkeni integer tipine dönüştürecektir
#**input(int())=>O zaman burda da kullanıcıdan veri alınır int() fonksiyonu ile alınan değeri sayı tipine dönüştürür**#

##**1. VE 2.ADIM**#



#toplam=int()
##Burası 3.adımdır.Çünkü burda yaptığımız şey aslında toplam diye bir değişken tanımladık ve değişkenin tipi'de integer olarak
##belirledik
##**3.ADIM**#


#toplam=birinci_sayi+ikinci_sayi
##Burası da aslında 4.adımdır.
#Burda da birinci sayı ve ikinci sayıyı topladık ve önceden tanımladığımız toplam değişkenini iki sayının toplamına eşitledik.
##**4.ADIM**##

#print(toplam)
#5.adım ya da son adım diyebiliriz.Burda da print fonksiyonu ile konsol ya da terminal ekranına ya da bilgisayarda etkileşime geçecek arayüze göre
#ekranına göre ekrana toplam değişkenin sonucunu yazdırdık



##İşte en basit algoritma böyledir diyebiliriz.Tabiki daha karmaşık çözümlerle yapılmış algoritmalar daha çok ama en basit dille
##anlaşılması açısından anlatmaya çalıştım.

##Bu arada algoritma illa 5.adımda olmak zorunda değildir yani adımlarınızdan şöyle bir direk yapabiliriz toplam diye bir değişken
##tanımlayabiliriz ve hemen birinci ve ikinci sayının toplayıp o toplam değişkenini atayabiliriz yani sözde kodda şöyle de yazabiliriz

#Sözde kod(Pousedo-Code)
#1)Kullanıcıdan 1.sayı al ve alınan sayıyı 1.sayı diye değişkene ata(eşitle)
#2)Kullanıcıdan 2.sayı al ve alınan sayıyı 2.sayı diye değişkene ata
#3)Toplam diye bir değişken oluşturup 1.sayı ile 2.sayıyı toplayarak toplam değişkenine atayabiliriz
#4)Toplama sonucu toplam değişkene atanan değeri yani kısacası toplam değişkeni ekrana yazdır

##Yani daha kısa yolla da algoritmamızı oluşturabiliriz.Olabildiğince öz ve en kısa yolla çözüme kavuşmak algoritmamız ve programımız
##için önemlidir ve avantajlı olmaktadır.
#Fakat her zaman en kısa yolla çözüme kavuşalabilmeyebilir ya da çözüme istediğimiz şekilde ulaşamayabiliriz.
#Bazen bir tık uzayabilir ve çözüme ancak o bir tık uzun yolla istediğimiz şekilde çözüme kavuşabiliriz.

#Ama algoritmamızın performansının en uygun olabilecek ya da optimum  şekilde sorunumuzun çözüm bulması kriterlerimizdendir.

##Algoritmamızın gereksiz tekrarlardan uzak tutabilmekte başka bir kriterimizidir.Bunu da söylemeden es geçmeyelim.

##***Yine sizlere tavsiyem internet Algoritma nedir ya da algoritma diye Google'da arama yaparak araştırmalar yapmanızdır.***##

##Bunları söyledikten sonra BİG-O ve Kod Karmaşıklığı konularına giriş yapabiliriz


#Algoritma ya da Kod Karmaşıklığı

#Diyelim ki çözmek istediğim bir problem için iki farklı ama sonuçta aynı şeye varılabilen algoritmalarımız var ve hangisi kullanmamız
#gerektiği konusunda karar vermeliyiz.Akla gelince aslında çalışma hızlarını deneyerek bir çıkarım yapabiliriz.Ama bu sefer
#çalışma zaman hızı ile orantılı olmayabilecek bir bellek gereksinimi durumu söz konusu.Yani zaman olarak belki hızlı ama program
#çalışımı için gerekli bellek gereksinimine sahip değilse ya da verilerin tutulması için yeterli alan ayrılayamadıysa programımız istediğimiz
#şekilde çalışmayabilir.Kimi program hızlıdır ama çok bellek gereksinimi ister kimisi de tam tersi olabilir.

#O yüzden biz algoritmaları karşılaştırırken runtime(çalışma hızı) 'a göre karşılaştırma yapmayız.
#Bunun yerine BİG-0,OMEGA-0 ve THETA-0 dediğimiz kod karmaşıklığı fonksiyonlarından faydalanırız.
#Bu fonksiyonlar genel olarak programızdaki kodların ya da fonksiyonları ne kadar büyüme olduğunu gösterir.

#Biz burda En kötü durumda kodun büyümesinden yani BİG-O fonksiyonundan bahsedecez.Çünkü genelde algoritmanın büyümesi ya da
#karmaşıklığına bakılırken en kötü durumu incelenir

#BİG-0
#BİG-0 dediğimiz gibi kodun büyümesini gösteren bir fonksiyondur ve en kötü durumda oluşacak büyümeyi inceler.BİG-O'daki büyüme
#katsayısı ne kadar çok artarsa aslında algoritmamızın aslında o kadar çok da daha kötü durumda olur.Katsayımız tam tersine
#ne kadar çok küçükse de algoritmamız o kadar iyi durumda olduğunun bilgisine sahip oluruz.Tabi biz önce katsayılarını,karşılık gelen,
#sözlü ifadesini ve daha sonrasında birkaç örnekle BİG-O analizini anlamaya çalışacaz.Bu sözel kısım eminim tam yetmeyecektir :)


#Big-0           #İsim
#  1             #Sabit                                                         |
# log(n)         #Logaritmik(Parçalı ya da bölümlü diyelim :D)                  |  Aşağıya doğru gittikçe Big-O katsayıları büyümekte ve buna bağlı olarak kodda karmaşıklık
#  n             #Linear(doğrusal)                                              |  büyümekte ve bundan dolayı aşağı doğru gittikçe en kötü duruma doğru gitmektedir.
# n*log(n)       #Logaritmik Linear(Parçalı + Doğrusal gibi düşünelebilir)      |
# n^2            #Kuadratik ya da Kare                                          |
# n^3            #Kübük ya da Küp                                               |
# 2^n            #Eksponiyel(2 üzeri n ya da 2 tabanında üstel)                 |
#                                                                              ▼


#Pekala katsayıları gördük ama bunların hepsi ne anlama geliyor tek tek ve örneklerle anlamaya çalışalım.

#Big(O)=1 durum nedir?Sabitten kastımız nedir?
#1 aslında biz programımızda tek seferlik yaptığımız işlemlerdir.Örnek verecek olursak:Kullanıcıdan veri alma( Hani phyton'dan input fonksiyonu kullanıyorduk),iki sayı ya da sayılarla
#dört işlem yapmak,şart ifadeleri kullanarak verimizin istediği şartı sağlıyor mu ona bakmak(Phyton'da if else ve elif'lerden bahsediyorum) kısacası programımızda belirli uzunlukta değil
#anında yapılan bu işlemlerin büyüme hızına aslında biz sabit ya da BİG(0)=1 diyebiliriz.Örneklerle ve ilk algoritmamızı da anlatarak pekiştirmeye çalışalım.

#Şimdi ilk o algoritma örneğimizi kullanalım.Kodları tekrardan aşağıdadır

#birinci=int(input("Birinci sayı:  "))   #BİG(0)=1
#ikinci=int(input("İkinci sayı      "))  #BİG(0)=1

#toplam1=int()                           #BİG(0)=1

#toplam1=birinci+ikinci                  #BİG(0)=1

#print(toplam)                           #BİG(0)=1


#Şimdi burda da beş tane adım olmuş ve her birin yaptığı işlem aslında bir seferde.
#Neden çünkü herhangi döngüye ya da belirli uzunluk ya da zamana kadar biz tekrar tekrar işlemler yapılmıyor.
#İlk iki işlem program çalıştırdığımızda bir seferde yaptığımız aslında veri girişi ya da kullanıcıdan veri alma işlemi.
#Kullanıcıdan veri alınması her biri için program bitene kadar tek seferde olacağı için aslında her bir kod başına düşen en kötü durumda büyüme hızı 1'dir.

#Üçüncü işlemimizde aslında önceki iki işlem gibi benzerlik gösteren ama kullanıcıdan değer almayıp sadece veri türünü belirlediğimiz bir değişken oluşturduk.
#Bu da program çalıştığın an da sıra bu toplam1 değişkeni tanımlanması ya da hafıza da oluşturulduğu zaman program bitene kadar sadece bir kere yapacak o yüzden
#biz 3.aşama içinde diyebiliriz ki büyüme hızı 1'dir.

#4.işleme baktığımız zaman burda kullanıcıdan alınan iki sayı üzerinde toplama işlemi yapılmış ve 3.aşamada oluşturduğumuz değişkene eşitlenmiş.Evet burda aslında iki işlem yapılmış
#ama bu işlemler program çalıştığı süre içinde bir daha üzerinden geçilip aynı işlemler yapılmıyor yani tek seferde gerçekleşiyor o yüzden 4.kısım da da kodun büyüme hızı için 1 diyebiliriz.


#5.aşama üzerinde yaptığımız işlemler sonucu verimizi print ile ekrana yazdırıyoruz ve bu yazdırma işlemimiz programın çalışması esnasında bir seferde yapıp zaten son işlem olduğu için
#otomatikten programımız sona erecektir.Yani anlayacağınız gibi bu son aşamada aslında tek seferde yazdırma işlemini yaptığı için kodun büyüme hızı 1'dir.


#Pekala bir iki örnek daha inceleyelim beraber.Bu sefer if else statmentları kullanılalım.


#sayi=int(input("Bir sayı giriniz:   "))

#if sayi%2==0:
    #print("Bu sayı çift sayıdır")

#else:
    #print("Bu sayı tek sayıdır")


#Burda sadece BİG(0) analiz etmesine yönelik bir şey yaptığımız için şimdilik basit bir örnek verecem.
#Burda ne oluyor diyecek olursak girilen sayının çift mi yoksa tek sayı olduğunu mu kontrol ediyoruz.

#Şimdi kodların BİG(O)'sularından ve nedenlerini açıklayalım.

#Birinci kod da zaten önceden söylediğimiz gibi programı çalıştırdığımızda tek seferlik olarak süreklilik olmayacaktır.Yani tek seferde sayımıza girecez o yüzden Big(0)'su 1 olacaktır.

#İkinci kod ve üçüncü kod yani if ve else bloklarında programımızı çalıştırdığımızda sayıya girdiğimizde bir tane kontröl yapacak ve bu süreklikik ya da döngüsel bir süreç olmayacaktır.
#o açıdan da aslında if ve else bloklarında da Big(0)'su 1 olacaktır.


#Artık o zaman BİG(O) fonksiyonun sonucu  n ve log(n) olan BİG(0)'lardan bahsedelim ve ayrıca kod üzerinden karmaşıklığı da gösterelim.

#BİG(O)=n ve BİG(O)=log(n)

#Öncelikle n bize ne anlam katmalıdır bize şu anlamı bize idrak etmemiz gerekir.O da şu:Yazdığımız bir program yapacağımız işlemlerde döngü varsa ya da işlem tekrarlayarak belirli
#uzunluğa kadar işlem devam ediyorsa buradaki kodda karmaşıklığı n olacaktır.Peki neden n diyoruz?Çünkü biz fonksiyonumuzda 5 olsun 10 olsun kaça kadar işlem yaparsa yapsın denklemin
#gösteriliş literatüründe sonuçta belirli bir yere kadar ilerleyeceği için biz de uzunluğunu kaç olduğunu bilmek zorunda olmadan n diye bir değişken atayabiliriz ve o açıdan biz kodun BİG(O)
#olarak n denilir genel literatürde.Gelin örnek üzerinden gösterelim.

# Örneğimiz sıralı bir sayısının da aradığımız sayıyı aramak olsun.Yani derslerde de belki duyduğunuz basit bir doğrusal arama algoritması da diyebiliriz.


sayi_liste=[1,2,3,4,5,6,7,8,9,10]

aranan_sayi=int(input("Aradığınız sayıya giriniz:   "))

for i in sayi_liste:

    if(aranan_sayi==i):
        print(str(i)+". seferde aradığınız sayıyı buldunuz")
        break

    else:
        print(str(i)+". seferdesiniz daha sayıyı bulamadınız")



#Şimdi gelin kodlarımız inceleyelim ve BİG(O)'ları hakkında konuşalım.

#Bir kere en başta bir sayı listesi tanımlamışız ve dikkat edin sayılar sıralı bir şekilde liste içinde yer almış.
#Burda öyle yapmamız nedeni de aslında da en basit bir şekilde arama yapmak ya da doğrusal bir şekilde arama yapmak istiyoruz.
#Bu doğrusal aramada da aslında yaptığımız sayı listesinin uzunluğunu aşmadığımız sürece gördüğünüz gibi girdiğimiz sayı ile sayı listesinin içindeki sayı ile eşit mi diye
#kontrol ediyoruz sadece eşitse sayıyı kaçıncı sefer bulduysak break komutu ile döngüden çıkıyoruz eğer daha bulamadıysak bulana kadar döngü içinde dolaşmaya
#devam edecez bulunca da döngüden çıkacaz.
#İşte bu tek tek eşit mi kontrol yaptığımız için sayıları sıralı bir şekilde verdik burda.
#Yoksa sıralı olmasa sayılar üzerinde kontrol yapacağımız zaman eşittir operatörü yerine küçüktür ya da büyüktür gibi operatörlerden faydalanabilirdik.
#Zaten bu tür bir algoritmaya da doğrusal(linear) arama demeyecektir.

#Liste tanımlama işleminden sonra kullanıcıdan bir sayı alınmaktadır.Bu sayıda döngü içinde sayı listesindeki kaçıncı sayıdaysak o listedeki sayı ile kullanıcı olarak girdiğimiz sayı karşılaştırma
#yapılacaktır.Şimdi buraya kodlarımızın BİG(O)'su için diyebiliriz ki aslında BİG(O)'su 1'dir.Neden çünkü aslında buraya kadar yapılan işlemler aslında programımız çalıştığında bir seferde
#gerçekleşmiş oluyor yani buraya kadar süreklilik olmuyor.

#Şimdi kodlarımızdan asıl mevzuya yani döngü kısmından başlayalım.Şimdi öncelikle şunu kısa bir dipnot olarak söyleyelim genelde döngü bloğunun içinde yer alan her kodun karmaşıklığı
#aslında ya da kısacası döngü bloğunun olduğu yerde kod karmaşıklığı aslında BİG(O)'su n'dir.Neden peki?Çünkü biz döngüyü kullanma amacımız aslında belirlediğimiz uzunluğa kadar süreklilik
#sağlayarak işlem yapmamızdır.Şimdi belirli uzunluğu biz literatürde de 5 ya da 10 demeyiz de sayıyı aslında n diye bir değişkene atarız ve BİG(0)=n 'dir deriz aslında.
#Burdaki n aslında **uzunluk miktarı kadar bir değer** diyebiliriz.Peki kod üzerinden biraz detaylandıralım.



#for i in sayi_liste:

    #if(aranan_sayi==i):Big(O)=1(kod bloğu) * n(döngü)=n
        #print(str(i)+". seferde aradığınız sayıyı buldunuz")   ==> Buradaki if bloğu normalde aslında bildiğiniz gibi kod karmaşıklığı 1'dir ama döngü olduğu zaman aslında BİG(O)'da şöyle
                                                                   #bir işlemle n oluyor. if bloğu kod karmaşıklığı(1) * döngü uzunluğu ya da uzunluk miktarı(n) =n
                                                                   #daha kısa bir yazımla==>                        1  *  n   = n


        #break

    #else:Big(O)=1(kod bloğu) * n(döngü)=n
        #print(str(i)+". seferdesiniz daha sayıyı bulamadınız") ==>Yukarıda da olduğu gibi burda da kod karmaşıklığı 1*n ile n olacaktır.
                                                                   #Peki sözlü olarak nedeni için ne diyebiliriz?Diyebileceğimiz şey şu:
                                                                   #burada gerçekleşen eşitlik kontrol if olsun aksi durum olan else olsun program
                                                                   #çalıştığında bir seferde değil bizim belirlediğimiz uzunluğa kadar süreklilik arz ederek
                                                                   #kontrol devam ettiği için diyebiliriz.




#Peki buradan yaptığımız çıkarım döngü ile döngü bloğunun olduğu yerde kod karmaşıklığı n dedik ve aynı zamanda döngüden önceki kısımdaki kodların karmaşıklığına 1 dedik.O zaman toplam
#BİG(O) için n+1 ya da 2 tane kod karmaşıklığı 1 olduğu için n+2 mı diyecez?Aslında n+1 diyebiliriz ama genel literatürde biz yine kodun karmaşıklığı daha büyük olan n'dir o yüzden
#biz genel literatürde BİG(O) için yine n denilir.Bu arada Big(O)'su n ya da 1'in başına katsayı olarak(5*1,10*1,10*n,5*n)  hangi sayı olursa olsun başındaki katsayı önemli değil.
#Biz yine genel literatürde kodumuzun karmaşıklığına göre n ya da 1 deriz.


#**Önemli Dipnot**#

#**Peki güzel!!!Şimdi bir önemli noktada dikkatli olmamız gerekir.Gelin kodumuzu baştan aşağıda bir daha yazılmış haliyle o dikkat edilecek husustan bahsedelim**

#sayi_liste=[1,2,3,4,5,6,7,8,9,10]

#aranan_sayi=int(input("Aradığınız sayıya giriniz:   "))

#for i in sayi_liste:

    #if(aranan_sayi==i):
        #print(str(i)+". seferde aradığınız sayıyı buldunuz")==>Eğer kullanıcıdan girilen sayı 1'se ilk karşılaştırma esnasında 1.indexteki sayı 1'dir ve ikisi birbirine eşittir.
                                                                #O zaman eşittir bloğu çalışacak ve işlemler bir seferde hal olacak o zaman.Buradaki kodun Big(O)'su 1'dir.
        #break

    #else:
        #print(str(i)+". seferdesiniz daha sayıyı bulamadınız")


#Bu kodu derleyip çalıştırdığımız şöyle bir senaryo durum olursa,
#programımızı çalıştırdığımız örneğin aramak istediğimiz sayı direk 1 sayısı ise ve kontrol yaptığımız da 1 sayısını bulduk diye yazdırıp döngüden çıktığımızda buradaki kod karmaşıklığı
#gerçekten yine ** n midir ? **

#**Hayır değil!!!Hobaaa!!!Eeh,eğer bir kod üzerinden karmaşıklık incelemesi yaptığımızda eğer kodda döngü varsa direk BİG(O)'ya direk 1 demiyor muyduk?Diyorduk ama burda istisna bir durum
#var.Nedeni açıklayalım.Yukarıdaki kodu çalıştırdığımızda eğer sayı olarak 1 girersek
#döngü içinde sayı listesindeki ilk önce birinci sayı ile girdiğimiz sayı ile eşitlik kontrolü yapacaz ve tabi birinci sayı ile aradığımız sayı birbirine eşit olduğuna kanaat getirelecek
#ve yazımızı verecek hemen döngüden çıkacaz.O zaman burda bir kere programımız çalıştığında eşitlik kontrolü yapılacak yani tek seferde işlem yapacaz.
#O zaman kod karmaşıklığı için diyebiliriz ki 1'dir**.


#Umuyorum bu örnek ile BİG(O)=n mevzusu anlaşılmıştır.Şimdi o zaman BİG(O)=log(n)'den devam edelim.

#BİG(O)=log(n)

#log(n) diyince ne anlamalıyız biz?Öncelikle söyleyeceğim bir ifadeyle şunu anlayabilirsiniz:Bizim belirli uzunluk miktarımız var ve
#biz bu uzunluk miktarını belirlediğimiz parça sayısına bölümüdür diyebiliriz

#Yani örnek verecek olursak:Bir döngümüz var döngünün uzunluğu 100 diyelim eğer biz bu uzunluğu 10'ya bölürsek artık döngü uzunluğumuz 10 olacaktır ve yapacağımız işlemler artık uzunluk 10'a kadar
#sürecektir.

#Logaritma da aslında bizim 100'i kaça bölersek 10'u elde edeceğimiz yani 10'u kaç üst alırsak 100 olduğunu söyleyen bir fonksiyondur matematiksel açıdan.
#Böyle düşünürsek aslında uzunluğun 10 olması için 100'den kaç parça bölmemiz gerektiğini buluruz yani 2 buluruz ve uzunluktan da 2 ye böldüğümüzde artık döngümüzün
#yeni uzunluğumuz 10 olacaktır ve 10'a kadar işlemlerimizi gerçekleştirecez.

#O zaman diyebiliriz ki uzunluk/10 desek ya da uzunluk/2 diyelim farketmez biz bu uzunluk/2 ya da uzunluk/10'a değişken olarak log(n) diye bir değişkene tanımlayabiliriz.Yani önceden
#nasıl 10 denilen ya da 5 denilen uzunluk miktarına değişkene n diyip BİG(O)'suna n dediysek o zaman burda da eğer uzunluğu belirli bir sayıya ya da parçaya bölüp o yeni uzunlukta
#döngü içinde işlem yapıyorsak burada biz kod karmaşıklığına log(n) diyebiliriz.

#Örnek üzerinde görmeye çalışalım log(n) kod karmaşıklığının nasıl olduğunu
#Örnek olarak ikili arama algoritması örneği yapacaz.Bu algoritma nasıl algoritma nedir diye soracaksınız.
#Şöyle biraz açıklayalım:Elimizde diyelim ki 11 tane sayının yer aldığı ve sayıların sıralı olduğunu bir sayı listesi olduğunu düşünelim.Burda da ikili arama yapacaz diyelim.O zaman
#şöyle bir şey yapacaz:11 tane sayının sağ,orta ve sol diye aslında aslında yarıya ayırma yapacaz.Şöyle ki bir örnek üzerinden gösterelim

  #   sayı listesi=>    1,2,3,4,5,6,7,8,9,10
  #   yarıya ayırma=>   1,2,3,4,5|   6    |7,8,9,10,11
  #                       sol       orta       sağ


  #Şimdi burada biz ortadaki sayı 6 olarak kabul ederiz ve bizim de arama yapmak istediğimiz bir sayımız var ve ikisi üzerinde bir eşit midir karşılaştırma yaparız eğer şait aradığımız
  #sayı ile ortadaki sayı birbine eşitse şait sayıyı bulmuş oluruz ve hemen döngüden çıkarız burda da zaten kod karmaşıklığı 1 olacaktır.Çünkü tek seferde sayıyı buluyor.
  #Fakat değilse diğer iki durum yani aradığımız sayı ortadakiden küçükse ya da büyükse durumu olursa ne olacak?
  #Diyelim ki aradığımız sayı ortadaki sayıdan küçükse ne olacak o zaman listemizde aslında tam anlamıyla yarıya bölünme olacak
  #yani artık aradığımız sayı bulmak için artık sadece ilk beş elemana bakacaz ve burda artık yine karşılaştırma yapacaz.
  #Hatta burdaki ilk 5 elemandan da yarıya bölünme gerçekleştirebiliriz ya da sadece doğrusal sola kayarak karşılaştırma yapabiliriz

  #Birazcık liste üstünden gösterecek olursak

  #   1,2,3,4,5|      6     |7,8,9,10,11

  #aradığımız sayı 6'dan küçükse  o zaman durum şu olacak=>  1,2,3,4,5  |  6,7,8,9,10,11(Burayı artık unutalım!!!)
                                                             #artık yeni liste(eski listeden yarıya böldük ve sol kısmı aldık)=>1,2,3,4,5
                                                             #diyelim ki aradığımız sayı 2

                                                             #listenin son elemanı(5)<=2 ?? Hayır değil sola kay ve son eleman 4 olur
                                                             #4<=2  ?? Hayır değil sola kayma devam et
                                                             #Ta ki 2 yi bulana kadar yani: 2<=2 ? Evet eleman bulundu


  #Tabi burda aslında listede yarıya bölmeyi yaptıysak yarıya bölünmüş liste içinde de yeniden listede yarıya bölüm yapabiliriz şöyle ki :

  #Yeni yarıya bölünmüş liste=>1,2,3,4,5

  #Yeniden yarıya bölünmesi hali sonucu liste=>    1 , 2 |  3  |  4 , 5
                                              #     sol    orta    sağ

  #En son da dediğim gibi yarıya bölünmüş liste içinde yine yarıya bölebiliriz.Şu an için bu algoritmanın kodlarını buraya yazmayacam ama yakın zamanda hemenden
  #sizlere tam haliyle hazır olduğunda sizlere ikili arama algoritması kod örneği atacam ve kod karmaşıklığını kod üzerinden göstermeye çalışıcam












































