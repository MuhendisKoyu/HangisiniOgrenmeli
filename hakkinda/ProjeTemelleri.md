Dil ve Araçlar (Ek kütüphaneler pyproject.toml dosyasında)
* Python
* Pyrogram-async

Botun hazırlanma sürecinin ilerleyişi, ana yapısı ve ilgili konulara aşağıda yer verilmeye çalışılmıştır. Taslak olarak bir gidişat belirlemeye çalıştım. Detaylar ayrıca Telegram veya Discord grubunda konuşulabilir.

Yapılacak işin amacına uygun bir şekilde sonuçlanabilmesi için ilgili konuların detaylı bir şekilde araştırılmasına ihtiyaç duyulmaktadır. Projenin zorluğunu kararlaştırılan sorular belirleyecektir. Sonradan soru eklenebilmesi vb. bütün süreç programlama öncesi yapılacak hazırlık ile netleşecektir. Aksi takdirde programlama sırasında akla yeni bir soru gelmesi bütün gidişatı etkileyebilir. Elde edilecek sonuç gerçekten her yerde önerilen bir hale de gelebilir, internetteki sırada programlama dili seçme yazısına da dönebilir. Bu da projeyi geliştiren arkadaşların elinde olan bir durumdur.

## Ana Sorular

* Yaş
* Eğitim  
* Yabancı dil bilgisi (Cevaplara etki etmese de yabancı dil bilgisinin kaynaklara erişim açısında sağlayacağı kolaylık. Belki bununla ilgili ufak bir yazı.)
* İlgilendiği alan (Öncelikle programlama alanlarının belirlenmesi lazım [Üniversitelerin yüksek lisans sayfalarından vs. alanlar listesi oluşturulabilir. Standart olan mobil, web vb. alanların yanı sıra Doğal Dil İşleme, Görüntü İşleme, Gömülü Sistemler, Yapay Zeka gibi konulara da yer verilebilir.
	* [BU LINKTEKİ](https://muhendisbilir.com/programlama-dilleri-uygulama-alanlari/) Programlama Dilleri ve Uygulama Alanları yerine Bilgisayar Mühendisliği/Yazılım Geliştirme/Programlama Alanları ve Uygulandığı diller tarzında bir yazı olabilir.
	* Belki [BU LINKTEKİ](https://www.northeastern.edu/graduate/blog/computer-science-specializations/) gibi fakat biraz daha detaylı Alanlar hakkında bilgi edinebilmesi için detaylara hakim bir yazı.)
* Öğrenme zorluğu

Sorulacak sorular ve cevaplar kodlama öncesinde detaylı bir şekilde oluşturulmalıdır. Soru-Cevap ilişkisi için ayrıca bottaki butonların ve butonlardan dönen verilerin nasıl işleneceğini anlatmaya çalışacağım. Araştırma kısmı bu projenin %80'ini oluşturuyor diyebiliriz. Üstteki sorular örnek niteliğindedir. Hazırlanacak akış şeması için [DrawIO](https://draw.io) sitesi kullanılabilir.

### Örnek akış şemaları

* Bazı gereksiz detaylar ve yanlış yönlendirme var gibi fakat örnek olması bakımından güzel bir akış şeması. Gruplarda sık sık paylaşıldığını görüyorum. Buradan fazlasıyla esinlenilebilir ve biraz iyileştirme ile sunulma imkanı da mevcut fakat daha özgün birşey olması bizim faydamıza olur.
[Örnek Akış Şeması 01](https://www.dailyinfographic.com/wp-content/uploads/2015/06/OBHEr1J.png)

* Biraz yes no ile işi bitirmiş olsalar da incelemeye değer.
[Örnek Akış Şeması 02](https://3.bp.blogspot.com/-Sf5SOggz8Ko/V2YK02TIFQI/AAAAAAAAM7Y/EDbEZ5vM8-gX4OI5w4sNGVk8V9ayKgYqACLcB/s1600/screen05.png)

## İlerleme
* Verilen cevaplara göre alanlara uygun dilleri puanlama yaparak sonuç kısmında ilk 3 sonucu göstermek.

	* Soru1 -> Java +1, C# +1, Kotlin +1
	* Soru2 -> C# +1, C++ +1, Java +1
	* Soru3 -> PHP +1, JS +1, Python +1

Şeklinde ilerledikten sonra son kısımda en yüksek puanlı diller listelenir.

* Sorular ve cevaplar net olur. İlerlemenin sonucunda tek bir dil önerilir.


### İncelenebilecek Kaynakar
* https://muhendisbilir.com/programlama-dilleri-uygulama-alanlari/
* https://www.pluralsight.com/blog/software-development/choose-programming-language
* https://mkdev.me/en/posts/how-to-choose-a-programming-language
* http://codedad.co.uk/guide-to-choosing-your-first-programming-language/

C/C++ İnşa Sistemleri çeviri projesinde olduğu gibi bu projemizde de amacımız yazılım alanında kaliteli Türkçe kaynak eksikliğini gidermeye çalışmak ve bu alanda ilgili insanlara rehber olabilmektir. Google'da karşımıza çıkan, yazmak için yazılmış sıradan yazılar yerine gerçekten faydalı içerikler üretebilmek herkesin altından kalkabileceği bir iş değildir. 
