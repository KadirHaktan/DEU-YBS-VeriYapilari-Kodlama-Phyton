

#Nesne Yönelimli Programlama(Object Oriented Programming) alakalı giriş bir örnek olmakla beraber burda olabildiğimce
#SOLID prensibi olan Single Responsibility Principle ve Design Patternlarını uygulamaya çalışmış bulunmaktayım.Tabi bu OOP nedir,
#mantitiletesi nedir,neden gerçek hayat örneklerinde tercih ediliyor,sağladığı avantajlar vs biraz konuşmak isterim.

#Nesne Yönelimli programlama dediğimiz husus aslında en basidiyle gerçek dünyadaki herhangi bir insanı,bir cisimi,yapilan işlemi kısacası
#her türlü kavramı nesne olarak düşünelerek programlama yapılması diyebiliriz.Tabi bu nesnenin bazı işlevleri ve özellikleri olur ve
#bu nesne gibi birden fazla benzeri olabilir yani fonksiyonları ve sahip olduğu özellikleri başka bir nesnede de olabilir.O zaman
#bu nesneler bir gruba mensuba olabilir mi?Evet olabilir ve öyledir :) Yani aslında bu birbine benzeyen nesneler ait oldukları
#bir **sınıfları(Class)** vardır.

#Sınıfda aslında en basit anlamda katkısı şudur ki: Nesnelere ait özellikleri ve işlemleri(metot ya da fonksiyon da denilebilir)
#saklamamızı sağlar.

#Birbine benzeyen nesneler bir gruba ya da sınıfa mensuptur demiştir.Ama sadece böyle bir durum yoktur.Mesela
#bir şirketteki herkes aslında çalışan ve bu çalışanlar ortak özellikleri arasında hepsinde bir ad,soyad ve ID gibi
#özellikleri var ama aynı zaman da çalışanlar arasında yöneticilerde var ya da diyelim ki yazılım geliştiricileri de var
#demi?Mesela yazılım geliştirici kullandığı programlama diller alakalı bir bilgimiz yani özelliğimiz de olabilir ama tabi
#halan herkes gibi bir adı,soyadı ve ID numarası da var.O zaman yazılım geliştiricisi çalışan grubunun özel bir çeşidir ya da
#alt sınıfıdır diyebiliriz.Hangi çalışan olursa bahsettiğimiz özelliği çalışan grubundan almaktadır yani aslında çalışanlar grubu
#diğer özel gruplara bu özellikleri **miras etmektedir(inheritance(kalıtım))**

#Her çalışana ait tam bilgi bize gösterebileceği bir arayüz sağlayan bir işlevi olabilir;ama her çalışana ait tam bilgileri
#gösteren yapı hepsinde aynı olmayabilir yani genel çalışan da sadece ad,soyad ve ID bilgilerini gösterirken;fakat bir yazılım
#geliştiricisi ile alakalı işiyle alakalı bilgilerde almak isteyebiliriz veya da maaş bilgisini de isteyebiliriz.Bir çalışan örneği
# de verecek olursak yönetici olan çalışanların da mesela yönettiği departman olabilir,kademe bilgisini alabiliriz.
#her çalışan alacağımız bilgiler farklı bir şekilde sistemizde değiştirerek bize farklı farklı sonuçlar vermesini sağlayabiliriz.
#Yani kısacası sahip olanan işlevi içeriği değiştirebiliriz ya da **genel yapısından soyutlaştırabiliriz(abstraction)**.OOP'de
# **soyutlama** dediğimiz mevzu burda yer almaktadır.


##OOP'nin soyutlama teknikleri ile kalıtım yapısını kullanabilmemiz sayesinde gerçek dünya örnekleri geliştirme de
##bize de esnekliği açık olması yönüyle ya da üzerinde yapılacak değişimler de geliştirdiğimiz uygulamanın adapte olabilmesinde çok önemli
##katkıları vardır.Yani uygulamamızı değişime açık olacağı için sürdürelebilir bir yapı oluşturmamız da katkısı olacaktır.Şimdi
##bir örnekle açıklamaya çalışırsak:Diyelim ki bir müşteri kaydı yapan basit bir web uygulaması geliştirmeksizin
#ve kullandığınız veritabanı sistemi MySQL.Fakat yarın öbür gün yöneticiniz ya da müşteriniz dedi ki ben artık Oracle
##veritabanında kayıtlarımı görmek istiyorum dedi.Şimdi ne yapmanız gerekir?Düşünelim MySQL için de olsun
##Oracle için de data manipülasyon işlemleri ve giriş işlemleri gerçekleştirmekteyiz.O zaman Veriye erişim sağlayabileceğimiz
##genel fonksiyonların yer aldığı bir yapı kursak daha sonrasında bu genel yapıyı miras olarak alabilecek bir Oracle ve MySQL yapıları
##yer alsa güzel olmaz mı?Olur çünkü bakın hepsi Insert işlemi hepsi Delete işlemi yapabilecek sadece işlemlerin içerikleri farklı;
##Genel yapı ya da altyapı aynı bakacak olursak.Görselleştirirsek örneğimizi

