# Türkiye için üretim ve teknoloji parametreleri: ayrıntılı tarama ve dört geçişli denetim

Tarih: 12 Ekim 2026  
Kapsam: Türkiye ekonomisine ait üretim fonksiyonu, teknoloji şokları, faktör payları, TFV, ikame esneklikleri, girdi yapısı ve kamu sermayesi parametreleri.

## 1. Teslim edilen araştırma seti

İlk tarama ile ardından yapılan üç boşluk-odaklı denetim sonunda 66 kaynak kaydı oluşturuldu. Bunların 49 PDF'i yerel arşive alındı; dosya imzası, açılabilirliği/sayfa sayısı ve SHA-256 özeti kontrol edildi. Yerel arşivdeki 46 belge Türkiye için doğrudan kapsam içidir; üçü arama sırasında yanlış eşleştiği anlaşıldığı için özellikle `excluded` olarak korunmuştur. DergiPark'ın PDF bağlantısından DOCX sunduğu bir kaynak özgün biçiminde ayrıca arşivlendi. PDF'i yasal ve teknik olarak arşivlenemeyen kapsam-içi kaynakların sayısal tabloları yalnız erişilebilen tam metin üzerinden doğrulandı. Bir aday kaynak doğrulama beklemektedir.

Ana tabloda 1.906 ayrı gözlem vardır. Bunların 1.785'i yerel PDF'den, 121'i erişilebilir web tam metninden doğrulanmıştır. Her gözlem bir kaynak × parametre × dönem × sektör × yöntem kombinasyonudur. 84 iki dilli kontrollü parametre tanımı kullanılmıştır.

## 2. Yöntem

Kaynaklar TCMB, IMF, Kalkınma Bakanlığı/SBB, BETAM, üniversite arşivleri ve hakemli dergilerden tarandı. Mümkün olduğunda doğrudan kurum/yayıncı PDF'i kullanıldı. Her sayısal değer PDF içindeki tablo, şekil veya metinle tekrar kontrol edildi. Kayıtlar aşağıdaki ayrımlara göre sınıflandı:

- ekonometrik tahmin;
- veriden hesaplanan/türetilen değer;
- kalibrasyon veya varsayım;
- başka ülke/literatürden aktarılan dış kalibrasyon;
- test edilip reddedilmeyen model kısıtı;
- yaklaşık veya zamana göre değişen betimleyici sonuç;
- tarihsel gerçekleşme karşısında ileriye dönük projeksiyon.

Bu ayrım özellikle sermaye payı, amortisman ve TFV için zorunludur. Aynı isim altında görünen değerler çoğu zaman aynı ekonomik nesneyi ölçmemektedir.

## 3. En önemli bulgular

### Sermaye-emek ikame esnekliği

Tahminler yöntem ve toplulaştırma düzeyine oldukça duyarlıdır:

- Songur'un 1950-2011 toplam ekonomi CES tahmini: **0,032**.
- Andıç'ın 1991-2016 normalize CES sistem tahmini: **0,639** (standart hata 0,043); birim esneklik güçlü biçimde reddedilir.
- Kılıç-Yılmaz firma paneli sektör tahminleri: **0,2250-0,4183**; altı sektörün tamamında 0,5'in altındadır. Sonuçlar konferans metninde “preliminary” olarak sunulur.
- Enerjiyi dış yuvaya ekleyen Küçük-Kumbaroğlu-Sarıca çalışmasında sermaye-emek bileşimi ile enerji arasındaki esneklik **0,645513**; yüzde 95 güven aralığı **0,180220-1,110806**'dır.

Bu değerlerin tek bir “Türkiye ikame esnekliği” ortalamasında birleştirilmesi uygun değildir. Toplam ekonomi, sektör/firma paneli ve iç içe enerji-CES yapıları ayrı karşılaştırma panellerinde gösterilmelidir.

### Faktör payları

Sermaye payı için kayıtlı değerler yaklaşık **0,3214 ile 0,60** arasında değişir; fakat statüleri farklıdır:

