# Sermaye ve Yatırım: Türkiye Parametre ve Tahmin Derlemesi

## 1. Amaç ve kapsam

Bu tarama, Türkiye için **sermaye ve yatırım** başlığı altında kullanılabilecek yapısal parametreleri, kalibrasyonları, kamu yatırımı çarpanlarını ve firma-yatırım denklemi katsayılarını tek bir denetlenebilir veri yapısında toplar. Çalışma, önceki **Üretim ve Teknoloji** derlemesiyle aynı üç katmanlı yapıyı kullanır:

1. `data/parameter_dictionary.csv`: kavram ve karşılaştırma kuralları;
2. `data/sources.csv`: kaynak künyesi, erişim ve arşiv durumu;
3. `data/capital_investment_estimates.csv`: kaynak–parametre–örneklem–model düzeyinde uzun biçimli tahminler.

Tarama yalnızca “yatırım” sözcüğü geçen çalışmaları toplamakla sınırlı değildir. DSGE yatırım bloğu, sermaye stokunun kurulması, kamu–özel yatırım ilişkisi, kamu yatırımının çıktı etkisi, finansal kısıtlar, nakit akışı, Tobin'in q'su, kaldıraç, ticari kredi, faiz ve borç şokları birlikte taranmıştır.

## 2. Tarama ve doğrulama yöntemi

### 2.1 Arama eksenleri

- Türkiye/Turkey + investment adjustment cost, capital adjustment cost, depreciation, investment shock;
- Turkey + public investment multiplier, infrastructure investment, crowding out/crowding in;
- Turkish firms + investment cash flow sensitivity, Tobin's q, leverage, debt overhang, trade credit;
- Turkey + public debt/private investment, domestic debt, external debt service;
- Turkey + capital stock, imported investment goods, accelerator model;
- TCMB/CBRT, IMF, üniversite tez arşivleri, DergiPark ve hakemli dergi arşivleri.

### 2.2 Dahil etme ölçütleri

Bir çalışma aşağıdaki koşullardan en az birini sağlıyorsa kapsam içine alınmıştır:

- Türkiye için bir yatırım/sermaye parametresi kalibre veya tahmin ediyor;
- kamu yatırımının çıktı veya özel yatırım üzerindeki nicel etkisini veriyor;
- firma yatırım denkleminde nakit akışı, q, kaldıraç, kredi, faiz veya büyüme katsayısı raporluyor;
- kullanılan sermaye serisinin amortisman veya bileşim varsayımını açıkça veriyor;
- doğrudan katsayı vermese de önemli bir Türkiye bulgusuyla literatür boşluğunu belgeliyor.

### 2.3 Sayısal aktarım protokolü

- Her sayı PDF sayfası ve tablo/şekil/eşitlik konumuyla kaydedildi.
- Standart hata, güven aralığı, t-istatistiği ve p-değeri birbirine dönüştürülmeden ayrı biçimde notlandı.
- Kalibrasyon, dışsal kalibrasyon, varsayım, hedef ve tahmin statüleri ayrıldı.
- Aynı çalışmanın alt örneklemleri ve sağlamlık kontrolleri ayrı satırdır.
- OCR güvenilir olmayan taranmış tablolar sayısallaştırılmadı; kaynak yine katalogda tutuldu.
- Bir katsayı kaynakta oran-düzeyi denkleminden geliyorsa “esneklik” olarak yeniden adlandırılmadı.

## 3. Kapsam özeti

İlk turda **21 yeni kaynak** (S067–S087) kataloglandı; takip kontrolünde daha önce PDF'leri indirilmiş fakat katalog ve tahmin tablosuna bağlanmamış **3 kaynak** (S088–S090) da eklendi. Böylece sermaye-yatırım genişlemesi **24 kaynağa** ulaştı. Bunların **23 PDF'si** yerel arşivdedir. IMF WP/11/150'nin resmi sayfası ve aranabilir tam metni doğrulandı; sunucu otomatik PDF isteğini engellediği için S068'in `local_pdf` alanı bilinçli olarak boş bırakıldı.

