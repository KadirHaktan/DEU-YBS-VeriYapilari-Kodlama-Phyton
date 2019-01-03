
##Örnek1

##5 tane öğrenci'nin matematik sınav notunu öğretmen sırasıyla okuyacaktır.Bu okuma işlemi nasıl yapılır?Buyrun aşağıdaki koda bakalım

Ogrenciler={
    1:("Kadir Haktan Yücesoy",73),
    2:("Ceyhun GünAteş",66.5),
    3: ("Selami GünSoy",88),
    4: ("Tarık Gürleci",91),
    5:("Zeynep Karasu",79)
}
##Burda gördüğünüz gibi Öğrenciler diye bir sözlük tipinde bir veri yapısı oluşturduk.Bu sözlük veri yapısında anahtar(key) olarak
##öğrencinin sıra numarası ya da sırası verisi saklıyoruz ve değer(value) olarak da gördüğünüz gibi tuple(demet) tipinde bir veri yapısı var ve bu veri
##yapısı içinde de bir isim-soyad ve matematik notu diye iki değişken tutulmuştur.

##Şimdi peki neden ben bu örnekte bir sözlük veri yapısı kullandım ve sözlüğün değer(value)'ni bir tuple tipinde şeklinde oluşturdum??

#Şimdi bizim bir sıra numaramız var ve öğretmen herkesin notlarını okurken notları daha hızlı okuması için bu sıra numarasına ithiyacı var.
#Bu sıra numarasına göre de bunun karşılığı ismi ve notu açıklaması da gerek tabi doğal olarak.
# Yani düşündüğünüzde sözlük şeklinde tutulmuş olması sizce de mantıklı değil mi?
#Çünkü siz eşşiz bir anahtar yapı sayesinde yani herkese özgü bir sıra numarası sayesinde notunu da görebilmektesiniz.
#O zaman bu örnekte sözlük veri yapısı kullanmak çok mantıksız olmayacaktır.


##Peki sözlükte value olarak neden tuple kullandık diyecek olursak:Sonuçta biz notta ve isimde bir değişiklik yapmayacaz.
#Tabi hoca not değerlendirmesi olursa burada tuple kullanmak sakıncalı olabilir hatta sözlük bile oluşturmayabilirdik.
#Ama biz burda notun hesaplanmasını doğru varsayarsak üzerinde bir daha değişiklik yapmayacaz.Hatırlayın tuple'lar listeler gibi
#index yardımıyla erişebilirdi ama index ile eriştiğimiz değer üzerinde yeni bir değişken tanımlaması ya da değeri değiştiremiyorduk.

#Dict'lerde üzerinde değişiklik yapılmayacak veriler sakladığı için aslında tuple saklayabiliyor ama liste veri yapısı saklayamaz.Çünkü demin ki
#hatırlattığımız farktan nedeni ile yani veri üzerinde değişiklik yapıldığı için liste tipinde veri yapısını bir sözlük içinde kullanamıyoruz.





for a,b in Ogrenciler.items():
    print(a,".Öğrenci ismi soyadı ve notu:{} ve matematikten {} almıştır ".format(b[0],b[1]))

##Burada yaptığımız şey şu:for döngüsü açtık ve for döngüsünde her bir key ve value üzerinde dolaşmamız gerekiyor.O yüzden burda her bir key için a
##değişkeni oluşturulmuş ve her bir value için de temsil edecek bir b değişkeni yaratılmış ve bunlar sözlük içinde bütün key ve value etrafında dolaşacak
##Bunu nerden anlıyoruz çünkü in Ogrenciler.items()'dan yani Ogrenciler sozluğundeki her bir key ve value'dur.

#Kısacası:keys+values=items gibi düşünebilir
#Burada bir Ogrenciler.items() dediğimizde bir fonksiyondur ve dediğimiz gibi sözlükteki tüm key ve value yapılarını gösterir.

#Döngü içinde bir yazdırma işlemi yapıldı görüldüğü gibi,a dediğimiz değişken dediğimiz döngü bitmediği sürece Ogrenciler sozluğundeki her bir key'dir.
#B dediğimizde yine yukarıda söylediğim gibi sözlükteki her bir value'dur.

##Şimdi format içindeki b[0]  b[1] nerden geliyor?Şöyle ki:b bizim her bir value'muzdu demi?O her bir value yapımız bir tuple tipinde gördüğünüz gibi.
##Tuple içinde de dikkat edin iki tane eleman var.O zaman ben o tuple içindeki her bir elemana tek tek erişmeliyim ki isim-soyad ve notu ayrı ayrı yazdırabiliyim.
##O zaman listelerde olduğu gibi burda da index kullanacaz ve burda da ilk iki elemana ulaşacağımız bir 0.index bir 1.index'e ulaşmamız yeterli olacaktır.



























