- 0,3214: öz-istihdam düzeltilmiş emek payının tamamlayıcısı, büyüme muhasebesi hesabı;
- 0,40 ve 0,50: sırasıyla TCMB DSGE ve IMF potansiyel büyüme çalışmalarında kalibrasyon;
- 0,493: normalize CES dağılım parametresi;
- 0,51 ve 0,53: sektör paylarından hesaplanan toplam ekonomi sermaye payları;
- yaklaşık 0,60: TCMB potansiyel büyüme çalışmasındaki dönem ortalaması.

2025 tarihli TCMB firma mikroverisi çalışması ayrıca yöntem duyarlılığını doğrudan gösterir. 2009-2023 panelinde sermaye çıktı esnekliği sektör ve tahminciye göre **0,053-0,131**, emek çıktı esnekliği **0,573-0,967** aralığındadır. Sabit etkiler, Levinsohn-Petrin, Olley-Pakes, ACF düzeltmeleri ve Wooldridge tahminleri ayrı gözlemler olarak saklandı; bunlar ulusal gelir payı değil firma üretim fonksiyonu katsayılarıdır.

Sitede “sermaye payı” filtresi mutlaka `estimate_status` ve `definition_variant` alanlarını da göstermelidir.

### Teknoloji şokları

TCMB'nin 2002Q1-2012Q2 DSGE tahmininde:

- kalıcı teknoloji şoku sürekliliği **0,475** (0,381-0,566);
- durağan teknoloji şoku sürekliliği **0,816** (0,743-0,891);
- kalıcı teknoloji şoku oynaklığı **0,071** (0,058-0,083);
- durağan teknoloji şoku oynaklığı **0,085** (0,063-0,106).

Bu değerler çeyreklik modele ve model içi ölçeklendirmeye bağlıdır. Özellikle şok oynaklıkları farklı DSGE çalışmalarından doğrudan ortalanmamalıdır.

### TFV ve sektörel verimlilik

Çalışmalar ortak bir yön gösterse de yöntemleri farklıdır:

- Atiyas-Bakış'ta 2002-2011 standart TFV büyümesi tarımda **%2,49**, sanayide **%1,26**, hizmetlerde **%1,65**; beşeri-sermaye düzeltmesiyle sırasıyla **%2,22**, **%0,95**, **%1,27**'dir.
- BETAM 1980-2018 çalışmasında sanayi TFV'si 1981-1989'da **%4,5**, 2014-2018'de **%1,1**; hizmetler aynı dönemlerde **-%0,8** ve **-%0,5**'tir.
- BETAM 2000-2022 çalışmasında toplam TFV büyümesi 2003-2007'de **%2,2**, 2008-2010'da **-%3,9**, 2011-2014'te **%1,3**, 2015-2022'de yalnızca **%0,1**'dir.
- Aynı güncel çalışmada 2015-2022 sektör değerleri tarım **%1,5**, sanayi **%0,9**, hizmetler **%0,5**, inşaat **-%6,1**'dir.
- IMF'nin değerleri “TFV büyümesinin potansiyel büyümeye katkısı”dır: 2002-2003'te **3,4 yüzde puan**, 2011-2014'te **-0,4 yüzde puan**; 2015-2020 için **0,7 yüzde puan** değeri projeksiyondur.

TFV bir yapısal parametre olmaktan çok, seçilen üretim fonksiyonu ve girdi ölçümünden kalan artıktır. Saat, beşeri sermaye, kapasite kullanımı, kayıt dışılık ve ölçüm hataları modele göre TFV'nin içine girebilir.

### İthal ve ara girdi yapısı