Güncellenmiş sermaye-yatırım tablosunda **341 sayısal gözlem** vardır. Gözlemler 23 sayısal kaynakta ve 50 ayrı sermaye/yatırım parametre kimliğinde dağılır. Ayrıca S068, S081, S085 ve S087 literatür kapsamını tamamlamak üzere kataloglanmış, fakat güvenilir ve karşılaştırılabilir bir yapısal katsayı aktarılmamıştır.

Sayısal yoğunluk özellikle firma yatırımında yüksektir:

- nakit akışı duyarlılığı: 71 gözlem;
- 2018 borç şoku etkisi: 30 gözlem;
- Tobin q duyarlılığı: 24 gözlem;
- doğrusal kaldıraç etkisi: 23 gözlem;
- parasal duruş × nakit akışı etkileşimi: 21 gözlem;
- kamu yatırımı çıktı çarpanı: 15 gözlem.

## 4. Ana bulgular

### 4.1 DSGE yatırım bloğu ve sermaye birikimi

S001'in Türkiye için tahmin ettiği küçük açık ekonomi DSGE modelinde yatırım ayarlama maliyeti **5,457** (yüzde 90 artçıl aralık 3,965–6,885), sermaye ayarlama maliyeti **1,084** (0,577–1,600) ve yatırım şoku sürekliliği **0,914**'tür. Aynı modelde yatırım şoku çıktı varyansının yüzde **13,10**'unu, yatırım varyansının yüzde **45,20**'sini açıklar (PDF s. 38–39).

S067'nin bankacılık kesimli DSGE kalibrasyonunda çeyreklik amortisman **0,035**, yatırım ayarlama maliyeti **4**, yerli yatırım malı payı **0,87**, ithal yatırım malı payı **0,13**, durağan durum yatırım/GSYH oranı **0,15** ve yıllık yatırım/sermaye oranı **0,148**'dir (PDF s. 48). Bu modelin koşulsuz ayrıştırmasında yatırım oynaklığının yüzde **92,67**'si TFV şokuna, yüzde **4,55**'i ülke risk primi şokuna atfedilir (PDF s. 49).

S082'de çeyreklik amortisman **0,035**, sermaye ayarlama maliyeti **3,6254** olarak kalibre edilir (PDF s. 193). İkinci değer Alp ve Elekdağ'a atfedilen dışsal kalibrasyondur; Türkiye verisinden bu tezde yeniden tahmin edilmiş bir katsayı değildir.

S002 sermaye hizmetlerini inşaat için **0,60**, makine-teçhizat için **0,40** ağırlıkla toplar; yıllık amortisman varsayımları sırasıyla **0,02** ve **0,16**'dır (PDF s. 4). S028 imalat sanayii sermaye stoku hesabında tüm varlıklar için yıllık **0,06** kullanır. Bu oranlar varlık kapsamı farklı olduğu için doğrudan ortalanmamalıdır.

### 4.2 Kamu yatırımının çıktı etkisi

S070'in 2002Q1–2012Q4 dönemi SVAR tahmininde kamu yatırımının etki çarpanı **2,1**, tepe çarpanı **3,6** (ikinci çeyrek) ve bir yıllık kümülatif çarpanı **1,7**'dir (PDF s. 14). Alternatif eşbütünleşme ve sıralama varsayımları bir yıllık değeri **0,4–1,7** aralığına taşır (PDF s. 15).

S071'in daha güncel 2007Q1–2024Q2 yerel projeksiyonunda kamu yatırımı etki çarpanı **0,9**, bir yıllık kümülatif çarpan **1,8**, beşinci çeyrekte ulaşılan tepe değer **2,4**'tür (PDF s. 57). S070 ve S071 arasındaki fark bir çelişki olarak değil; dönem, yöntem, şok tanımlama ve raporlanan ufuk farkı olarak okunmalıdır.

S084'ün 2012Q1–2022Q3 ARDL modelinde kamu yatırımının çıktı esnekliği uzun dönemde **0,283649**, kısa dönemde **0,083603**'tür (PDF s. 10–11). Bunlar harcama çarpanı değil log-log esnekliklerdir.

### 4.3 Kamu yatırımı, kamu borcu ve özel yatırım

Bu literatürde işaret ve büyüklük model tanımına duyarlıdır:

