
##Veri tipleri,değer atama,veriyi yazdırma

a=5
b="Hello World"
c=5.5
d=True
#a diye bir değişken tanımladık bu değişkenin veri tipi integer(sayı) dır
#b diye bir değişken tanımladık bu değişkenin veri tipi string(metin) dir.String aslında bir karakter(char) dizisidir.Stringler kısmında detayını yazacam
#c diye bir değişken tanımladık bu değişkenin veri tipi float(kayan noktalı virgülü değerler denilebilir.Daha kısa tabirle ondalıklı sayı) dir.
#d diye bir değişken tanımladık bu değişkenin veri tipi boolean(sadece doğru ya da yanlış diye tanımlanabilen veri tipi)dir.

print(a)
##hafıza da aldığımız veriyi ekrana göstermek için print fonksiyonundan faydalanıyoruz.Fonksiyon çağıram işlemleri sırasında
##fonksiyonun isminin yanına parantez açıp eğer bir parametre alacaksa parametreyi içine yazarız almayacaksa da parantez açıp kapatılır.


##değişkenimizin tipini öğrenmek için type fonksiyonundan faydalanarız.Type fonksiyonu parametre olarak herhangi bir  değişken alır.
##Örnek kullanım

print(type(a))##tipin ne olduğunu ekrana göstermek için yine print fonksiyonu da aynı zamanda kullandık

#****************************************************************************************************************#


###String veri yapısı,format biçiminde yazdırma##

##String veri yapısı bir metin ya da yazı tutmak için kullandığımız veri tipidir.String bir veri tipi tanımlarken çift tırnak açıp kapatmamız gerekir aksi takdir de oluşturduğumuz veri tipi
## string olmaz.Daha iyi anlaşılması için bir örnekle açıklayalım

a1="5"
print(type(a1))

a2=5
print(type(a2))

##Sizce a1 değişkenin veri tipi nedir?Ve aynı zamanda a2 değişkenin veri tipi nedir?Cevaba bakmadan önce isterseniz altı cümleleri kapatın ve düşünün :)

##Cevap:a1 değişkenin veri tipi stringdir;çünkü çift tırnak açtığımızda 5 sayısını aslında metin içine almış oluyoruz bu sebeple a1 değişkenin veri tipi string olacaktır.
##a2 değişkenin veri tipi anlayacağanız gibi integer(sayı) olacaktır.


#Dipnot:String aslında bir dizi ya da liste diyebiliriz.Yani metin olarak tanımladığımız bir değişkende metin içindeki her bir değer karakter aslında(harf,boşluk karakteri...).O yüzden
##string için bir karakter dizisi diyebiliriz.İlerde for döngüsüyle beraber bir örnekle gösteriyor olacam.


##Format biçiminde yazdırma ya da karakter dizilerini biçimli yazdırma
## string veri yapısına ait format metodundan faydalanılır. Bunun için örnek kod aşağıdaki gibidir

print("{} {} ".format("Merahaba","Dünya"))
##print fonksiyonu içinde çift tırnak açıp kapadıktan sonra nokta koyuluyor gördüğünüz gibi.Peki neden nokta?Şundan çift tırnak açıp kapadığım şey
#aslında string tipinde bir değişkendir ve string değişkenine ait phyton'da hazır olarak gelen özellik ve fonksiyonlarına erişebilmek için nokta kullanırız.
#Daha sonra hazır fonksiyonlardan format fonksiyonunu bulup parantez açtığımızda gördüğünüz gibi iki parametre istenmiş bizde yine iki tane string değişkenini parametre olaraka verdik.
#Peki bu parametre sayısı 1,3,5... yani istediğimiz sayıda olamaz mıydı?Olurdu ama olması için başta çift tırnak içine yazdığımız süslü parantez sayısı 2 tane olduğu için fonksiyonumuzda iki tane parametre almış

#çift tırnak içindeki her bir süslü parantezi formatlı adresi aslında format fonksiyonu içindeki her bir değer olarak düşünebiliriz yani:
  #1.süslü parantezi adresi->format fonksiyonu içindeki ilk parametre("" Merahba"")
  #2.süslü parantezi adresi->format fonksiyonu içindeki ikinci parametre(""Dünya"")

#Kısacası format fonksiyonun yaptığı işlev:metin olarak oluşturduğumuz değişkenimizin içindeki süslü parantezli istediğimiz formatta göstermeye yarıyor


##Strip ve Join Fonksiyonları

##Strip fonksiyonu metnimiz içindeki boşlukları ya da metin içindeki istediğimiz karakteri silmeye yarayan metottur.Kullanımı şu şekildedir

d1="  Merahba"
d2=d1.strip()

print(d1) ##Boşluklar silinmeden önceki durum
print(d2) ##Boşluklar silindikten sonraki durum

##   ""    Merahba"" değişkenimizdeki solda kalan boşlukları silmek için string veri tipisine ait strip fonksiyonu kullandık ve biz burada o boşlukların
## silinmiş halini d2 diye de atadık yine tabi atamaya yapmayabilirdiniz.yani sadece print(d1.strip()) de diyebilirdiniz.

d3="Merahba Dünya"
d4=d3.strip("Dünya")
print(d4)
##Merahba Dünya metni sağında olan Dünya kelimesini silmiş olup d4 değişkenine atayıp yazdırdık.

##Strip fonksiyonu gördüğünüz gibi herhangi bir parametre almassa sadece boşluklar varsa boşlukları siler ama bir parametre ya da değer girilirse
## o değer metin içinde varsa o değeri siler


##Join fonksiyonu bir metindeki her bir karakter arasında bir işaret ya da karakter koymamızı sağlar.Bu karakter yıldızdır çizgidir ne istersek.Örnekle gösterecek olursak:
character="*" ##d3 metin içindeki her bir karakter arasına konacak işaret
print(character.join(d3))##karakter ya da işaret burada d3 metin içine her bir araya katılıyor gibi düşenebiliriz.Burda da character değişkenin
                         ##join fonksiyonu kullanmamızı nedeni de katılan yapı aslında yıldız işaretidir.Yani katılma işlemini yıldız gerçekleştirecektir ve bu yıldız
                         ##nereye katılmak istiyorsa join fonksiyonunda parametre  olarak içine yine bir metin(string) parantez içine koyarız.


#****************************************************************************************************************#