- 2010 TCMB çalışmasının girdi-çıktı hesabında toplam ekonominin doğrudan+dolaylı ithalat gereği 1979'da **%7,6**, 2002'de **%15,1**; imalat sanayiinde **%11,6**'dan **%26,7**'ye çıkar.
- 2019 TCMB çalışmasında 2002-2017 ortalama ithal içerik üretim için **%18,3**, ihracat için **%31,5**'tir.
- 145 büyük imalat firması anketinde hammadde ve malzeme maliyeti sınai üretim maliyetinin **%88,5**'i; enerji ve su **%3,2**'sidir. Bu oranlar bütün imalat sanayiini temsil eden ulusal hesap katsayıları değil, örneklem-ağırlıklı anket sonuçlarıdır.

### Kamu altyapısı

Serdaroğlu'nun 1980-2013 Cobb-Douglas tahmininde, sabit getiri kısıtı altında birleşik kamu fiziki+sosyal altyapı sermayesi çıktı esnekliği **0,2417** (standart hata 0,1188)'dir. Fiziki ve sosyal altyapı ayrı girildiğinde katsayılar anlamlı değildir. Sabit getiri kısıtı F-testlerinde reddedilmez.

## 4. Kapsam durumu

| Parametre ailesi | Durum | En güçlü mevcut kaynaklar |
|---|---|---|
| Sermaye ve emek payları / çıktı esneklikleri | Çok güçlü; dört haneli ve NACE iki haneli ayrıntı var | S046, S051, S054, S060, S061 |
| Toplam ve sektörel TFV büyümesi | Çok güçlü; 1963-2024 tarihsel kapsama uzanıyor | S008, S009, S015, S052, S062, S066 |
| Kalıcı/durağan teknoloji şoku | Orta; tek doğrudan tahmin | S001 |
| Sermaye-emek ikame esnekliği | Güçlü ama yöntem duyarlı | S002, S003, S004 |
| Enerjiyle ikame | Güçlü; yakıt ve yenilenebilir türleri ayrıştırılmış | S005, S006, S021, S039, S040 |
| Ölçeğe göre getiri | Güçlü; sektör ve firma büyüklüğü kırılımları var | S055, S056, S059, S060 |
| Sabit üretim maliyeti | Zayıf | S001 yalnızca sıfır kâr normalizasyonu |
| Kapasite kullanım oranı | Sınırlı | S019 tarihsel bağlam; S008 ölçüm tartışması |
| Sermaye kullanım maliyeti | Açık araştırma boşluğu | DSGE tanımları ayrıca taranmalı |
| Ara ve ithal girdi payı | Güçlü | S011, S012 |
| Enerji girdisi payı | Sınırlı ama sayısal | S012 firma anketi |
| Petrol girdisi payı | Açık araştırma boşluğu | Enerji ve ithalat çalışmalarından ayrıştırılmalı |
| Kamu sermayesi çıktı esnekliği | Orta; ülke ve bölgesel VAR sonuçları | S007, S031, S032 |
| Kayıtlı/kayıt dışı verimlilik | Orta | S010 |
| Emek/sermaye artırıcı teknik ilerleme | Orta | S002 |
| Bölgesel teknik etkinlik ve TFV ayrıştırması | Güçlü | S029; 26 NUTS-2 bölgesinin tamamı |
| Bölgesel kamu sermayesi yayılmaları | Orta; sıralamaya duyarlı | S031, S032 |
| İmalat sermaye stoku ve amortisman | Güçlü; ölçüm duyarlılığı ayrıca kayıtlı | S028, S033, S051, S053 |
| BİT sermayesi ve BİT kullanan emek | Güçlü firma mikroverisi | S035, S036 |
| ERP/CRM/SCM/EDI/web sitesi | Güçlü ilişki tahminleri; nedensellik sınırlı | S034, S035 |
| Genişbant ve firma TFV'si | Güçlü güncel nedensel tasarım | S037 |
| Beşeri-fiziksel sermaye ikamesi | Orta; tek uzun dönem translog çalışması | S038 |
| Tarımsal üretim sınırı ve arazi/girdi esneklikleri | Güçlü; ulusal mikro ve mekânsal il çalışmaları | S041, S061, S064 |
| İmalat teknik etkinliği / DEA-SFA karşılaştırması | Güçlü ve yöntem çeşitliliği yüksek | S042-S048 |
| Metafrontier teknoloji açığı | Orta; tek kesit ve ölçek grupları | S048 |

