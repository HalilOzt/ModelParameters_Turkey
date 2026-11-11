# Veri yapısı

Bu klasör, Türkiye için üretim-teknoloji, sermaye-yatırım, fiyatlama-enflasyon-firma ve hanehalkı-tercihler parametrelerini kaynak, kavram ve gözlem düzeyinde ayırır. Amaç; aynı sayıyı tekrar girmeyi, kalibrasyonları tahmin gibi göstermeyi ve farklı tanım/birimlerdeki sonuçları birbirine karıştırmayı önlemektir.

## Dosyalar

- `data/parameter_dictionary.csv`: Kontrollü iki dilli parametre sözlüğü. Her parametrenin kalıcı kimliği, İngilizce/Türkçe adı, tipik sembolü, birimi ve karşılaştırma kuralı bulunur.
- `data/sources.csv`: Bir kaynak için tek satır. Yerel PDF yolu, erişim ve kapsam durumu burada tutulur.
- `data/production_technology_estimates.csv`: Bir kaynak-parametre-sektör-dönem kombinasyonu için tek satır. Aynı makaledeki farklı sektörler ve dönemler ayrı gözlemdir.
- `data/capital_investment_estimates.csv`: Sermaye ve yatırım ailesi için aynı uzun biçimli şemayı kullanır; alt örneklemler, sağlamlık tahminleri ve farklı ufuklar ayrı satırlardır.
- `data/pricing_inflation_firms_estimates.csv`: Fiyatlama, enflasyon ve firmalar ailesi için aynı uzun biçimli şemayı kullanır; fiyat türü, sektör, geçişkenlik ufku, enflasyon rejimi ve firma alt grubu ayrı satırlardır.
- `data/household_preferences_estimates.csv`: Hanehalkı ve tercihler ailesi için aynı uzun biçimli şemayı kullanır; tercih kalibrasyonları, tüketim ve emek arzı, risk paylaşımı, tasarruf, konut ve talep sistemi sonuçları ayrı satırlardır.
- `data/*_updated.csv`: Düzenleme anında temel CSV başka bir süreç tarafından kilitliyse, mevcut içerikle yeni kayıtların veri kaybı yaratmadan birleştirildiği sürüm. Kilit kalkınca temel dosyanın yerini alması amaçlanır.
- `sources/pdfs/SHA256SUMS.txt`: Arşivlenen PDF'lerin bütünlük özetleri.
- `sources/originals/`: Yayıncının PDF yerine sunduğu özgün belge gibi PDF dışı tam metinler; uzantı ve biçim yapay olarak değiştirilmez.

## Tahmin tablosu alanları

| Alan | Anlamı |
|---|---|
| `estimate_id` | Değişmeyen gözlem kimliği. |
| `source_id` | `sources.csv` içindeki kaynağa yabancı anahtar. |
| `parameter_id` | `parameter_dictionary.csv` içindeki kavrama yabancı anahtar. |
| `value`, `lower_bound`, `upper_bound`, `standard_error` | Nokta değeri ve varsa belirsizlik bilgisi. |
| `unit` | Değerin kesir, yüzde, yıllık yüzde puan, esneklik veya model birimi olduğunu gösterir. |
| `estimate_status` | Sayının tahmin, kalibrasyon, varsayım, türetilmiş sonuç, kısıt veya tahmin/projeksiyon olduğunu belirtir. |
| `model_family`, `estimation_method` | Model ve yöntem. |
| `data_period`, `frequency`, `sector` | Örneklem ve kapsam. |
| `definition_variant` | Aynı üst kavram altındaki kesin tanım; örneğin standart Solow artığı ile beşeri-sermaye-düzeltilmiş TFV'yi ayırır. |
| `source_pdf_page`, `source_locator` | PDF sayfası ve tablo/şekil/bölüm konumu. |
| `verification_status` | Yerel PDF'den veya web tam metninden doğrulama durumu. |
| `notes` | Karşılaştırmayı etkileyen uyarılar. |

## `estimate_status` için yorumlama sırası

1. `estimated`: Veriden ekonometrik olarak tahmin edilmiş katsayı.
2. `calculated` / `estimated_derived` / `derived`: Gelir payı, büyüme muhasebesi artığı veya girdi-çıktı hesabı gibi veriden türetilmiş değer.
3. `calibrated` / `assumed`: Tahmin öncesi sabitlenmiş değer.
4. `external_calibration`: Türkiye verisinden değil, başka bir çalışmadan alınmış kalibrasyon.
5. `tested_restriction_not_rejected` / `model_selected_restriction`: İstatistiksel test veya model seçimi sonucu uygulanan kısıt.
6. `forecast_contribution`: Gerçekleşme değil, ileriye dönük projeksiyon.
7. `estimated_preliminary`, `approximate_*`, `descriptive_time_varying_result`: Doğrudan nihai sabit parametre gibi kullanılmaması gereken sonuç.
8. `descriptive_statistic`, `range_reported`: Sırasıyla betimsel örneklem özeti ve tek nokta yerine kaynakta aralık olarak verilen değer.