- S079'un 1986–2014 oran-düzeyi denkleminde kamu yatırımının özel yatırım katsayısı **-1,641885**, iç borcun katsayısı **-0,181155**'tir (PDF s. 28).
- S080'in 1975–2020 ARDL modelinde kamu yatırımı esnekliği uzun dönemde **-0,3622**, kısa dönemde **-0,1587**; iç kamu borcu esnekliği sırasıyla **-0,1079** ve **-0,2900**'dır. Dış kamu borcu pozitif, dış borç servisi negatiftir (PDF s. 13). FMOLS ve DOLS sağlamlık tahminleri de ayrı satırlarda korunmuştur (PDF s. 14).
- S083'te toplam kamu yatırımı özel yatırımı dışlarken, altyapı yatırımı bazı esnek hızlandıran denklemlerde pozitif; altyapı dışı kamu yatırımı negatiftir (PDF s. 7). Bu çalışma katsayıları kaynak denkleminin özgün ölçeğinde saklanmıştır.
- S086'nın yapısal kırılmaları dikkate alan kısa dönem denkleminde kamu yatırımı katsayısı **0,31**, banka kredisi katsayısı **0,26**'dır (PDF s. 12).

Dolayısıyla “kamu yatırımı özel yatırımı dışlar mı?” sorusunun tek bir parametre cevabı yoktur. Kamu yatırımının bileşimi, tahmin dönemi, borçlanma kanalı, kısa/uzun dönem ayrımı ve değişkenlerin ölçeği zorunlu filtrelerdir.

### 4.4 Nakit akışı ve Tobin'in q'su

S072'nin BIST firmaları için sabit etkiler tahmininde nakit akışı duyarlılığı firma büyüklüğüne göre belirgin biçimde değişir. Firma-bazlı büyüklük sınıflamasında küçük, orta ve büyük gruplar için katsayılar sırasıyla **-0,0743**, **0,2310** ve **0,3355**'tir (PDF s. 10). Uç nakit akışı gözlemleri çıkarıldığında sonuçlar önemli ölçüde değiştiğinden tüm sağlamlık panelleri ayrı kaydedilmiştir (PDF s. 12–13).

S073'ün sistem-GMM sonuçlarında nakit akışı katsayısı tüm firmalarda **0,1771**, küçük iş gruplarında **0,4857**, bağımsız firmalarda **0,5136**'dır; büyük iş grupları ve yabancı ortaklı firmalarda çok daha küçüktür (PDF s. 13). Parantez içindeki değerler standart hata değil p-değeridir; `notes` alanı bunu açıkça belirtir.

S075'in fark-GMM modelinde nakit akışı katsayısı KOBİ'lerde **0,163**, büyük firmalarda **0,060**, tüm örneklemde **0,100**'dür. Tobin q katsayıları sırasıyla **1,403**, **1,121** ve **1,001**'dir (PDF s. 28). Buradaki parantez içi değerler t-istatistiğidir.

### 4.5 Parasal koşullar, finansal kısıtlar ve ticari kredi

S074, 2005–2014 imalat firmalarında temel sistem-GMM denklemine parasal duruş ve finansal koşul etkileşimleri ekler:

- temel nakit akışı katsayısı KOBİ'lerde **0,215**, büyük firmalarda **0,197**;
- ticari kredi katsayısı KOBİ'lerde **0,460**, büyük firmalarda **0,630**;
- kaldıraç katsayısı sırasıyla **-0,375** ve **-0,151**'dir (PDF s. 21);
- genişletici parasal duruş ile nakit akışı etkileşimleri kullanılan göstergeye göre **-0,113 ile -0,349** arasındadır (PDF s. 23);
- küresel finansal kriz × nakit akışı etkileşimi **0,379**'dur (PDF s. 29).

S078'in anket ve idari veriyi eşleştiren modelinde yatırım/sermaye denklemindeki nakit akışı katsayısı **0,91**; zaman etkileri eklendiğinde **0,73**'tür. Nakit akışı × finansal kısıt etkileşimi sırasıyla **-0,20** ve **-0,19**'dur (PDF s. 13). Finansal kısıt endeksinin panel-logit ağırlıkları ayrıca saklanmıştır (PDF s. 14); bunlar yatırım denklemindeki doğrudan marjinal etkiler değildir.

### 4.6 Kaldıraç, borç yükü ve 2018 şoku

