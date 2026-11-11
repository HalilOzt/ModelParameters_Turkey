# Türkiye Ekonomisi Model Parametreleri

[![Canlı site](https://img.shields.io/badge/canlı%20site-GitHub%20Pages-23665f)](https://halilozt.github.io/ModelParameters_Turkey/)
[![GitHub Pages](https://github.com/HalilOzt/ModelParameters_Turkey/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/HalilOzt/ModelParameters_Turkey/actions/workflows/deploy-pages.yml)

Türkiye ekonomisine ilişkin model parametrelerini tek bir karşılaştırılabilir katalogda toplayan açık araştırma projesi. Uygulama; tahminleri, kalibrasyonları ve betimsel istatistikleri kaynak, yöntem, dönem, sektör ve tanım farklarını koruyarak keşfetmeyi sağlar.

**Canlı uygulama:** [halilozt.github.io/ModelParameters_Turkey](https://halilozt.github.io/ModelParameters_Turkey/)

## Proje özeti

- 131 kaynak kaydı
- 233 kontrollü, iki dilli parametre tanımı
- 3.921 kaynak-parametre-sektör-dönem-yöntem gözlemi
- 4 araştırma alanı: üretim ve teknoloji, sermaye ve yatırım, fiyatlama-enflasyon-firmalar, hanehalkı ve tercihler
- 3.800 PDF ve 121 web tam metni üzerinden doğrulanmış sayısal kayıt

## Uygulama

Statik ve bağımlılıksız web arayüzü; parametre ve kaynak araması, çoklu filtreleme, kaynak/parametre detay sayfaları, yöntem notları ve CSV indirmeleri sunar. GitHub Pages dağıtımı her `main` güncellemesinde GitHub Actions ile otomatik olarak yenilenir.

Yerelde çalıştırmak için:

```powershell
python sites/turkiye-ekonomisi-parametreleri/build_data.py
python -m http.server 8000 --directory sites/turkiye-ekonomisi-parametreleri/dist
```

Ardından `http://localhost:8000` adresini açın.

## Başlangıç noktaları

- Araştırma özeti ve bulgular: `docs/production_technology_research_report.md`
- Sermaye ve yatırım araştırma raporu: `docs/capital_investment_research_report.md`
- Fiyatlama, enflasyon ve firmalar araştırma raporu: `docs/pricing_inflation_firms_research_report.md`
- Hanehalkı ve tercihler araştırma raporu: `docs/household_preferences_research_report.md`
- Alan ve statü açıklamaları: `docs/data_dictionary.md`
- İki dilli parametre sözlüğü: `data/parameter_dictionary.csv`
- Kaynak kataloğu: `data/sources.csv`
- Uzun biçimli tahmin tablosu: `data/production_technology_estimates.csv`
- Sermaye ve yatırım tahmin tablosu: `data/capital_investment_estimates.csv`
- Fiyatlama, enflasyon ve firmalar tahmin tablosu: `data/pricing_inflation_firms_estimates.csv`
- Hanehalkı ve tercihler tahmin tablosu: `data/household_preferences_estimates.csv`
- Birleşik güncel kaynak, parametre ve sermaye-yatırım sürümleri: `data/sources_updated.csv`, `data/parameter_dictionary_updated.csv`, `data/capital_investment_estimates_updated.csv`
- Arşivlenen PDF'ler: `sources/pdfs/`
- PDF bütünlük özetleri: `sources/pdfs/SHA256SUMS.txt`

## Veri modeli

Katalog üç katmanlıdır:

1. **Kaynak:** Yazar, yıl, kurum, DOI, yayıncı bağlantısı ve erişim durumu.
2. **Kavram:** Türkçe/İngilizce ad, sembol, birim, tanım ve karşılaştırma kuralı.
3. **Gözlem:** Tekil kaynak-parametre-sektör-dönem-yöntem kombinasyonu.

Bu yapı, aynı isim altındaki ekonometrik tahminlerin, kalibrasyonların, büyüme muhasebesi artıklarının ve betimsel istatistiklerin yanlışlıkla tek seri kabul edilmesini engeller.

## Kullanım ilkesi

Bir değeri sitede göstermeden önce `estimate_status`, `unit`, `definition_variant`, `data_period`, `sector` ve `verification_status` alanları birlikte okunmalıdır. Aynı parametre adı altındaki kalibrasyonlar, ekonometrik tahminler, büyüme muhasebesi artıkları ve betimsel mikro-fiyat istatistikleri varsayılan olarak ayrı seri olmalıdır.

> Not: 17 Ekim 2026 güncellemesi sırasında üç temel CSV başka bir süreç tarafından kilitliydi. Birleşik ve doğrulanmış içerik veri kaybı yaratmamak için `_updated.csv` sürümlerine yazıldı. `scripts/build_pricing_dataset.py` ve `scripts/build_household_dataset.py` birleşik sürümleri idempotent biçimde yeniden üretir.

## Kaynak dosyaları hakkında

İndirilen makale PDF'leri ve tam metin çıktıları, dosya boyutu ve yeniden dağıtım hakları nedeniyle herkese açık GitHub deposuna eklenmez. Yerel arşivin bütünlük özetleri `sources/pdfs/SHA256SUMS.txt` dosyasında tutulur; türetilen katalog, raporlar, kod ve indirilebilir veri tabloları depoda yer alır.
