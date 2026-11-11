# Hanehalkı ve tercihler: Türkiye tahminleri araştırma raporu

## Kapsam ve sonuç

Bu tarama, Türkiye için hanehalkı tercihlerini ve bunların gözlenebilir sonuçlarını ölçen dört literatür kümesini birlikte ele alır:

1. DSGE ve genel denge modellerindeki yapısal tercih kalibrasyonları,
2. tüketim, emek arzı ve risk paylaşımı tahminleri,
3. tasarruf, ihtiyati tasarruf ve bireysel emeklilik sonuçları,
4. konut ve mal grubu talep esneklikleri.

Araştırma sonunda 18 yeni kaynak PDF olarak arşivlendi. Önceden arşivlenmiş dört model kaynağındaki hanehalkı blokları da yeniden incelendi. `data/household_preferences_estimates.csv` dosyasında 20 kaynaktan, 52 ayrı parametre kimliği altında 945 sayısal gözlem bulunmaktadır. Bütün gözlemler yerel PDF sayfasından doğrulanmış, tablo veya metin konumu kaydedilmiştir.

S128 Dünya Bankası sentez raporu ve S131 TCMB Hanehalkı Finans ve Tüketim Anketi metodoloji raporu kaynak kataloğuna alınmış; fakat özgün tahmin üretmedikleri veya özgün çalışmaları özetledikleri için yinelenen sayısal gözlem yaratılmamıştır.

## Tarama ve kayıt yöntemi

- TCMB çalışma tebliğleri, Kalkınma Bakanlığı/SBB uzmanlık tezi, Dünya Bankası raporu, BETAM çalışma tebliği ve hakemli dergi makaleleri tarandı.
- Yalnız Türkiye verisi kullanan tahminler ile Türkiye için kurulmuş modeller çekirdek kapsama alındı.
- Çok ülkeli bireysel emeklilik paneli Türkiye'yi içerdiği için kaydedildi; ancak `notes` alanında Türkiye'ye özgü nedensel tahmin olmadığı açıkça belirtildi.
- Her değer `estimated`, `calibrated`, `external_calibration`, `model_implied`, `estimated_derived`, `forecast_contribution` veya `scenario_calculation` statülerinden uygun olanıyla işaretlendi.
- Aynı makaledeki alternatif tanımlar, yöntemler, sektörler, yaş/kohort grupları ve senaryolar ayrı satırlara yazıldı.
- Esneklik, yüzde, yüzde puan, kesir, log puan ve kaynak-özel regresyon katsayıları birbirine dönüştürülmeden korundu.
- Basılı tabloda sıra dışı görünen değerler “düzeltilmedi”; kaynakta yazıldığı biçimde ve uyarı notuyla saklandı.

## Kaynak envanteri

| Kimlik | Kaynak | Ana katkı | Sayısal kayıt |
|---|---|---|---:|
| S001 | Yüksel (2013) | DSGE tercih ve işgücü şokları | 11 |
| S067 | Mimir ve Sunel (2015) | Bankacılık DSGE hanehalkı kalibrasyonu | 9 |
| S082 | Çufadar (2012) | Konutlu DSGE tercih kalibrasyonu | 6 |
| S104 | Firma beklentileri çalışmasının DSGE eki | Genel tercih kalibrasyonu | 4 |
| S114 | Ceritoğlu (2013) | Gelir, faiz, kredi ve iş beklentilerinin tüketim etkisi | 45 |
| S115 | Ceritoğlu (2011) | Emek geliri riski ve ihtiyati tasarruf | 24 |
| S116 | Ceritoğlu (2020) | Cari ve sürekli gelirden MPC; yaş farklılıkları | 16 |
| S117 | Ceritoğlu (2017) | Kohortlar arası risk paylaşımı ve refah kazancı | 132 |
| S118 | Ceritoğlu (2012) | Sağlık sigortası ve ihtiyati tasarruf | 32 |
| S119 | Ceritoğlu (2017) | Konut talebi gelir, fiyat ve faiz esneklikleri | 8 |
| S120 | Ceritoğlu (2017) | Konut sahipliği, borç ve konut servetinde kohort etkileri | 159 |
| S121 | Pektaş Erdem (2017) | Hanehalkı tasarruf oranının 2SLS belirleyicileri | 79 |
| S122 | Aykaç (2016) | İşgücü arzının ücret esnekliği | 12 |
| S123 | Telatar, Telatar ve Türkmen (2000) | Frisch talep sistemi ve dönemler arası ikame | 16 |
| S124 | Alpay ve Koç (2002) | Tam Marshallgil/Hicksgil talep matrisi | 210 |
| S125 | Çebi Karaaslan, Oktay ve Alkan (2022) | Tasarruf yapma olasılığı esneklikleri | 70 |
| S126 | Ceritoğlu ve Eren (2014) | 2050'ye demografik tasarruf projeksiyonu | 16 |
| S127 | Aktaş vd. (2012) | Yıllık ve gelir dilimi bazında tasarruf katsayıları | 72 |
| S129 | Özel ve Yalçın (2013) | Emeklilik reformu etkisi ve BES senaryoları | 17 |
| S130 | Kalafatcılar (2019) | Örtüşen nesiller modelinde tercih kalibrasyonu | 7 |