##IDataAccessLayer(Genel Veri Erişim Katmanı ya yapısı)=>***Bu genel yapı***
## -Veri Ekleme işlemi
## -Veri Silme işlemi
## -Veri Güncelleme işlemi
## -Veri Getirtme işlemi


##MySQLDataAccessLayer(MySQL için Veri Erişim yapısı) Miras alıyor=>IDataAccessLayer

## -Veri Ekleme işlemi
## -Veri Silme işlemi
## -Veri Güncelleme işlemi
## -Veri Getirtme işlemi


##OracleDataAccessLayer(Oracle için Veri Erişim yapısı) Miras alıyor=>IDataAccessLayer

## -Veri Ekleme işlemi
## -Veri Silme  işlemi
## -Veri Güncelleme işlemi
## -Veri Getirtme   işlemi


#Dikkat ederseniz iki sınıfta genel yapıdaki işlemleri kullanmaktayım ama işlemlerin içerikleri farklılık olacaktır.Yani veritabana
#örnek verirsek ekleme kodları her ikisinde de aynı şekilde yazılmayacaktır.Aynı işlevler ama işlevlerin işleyiş şekli farklı olacaktır.
#Genel yapıdan da kesinlikle farklı olacaktır yani ondan soyutlanmış olacaktır.İşte zaten buna demin dediğimiz gibi soyutlamadır aslında.
#İşte OOP'deki soyutlama ve kalıtım tekniklerinin gerçek hayat dünya örneğinde nasıl bir etkisi olabileceğini sizde anlayabilmişsinizdir.

##Peki hadi bi de PostegreSQL için de istenildi.Yapılamaz mı?Yapılır nasıl olsa temel altyapımız var sadece
##sadece yeni bir yapı oluşturup altyapıdan miras alıp onun üzerine genel yapıdaki işlevleri genel yapıdan soyutlamamız
##yeterli olacaktır.İşte OOP sağladığı avantajlardan en önemlilerden:***Yeni bir sistem istenildiğinde mevcut altyapı baz alınarak
##diğer sistemleri etkilemeden rahatlıkla sistemi kurabilmekteyiz.İstenildikçe rahatlıkla yeni bir şey eklenebilmektedir***.
#SOLID dediğimiz yazılım geliştirme prensibinin O harfindeki **Open Closed Principle** buna söylemektedir.Yani yeni sistem kururken
#mevcut sistemleri etkilenmeden yani üzerinde değişiklik yapmamayı söylemektedir.Biz de bahsettiğimiz örnekte bu prensibi
#gerçekleştirmekteyiz.

##Bu kadar teoriden sonra isterseniz örneğimiz hakkında konuşmaya başlayalım.Senaryomuz şu en basit haliyle:
##Bir satici farklı olabilecek müşteri tipine bir ürün satacaktır ve müşteri ödeme yapacaktır.Tabi ödeme türleri farklı çeşitlerde
##olabilecektir.Nakit ya da taksit şeklinde ödeme olabilecektir.Siz tabi bunun üstüne daha farklı ödeme türü düşünebiliriz.Ama siz
##şu an mantığı oturtmaya çalışın derim.Bu arada farklı tip müşteriler de var demiştik.Ben burda gerçek ve tüzel diye iki farklı
##söyledim siz burda çeşitlendirebilirsiniz yine dediğim gibi.Şimdi bizim senaryomuzda gerçek müşteriler nakit ve taksit ödeme
##yapabilmektedir fakat tüzel müşteriler sadece taksit ödeme yapabildiğini düşündük.Siz yine kendinize göre farklılık yapabilirsiniz.
##Burda şimdi biz müşteri tipine göre kısıtlamaları nasıl yapabiliriz bunu düşünelim.

##Şimdi satıcı bir çeşit olacaktır çünkü bir satıcıdan bahsettik.O zaman Satici diye sınıfımız olsa ve satacağı ürünün fiyatı
##bilinse yeterli olunur mu?Olunur :D