## 5. İkinci geçişte yakalanan başlıca eksikler

İkinci tarama, ilk setin özellikle eski üretim fonksiyonu literatürü, bölgesel çalışmalar ve firma düzeyinde dijital teknoloji sonuçlarında eksik kaldığını gösterdi.

- **Normalize CES'in önceki örneklemi:** S022, 1991-2014 dönemi için ikame esnekliğini 0,799 (SH 0,026), emek-artırıcı teknik ilerlemeyi yıllık 0,015 ve sermaye-artırıcı teknik ilerlemeyi -0,011 olarak tahmin eder. Bu kaynak, sonraki güncellemenin yerine geçirilmedi; ayrı bir tahmin vintajı olarak saklandı.
- **Eski imalat üretim fonksiyonları:** S023 ve S024, 1970-1999 ile 1985-2001 dönemleri için Cobb-Douglas, CES, translog ve “yeni CES” sonuçlarını ekledi. Bazı çok yüksek ölçek esneklikleri kullanılan sermaye/emek vekillerine duyarlı olduğundan uyarı notlarıyla tutuldu.
- **Yıllık büyüme muhasebesi:** S025'in 1998-2010 yıllık TFV katkıları, yalnız dönem ortalamaları yerine bütün yıllar için kaydedildi. S033'teki 1972-2000 uzun dönem sermaye birikimi/TFV ayrıştırması da eklendi.
- **Bölgesel sınır analizi:** S029'un 2004-2020 ortalama teknik etkinliği 0,906'dır. Yıllık teknik değişme 0,0323 iken ölçek etkisi -0,0325 ve teknik etkinlik değişmesi -0,00192'dir; böylece ortalama TFV değişmesi -0,0021 olur. 26 NUTS-2 bölgesinin tamamı ayrı satırlardadır; TRA2 0,048 ile üstte, TRC2 -0,040 ile alttadır.
- **Kamu sermayesi taşmaları:** S032, yedi coğrafi bölge için bölge içi ve bölge dışı kamu sermayesi etkilerini ayırır. Tablodaki alt/üst değerler güven aralığı değil, VAR değişken sıralamaları boyunca sağlamlık aralığıdır. Bu nedenle aşırı büyük veya negatif değerler doğrudan yapısal esneklik gibi kullanılmamalıdır.
- **Dijital teknoloji:** S034-S036 ile ERP, CRM, SCM, EDI, web sitesi, yazılım sermayesi, BİT kullanan emek ve BİT/BİT-dışı sermaye katsayıları eklendi. S035'in ACF tahmininde bölünmüş emekli modelde sermaye 0,202, BİT-dışı emek 0,443 ve BİT emeği 0,376'dır. S036'da BİT-sermaye katsayısı spesifikasyona göre 0,0151-0,0230 aralığındadır.
- **Genişbant:** S037, DSL, diğer sabit ve mobil genişbant için imalat, hizmetler ve BİT sektörlerinde tedavi edilen/edilmeyen firma etkilerini ayrı verir. Kayıtlar yüzde değil log-TFV puanı olarak saklandı; istatistiksel anlamsız sonuçlar ayrıca işaretlendi.
- **Sermaye stoku varsayımları:** S028'in imalat sermaye stoku hesabındaki yıllık yüzde 6 amortisman; S035'in maddi sermaye için yüzde 5, yazılım/maddi olmayan sermaye için yüzde 25 varsayımları ayrı tanımlar olarak işlendi.

S026 ikinci taramada anahtar kelime eşleşmesiyle aday oldu, ancak ampirik TFP süreçlerinin ABD ve AB-15'e ait olduğu görülünce kapsam dışı bırakıldı. Bu kayıt yanlış pozitifleri görünür kılmak amacıyla silinmedi.