## Temel karşılaştırma kuralları

- Yıllık ve çeyreklik şok sürekliliği veya amortisman oranları dönüşüm yapılmadan kıyaslanmaz.
- CES dağılım parametresi, gözlenen sermaye gelir payı ve Cobb-Douglas çıktı esnekliği aynı değişken değildir.
- Üretimin ithal içeriği ile ihracatın ithal içeriği farklı paydalara sahiptir.
- TFV büyümesi; standart Solow artığı, beşeri-sermaye-düzeltilmiş artığı, potansiyel TFV ve büyümeye katkı olarak ayrı tutulur.
- Stokastik sınır ayrıştırmasındaki teknik değişme, teknik etkinlik değişmesi ve ölçek etkisi, Solow artığı TFV ile aynı seri değildir.
- `lower_bound` ve `upper_bound` çoğunlukla güven aralığıdır; ancak S032'de farklı VAR sıralamalarındaki en küçük/en büyük değerleri gösterir. Bu istisna `notes` alanında açıkça işaretlenmiştir.
- ERP, CRM, SCM, EDI ve web sitesi katsayıları çoğunlukla log verimlilik regresyonlarındaki kullanıcı kuklalarıdır; nedensel etki gibi yorumlanmamalıdır. Genişbant kayıtları ise endojen geçiş regresyonundan tedavi etkileridir ve `log_points` birimindedir.
- Dijital sermaye, yazılım stoku, yazılım yatırımı ve BİT kullanan işgücü farklı girdilerdir; aynı “dijitalleşme etkisi” serisinde birleştirilmez.
- Translog üretim fonksiyonundaki birinci-derece katsayılar, girdiler ortalama etrafında merkezlenmemişse doğrudan ortalama çıktı esnekliği değildir. Bu kayıtlar `definition_variant` ve `notes` alanlarında açıkça “first-order translog coefficient” olarak işaretlenir.
- İkili ikame esneklikleri mutlaka iki girdinin adıyla filtrelenmelidir. Sermaye-doğal gaz, emek-hidroelektrik ve yakıtlar arası değerler tek bir genel ikame serisi olarak ortalanmaz.
- Etkinlik tablolarında `lower_bound` ve `upper_bound` alanları güven aralığı değil örneklem minimumu/maksimumu, `standard_error` alanı ise bazı kayıtlarda örneklem standart sapması olabilir; bu kullanım `notes` alanında belirtilir.
- Stokastik sınırdaki `gamma` etkinsizlik varyansı payıdır; teknik etkinlik skoru değildir. Grup sınırı, birleşik sınır ve metafrontier etkinlikleri de ayrı `definition_variant` değerleriyle saklanır.
- Teknolojik değişmenin girdi yanlılığı, nötr teknik değişme hızı değildir. Girdi adı, işaret konvansiyonu ve kaynakta 100 ile çarpılıp çarpılmadığı birlikte okunur.
- Maddi olmayan sermaye, yazılım, patent ve şerefiye katsayıları aynı toplama düzeyinde değildir; toplam maddi olmayan sermaye esnekliği alt bileşenlerle toplanmaz.
- Büyüme muhasebesindeki sermaye, beşerî sermaye ve TFV “katkıları” yüzde puandır; üretim fonksiyonu esnekliği veya ilgili girdinin büyüme hızı değildir.
- Sektörel değerler ancak aynı sektör kapsamı, dönemleştirme ve yöntemle karşılaştırılır.
- Web tam metninden doğrulanan fakat yerel PDF'si arşivlenemeyen kayıtlar `web_fulltext_verified` olarak kalır; kullanıcı arayüzünde bu durum görünür olmalıdır.
- Kamu yatırımı çarpanları, kamu yatırımı çıktı esneklikleri ve özel yatırım denklemi katsayıları aynı seri değildir; `unit`, `model_family` ve `definition_variant` ile ayrılır.
- Firma yatırımında nakit akışı, Tobin q, kaldıraç ve ticari kredi katsayıları ancak aynı yatırım paydası, firma evreni ve tahminci altında karşılaştırılır.
- Kaldıraç ile kaldıraç-karesi birlikte bulunan modellerde dönüm noktası türetilmiş sonuçtur; doğrusal katsayı tek başına marjinal etkinin yönünü vermez.
- Kaynakta parantez içinde verilen istatistiğin standart hata, t-istatistiği veya p-değeri olduğu `notes` alanından kontrol edilmelidir.
- Yatırım ve sermaye ayarlama maliyetleri ancak aynı fonksiyonel biçimdeki DSGE modelleri arasında doğrudan karşılaştırılabilir.
- Kur geçişkenliği; ticaret sınır fiyatı, ÜFE, TÜFE ve firma fiyatı için ayrı sonuçtur. Fiyat endeksi, şok normalizasyonu, kur işareti ve kümülatif ufuk eşleşmeden karşılaştırılmaz.
- `percent`, `fraction`, `percentage_points` ve `regression_coefficient` aynı ölçek değildir; yalnız birim bilgisi yeterli olduğunda ve tanım birebir eşleştiğinde dönüşüm yapılır.
- Fiyat değiştirme sıklığı ile Calvo fiyat yapışkanlığı aynı nesne değildir. İlki gözlenen fiyat değişimlerinin frekansı, ikincisi model döneminde yeniden fiyatlayamama olasılığıdır.
- İlan fiyatı, promosyon etkisinden arındırılmış düzenli fiyat ve gerçekleşen işlem fiyatı ayrı tutulur.
- Phillips eğrisi eğimleri enflasyon dönüşümü, maliyet göstergesi, çıktı açığı ve tahminci değiştiğinde yeni bir `definition_variant` gerektirir.
- Geçişkenlik hızı satırlarında `value` aralığın orta noktası, `lower_bound` ve `upper_bound` kaynakta verilen alt/üst ay sayısıdır; bu alanlar güven aralığı değildir.
- Firma beklenti çalışmalarında yüzde puan cinsinden TÜFE/ÜFE beklentileri ile üçlü ordinal ölçekli kendi fiyatı, maliyet ve görünüm cevapları aynı seride birleştirilmez.
- ATE, eşleştirilmiş ATT, OLS, CEM ve IV sonuçları tanımlama varsayımları nedeniyle ayrı varyantlardır.
- Piyasa yoğunlaşmasının mark-up etkisinde CR4 ve CR20 ölçüleri, yüksek enflasyon etkileşimi ve firma büyüklüğü etkileşimi ayrı kaydedilir.
- Standartlaştırılmış PLS-SEM yol katsayıları doğrudan fiyat esnekliği değildir; yalnız aynı gizil değişken ölçüm modeli içinde karşılaştırılır.
- Kaynak içi tutarsızlık düzeltilmeden saklanır. Örneğin S001 fiyat endekslemesi posterior ortalaması kaynakta 0,299 iken basılı güven aralığı 0,337-0,662'dir ve uyarı notuyla korunmuştur.
- Hanehalkı sonuçlarında tüketim miktarı, tasarruf miktarı, tasarruf oranı ve pozitif tasarruf yapma olasılığı farklı bağımlı değişkenlerdir; aynı seri içinde birleştirilmez.
- Cari gelir MPC'si, sürekli gelir katsayısı ve genel denge modelinin durağan durum MPC'si ayrı tanımlardır; model-içi sonuçlar mikro regresyon tahmini gibi sunulmaz.
- Probit katsayıları doğrudan olasılık veya marjinal etki değildir. Kohort katsayıları da referans kohorta göre farktır; `definition_variant` okunmadan mutlak düzey gibi yorumlanmaz.
- Marshallgil, Hicksgil ve Frisch fiyat esneklikleri farklı telafi ve fayda sabitliği kavramlarına dayanır. Talep malı ile fiyat malının yönü `sector` ve `definition_variant` alanlarında korunur.
- Riskten kaçınma katsayısı ile dönemler arası ikame esnekliği yalnız kaynak fayda fonksiyonu izin veriyorsa terslenebilir.
- İşgücü arzında mikro yoğun-marj ücret esnekliği ile DSGE emek faydasızlığı eğriliği aynı parametre değildir.
- Çok ülkeli emeklilik reformu katsayıları Türkiye'ye özgü nedensel etki sayılmaz; ülke kapsamı ve zorunlu/gönüllü sistem farkı `notes` alanında belirtilir.
- Demografik tasarruf sonuçları `forecast_contribution` statüsündedir; gerçekleşmiş tasarruf oranı olarak gösterilmez.