##Gereksinim=> Satici

##Ama şimdi müşterilerimiz farklı olabilmekte ama aynı zamanda müşterilere ait ad ve ID özellikleri de ne kadar farklı türleri
##olursa olsun farklı olabilmektedir demi ama türleri sonuçta ve bu yüzden onlar hakkında bilgi veren bir yapı görmek istediğimizde
##içerikler de de farklı olacaktır demi?İşte bu yüzden IMüsteri diye genel sınıfımız olabilir ve üstüne Gerçek ve Tüzel için de
##yarattığımız sınıflarda IMüsteri'den miras alırsa hepsindeki ortak yapılar olmasıyla beraber aynı işlevleri olmasına rağmen
##içeriğini değiştirebiliriz demi?Aynen :D

##Gereksinimler=>IMusteri(Genel Müşteri yapısı)
                #GercekMusteri
                #TuzelMusteri


##Biz ödemelerimiz de müşterilerde gerçekleştirdiğimiz yapıyı kurabiliriz demi?Çünkü ödemelerin hepsinde bir ödeme olacak ama kimisi
##taksitle olacak kimisi de nakit olacak.Yani ödeme tipi değişecek.****Tabi aşağıda bu arada uyarıyım ben ödeme işlemleri hepsinde
##aynı şekilde hesaplayacak ama üstünde değişiklik yapılabilir.Siz ona aldırmayın :D Ben o açıdan tiplerin farklı olabileceğini
##alt sınıflarımda sadece string veri tipiyle belirttim şimdilik.Siz sonrasında ödeme esnasında yapılacak işlemleri değiştirebilirsiniz****

##Gereksinimler=>IOdeme(Genel Ödeme yapısı)
               #NakitOdeme
               #TaksitOdeme


##Şimdi müşteriye göre de ödeme şekillerinde kısıt olabileceğinden bahsetmiştik.Yani tüzeller sadece taksit ; ama gerçek müşteriler
##hem taksit hem de nakit şekilde ödeyebileceğini söyledik.Ben burda şurda mantık yürüttüm.Bu ödeme ve müşteri yapılarının bir
##genel hattı var demi o zaman genel hat olan yapıları bi arada oluşturup işlemlerini de gerçekleştirebileceğim bir toplu yapı ya da
## **Fabrika** düşündüm ve içersinde de genel yapıları çağırabilecem ve ayrıca  genel yapıların fonksiyonlarını da kullanabileceğim işlemler tanımladım.
##Yani müşteri ve ödeme nesnelerimi çağırabileceğimi,müşteri ve ödeme bilgilerini alabileceğim ve ödeme işlemlerini tek yerde yapabileceğim
#bir **fabrika** oluşturdum.Bu yapıya da aslında tasarım desenleri dediğimiz yapılardan bir tanesi olan Abstract Factory Design Pattern
#(Soyut Fabrika Tasarım Deseni) denilmektedir.Bu fabrika da genel hat kurulmaktadır ama bizim ödeme şekillerde müşteriye göre farklılık
#olmaktadır gerçekler hem nakit hem taksit ; ama tüzeller sadece taksit ödeyebilmekte.O zaman farklı fabrikalar ya da tüm işlemleri
#bi arada gerçekleştirmemi sağlayan fonksiyonlarun içeriğinde farklılık oluşturmam gerekir.Yani genel müşterisi nesnesi döndürecek
#fonksiyon yerine gerçek müşteri nesnesi döndürecek fonksiyon kullanmam gerekir aynı şekilde ödemeler de genel ödeme yerine ya taksit
#ya da nakit ödeme yapacak nesne tanımlamalarına gitmem lazım.Yani genel fabrikadan türecek farklı fabrikalar oluşturacam.O farklı fabrikadan
#metotları alacak ama içerikleri değiştirilecek yani soyutlanacaktır.

#Gereksinimler=>IBusinessFactory(Genel fabrika ve içersinde de genel odeme ve genel musteri yapıları kurulmakta ve işlemleri gerçekleştirilmekte)
                #TipBirGercekMusteriFactory(Nakit ödeme ve Gerçek Müşteri yapısı yer almakta)
                #TipİkiGercekMusteriFactory(Taksit ödeme ve Gerçek Müşteri yapısı yer almakta)
                #TüzelMusteriFactory(Taksit ödeme ve Tüzel Müşteri yapısı yer almakta)