## 6. Üçüncü geçişte yakalanan başlıca eksikler

Üçüncü tarama; tez, eski dergi arşivi, açık çalışma kâğıdı deposu ve yöntem-odaklı anahtar kelimelerle tekrarlandı. Bu geçişte 13 yeni kaynak kaydı, 11 arşivlenmiş PDF ve 403 yeni sayısal gözlem eklendi.

- **Beşeri ve fiziksel sermaye:** S038, 1950-2014 döneminde beşeri sermayenin çıktı esnekliğinin 1,235'ten 1,839'a yükseldiğini; fiziksel-beşeri sermaye ikame esnekliğinin 1,00112'den 1,00055'e hafifçe gerilediğini raporlar.
- **Enerji türlerinin ayrıştırılması:** S039 emek, sermaye, doğal gaz, petrol ve kömür için on ikili ortalama ikame esnekliği sağlar. S040 bu kapsamı hidroelektrik ve biyokütleyi de içerecek biçimde 1988-2023'e genişletir; yedi ortalama çıktı esnekliği, on bir faktörler-arası ve on yakıtlar-arası ikame esnekliği ayrı kaydedildi.
- **Tarım işletmeleri:** S041'in daha önce yalnız özet düzeyinde görünen PDF bağlantısı dergi sayfasındaki atıf meta-verisinden bulundu. 681 bitkisel üretim işletmesinde ortalama teknik etkinlik 0,7158; arazi, emek ve tohum-gübre-ilaç bileşimi çıktı esneklikleri sırasıyla 0,12811, 0,50131 ve 0,24395'tir.
- **Özel imalat stokastik sınırı:** S042, 1985, 1990 ve 1995 kesitlerinde 22 üç haneli imalat kolu için emek, sermaye, elektrik ve etkinsizlik-varyansı payı katsayılarını verir. Katsayıların girdi düzeyi tanımına duyarlı olması nedeniyle log-esneklik gibi yeniden etiketlenmedi.
- **DEA-SFA karşılaştırması:** S043'te toplam imalat için ortalama etkinlik SFA'da 0,814, DEA-CRS'de 0,923 ve DEA-VRS'de 0,955'tir; kamu ve özel alt örneklemleri ayrı satırlardır.
- **Firma düzeyi etkinsizlik belirleyicileri:** S044'te sermaye ve emek çıktı esneklikleri 0,509 ve 0,521'dir. Ortalama etkinsizlik 0,14'tür; ihracat ve büyüme etkinsizliği azaltırken sermaye-hasıla oranı artırır. S047 yazılım yatırımı, Ar-Ge personeli, dışa açıklık ve dış kaynak kullanımı katsayılarını yüksek/düşük teknoloji firmaları için ayırır.
- **Geçici ve kalıcı etkinlik:** S045, gıda sanayiinde kısa dönem, uzun dönem ve toplam etkinliği sırasıyla 0,7964, 0,7288 ve 0,5811 olarak tahmin eder.
- **Dört haneli imalat üretim fonksiyonları:** S046'nın 51 SIC4 sektörü için emek, elektrik, yakıt, malzeme ve sermaye Olley-Pakes katsayılarının tamamı—255 gözlem—aktarıldı. Bunlar toplulaştırılmadı; sektör kodu ve t-istatistiği korundu.
- **Ölçek ve teknoloji açığı:** S048'in küçük ile orta/büyük firmaları ayıran grup sınırı, birleşik sınır, metafrontier etkinliği ve teknoloji açığı oranları altı imalat alt sektörü için kaydedildi.

Bu tarama aynı zamanda Taymaz-Saatçi'nin 1987-1992 tekstil, çimento ve motorlu taşıt tesislerini kapsayan 1997 çalışmasını (S049) ve Demiroğlu'nun sermaye hizmetleri notunu (S050) yeniden teyit etti; ancak yasal açık tam metin veya güvenilir sayısal tablo elde edilmediği için bu iki kaynaktan tahmin satırı üretilmedi.

