

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





class IMusteri:

    def __init__(self,):
        self.MusteriID = int()
        self.MusteriAd = str()




    def CustomerMoney(self):
        Butce=int(input("Müşterinin bütçesi:  "))
        return Butce


    def ShowCustomerInfo(self):
        return "MüşteriID=>", self.MusteriID, "MüşteriAdı=>", self.MusteriAd,



class GercekMusteri(IMusteri):

    def __init__(self,):
        self.MusteriTip="Gerçek müşteri"
        super().__init__()

    def ShowCustomerInfo(self):
        return "MüşteriID=>", self.MusteriID, "MüşteriAdı=>", self.MusteriAd, "Müşteri Tipi=> ",self.MusteriTip



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


class NakitOdeme(IOdeme):

    def __init__(self, urunFiyat,Butce):
        self.OdemeTipi = "Nakit"
        super().__init__(urunFiyat)


    def OdemeBilgileri(self):
        return "Ödeme tipi:",self.OdemeTipi,"Odeme Tutarı:",str(self.Satici.Fiyat)





class TaksitOdeme(IOdeme):

    def __init__(self, urunFiyat, musteri):
        self.OdemeTipi = "Taksit"
        super().__init__(urunFiyat)


    def OdemeBilgileri(self):
        return "Ödeme tipi:   ", self.OdemeTipi, "\nOdeme Tutarı:  ", self.Satici.Fiyat




class IBusinessFactory:

    def __init__(self, ID, Name, ProductPrice):
        self.ID = ID
        self.Name = Name
        self.ProductPrice = ProductPrice

    def CreateInstanceToCustomer(self):
        Customer = IMusteri()
        Customer.MusteriID = self.ID
        Customer.MusteriAd = self.Name

        return Customer

    def CreateInstanceToPay(self):
        Customer = self.CreateInstanceToCustomer()
        Pay = IOdeme(self.ProductPrice)

        return Pay

    def TransactionalOperations(self):
        pay=self.CreateInstanceToPay()

        print("Ödeme sonrası kalan para:  ",pay.OdemeYapma())

        print("Müşteri bilgileri:  ", self.CreateInstanceToCustomer().ShowCustomerInfo())

        print("Ödeme bilgileri:  ",pay.OdemeBilgileri())


class TipBirGercekMusteri(IBusinessFactory):

    def CreateInstanceToCustomer(self):

        Customer = GercekMusteri()
        Customer.MusteriAd = self.Name
        Customer.MusteriID = self.ID

        return Customer

    def CreateInstanceToPay(self):
        Customer = self.CreateInstanceToCustomer()
        Pay = NakitOdeme(self.ProductPrice, Customer)

        return Pay





class TipIkiGercekMusteri(IBusinessFactory):

    def CreateInstanceToCustomer(self):
        Customer=GercekMusteri()
        Customer.MusteriAd=self.Name
        Customer.MusteriID=self.ID

        return Customer


    def CreateInstanceToPay(self):
        Customer=self.CreateInstanceToCustomer()
        Pay=TaksitOdeme(self.ProductPrice,Customer)

        return Pay



gercek_musteri_1 = TipBirGercekMusteri(1001, "Haktan", 10000)
gercek_musteri_1.TransactionalOperations()

print("")


gercek_musteri_1=TipIkiGercekMusteri(gercek_musteri_1.ID,gercek_musteri_1.Name,gercek_musteri_1.ProductPrice)
gercek_musteri_1.TransactionalOperations()