#******************************************************************************************************************#
#Eğer daha detaylı araştırma yapacam derseniz,
#Google'dan muhakak design Pattern,Abstract Factory design ve SOLID yazılım geliştirme prensibi nedir araştırmanızı tavisye ederim :D
#Kafanızda bazı şeylerin daha iyi oturmasına da katkısı olması açısından da faydalı olur :)


#Kod açıklamaları yakında gelecektir.Ama yinede bu şekilde incelemenizi tavsiye ederim.Takıldığınız bir nokta olursa
#soru sormaktan çekinmeyiniz :D
#*******************************************************************************************************************#





class Satici:

    def __init__(self, urunFiyat):
        self.Fiyat = urunFiyat


#Burdaki kodda Satici ile alakalı olan ve satacağı ürünün fiyatı tutulduğu class yapısını oluşturduk.Satici alakalı
#bir nesne üretilebilmesi içinde urunFiyat değerinin tanımlanması zorunlu kıldırmış bulunmaktayız



class IMusteri:

    def __init__(self,):
        self.MusteriID = int()
        self.MusteriAd = str()




    def CustomerMoney(self):
        Butce=int(input("Müşterinin bütçesi:  "))
        return Butce

    #Müşterinin bütçe bilgisini alabilmek için müşteriden girilecek bilgi yoluyla bize Bütçe değerini döndüren fonksiyon


    def ShowCustomerInfo(self):
        return "MüşteriID=>", self.MusteriID, "MüşteriAdı=>", self.MusteriAd,

    #Müşteri ile alakalı bilgileri bize gösteren fonksiyon




#IMusteri dediğimiz sınıf Gerçek ve Tüzel müşteriler sınıfların miras veren sınıftır.Bu sınıfın sahip olan MusteriID ve MusteriAd
#özellikleri alt sınıflarında da geçerli olmakla beraber ShowTheCustomerInfo ve CustomerMoney dediğimiz fonksiyonlarda diğer
#ondan miras alan Gerçek ve Tüzel müşterilerinde de bu fonksiyonlarında da kullanabilmekte.Çünkü IMüşteriden miras aldılar.



class GercekMusteri(IMusteri):

    def __init__(self,):
        self.MusteriTip="Gerçek müşteri"
        super().__init__()

    def ShowCustomerInfo(self):
        return "MüşteriID=>", self.MusteriID, "MüşteriAdı=>", self.MusteriAd, "Müşteri Tipi=> ",self.MusteriTip


#GercekMusteri sınıfı görüldüğü üzere parantez içinde IMusteri dediğimiz zaman,Gercek Musteri sınıfı IMusteri sınıfından
#miras almaktadır.Miras aldığı içinde genel sınıfımız içinde yer alan ShowCustomerInfo ve CustomerMoney metotlarını
#uygulayabilmekteyiz.Biz burda kod olarak ShowCustomerInfo metotunu kullandık ve döndürdüğü değerde ufak bir değişiklik
#yapmış bulunmaktayız.Öte yandan IMusteri de tanımlamadığımız fakat bu ve diğer TuzelMusteri sınıfında tanımladığımız MusteriTip
#özelliğini de metin ifademizde ifade ederek metodun sonucunu döndürmüşüz.Fakat IMusteri sınıfımızda MüşteriTipi diye bir özelliği
#yok bu sebeple ShowCustomerInfo metodunda da değer döndürürken Müşteri Tipi bilgisine de göstermedik ama diğer iki sınıfta mevcut.Yani
#genel yapıdaki halinde farklılaştırdık yani soyutlaştırdık.

#Peki diyeceksiniz neden burda CustomerMoney fonksiyonunu kullanmadık?Aslına bakacak olursak bu fonksiyon GercekMusteri sınıfında çalışıyor
#ürettiğimiz nesne ile metodu çağırdığımız da fakat ben burda çağırmadım çünkü zaten müşterinin bütçesini dediğimiz şey tüm müşteriler
#için ortak bir şey yani bundan farklılaştırma yapmaya gerek yok.Genel yapıda bunu nasıl oluşturduysak diğer alt sınıflarda da bu yapı
#bu şekilde diğer sınıfta aynı fonksiyon aynı işlevsellik metot yer almaya devam edecektir.


class TuzelMusteri(IMusteri):
    def __init__(self,):
        self.MusteriTip = "Tüzel müşteri"
        super().__init__()

    def ShowCustomerInfo(self):
        return "MüşteriID=>", self.MusteriID, "MüşteriAdı=>", self.MusteriAd, "Müşteri Tipi=> ", self.MusteriTip