## 7. Dördüncü geçişte yakalanan başlıca eksikler

Dördüncü tarama eski çalışma kâğıdı serileri, yazar arşivleri, yakın tarihli dergi sayıları, kaynakçadan geriye izleme ve tarım/çimento gibi sektör anahtar sözcükleriyle yürütüldü. Önceki sürüme göre 16 kaynak, 12 PDF, 1.130 sayısal gözlem ve 20 kontrollü parametre tanımı eklendi.

- **1983-2001 imalat mikroverisi:** S051, yaklaşık yılda 10 bin işyerini kullanan çalışmadan 61 dört haneli ISIC sektörünün sermaye, enerji, ara girdi, üretim işçisi ve idari emek katsayılarını; sermaye ölçümüne duyarlılığı; teknoloji yanlılığını ve firma grubu üretkenlik artışlarını ekledi. Tahmin edilen yıllık amortisman %6,7; sağlamlık alternatifi %10'dur.
- **Uzun tarihsel TFV serileri:** S062, Krueger-Tuncer'in 1963-1976 sektör ve alt dönem sonuçlarını; S052 ise kapsamı 1963-1983'e uzatan 21 sektör/toplam serilerini veri setine taşıdı. Böylece eski literatür yalnız ikincil atıflara dayanmıyor.
- **Maddi olmayan sermaye:** S054, 2003-2012 firmalarında Olley-Pakes ve sistem GMM ile BİT/BİT-dışı, maddi/maddi olmayan, yazılım, patent ve şerefiye sermayesi çıktı esnekliklerini ayrı kaydeder.
- **Teknik değişme, etkinlik ve ölçek:** S055 ve S059 birlikte 1987-1997 için dokuz iki haneli ve 79 dört haneli imalat kolunda teknik değişme, ortalama teknik etkinlik ve ölçeğe göre getiri sağlar. S056, çimentoda 1980-1993 translog sınır katsayılarını ve özelleştirme sonrası etkinsizlik katsayısını içerir; özelleştirme sonrası katsayı istatistiksel olarak anlamlı değildir.
- **Firma büyüklüğü ve yabancı mülkiyet:** S058, 1983-2001 emek üretkenliği artışını KOBİ, büyük ve yabancı işyerleri için altı döneme ayırır. Bu sonuçlar S051'in daha geniş raporuyla bağlantılı olmakla birlikte ayrı yayın vintajı olarak tutuldu.
- **Güncel imalat esneklikleri:** S060, 2007-2021 için 23 NACE iki haneli imalat kolunda translog ve Cobb-Douglas emek/sermaye çıktı esneklikleri ile ölçeğe göre getiriyi verir. Yöntemler arası fark aynı sektör için doğrudan görülebilir.
- **Tarım girdilerinin ayrıştırılması:** S061, ulusal 2002 ve 2004 çiftçi hanehalkı araştırmalarından emek, hayvan varlığı, arazi, tohum, gübre, ilaç, su, mazot, elektrik, diğer maliyet ve yem esnekliklerini ekledi. S064'ün 2000 ve 2007 il-düzeyi mekânsal esneklik çalışması da kataloglandı; açık sayısal tablo bulunamadığı için tahmin satırı üretilmedi.
- **En güncel büyüme muhasebesi:** 28 Eylül 2026'da yayımlanan S066, 1981-2024 için sermaye esnekliğini 0,46 tahmin eder. Tüm dönemde yıllık ortalama sermaye, beşerî sermaye ve TFV katkıları sırasıyla 2,83, 1,63 ve 0,13 yüzde puandır; altı alt dönem ayrı kaydedildi.
- **Üretkenlik belirleyicileri ve tamamlayıcılık:** S063, teknik/nitelikli emek ile makine ve bilgisayar sermayesi tamamlayıcılığını; S065 ise 1992-2001'de düşük fiyat-maliyet marjı ve ithalat nüfuzunun emek üretkenliği büyümesiyle ilişkisini belgeledi. S053, 19 il için 1994-1997 göreli üretkenlik hesabını ve 19 yıllık varlık ömründen türeyen amortisman varsayımını ekledi.