## 1. Yapısal tercih parametreleri

### İskonto faktörü

- S001 küçük açık ekonomi DSGE modeli: çeyreklik `beta = 0,9928`; yüzde 3 yıllık reel faiz hedefiyle kalibre edilmiştir.
- S067 bankacılık DSGE modeli: `beta = 0,9821`; yüzde 7,48 yıllıklandırılmış reel mevduat faizi hedefidir.
- S082 konutlu DSGE: baz modelde `0,985`, alternatifte `0,990`.
- S104 ve S130: `0,99`.

Bu değerler aynı ekonomik nesneyi temsil etse de hedef reel faiz, model yapısı ve durağan durum büyüme düzeltmesi eşleşmeden ortalanmamalıdır.

### Riskten kaçınma ve dönemler arası ikame

- Göreli riskten kaçınma S067'de `2`, S082 ve S104'te `1` olarak kalibre edilmiştir.
- S130 örtüşen nesiller modelinde dönemler arası ikame esnekliği `0,5`'tir. Kaynaktaki `sigma=(1-rho)^-1` bağıntısına karşılık gelen fayda eğrilik üssü `rho=-1` ayrıca saklanmıştır; bu değer doğrudan “riskten kaçınma katsayısı” diye etiketlenmemiştir.
- S123 Frisch talep sistemi Türkiye için toplam dönemler arası ikame esnekliğini `0,048` tahmin eder. Mal grubu değerleri `0,011` ile `0,109` arasındadır.

Model kalibrasyonları ile ekonometrik Frisch talep sistemi tahmini aynı sütunda doğrudan karşılaştırılmamalıdır. S123'ün değeri 1988Q1-1999Q2 dönemi ve belirli bir talep sistemi normalizasyonuna aittir.

### Alışkanlık, emek tercihi ve tüketim bileşimi

- Dışsal alışkanlık sürekliliği S067'de `0,7`, S082'de baz `0,9` ve alternatif `0,8`, S104'te `0,5`tir.
- S001'de emek arz esnekliği dışsal kalibrasyon olarak `1`dir. S067 tablosu `xi=5` değerini “labor supply elasticity” diye etiketler; model metni bunun ters esneklik/eğrilik rolü oynayabileceğini düşündürdüğünden özel uyarıyla saklanmıştır.
- S122'nin Türkiye mikro verisine dayalı yoğun marj ücret esnekliği fark-GMM'de `0,094`, sistem-GMM'de `0,059`, OLS'de `0,019`dur. Makalenin öne çıkardığı değer yaklaşık `0,06`dır.
- S001 tüketimde ithal mal ağırlığını `0,25`, S067 ise `0,60` kalibre eder. Bunlar modeldeki farklı ticaret ve bankacılık bloklarına aittir; gözlenen ithalat harcama payı gibi yorumlanmamalıdır.

## 2. Tüketim eğilimleri ve finansal koşullar

### Gelire duyarlılık

S114'te toplam tüketim büyümesinin reel harcanabilir gelir büyümesine katsayısı modele göre `0,267-0,895`; dayanıklı mal tüketiminde `0,353-1,789`; dayanıksız mal ve hizmetlerde `0,039-0,555` aralığındadır. Bu aralık güven aralığı değil, farklı araç ve kontrol setlerine sahip GMM spesifikasyonlarıdır.

Reel faiz katsayıları toplam tüketimde `-0,004` ile `-0,002`, dayanıklı tüketimde `-0,006` ile `0,002` arasında değişir. Kredi büyümesi katsayıları toplam tüketimde `0,078-0,099`, dayanıklı tüketimde `0,158-0,192`dir. İş beklentileri katsayısı dayanıklı tüketimde `0,446-0,499` ile diğer tüketim bileşenlerinden daha büyüktür.

### Marjinal tüketim eğilimi

S116'nın cari gelirden MPC tahminleri tüm örneklemde yaklaşık `0,833-0,900`dür. Yaş gruplarında yaşlılar `1,014`, orta yaşlılar `0,804`, gençler `0,617` olarak tahmin edilmiştir. Sürekli gelir katsayıları alternatif tanımlarda `0,674-1,001` aralığındadır.

S130 genel denge modelinin başlangıç durağan durumunda model-içi MPC emekliler için `0,025`, çalışanlar için `0,018`dir. Bunlar mikro regresyon katsayısı değil, modelin çeyreklik durağan durum sonuçlarıdır.