S076'nın 2009–2019 idari firma panelinde yatırım-kaldıraç ilişkisi ters U biçimindedir. Tercih edilen tam örneklem modelinde doğrusal kaldıraç katsayısı **0,04664**, kare terim **-0,02937** ve dönüm noktası **0,794**'tür (PDF s. 12). Dönüm noktası KOBİ'lerde **0,791**, büyük firmalarda **0,958**; ihracatçılarda **0,969**, ihracatçı olmayanlarda **0,773**'tür (PDF s. 15–16). Bu dönüm noktaları tahmin edilmiş iki katsayıdan türetilmiş sonuç olarak işaretlendi.

S077, 2018 finansal çalkantısını farkların farkı tasarımıyla kullanır. Sürekli kaldıraç ölçüsünde şok sonrası yatırım etkisi **-0,04383**; yüksek-kaldıraç göstergesinde **-0,01495**'tir (PDF s. 14). Etki mikro, küçük, orta, büyük; ihracatçı/ihracatçı olmayan; genç/yaşlı ve nakit akışı grupları için ayrı tutulmuştur (PDF s. 17–20). En belirgin sürekli-kaldıraç etkilerinden biri ihracatçı olmayan firmalarda **-0,05554**'tür.

### 4.7 Takip kontrolünde eklenen kaynaklar

S088'in eşleştirilmiş firma örnekleminde borsaya kotasyonun imalat firmalarının brüt maddi varlıklarına etkisi **0,283** (SH 0,124), net maddi varlıklarına etkisi **0,441** (SH 0,151) log puandır (PDF s. 18). İmalat dışı firmalardaki işaret farklıdır; bu nedenle kotasyon etkisi sektör ayrımı olmadan tek katsayıya indirgenmemelidir.

S089, 2012-2014 ortalama toplam yatırım/GSYH oranını **%20,3** olarak verir (PDF s. 17) ve büyüme muhasebesi simülasyonunda yıllık sermaye amortismanını **%3,6** varsayar (PDF s. 75). İlk değer betimsel oran, ikincisi rapor kalibrasyonudur.

S090'ın 1968-2006 kullanıcı maliyeti modelinde sermaye stoku yıllık **0,17** amortisman varsayımıyla kurulur; uzun dönem sermaye-çıktı esnekliği **0,78** (SH 0,00756) tahmin edilir. Yüksek amortisman oranı modelin sermaye kapsamı ve seri yapımıyla birlikte okunmalıdır.

## 5. Kaynak envanteri ve aktarım kararı

| ID | Kısa tanım | Yerel PDF | Sayısal aktarım |
|---|---|---:|---:|
| S067 | Mimir–Sunel bankacılık DSGE | Evet | Evet |
| S068 | Alp–Elekdağ kriz dönemi para politikası | Hayır; resmi tam metin | Hayır |
| S069 | Çebi–Özdemir doğrusal olmayan maliye | Evet | Evet; rejim eşiği |
| S070 | Çebi kamu harcaması çarpanı | Evet | Evet |
| S071 | TCMB Enflasyon Raporu 2025-II, Kutu 3.1 | Evet | Evet |
| S072 | Çobanoğlu–Gümrah nakit akışı | Evet | Evet |
| S073 | Çetenak–Vural iş grupları | Evet | Evet |
| S074 | Gül–Taştan finansal kısıtlar | Evet | Evet |
| S075 | Özmen–Şahinöz–Yalçın firma yatırımı | Evet | Evet |
| S076 | Yarba şirket borçluluğu | Evet | Evet |
| S077 | Yarba 2018 borç yükü şoku | Evet | Evet |
| S078 | Karasoy Can–Coşar kısıt endeksi | Evet | Evet |
| S079 | Kesbiç–Dündar–Devrim iç borçlanma | Evet | Evet |
| S080 | Serin–Demir kamu borcu | Evet | Evet |
| S081 | Arslan kamu/özel sermaye | Evet; tarama | Hayır; OCR riski |
| S082 | Çufadar doktora tezi/DSGE | Evet | Evet |
| S083 | Akkina–Celebi özel sabit yatırım | Evet | Evet |
| S084 | Yıldız–Kavak–Aktan kamu yatırımı ve büyüme | Evet | Evet |
| S085 | Gültekin Tarla–Temiz dışlama etkisi | Evet | Hayır; nitel sonuç |
| S086 | Çelik yapısal kırılmalar | Evet | Evet |
| S087 | Uslu–Altun Ada sabit sermaye ve gelir | Evet | Hayır; VAR/Granger |
| S088 | Yarba–Yassa borsaya kotasyon ve yatırım | Evet | Evet |
| S089 | Dünya Bankası Türkiye yatırım iklimi | Evet | Evet; betimsel/kalibrasyon |
| S090 | Mert kullanıcı maliyeti ve kapasite kullanımı | Evet | Evet |