S057'nin DergiPark “PDF” bağlantısı gerçekte Word belgesi döndürdüğü için dosya uzantısı yapay biçimde değiştirilmedi. Özgün DOCX `sources/originals/` altında tutuldu; yerel dönüştürücü bulunmadığından PDF üretilmedi.

## 8. Kalite ve karşılaştırılabilirlik notları

1. **Kalibrasyon tahmin değildir.** Örneğin 0,4 veya 0,5 sermaye payları model kurulumunda sabitlenirken 0,53 gelir paylarından hesaplanır.
2. **Dönemler örtüşse bile yöntem değişebilir.** 2008-2010 TFV'si farklı çalışmalarda saat, beşeri sermaye ve sektör yeniden tahsisini farklı ele alır.
3. **Sektör adları standartlaştırılmalıdır.** “Sanayi” bazı kaynaklarda madencilik+imalat+enerji hizmetlerini içerir; “manufacturing” yalnız imalattır.
4. **Birimin görünür olması gerekir.** 0,035 çeyreklik amortismanı yüzde 3,5 yıllık değer gibi sunmak ciddi hata olur; kaynak bunu yaklaşık yüzde 14 yıllık olarak açıklar.
5. **Grafikten okunan yaklaşık değerler işaretlenmelidir.** Bu sürümde yalnız metin veya açık şekil etiketi bulunan değerler alındı; görsel eksen interpolasyonu yapılmadı.
6. **Arşiv durumu kullanıcıya gösterilmelidir.** `web_fulltext_verified` değerler doğrulanmıştır ama yerel dosya henüz yoktur.

## 9. Kalan boşluklar ve sonraki tarama öncelikleri

1. Kapasite kullanım maliyeti ve sabit üretim maliyeti içeren Türkiye DSGE modelleri.
2. Petrol, doğal gaz ve elektrik girdilerini ayrı veren daha fazla sektör üretim fonksiyonu; mevcut ayrıştırma hâlâ ağırlıkla toplam ekonomi düzeyindedir.
3. TCMB 2025 katsayılarının daha dar NACE sektör kırılımlarına genişletilmesi.
4. Kamu altyapısı sonucunun alternatif sermaye stoku ve nedensellik yöntemleriyle sağlamlık kontrolleri; S031'in ödeme duvarı arkasındaki tam tablosu.
5. 2022 sonrası girdi-çıktı ve sektörel TFV güncellemeleri; toplam ekonomi TFV'si artık 2024'e kadar kapsanıyor.
6. Erişim sorunu yaşayan S003, S005, S007, S014, S029, S032 ve S035 PDF'lerinin yasal kurumsal/yazar aynaları. S029'un doğrudan indirmesi anti-bot doğrulamasında kaldı; otomatik engel aşılmadı. Taymaz-Saatçi (1997) ve Demiroğlu (2012) için açık tam metin/tablo araması sürdürülmeli.

## 10. Kapsam dışı ve yanlış eşleşmeler

- S016 TCMB belgesi kurum olarak Türkiye kaynaklı olsa da model kalibrasyonu ABD ekonomisine aittir; hiçbir değeri ana tabloya alınmadı.
- S017 dosyası adlandırma sırasında Türkiye raporu sanılmış, fakat Hollanda Seçilmiş Konular raporu olduğu doğrulanmıştır; hiçbir değeri ana tabloya alınmadı.
- S026 başlığındaki trend şokları Türkiye çalışması izlenimi verse de ampirik kalibrasyon ABD ve AB-15 içindir; hiçbir değeri ana tabloya alınmadı.
- S013 yeterli bibliyografik ve tam metin doğrulaması yapılana kadar yalnız aday kaynak olarak tutulmuştur.

Bu açık kayıtlar, araştırma sürecindeki yanlış pozitifleri gizlemek yerine denetlenebilir kılar.
