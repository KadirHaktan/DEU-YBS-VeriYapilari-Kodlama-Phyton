

def BilgiTopla(liste,kaynak):
    liste.append(kaynak)

##kaynak listemizin içindeki her bir kaynağı alıp listenin içine ekleyen fonksiyon


def SosyalMedyaSayilariAlma(sosyal_Medya_sayi,liste):
    for i in liste:
        if i=="Sosyal Medya":
            sosyal_Medya_sayi+=1


    return sosyal_Medya_sayi

##liste içindeki kaynaklardan sosyal medya olanların sayısını toplamak için sosyal_Medya_sayi denilen bir değişkenle alacaz ve
##almak için de for döngüsüyle tüm liste dolaşıyoruz ve dolaşırken liste içindeki kaynaklardan Sosyal Medya olan varsa şait sosyal medya
##sayi denilen değişkenin sayi değerini 1 artıyor ve bu döngü sürdüğü sürece Sosyal Medyayı buldukça yapacaktır.Sonuçta fonksiyonda
##sosyal medya sayısının alabilmek için return ile değeri döndürüyoruz.


def OrganikAramaSayilariAlma(organik_arama_sayi, liste):
    for i in liste:
        if i == "Organik Arama":
            organik_arama_sayi += 1

    return organik_arama_sayi

##Bir Yukarsında  bahsettiğim olay burda da geçerli sadece organik arama alakalı liste içinde kaç tane olduğunu bulacaz


def UcretliReklamSayilariAlma(ucretli_reklam_sayi, liste):
    for i in liste:
        if i == "Ucretli Reklam":
            ucretli_reklam_sayi+= 1

    return ucretli_reklam_sayi

##İki üst yukarda bahsettiğim olay ile aynıdır sadece burda da ücretli reklam sayisini bulacaz



def MaximumSayiBul(sosyalMedyaSayi,UcretliReklamSayi,OrganikAramaSayi,liste):
    Social=SosyalMedyaSayilariAlma(sosyalMedyaSayi,liste)
    Search=OrganikAramaSayilariAlma(OrganikAramaSayi,liste)
    NotFreeAdvertisement=UcretliReklamSayilariAlma(UcretliReklamSayi,liste)

    if Social>Search and Social>NotFreeAdvertisement:
        print("Sosyal Medya araciliğiyla en çok sitemize ziyaret edilmekte\n")
        return (Social/(Social + Search + NotFreeAdvertisement))*100

    elif Search>Social and Search>NotFreeAdvertisement:
        print("Organik Aramalar ile en çok siteye ziyaret edilmekte\n")
        return (Search / (Social + Search + NotFreeAdvertisement)) * 100

    elif NotFreeAdvertisement>Social and NotFreeAdvertisement>Search:
        print("Ücretli Reklamlar aracılığıyla en çok siteye ziyaret edilmekte\n")
        return (NotFreeAdvertisement/(Social + Search + NotFreeAdvertisement))*100

    else:
        print("Ziyaretçilerin erişim kaynakların sayıları birbirine eşittir")
        return  ((Social + Search + NotFreeAdvertisement)/3)*100


#Maximum bulma fonksiyonunda da yukarıda kullandığımız sosyal medya,organik arama ve ücretli reklam sayılarını liste içindeki
#sayı miktarını elde ettiğimiz fonksiyonları kullandık ve bu bir sayı türünde bir değer döndürdüğü için de aslında biz bunları
#değişkenlere atayabiliriz ki daha sonrasında büyüklük karşılaştırma yaparken işimiz görsün.Yapılan karşılaştırmalarda büyük olan hangisi
#ise toplam kaynaklar arasında maximum sayıda bulunan kaynağın yüzde kaçlık dilimde olduğu fonksiyonda return ifadesi ile yüzdelik ifadesini
#döndürüyoruz


trafik_kaynak_liste=list()





while True:
    kaynak = input("Sitemize hangi kaynak aracılığıyla ulaştınız?  ")
    BilgiTopla(trafik_kaynak_liste,kaynak)

    devam = input("Ziyaretçilerimize halan soru sormak istiyor musunuz?  ")

    if devam=="Evet" or devam=="evet":
        continue

    elif devam=="Hayır" or devam=="hayır":
        break


print("")

sosyal_medya_sayi=int()
organik_arama_sayi=int()
ucretli_reklam_sayi=int()


maksimum_sonuc=MaximumSayiBul(sosyal_medya_sayi,organik_arama_sayi,ucretli_reklam_sayi,trafik_kaynak_liste)

print(maksimum_sonuc)