## 3. Risk paylaşımı ve ihtiyati tasarruf

S117, tüketim büyümesinin kohort gelirine duyarlılığını Türkiye geneli, kırsal-kentsel ayrımı ve yaş grupları için rapor eder. Kohort geliri katsayıları temel bölgesel spesifikasyonlarda `0,388-0,701`; yaş gruplarında `0,283-0,756` arasındadır. Tam sigorta ile elde edilecek sürekli-tüketim eşdeğeri refah kazancı, riskten kaçınma `2` iken Türkiye genelinde `%0,53`, `5` iken `%1,32`dir. Kırsal kesimde karşılıkları `%1,01` ve `%2,53`tür.

S115'te emek geliri riski katsayıları iki risk tanımına ve iki tasarruf tanımına göre yaklaşık `0,000120-0,000338` aralığındadır. Katsayıların küçük görünmesi risk değişkeninin ölçeğinden kaynaklanır. Makalenin örneklem ortalamasındaki esneklik hesabına göre emek geliri riskindeki yüzde 10 artış tasarrufu yaklaşık yüzde `2,2-3,5` artırmaktadır.

S118'de sigorta türü endojen kabul edildiğinde zorunlu sigortanın tasarruf katsayısı kullanılan tasarruf tanımına göre `135,237` veya `188,794`; gönüllü özel sigortanın katsayısı `-507,220` veya `-708,092`; yeşil kartın katsayısı `-205,761` veya `-287,248`dir. Bunlar parasal tasarruf düzeyi regresyonlarıdır; oran ya da esneklik değildir.

## 4. Tasarruf davranışı

### Hanehalkı tasarruf oranı

S121'in 2004-2013 2SLS tahmininde log reel gelir katsayısı `0,159`, tüketici kredisi/GSYH katsayısı `-0,017`, çalışan kadın payı `0,100`, genç bağımlılık `-0,083`, yaşlı bağımlılık `0,121`dir. Gelir dilimleri itibarıyla gelir katsayısı birinci dilimde `0,425`, beşinci dilimde `0,239`dur.

S127'de yıllık log gelir katsayısı 2003-2008 arasında `0,026-0,147` aralığındadır. Havuzlanmış gelir dilimi regresyonunda katsayı `0,065`; Q1-Q4 için `0,117-0,175`, Q5 için `0,028`dir. Çocuk bağımlılık katsayısı bütün yıllarda negatiftir; yaşlı bağımlılık katsayısı çoğu yılda pozitiftir. Emekli aylığının hane gelirindeki payı bütün yıllarda `-0,055` ile `-0,112` arasındadır.

### Tasarruf yapma olasılığı

S125'in 2015-2017 logit/probit sonuçlarında gelir dilimi katsayıları güçlü ve monotondur: Q2 için `0,671/0,737`, Q5 için `2,114/2,231`. Özel sigorta `0,351/0,407`, ikinci konut `0,209/0,246`; kiracılık `-0,334/-0,378`, kredi kartı sahipliği `-0,149/-0,156`, sigara kullanımı `-0,279/-0,318` olarak raporlanmıştır. Bunlar tasarruf miktarının değil, pozitif tasarruf yapma olasılığının esneklikleridir.

### Demografik projeksiyon

S126'ya göre yalnız demografik değişim hanehalkı tasarruf oranını 2010-2050 arasında `2,21` yüzde puan artırıp 2050'de `%11,24` düzeyine taşımaktadır. İşgücüne katılım ve üniversite mezuniyetindeki değişimler eklendiğinde toplam artış `7,61` puan, 2050 seviyesi `%17,72`dir. Bileşen katkıları demografi `1,91`, işgücüne katılım `1,45`, üniversite eğitimi `4,59`, çapraz etki `-0,35` puandır.

### Bireysel emeklilik

S129'un 16 gelişmekte olan ülkeyi kapsayan panelinde özel emeklilik reformunun birikimli tasarruf oranı katsayısı yedinci gecikmede sabit etkilerle `1,450`, sistem-GMM ile `1,474` yüzde puana ulaşır. Çalışma, etkinin çoğunlukla zorunlu sistemlerden geldiğini ve Türkiye'nin gönüllü BES'i için doğrudan aynı büyüklüğün beklenmemesi gerektiğini vurgular.

Türkiye BES birikim senaryosunda emeklilik fonunun devlet katkısı oranına esnekliği `0,29`, fon işletim giderine `-0,31`, yönetim giderine `-0,03`tür.

## 5. Konut tercihleri ve serveti

S119'da konut talebinin sürekli gelir esnekliği üç spesifikasyonda da `0,243`tür. Fiyat esnekliği `-0,289` ve `-0,353`, reel mortgage faizi esnekliği `-0,0128`dir; fiyat ve faiz tahminleri geniş standart hatalara sahiptir. Genişletilmiş ev sahibi örnekleminde gelir esnekliği `0,25`, faiz esnekliği `-0,024` bulunmuştur.

