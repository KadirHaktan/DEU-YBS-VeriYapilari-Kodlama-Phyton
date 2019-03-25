


#############################################################3


trafik_kaynak_liste=list()
##ziyaretçilerimizin ulaştığı kaynakları bir liste içinde tutuyoruz.Çünkü liste içinde sonradan kaynakların her birinden
##kaç tane olacağını gözlemlemize yarayacak


while True :##Doğru olduğu sürece döngü devam etsin dediğimiz döngü.Yani biz halan ziyaretçilerimizden bilgi almak istiyorsak
            ##Evet diyip continue anahtar kelimesiyle halan kullanıcılarıdan bilgi almaya devam ama istemiyorsak True olan False olacak ve
            ##break komutuyla döngüden çıkıcaz

     trafik_kaynak=input("Ziyaretçi olarak nereden ulaştınız?  ")
     ##trafik kaynaklarımızı string türünden alacaz ve kullanıcıdan alıyoruz gördüğünüz gibi
     trafik_kaynak_liste.append(trafik_kaynak)
     ##her seferinde kaynağı sordukça trafik kaynak listemizin içine append fonksiyonu ile ekleyecez

     devam=input("Ziyaretçilerimize halan nereden ulaştıklarını soralım mı?  ")
     ##Halan bilgi alıp almayacağımız sorduğumuz kısım

     if devam=="Evet" or devam=="evet":
          continue

     elif devam=="Hayır" or devam=="hayır":
          break




sosyal_medya_sayi=trafik_kaynak_liste.count("Sosyal Medya")
organik_arama_sayi=trafik_kaynak_liste.count("Organik Arama")
ucretli_reklam_sayi=trafik_kaynak_liste.count("Ücretli Reklam")

##count fonksiyonu liste içinde tuttuğumuz veriden liste içersinde kaç tane olduğunu bize integer(sayı) veri tipinde bir değer döndüren
##fonksiyondur.Sayı türünde bir veri döndürdüğüne göre de biz de bir değişkene de atayabiliriz ki bunu.Örneğin liste içindeki Sosyal Medya sayısını
##da sosyal_medya_sayi diye dediğimiz değişkene atamış olduk.

##Count fonksiyonu anlaşılması açısından bir örnekle yine söyleyim sizlere.Örneğin liste içinde Sosyal Medya metni 5 tane varsa eğer count fonksiyonu
##liste içinde tek tek dolaşarak Sosyal Medya denilen metni bulacaktır bulduğu yerde her seferinde sayının miktarını 1 artıracaktır ve döngü sona erene kadar
##devam edecektir ve sonuçta 5 tane Sosyal Medya olduğu için fonksiyon bize 5 değerini döndürecektir.


if sosyal_medya_sayi>organik_arama_sayi and sosyal_medya_sayi>ucretli_reklam_sayi:
     print("Ziyaretçilerimiz en çok sosyal medya aracılığıyla sitemize ulaşıyor")

elif organik_arama_sayi>sosyal_medya_sayi and organik_arama_sayi>ucretli_reklam_sayi:
     print("Ziyaretçilerimiz en çok organik aramalar aracılığıyla sitemize ulaşıyor")

else:
     print("Ziyaretçilerimiz en çok ücretli reklamlar aracılığıyla sitemize ulaşıyor")










