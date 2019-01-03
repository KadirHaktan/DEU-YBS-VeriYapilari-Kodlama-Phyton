

#Örnek2

#Girdiğimiz bir kelimenin palindrome olup olmadığını sorgulayan kodumuz.Gelin hep beraber bakalım kodlarımıza bakalım

#Palindrome kelime=>Kelime kendisinin okunuşu da tersten okunuşu da aynı olan kelimedir
#Örneğin:Kısık kelimesi tersten okursanız yine okunuşu aynı olacaktır.İşte bu tarz kelimelere biz Palindrome kelime diyoruz

kelime=input("Bir kelime giriniz:   ")
#kelime diye bir değişken tanımladım ve bu değişken tanımlanırken input diye bir fonksiyon kullanmışız.İnput ne demek,peki?
#İnput fonksiyonu ile program çalıştığı zaman kullanıcıdan bir değer girmesini istenirse input fonksiyonu kullanırız.

kelime_harf_liste=list(kelime)
#Kelime_harf_liste diye bir değişken tanımladık ve bu değişkenimizin liste tipinde olup biz string olarak değer aldığımız kelime değişkenini burda
#liste veri tipine dönüştürdük.Yani string bir değişkeni liste veri tipine dönüştürdük.Tip dönüşümü diyebiliriz.Bu tip dönüşümü yapılan değeri
#kelime_harf_liste denilen değişkene de bu tip dönüşümü yapılan veriye atanmmış oldu.

#Yani örnek verecek olursam:kelime=>"AYA" ise
#kelime_harf_liste=["A","Y","A"] olmuş olur

kelime_harf_liste.reverse()
#String'den liste veri tipine dönüştürdüğümüz değişkenimizi reverse metotu ile liste'nin içindeki her bir elemanın yerini ters yönde değişmiş oldu.
#Örnek verecek olursam:
#kelime_harf_liste=["K","a","l","e","m"] ise
#kelime_harf_liste.reverse() metodunu kullandıktan sonra listemiz şu şekilde olacak:
#kelime_harf_liste=["m","e","l","a","K"]

#Yani listenin son elemanı gidiyor ilk elemanı oluyor mesela ,ilk elemanda son eleman oluyor.
#!!Ama listedeki ortadaki eleman(l harfi) ters çevirilirse bile dikkat edin değişmemiş
##Bunlar hariç listedeki 4.eleman 2.eleman olmuş ,2.elemanda 4.eleman olmuş




kelime1=list()
#kelime1 diye bir liste tipinde değişken tanımladım.Bu liste önceki kelime_harf_liste'den farkı ters çevrilmemiş hali olacaktır.Yani
#Normal kelime diyelim Bakır olsun,kelime_harf_liste bu kelimenin harflerin tersten sıralanışıdır(["r","ı","k","a","B"])
#ama kelime1 harflerin kelimeyi ne verdiysek harflerin sıralanışı öyledir(["B","a","k","ı","r"])



for i in kelime:
    kelime1.append(i)
    #kelime denilen string'imizin uzunluğu geçmediği sürece kelime1 listesi içine kelime string'deki
    #her bir harfi kelime1'e eleman olarak ekleyecektir,bu kod.Append fonksiyonu kelime'deki her bir harfi
    #listenin sonuna hep ekleyecektir.Yani kod aslında şöyle işliyor

    #kelime="AYA"

    #kelimenin ilk harfi eklenişi-->"A" (Kelime1 değişkeninde ilk seferinde bir eleman olmadığı sona ekleme bile görünüşte listenin ilk yerine eklemek gibi)
    #kelime ikinci harfi eklenişi-->"A","Y"("Dikkat et ilk elemandan sonra yani A'dan sonraki yere ekledi Y o anlık son yerdir)
    #kelime üçüncü harfi eklenişi-->"A","Y","A"(Harfler hep önceki harften sonrasına ekleniyor)




#Evet if else'lere ne kadar derste giriş yapılmamış olsa da bu örnekte liste ve string veri yapısını kullanırken Palindrome kelimenin olup olmadığının
#kontrolü için if ve else yapısının kullanmak zorunda kaldım.

#İf ve Else yinede biraz açalım.Ne de olsa gelecekteki derslerde sık sık göreceksiniz
#İf yapısı aslında şunu yapar:
#Bizim istediğimiz koşul sağlanıyor mu kontrolü yapar ve eğer koşul sağlarsa yapmak istediğimiz birincil işlemleri gerçekleştiriz

#Yani örneğin 4 sayısı 2'e bölümünden kalan sıfır ise bizim 4 sayımızın çift sayısı olduğunun koşulu sağlıyor demektir
#ve bu koşul sağladığını belirtebiliriz.

#Ama örneğin 5 sayısı 2'ye bölümünden kalan sıfır mı diye if ile kontrol ediyoruz ama tam bölünmüyor
#o zaman diğer durum olan tek sayı olması kanaatine varacaz ve diğer durum olan yani çift sayı değilse(else) durumunu belirtiriz.
#İşte burda parantez belirtiğim gibi istediğimiz durumun aksi olması durumunda aksi olan durumu belirtmek için else yapısından faydalanarız




if kelime1==kelime_harf_liste:
    print("Kelime palindrome kelimedir")
else:
    print("Kelime palindrome kelime değildir")

#Burdaki if else blokları şunu söylüyor eğer kelime1 listesindeki her bir elemanın sıralınışı
#kelime_harf_liste listesindeki her bir elemanın sıralanışı eşse bu kelime palindrome kelime durumunu gerçekleştiriyor
#ve aksi olmayan durumu if içinde belirtmiş oluyoruz

#Yani ["a","y","a"](düz hali) ==  ["a","y","a"](ters hali)
#düz halindeki her bir eleman tersteki her bir elemanla aynı mı diye bakıyor ve görüldüğü gibi düzdeki 1.eleman tersteki 1.elemanla eşleşiyor
#aynı şekilde düzdeki 2. ve 3. de tersteki 2. 3. elemanlarla eşleşiyor.O zaman listelerin eşitlik koşulu sağlıyor o yüzden de kelimenin palindrome
#olduğuna kanaat getirelebiliyor.Ama aksi durum olursa else bloğu işleyecek ve palindrome kelime olmadığının kanaatini ekrana göstermiş olacak programmız.


#Aksi durumla alakalı bir örnek gelsin şimdi(Hatta Uyarı Nitelikli biraz!!)

#["A","y","a](düz hali)== ["a,"y","A](ters hali)
#evet normalde aslında okunuşta bakınca bu bir palindrome kelime bu doğru.Ama programızda okunuşa bakmıyor harflerin hafızadaki yerine bakıyor.
#Hatırlayın ASCII tablosunda büyük a ile küçük A hafıza da aynı yerdeler mi ya da aynı hafıza da aynı şeyi mi gösteriyor.Hayır hafıza da ikisi farklı
#yerde tutuyor.Farklı yerlerde tutulduğu için programımıza örneğim Aya girdiğimiz zaman evet normalde gerçekten palindrome kelime ama iki harfin hafıza da
#farklı yerlerde tutulması nedeniyle bize çıktı olarak else bloğunu işleyip kelimenin palindrome olmadığını söyleyecek.
#Bu da yazdığımız kodda dikkat edilecek husustur diyebilirim sizlere.