S120, 1945 doğum kohortuna göre 1946-1975 kohortlarının konut sahipliği, ikinci konut, konut borcu ve konut değeri profillerini tam olarak kaydeder. 1975 kohortunun konut sahipliği katsayısı `-0,461`, konut borcu katsayısı `0,208`dir. Aynı kohortun konut değeri etkisi kalite düzeltmesi öncesi `1,688` log puan, kalite düzeltmesi sonrası `0,670` log puandır. Kalite düzeltmesi genç kohortların yüksek konut değerinin önemli bölümünü açıklar; fakat etkiyi tamamen ortadan kaldırmaz.

## 6. Talep sistemi esneklikleri

S124'ün 1994 Hanehalkı Tüketim Harcamaları Anketiyle tahmin ettiği 10 mal gruplu AIDS sisteminde 100 Marshallgil ve 100 Hicksgil fiyat esnekliği ayrı satırlarda tutulur. Marshallgil öz-fiyat esneklikleri gıdada `-0,71`, giyimde `-0,98`, konutta `-0,74`, mobilyada `-0,84`, sağlıkta `-1,33`, ulaştırmada `-0,25`, enerjide `-0,39`, eğitimde `-1,24`, turizmde `-1,07`, diğer mallarda `-0,84`tür.

Harcama esneklikleri gıda `0,56`, giyim `1,20`, konut `0,87`, mobilya `1,64`, sağlık `0,74`, ulaştırma `1,94`, enerji `1,70`, eğitim `1,94`, turizm `1,10`, diğer mallar `1,52` olarak tahmin edilmiştir. Çapraz fiyat esneklikleri talep malı ve fiyat malı yönü korunarak kaydedilmiştir; matris simetrik olmak zorunda değildir.

S123'ün Frisch sisteminde harcama esneklikleri gıda `1,256`, yarı-dayanıklı/dayanıksız mallar `0,525`, enerji-ulaştırma-haberleşme `0,360`, hizmetler `2,261`, konut `0,227`dir. S123 ve S124 farklı dönem, veri yapısı ve talep sistemi kullandığı için sonuçları tek bir “Türkiye harcama esnekliği” ortalamasına indirgemek doğru değildir.

## Karşılaştırma ve kullanım uyarıları

1. **MPC aynı birimde değildir.** Mikro tüketim-gelir regresyonu, parasal tasarruf denklemindeki gelir katsayısı ve genel denge modelinin durağan durum MPC'si ayrı serilerdir.
2. **Riskten kaçınma ile IES otomatik olarak birbirinin tersi değildir.** Bu ilişki yalnız kullanılan fayda fonksiyonu buna izin veriyorsa kurulabilir.
3. **İşgücü arzında yoğun/geniş marj ayrımı korunmalıdır.** S122 yoğun marj ücret esnekliğini ölçer; DSGE kalibrasyonları tercih eğriliğini temsil edebilir.
4. **Tasarruf miktarı, tasarruf oranı ve tasarruf yapma olasılığı farklı bağımlı değişkenlerdir.** Aynı parametre grafiğine konmamalıdır.
5. **Kohort katsayıları mutlak düzey değildir.** S120'de 1945 doğum kohortu referanstır; katsayılar referansa göre farktır.
6. **Probit katsayısı marjinal etki değildir.** Olasılık değişimine dönüştürmek için örneklemdeki kovaryat değerleri ve normal yoğunluk gerekir.
7. **Fiyat esnekliği matrisi yönlüdür.** “Talep edilen mal” satırı ile “fiyatı değişen mal” sütunu ters çevrilmemelidir.
8. **Projeksiyon tahmin değildir.** S126 sonuçları varsayılan demografik, eğitim ve işgücüne katılım patikalarına bağlıdır.
9. **BES panel sonucu Türkiye'ye doğrudan taşınmamalıdır.** Çok ülkeli örneklemin çoğu zorunlu sisteme sahiptir.
10. **Kaynak tablolarındaki sıra dışı değerler korunmuştur.** Özellikle S117 refah tablosundaki bazı `rho=2` ve `rho=5` çiftleri monoton değildir; veri temizliği sırasında değiştirilmemiştir.

## Dosyalar

- Tahminler: `data/household_preferences_estimates.csv`
- Güncel kaynak kataloğu: `data/sources_updated.csv`
- Güncel iki dilli parametre sözlüğü: `data/parameter_dictionary_updated.csv`
- PDF arşivi: `sources/pdfs/`
- Bütünlük özetleri: `sources/pdfs/SHA256SUMS.txt`
- Yeniden üretim betiği: `scripts/build_household_dataset.py`