## 6. Karşılaştırma için zorunlu uyarılar

1. **Çarpan ≠ esneklik ≠ regresyon katsayısı.** Kamu yatırımı için bu üç birim ayrı tutulmalıdır.
2. **Çeyreklik amortisman yıllık amortisman değildir.** Dönüşüm yapılacaksa bileşik dönüşüm ve varlık bileşimi belirtilmelidir.
3. **Ayarlama maliyeti parametresi model-spesifiktir.** Fonksiyonel biçim aynı değilse düzey karşılaştırması yanıltıcıdır.
4. **Nakit akışı duyarlılığı finansal kısıtın kusursuz ölçüsü değildir.** Ajans problemi, büyüme fırsatları ve ölçüm hatası aynı katsayıyı etkileyebilir.
5. **Kaldıraç modellerinde doğrusal ve kare terim birlikte okunur.** Tek başına doğrusal katsayı marjinal etkinin her yerde pozitif olduğu anlamına gelmez.
6. **Alt örneklem katsayıları havuzlanmamalıdır.** Firma büyüklüğü, ihracat durumu, iş grubu üyeliği ve nakit akışı sınıfları farklı iktisadi popülasyonlardır.
7. **Parantez içi istatistik aynı şey değildir.** S073 p-değeri, S075 ve S083 t-istatistiği, çoğu diğer firma çalışması standart hata raporlar.
8. **Dışsal kalibrasyon Türkiye tahmini değildir.** S001 ve S082'de bazı parametreler Türkiye modelinde kullanılsa da başka çalışmalardan alınmıştır.
9. **Borç tanımı önemlidir.** İç kamu borcu, dış kamu borcu, dış borç servisi ve firma kaldıraç oranı farklı kanallardır.
10. **Nedensellik iddiası yönteme bağlıdır.** Sabit etkiler, sistem GMM, SVAR, yerel projeksiyon ve farkların farkı aynı tanımlama gücüne sahip değildir.

## 7. Boşluklar ve sonraki tarama gündemi

- Türkiye için doğrudan sermayenin kullanıcı maliyeti ve yatırımın kullanıcı maliyeti esnekliği tahminleri az görünmektedir.
- Kontrollü sözlükteki yatırım oranı, sermaye/çıktı oranı ve sermaye stoku büyümesi için bu turda tanıma tam uyan, güvenilir biçimde sayısallaştırılmış bir tahmin bulunamadı; sözlük girdileri sonraki tarama için korunmuştur.
- Konut yatırımı, stok yatırımı ve yeşil/dijital yatırım ayrı alt aileler olarak genişletilebilir.
- Kamu yatırımının altyapı alt bileşenleri için güncel mikro/bölgesel tahmin açığı vardır.
- Tarım ve enerji yatırımlarında firma/tesis düzeyi ayarlama maliyeti parametreleri ayrıca taranmalıdır.
- S081 gibi taranmış eski çalışmalar için güvenilir çift girişli tablo transkripsiyonu yapılmadan katsayı eklenmemelidir.
- Erişime kapalı yayıncı tabloları, yalnızca özetten hareketle sayısallaştırılmamalıdır.

## 8. Yeniden üretilebilirlik

- Kaynak künyeleri ve URL'ler: `data/sources_updated.csv`
- Kontrollü parametre adları: `data/parameter_dictionary_updated.csv`
- Sayısal kayıtlar: `data/capital_investment_estimates_updated.csv`
- Yerel tam metinler: `sources/pdfs/`
- Dosya bütünlüğü: `sources/pdfs/SHA256SUMS.txt`

Bir web arayüzünde her değer gösterilirken en az `estimate_status`, `unit`, `definition_variant`, `data_period`, `sector`, `source_pdf_page` ve `verification_status` alanları birlikte sunulmalıdır.