class IOdeme:

    def __init__(self, urunFiyat):
        self.urunFiyat = urunFiyat
        self.musteri =IMusteri()
        self.Satici = Satici(urunFiyat)


    def OdemeBilgileri(self):
        return "Ödeme ile ilişki özel içerik bilgi yer almamaktadır"

    def OdemeYapma(self):
        return self.Satici.Fiyat-self.musteri.CustomerMoney()

    #Ödeme işlemi gerçekleştiren fonksiyon.Bu fonksiyon diğer IOdeme'den miras alan sınıflarda da aynı şekilde
    #ödeme işlemini yapacağını düşündüğümüz için aslında burda bir kere tanımlamasını ve değeri döndürmesini
    #gerçekleştirdiğimiz için diğer sınıflarda ayrıtten tekrardan tanımlamaya gerek olmamaktadır.Bu fonksiyon hem
    #Tuzel de de çalışacaktır Gerçek Müşteri de de çalışacaktır.



#IOdeme dediğimiz sınıf Nakit ve Taksit olarak yapılacak ödemeler için genel yapıdır.Diğer iki sınıf(Nakit ve Taksit) IOdeme'den
#miras alacaktır.Odeme yaparken ithiyacımız olan iki husus vardır onlarda:Müşteri ve Satıcı.Tabi biz satıcı sınıfımızda
#bir nesne üretirken de urunFiyatını da zorunlu olarak girmeliyiz ki nesne üretilebilsin işte o yüzden bizde IOdeme sınıfından bir
#nesne üretilirken de zorunlu olarak urunFiyat değeri almamız gerektiğini init fonksiyonumuz da belirtmiş bulunmaktayız.

#IOdeme içinde de ödeme bilgilerini ve ödeme işlemini gerçekleştirebileceğimiz iki farklı fonksiyon bulunmaktadır.Ödeme bilgileri
#her ödeme şeklindeki farklılık olacağı için biz ödeme bilgilerini alacak fonksiyonu miras verdiğimiz sınıflarda içeriğini değiştirmekteyiz.
#Yani Nakit ödeme ödeme tipi Nakit derken Taksitte Taksit diyecektir.Genel sınıftaki o fonksiyonun yapısından farklılaştırmaktadır.Kısacası
#soyutlama söz konusu olacaktır.


class NakitOdeme(IOdeme):

    def __init__(self, urunFiyat):
        self.OdemeTipi = "Nakit"
        super().__init__(urunFiyat)


    def OdemeBilgileri(self):
        return "Ödeme tipi:",self.OdemeTipi,"Odeme Tutarı:",str(self.Satici.Fiyat)





class TaksitOdeme(IOdeme):

    def __init__(self, urunFiyat):
        self.OdemeTipi = "Taksit"
        super().__init__(urunFiyat)


    def OdemeBilgileri(self):
        return "Ödeme tipi:   ", self.OdemeTipi, "\nOdeme Tutarı:  ", self.Satici.Fiyat



#Genel sınıflarından nesnelerin üretildiği ve sahip olduğu fonksiyonların bi arada kullanıldığı genel fabrika sınıfımız.

class IBusinessFactory:

    def __init__(self, ID, Name, ProductPrice):
        self.ID = ID
        self.Name = Name
        self.ProductPrice = ProductPrice

    #Biz müşteriden ve ödemeden bir nesne ürettiğimiz de bu nesnelere ait bazı özellikler var onları tanımlayabilmek
    #için aslında burda Müşteri için ID ve Name özelliğini bir fabrika nesne oluşturduğumuz nesnenin oluşabilmesi için
    #bu değerlerin tanımlanabilmesini zorunlu kılıyoruz ve tabi zaten ödeme için de bir nesne ürettiğimiz zaman zorunlu olarak
    #ürünfiyatı ile alakalı bir değer de tanımlama zorunlu kıldırıyoruz.Bunun içinde fabrikamıza ait bir nesne ürettiğimiz de
    #ID ve Name'de olduğu gibi ProductPrice diye bir değerin tanımlamasını zorunlu kıldırıyoruz.



    def CreateInstanceToCustomer(self):
        Customer = IMusteri()
        Customer.MusteriID = self.ID
        Customer.MusteriAd = self.Name

        return Customer

    #Müşteri ile alakalı bir sınıftan nesne üretmek için kullanılan fonksiyon aynı zamanda Müşteriye ait ID ve Ad özelliklerini
    #Fabrika sınıfımıza ait ID ve Name özelliklerine ataması gerçekleştirmiş bulunmaktayız ve bize müşteri tipinde bir nesne
    #döndürmektedir



    def CreateInstanceToPay(self):
        Pay = IOdeme(self.ProductPrice)

        return Pay


    #Ödeme ile ilgili bir nesne üreten fonksiyonumuz.Ödeme nesnesi üretilirken fabrikamızdan nesne üretilirken
    #tanımlanması zorunlu hale getirilen ürün fiyatını ödeme nesnesini oluştururken parantez içinde tanımlamışız dikkat edersiniz.
    #Çünkü biz ödeme sınıfında da ürün fiyatı değerinin tanımlamasını zorunlu kıldırmıştık hatırlarsanız.



    def TransactionalOperations(self):
        pay=self.CreateInstanceToPay()

        print("Ödeme sonrası kalan para:  ",pay.OdemeYapma())

        print("Müşteri bilgileri:  ", self.CreateInstanceToCustomer().ShowCustomerInfo())

        print("Ödeme bilgileri:  ",pay.OdemeBilgileri())


    #Müşteri ile ödeme alakalı işlemlerini hepsini çağırabilmemizi ya da kullanabilmemizi imkan sağlayan fonksiyondur.
    #Bu fonksiyon diğer oluşturacağımız fabrikalarda da ortak olarak gerçekleşeceği için diğer fabrikalarımız da tekrar
    #tekrar TransactionalOperations fonksiyonu çağırıp içine kod yazmadık.Çünkü hepsinde ödeme ile müşteri alakalı
    #işlemleri gerçekleştirecektir.Fark şurda olacaktır üretilen nesnelerde değişiklik olacaktır ve o nesneleri üreten
    #fonksiyonlar üzerinde soyutlama yapılacaktır.




class TipBirGercekMusteri(IBusinessFactory):

    def CreateInstanceToCustomer(self):

        Customer = GercekMusteri()
        Customer.MusteriAd = self.Name
        Customer.MusteriID = self.ID

        return Customer

    #Müşteri nesne türümüz Gerçek müşteri olunmuş.Genel fabrika sınıfımızda ise IMüşteri nesnesi üretilmişti yani Gerçek Müşterinin
    #miras aldığı sınıf.


    def CreateInstanceToPay(self):
        Pay = NakitOdeme(self.ProductPrice)
        return Pay

    #Ödeme ile alakalı IOdeme yerine ondan miras alan Nakit Ödeme türünde bir nesneyi üreten fonksiyon.





class TipIkiGercekMusteri(IBusinessFactory):

    def CreateInstanceToCustomer(self):
        Customer=GercekMusteri()
        Customer.MusteriAd=self.Name
        Customer.MusteriID=self.ID

        return Customer


    def CreateInstanceToPay(self):
        Pay=TaksitOdeme(self.ProductPrice)
        return Pay



gercek_musteri_1 = TipBirGercekMusteri(1001, "Haktan", 10000)
gercek_musteri_1.TransactionalOperations()

print("")


gercek_musteri_1=TipIkiGercekMusteri(gercek_musteri_1.ID,gercek_musteri_1.Name,gercek_musteri_1.ProductPrice)
gercek_musteri_1.TransactionalOperations()


#***Son olarak şunu söylemek isterim dikkat edersiniz satici ile alakalı işlemler ya da özellikler bir sınıf,müşteri için ayrı ve
#ödeme için de ayrı bir sınıf tanımlamaları yapıp bunlara ait sadece kendileri ile alakalı fonksiyon ve özellik atamaları
#yapılmaya çalışınıldığı.Diyeceksiniz müşteri içinde ya da ne biliyim satici içinde bir şekilde ödeme işlemlerini yapamaz mıydık?
#Ama biz ödemeyi de müşteri ve satıcı da farklı objeler olarak bakmaktayız onlara yüklediğimiz işlemler ve yapılar sadece onlara
#ait olmalı diye düşünülmektedir.Kısa tabirle bir sınıf sadece kendisiyle alakalı işlemler yapılmalı ya da tek tip işlemler yapılmalı
#Buna SOLID yazılım geliştirme prensiplerindeki S harfinde yer alan Single Responsibility Principle prensibi denmektedir.****

#Bu konuda da daha çok araştırma yapmak isterseniz google'dan muhakak araştırmanız öneririm.Çünkü kodlama yazma bakış açınıza
#fark yaratacak konulardır.Takıldığınız nokta da sorularınız olursa lütfen grupta soru sormaktan asla çekinmeyiniz