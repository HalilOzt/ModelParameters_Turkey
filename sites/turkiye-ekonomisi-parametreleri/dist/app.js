const state = {
  data: null,
  lang: new URLSearchParams(location.search).get("lang") === "en" ? "en" : "tr",
  paramFilters: { q: "", family: "", className: "", unit: "" },
  sourceFilters: { q: "", year: "", type: "" },
};

const copy = {
  tr: {
    locale: "tr-TR",
    title: "Türkiye Ekonomisi Model Parametreleri",
    metaDescription: "Türkiye ekonomisi için tahmin edilen ve kalibre edilen iktisadi model parametrelerini kaynak, yöntem ve dönem bazında keşfedin.",
    ogDescription: "131 kaynak, 233 parametre ve 3.921 gözlemden oluşan karşılaştırmalı açık araştırma kataloğu.",
    static: {
      skip: "İçeriğe geç", home: "Ana sayfa", brandTitle: "Türkiye Ekonomisi", brandSubtitle: "Model Parametreleri",
      menu: "Menü", navLabel: "Ana menü", parameters: "Parametreler", sources: "Kaynaklar", about: "Yöntem", downloads: "Veri",
      switchText: "EN", switchLabel: "View site in English", loading: "Veri kataloğu hazırlanıyor…",
      footerTitle: "Türkiye Ekonomisi Model Parametreleri", footerDescription: "Kaynak, yöntem ve tanım farklılıklarını görünür kılan açık araştırma kataloğu.",
      sourceLink: "Kaynak kodu GitHub'da inceleyin ↗", generated: "Son veri üretimi:",
    },
    families: {
      "production-technology": ["Üretim ve Teknoloji", "Üretim fonksiyonları, faktör payları, verimlilik ve teknoloji dinamikleri."],
      "capital-investment": ["Sermaye ve Yatırım", "Sermaye birikimi, yatırım davranışı, finansman koşulları ve kamu yatırımları."],
      "pricing-inflation-firms": ["Fiyatlama, Enflasyon ve Firmalar", "Fiyat ayarlama, enflasyon dinamikleri, geçişkenlik ve firma davranışları."],
      "household-preferences": ["Hanehalkı ve Tercihler", "Tüketim, tasarruf, emek arzı, konut ve hanehalkı tercihleri."],
    },
    status: {
      estimated: "Tahmin", calibrated: "Kalibrasyon", external_calibration: "Dışsal kalibrasyon", estimated_derived: "Türetilmiş tahmin",
      derived: "Türetilmiş", forecast_contribution: "Projeksiyon", model_implied: "Model sonucu", calculated: "Hesaplanan",
      descriptive_statistic: "Betimsel", pdf_verified: "PDF’den doğrulandı", web_fulltext_verified: "Web tam metni",
      archived: "Arşivlendi", in_scope: "Kapsam içi", excluded: "Kapsam dışı",
    },
    home: {
      eyebrow: "Türkiye için karşılaştırmalı araştırma kataloğu", heading: "İktisadi model parametrelerini tek yerde keşfedin.",
      lead: "Tahminleri, kalibrasyonları ve projeksiyonları; kaynak, yöntem, dönem ve tanım farklılıklarını kaybetmeden inceleyin.",
      searchPlaceholder: "Parametre, yazar, çalışma veya model ara…", searchLabel: "Katalogda ara", research: "Araştırma alanları",
      clusters: "Dört ana literatür kümesi", clusterLead: "Her alan kendi parametre tanımlarıyla tutulur; farklı ekonomik nesneler aynı seri içinde karıştırılmaz.",
      stats: ["kaynak kaydı", "iki dilli parametre", "sayısal gözlem", "arşivlenmiş PDF"], metrics: ["parametre", "gözlem", "kaynak"],
    },
    parameters: {
      eyebrow: "Kontrollü kavram sözlüğü", heading: "Parametreler", lead: "Türkçe ve İngilizce adları, sembolleri, karşılaştırma kuralları ve bunlara bağlı bütün sayısal gözlemleri inceleyin.",
      search: "Arama", searchPlaceholder: "Örn. iskonto faktörü, TFP, geçişkenlik", family: "Araştırma alanı", allFamilies: "Tüm alanlar",
      className: "Parametre sınıfı", allClasses: "Tüm sınıflar", unit: "Birim", allUnits: "Tüm birimler", clear: "Filtreleri temizle",
      columns: ["Parametre", "Sembol", "Sınıf", "Gözlem", "Kaynak", "Birim"], count: n => `${n} parametre gösteriliyor`, empty: "Bu filtrelerle eşleşen parametre bulunamadı.",
    },
    sources: {
      eyebrow: "Bibliyografik envanter", heading: "Kaynaklar", lead: "Çalışma tebliğleri, makaleler, tezler ve raporlar; erişim ve kapsam durumlarıyla birlikte.",
      search: "Arama", searchPlaceholder: "Başlık, yazar veya kurum", year: "Yıl", allYears: "Tüm yıllar", type: "Kaynak türü", allTypes: "Tüm türler", clear: "Filtreleri temizle",
      columns: ["Kaynak", "Yıl", "Tür", "Parametre", "Gözlem", "Durum"], count: n => `${n} kaynak gösteriliyor`, empty: "Bu filtrelerle eşleşen kaynak bulunamadı.",
    },
    estimates: {
      empty: "Bu kayda bağlı sayısal gözlem bulunmuyor.", columns: ["Değer", "Statü", "Kaynak / Parametre", "Model ve yöntem", "Dönem", "Konum"], se: "SH", page: "PDF s.",
    },
    parameterDetail: {
      back: "← Parametrelere dön", noSymbol: "Sembol yok", definition: "Tanım", comparison: "Karşılaştırma kuralı", records: "Sayısal kayıtlar", observation: "gözlem",
      summary: "Kapsam özeti", source: "Kaynak", unit: "Birim", area: "Alan",
    },
    sourceDetail: {
      back: "← Kaynaklara dön", noDate: "Tarih yok", info: "Kaynak bilgisi", callout: "Yerel PDF araştırma doğrulaması için arşivlenmiştir; kamuya açık sitede yayıncı bağlantısı sunulur.",
      records: "Çıkarılan kayıtlar", observation: "gözlem", bibliography: "Bibliyografya", institution: "Kurum / dergi", year: "Yıl", pages: "PDF sayfası", parameter: "Parametre", scope: "Kapsam", original: "Orijinal yayına git ↗",
    },
    about: {
      eyebrow: "Şeffaf ve yeniden üretilebilir", heading: "Yöntem", lead: "Bu katalog aynı sayıyı iki kez girmemek, kalibrasyonları tahmin gibi göstermemek ve farklı tanımları birbirine karıştırmamak için kaynak, kavram ve gözlem katmanlarını ayırır.",
      cards: [
        ["Kaynak katmanı", "Her çalışma tek kaynak kimliğiyle tutulur. Yazar, yıl, kurum, DOI, yayıncı bağlantısı, erişim ve kapsam durumu ayrı alanlardır."],
        ["Kavram katmanı", "Her parametrenin Türkçe ve İngilizce adı, sembolü, birimi, tanımı ve karşılaştırma kuralı kontrollü sözlükte tanımlanır."],
        ["Gözlem katmanı", "Bir kaynak-parametre-sektör-dönem-yöntem kombinasyonu bir satırdır. Alternatif modeller ve sağlamlık tahminleri ayrı tutulur."],
        ["Doğrulama", "Değerlerin PDF sayfası ve tablo/şekil konumu kaydedilir. Yerel PDF arşivi bütünlük özetiyle korunur."],
        ["Tahmin ve kalibrasyon", "Ekonometrik tahmin, dışsal kalibrasyon, türetilmiş değer, model sonucu ve projeksiyon aynı statüde gösterilmez."],
        ["Karşılaştırılabilirlik", "Birim, model sıklığı, sektör, dönem ve kesin tanım eşleşmeden değerler otomatik olarak ortalanmaz veya tek grafikte birleştirilmez."],
      ],
    },
    downloads: {
      eyebrow: "Makinece okunabilir veri", heading: "Veri dosyaları", lead: "Kataloğun kaynak, parametre ve gözlem tablolarını UTF-8 CSV biçiminde indirin. Değerleri kullanırken statü, birim ve karşılaştırma kuralını birlikte okuyun.",
      files: ["Güncel kaynak kataloğu", "İki dilli parametre sözlüğü", "Üretim ve teknoloji tahminleri", "Sermaye ve yatırım tahminleri", "Fiyatlama, enflasyon ve firmalar", "Hanehalkı ve tercihler"],
    },
    notFound: { heading: "Kayıt bulunamadı", lead: "Aradığınız parametre veya kaynak veri kataloğunda bulunmuyor.", back: "Ana sayfaya dön" },
    error: { eyebrow: "Veri hatası", heading: "Katalog yüklenemedi" },
  },
  en: {
    locale: "en-US",
    title: "Model Parameters for the Turkish Economy",
    metaDescription: "Explore estimated and calibrated economic model parameters for the Turkish economy by source, method, and period.",
    ogDescription: "A comparative open research catalog with 131 sources, 233 parameters, and 3,921 observations.",
    static: {
      skip: "Skip to content", home: "Home", brandTitle: "Turkish Economy", brandSubtitle: "Model Parameters",
      menu: "Menu", navLabel: "Main navigation", parameters: "Parameters", sources: "Sources", about: "Methodology", downloads: "Data",
      switchText: "TR", switchLabel: "Siteyi Türkçe görüntüle", loading: "Preparing the data catalog…",
      footerTitle: "Model Parameters for the Turkish Economy", footerDescription: "An open research catalog that makes differences in sources, methods, and definitions visible.",
      sourceLink: "View the source code on GitHub ↗", generated: "Last data build:",
    },
    families: {
      "production-technology": ["Production and Technology", "Production functions, factor shares, productivity, and technology dynamics."],
      "capital-investment": ["Capital and Investment", "Capital accumulation, investment behavior, financing conditions, and public investment."],
      "pricing-inflation-firms": ["Pricing, Inflation, and Firms", "Price adjustment, inflation dynamics, pass-through, and firm behavior."],
      "household-preferences": ["Households and Preferences", "Consumption, saving, labor supply, housing, and household preferences."],
    },
    status: {
      estimated: "Estimated", calibrated: "Calibrated", external_calibration: "External calibration", estimated_derived: "Derived estimate",
      derived: "Derived", forecast_contribution: "Forecast contribution", model_implied: "Model-implied", calculated: "Calculated",
      descriptive_statistic: "Descriptive statistic", pdf_verified: "Verified from PDF", web_fulltext_verified: "Verified from web full text",
      archived: "Archived", in_scope: "In scope", excluded: "Excluded",
    },
    home: {
      eyebrow: "A comparative research catalog for Turkey", heading: "Explore economic model parameters in one place.",
      lead: "Compare estimates, calibrations, and projections without losing differences in sources, methods, periods, or definitions.",
      searchPlaceholder: "Search parameters, authors, studies, or models…", searchLabel: "Search the catalog", research: "Research domains",
      clusters: "Four major literature clusters", clusterLead: "Each domain retains its own parameter definitions so distinct economic concepts are never mixed into one series.",
      stats: ["source records", "bilingual parameters", "numeric observations", "archived PDFs"], metrics: ["parameters", "observations", "sources"],
    },
    parameters: {
      eyebrow: "Controlled concept dictionary", heading: "Parameters", lead: "Review English and Turkish names, symbols, comparison rules, and every linked numeric observation.",
      search: "Search", searchPlaceholder: "E.g. discount factor, TFP, pass-through", family: "Research domain", allFamilies: "All domains",
      className: "Parameter class", allClasses: "All classes", unit: "Unit", allUnits: "All units", clear: "Clear filters",
      columns: ["Parameter", "Symbol", "Class", "Observations", "Sources", "Unit"], count: n => `${n} parameters shown`, empty: "No parameters match these filters.",
    },
    sources: {
      eyebrow: "Bibliographic inventory", heading: "Sources", lead: "Working papers, journal articles, theses, and reports with their access and scope status.",
      search: "Search", searchPlaceholder: "Title, author, or institution", year: "Year", allYears: "All years", type: "Source type", allTypes: "All types", clear: "Clear filters",
      columns: ["Source", "Year", "Type", "Parameters", "Observations", "Status"], count: n => `${n} sources shown`, empty: "No sources match these filters.",
    },
    estimates: {
      empty: "No numeric observations are linked to this record.", columns: ["Value", "Status", "Source / Parameter", "Model and method", "Period", "Location"], se: "SE", page: "PDF p.",
    },
    parameterDetail: {
      back: "← Back to parameters", noSymbol: "No symbol", definition: "Definition", comparison: "Comparison rule", records: "Numeric records", observation: "observations",
      summary: "Scope summary", source: "Sources", unit: "Units", area: "Domain",
    },
    sourceDetail: {
      back: "← Back to sources", noDate: "No date", info: "Source information", callout: "The local PDF is archived for research verification; the public site links to the publisher's version.",
      records: "Extracted records", observation: "observations", bibliography: "Bibliography", institution: "Institution / journal", year: "Year", pages: "PDF pages", parameter: "Parameters", scope: "Scope", original: "Open the original publication ↗",
    },
    about: {
      eyebrow: "Transparent and reproducible", heading: "Methodology", lead: "The catalog separates source, concept, and observation layers to avoid duplicate entries, prevent calibrations from being presented as estimates, and keep distinct definitions apart.",
      cards: [
        ["Source layer", "Each study has one source identifier. Authors, year, institution, DOI, publisher link, access status, and scope status are stored separately."],
        ["Concept layer", "Every parameter has controlled English and Turkish names, a symbol, unit, definition, and comparison rule."],
        ["Observation layer", "One source-parameter-sector-period-method combination forms one row. Alternative models and robustness estimates remain separate."],
        ["Verification", "PDF pages and table or figure locations are recorded for each value. A checksum manifest protects the integrity of the local PDF archive."],
        ["Estimates and calibrations", "Econometric estimates, external calibrations, derived values, model-implied results, and projections are never presented as the same status."],
        ["Comparability", "Values are not automatically averaged or combined until their units, model frequency, sector, period, and exact definitions match."],
      ],
    },
    downloads: {
      eyebrow: "Machine-readable data", heading: "Data files", lead: "Download the catalog's source, parameter, and observation tables as UTF-8 CSV files. Read status, unit, and comparison rules together when using a value.",
      files: ["Current source catalog", "Bilingual parameter dictionary", "Production and technology estimates", "Capital and investment estimates", "Pricing, inflation, and firms", "Households and preferences"],
    },
    notFound: { heading: "Record not found", lead: "The requested parameter or source is not in the data catalog.", back: "Return home" },
    error: { eyebrow: "Data error", heading: "The catalog could not be loaded" },
  },
};

const app = document.querySelector("#app");
const nav = document.querySelector("#site-nav");
const menuButton = document.querySelector("#menu-button");
const languageSwitch = document.querySelector("#language-switch");

function c() { return copy[state.lang]; }
function locale() { return c().locale; }

function esc(value = "") {
  return String(value).replace(/[&<>'"]/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[char]);
}

function normalize(value = "") {
  return String(value).toLocaleLowerCase(locale()).normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function formatNumber(value) {
  if (value === null || value === undefined || value === "") return "—";
  if (typeof value !== "number") return esc(value);
  const abs = Math.abs(value);
  const maxDigits = abs !== 0 && abs < 0.001 ? 8 : abs < 1 ? 4 : 3;
  return new Intl.NumberFormat(locale(), { maximumFractionDigits: maxDigits }).format(value);
}

function humanize(value = "") {
  return c().status[value] || String(value).replaceAll("_", " ").replace(/\b\w/g, x => x.toUpperCase());
}

function badge(status = "") {
  let cls = "";
  if (status.includes("estimated")) cls = "estimated";
  else if (status.includes("calibrat")) cls = status.includes("external") ? "external" : "calibrated";
  else if (status.includes("forecast") || status.includes("scenario")) cls = "forecast";
  return `<span class="badge ${cls}">${esc(humanize(status))}</span>`;
}

function familyName(id) { return c().families[id]?.[0] || id; }
function familyDescription(id) { return c().families[id]?.[1] || ""; }
function parameterName(parameter) { return state.lang === "en" ? parameter?.name_en : parameter?.name_tr; }
function secondaryParameterName(parameter) { return state.lang === "en" ? parameter?.name_tr : parameter?.name_en; }

function routeInfo() {
  const raw = location.hash.replace(/^#/, "") || "home";
  const [route, value] = raw.split("=");
  return { route, value: value ? decodeURIComponent(value) : "" };
}

function setActiveNav(route) {
  document.querySelectorAll("[data-nav]").forEach(link => {
    if (link.dataset.nav === route) link.setAttribute("aria-current", "page"); else link.removeAttribute("aria-current");
  });
}

function applyStaticCopy() {
  const text = c();
  const baseUrl = "https://halilozt.github.io/ModelParameters_Turkey/";
  const canonical = state.lang === "en" ? `${baseUrl}?lang=en` : baseUrl;
  document.documentElement.lang = state.lang;
  document.title = text.title;
  document.querySelector('meta[name="description"]').content = text.metaDescription;
  document.querySelector('meta[property="og:locale"]').content = state.lang === "en" ? "en_US" : "tr_TR";
  document.querySelector('meta[property="og:title"]').content = text.title;
  document.querySelector('meta[property="og:description"]').content = text.ogDescription;
  document.querySelector('meta[property="og:url"]').content = canonical;
  document.querySelector('link[rel="canonical"]').href = canonical;
  const values = {
    "skip-link": text.static.skip, "brand-title": text.static.brandTitle, "brand-subtitle": text.static.brandSubtitle,
    "menu-button": text.static.menu, "nav-parameters": text.static.parameters, "nav-sources": text.static.sources,
    "nav-about": text.static.about, "nav-downloads": text.static.downloads, "loading-text": text.static.loading,
    "footer-title": text.static.footerTitle, "footer-description": text.static.footerDescription,
    "footer-source-link": text.static.sourceLink, "generated-label": text.static.generated,
  };
  Object.entries(values).forEach(([id, value]) => { const element = document.getElementById(id); if (element) element.textContent = value; });
  document.querySelector("#brand-link").setAttribute("aria-label", text.static.home);
  nav.setAttribute("aria-label", text.static.navLabel);
  languageSwitch.textContent = text.static.switchText;
  languageSwitch.setAttribute("aria-label", text.static.switchLabel);
  updateGeneratedDate();
}

function updateGeneratedDate() {
  if (!state.data) return;
  document.querySelector("#generated-date").textContent = new Intl.DateTimeFormat(locale(), { dateStyle: "long" }).format(new Date(`${state.data.meta.generated_on}T12:00:00`));
}

function statsMarkup(meta) {
  const labels = c().home.stats;
  const values = [meta.source_count, meta.parameter_count, meta.estimate_count, meta.archived_pdf_count];
  return `<div class="stats">${values.map((value, index) => `<div class="stat"><strong>${value.toLocaleString(locale())}</strong><span>${labels[index]}</span></div>`).join("")}</div>`;
}

function renderHome() {
  const text = c().home;
  const { meta, families } = state.data;
  app.innerHTML = `
    <section class="hero"><div class="shell">
      <p class="eyebrow">${text.eyebrow}</p><h1>${text.heading}</h1><p class="hero-lead">${text.lead}</p>
      <form class="hero-search" id="hero-search"><input id="hero-query" type="search" autocomplete="off" placeholder="${text.searchPlaceholder}" aria-label="${text.searchLabel}" /><button class="primary-button" type="submit">${text.searchLabel}</button></form>
    </div></section>
    <div class="shell">${statsMarkup(meta)}</div>
    <section class="section"><div class="shell">
      <div class="section-head"><div><p class="eyebrow">${text.research}</p><h2>${text.clusters}</h2><p>${text.clusterLead}</p></div></div>
      <div class="family-grid">${families.map((family, index) => `<a class="family-card" href="#parameters" data-family-link="${family.id}"><div><small>0${index + 1}</small><h3>${esc(familyName(family.id))}</h3><p>${esc(familyDescription(family.id))}</p></div><div class="family-metrics"><span><strong>${family.parameter_count}</strong> ${text.metrics[0]}</span><span><strong>${family.estimate_count.toLocaleString(locale())}</strong> ${text.metrics[1]}</span><span><strong>${family.source_count}</strong> ${text.metrics[2]}</span></div></a>`).join("")}</div>
    </div></section>`;
  document.querySelector("#hero-search").addEventListener("submit", event => {
    event.preventDefault(); state.paramFilters.q = document.querySelector("#hero-query").value.trim(); location.hash = "#parameters";
  });
  document.querySelectorAll("[data-family-link]").forEach(link => link.addEventListener("click", () => { state.paramFilters.family = link.dataset.familyLink; }));
}

function optionList(items, selected, label, formatter = humanize) {
  return `<option value="">${label}</option>${items.map(item => `<option value="${esc(item)}" ${item === selected ? "selected" : ""}>${esc(formatter(item))}</option>`).join("")}`;
}

function renderParameters() {
  const text = c().parameters;
  const families = state.data.families;
  const classes = [...new Set(state.data.parameters.map(x => x.parameter_class).filter(Boolean))].sort();
  const units = [...new Set(state.data.parameters.flatMap(x => x.units).filter(Boolean))].sort();
  const f = state.paramFilters;
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">${text.eyebrow}</p><h1>${text.heading}</h1><p>${text.lead}</p></div></section>
    <section class="section"><div class="shell"><div class="filters">
      <div class="field"><label for="param-q">${text.search}</label><input id="param-q" type="search" value="${esc(f.q)}" placeholder="${text.searchPlaceholder}" /></div>
      <div class="field"><label for="param-family">${text.family}</label><select id="param-family">${optionList(families.map(x => x.id), f.family, text.allFamilies, familyName)}</select></div>
      <div class="field"><label for="param-class">${text.className}</label><select id="param-class">${optionList(classes, f.className, text.allClasses)}</select></div>
      <div class="field"><label for="param-unit">${text.unit}</label><select id="param-unit">${optionList(units, f.unit, text.allUnits)}</select></div>
    </div><div class="result-bar"><span id="param-count"></span><button class="clear-button" id="clear-params" type="button">${text.clear}</button></div>
    <div class="table-wrap"><table class="data-table"><thead><tr>${text.columns.map(column => `<th>${column}</th>`).join("")}</tr></thead><tbody id="parameter-rows"></tbody></table></div></div></section>`;
  const update = () => {
    const q = normalize(f.q);
    const rows = state.data.parameters.filter(p => {
      const hay = normalize(`${p.name_tr} ${p.name_en} ${p.parameter_id} ${p.definition} ${p.canonical_symbol}`);
      return (!q || hay.includes(q)) && (!f.family || p.families.includes(f.family)) && (!f.className || p.parameter_class === f.className) && (!f.unit || p.units.includes(f.unit));
    }).sort((a, b) => b.estimate_count - a.estimate_count || parameterName(a).localeCompare(parameterName(b), locale()));
    document.querySelector("#param-count").textContent = text.count(rows.length.toLocaleString(locale()));
    document.querySelector("#parameter-rows").innerHTML = rows.length ? rows.map(p => `<tr><td><a class="table-link" href="#parameter=${encodeURIComponent(p.parameter_id)}">${esc(parameterName(p))}</a><span class="subline">${esc(secondaryParameterName(p))} · ${esc(p.parameter_id)}</span></td><td class="symbol">${esc(p.canonical_symbol || "—")}</td><td>${esc(humanize(p.parameter_class))}</td><td class="number">${p.estimate_count}</td><td class="number">${p.source_count}</td><td>${esc(p.units.map(humanize).join(", ") || p.default_unit)}</td></tr>`).join("") : `<tr><td colspan="6" class="empty">${text.empty}</td></tr>`;
  };
  ["q", "family", "className", "unit"].forEach(key => {
    const id = { q: "#param-q", family: "#param-family", className: "#param-class", unit: "#param-unit" }[key];
    document.querySelector(id).addEventListener(key === "q" ? "input" : "change", event => { f[key] = event.target.value; update(); });
  });
  document.querySelector("#clear-params").addEventListener("click", () => { state.paramFilters = { q: "", family: "", className: "", unit: "" }; renderParameters(); });
  update();
}

function renderSources() {
  const text = c().sources;
  const types = [...new Set(state.data.sources.map(x => x.source_type).filter(Boolean))].sort();
  const years = [...new Set(state.data.sources.map(x => x.year).filter(x => typeof x === "number"))].sort((a, b) => b - a);
  const f = state.sourceFilters;
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">${text.eyebrow}</p><h1>${text.heading}</h1><p>${text.lead}</p></div></section>
    <section class="section"><div class="shell"><div class="filters">
      <div class="field"><label for="source-q">${text.search}</label><input id="source-q" type="search" value="${esc(f.q)}" placeholder="${text.searchPlaceholder}" /></div>
      <div class="field"><label for="source-year">${text.year}</label><select id="source-year">${optionList(years.map(String), f.year, text.allYears, x => x)}</select></div>
      <div class="field"><label for="source-type">${text.type}</label><select id="source-type">${optionList(types, f.type, text.allTypes, x => x)}</select></div>
    </div><div class="result-bar"><span id="source-count"></span><button class="clear-button" id="clear-sources" type="button">${text.clear}</button></div>
    <div class="table-wrap"><table class="data-table"><thead><tr>${text.columns.map(column => `<th>${column}</th>`).join("")}</tr></thead><tbody id="source-rows"></tbody></table></div></div></section>`;
  const update = () => {
    const q = normalize(f.q);
    const rows = state.data.sources.filter(s => {
      const hay = normalize(`${s.title} ${s.authors} ${s.institution_or_journal} ${s.source_id}`);
      return (!q || hay.includes(q)) && (!f.year || String(s.year) === f.year) && (!f.type || s.source_type === f.type);
    }).sort((a, b) => (b.year || 0) - (a.year || 0) || a.title.localeCompare(b.title, locale()));
    document.querySelector("#source-count").textContent = text.count(rows.length.toLocaleString(locale()));
    document.querySelector("#source-rows").innerHTML = rows.length ? rows.map(s => `<tr><td><a class="table-link" href="#source=${encodeURIComponent(s.source_id)}">${esc(s.title)}</a><span class="subline">${esc(s.authors)} · ${esc(s.institution_or_journal)}</span></td><td class="number">${esc(s.year || "—")}</td><td>${esc(s.source_type)}</td><td class="number">${s.parameter_count}</td><td class="number">${s.estimate_count}</td><td>${badge(s.scope_status || s.access_status)}</td></tr>`).join("") : `<tr><td colspan="6" class="empty">${text.empty}</td></tr>`;
  };
  document.querySelector("#source-q").addEventListener("input", event => { f.q = event.target.value; update(); });
  document.querySelector("#source-year").addEventListener("change", event => { f.year = event.target.value; update(); });
  document.querySelector("#source-type").addEventListener("change", event => { f.type = event.target.value; update(); });
  document.querySelector("#clear-sources").addEventListener("click", () => { state.sourceFilters = { q: "", year: "", type: "" }; renderSources(); });
  update();
}

function estimateTable(rows) {
  const text = c().estimates;
  if (!rows.length) return `<div class="empty">${text.empty}</div>`;
  return `<div class="table-wrap"><table class="data-table"><thead><tr>${text.columns.map(column => `<th>${column}</th>`).join("")}</tr></thead><tbody>${rows.map(r => {
    const source = state.data.sources.find(x => x.source_id === r.source_id);
    const param = state.data.parameters.find(x => x.parameter_id === r.parameter_id);
    const uncertainty = r.lower_bound !== null || r.upper_bound !== null ? ` [${formatNumber(r.lower_bound)}, ${formatNumber(r.upper_bound)}]` : r.standard_error !== null ? ` (${text.se} ${formatNumber(r.standard_error)})` : "";
    const target = source ? `#source=${encodeURIComponent(source.source_id)}` : `#parameter=${encodeURIComponent(param.parameter_id)}`;
    return `<tr><td class="number"><strong>${formatNumber(r.value)}</strong>${esc(uncertainty)}<span class="subline">${esc(humanize(r.unit))}</span></td><td>${badge(r.estimate_status)}</td><td><a class="table-link" href="${target}">${esc(source ? source.title : parameterName(param) || r.parameter_id)}</a><span class="subline">${esc(r.definition_variant || r.sector || "")}</span></td><td>${esc(r.model_family)}<span class="subline">${esc(r.estimation_method)}</span></td><td>${esc(r.data_period || "—")}<span class="subline">${esc(humanize(r.frequency))}</span></td><td>${r.source_pdf_page ? `${text.page} ${r.source_pdf_page}` : "—"}<span class="subline">${esc(r.source_locator || "")}</span></td></tr>`;
  }).join("")}</tbody></table></div>`;
}

function renderParameterDetail(id) {
  const text = c().parameterDetail;
  const p = state.data.parameters.find(x => x.parameter_id === id);
  if (!p) return renderNotFound();
  const rows = state.data.estimates.filter(x => x.parameter_id === id).sort((a, b) => a.source_id.localeCompare(b.source_id) || Number(a.value) - Number(b.value));
  const areas = [...new Set(rows.map(x => familyName(x.family_id)))].join(", ") || "—";
  app.innerHTML = `<section class="detail-header"><div class="shell detail-title"><a class="back-link" href="#parameters">${text.back}</a><p class="eyebrow">${esc(p.parameter_id)}</p><h1>${esc(parameterName(p))}</h1><span class="english-name">${esc(secondaryParameterName(p))}</span><div class="detail-chips"><span class="badge">${esc(p.canonical_symbol || text.noSymbol)}</span><span class="badge">${esc(humanize(p.parameter_class))}</span><span class="badge">${esc(humanize(p.default_unit))}</span></div></div></section>
    <div class="shell detail-grid"><div><article class="prose-card"><h2>${text.definition}</h2><p>${esc(p.definition)}</p></article><article class="prose-card"><h2>${text.comparison}</h2><p>${esc(p.comparison_rule)}</p></article><div class="section-head"><div><p class="eyebrow">${text.records}</p><h2>${rows.length.toLocaleString(locale())} ${text.observation}</h2></div></div>${estimateTable(rows)}</div>
    <aside><div class="summary-card"><h2>${text.summary}</h2><dl class="summary-list"><div><dt>${text.source}</dt><dd>${new Set(rows.map(x => x.source_id)).size}</dd></div><div><dt>${c().parameters.columns[3]}</dt><dd>${rows.length}</dd></div><div><dt>${text.unit}</dt><dd>${esc([...new Set(rows.map(x => humanize(x.unit)))].join(", ") || humanize(p.default_unit))}</dd></div><div><dt>${text.area}</dt><dd>${esc(areas)}</dd></div></dl></div></aside></div>`;
}

function renderSourceDetail(id) {
  const text = c().sourceDetail;
  const s = state.data.sources.find(x => x.source_id === id);
  if (!s) return renderNotFound();
  const rows = state.data.estimates.filter(x => x.source_id === id).sort((a, b) => a.parameter_id.localeCompare(b.parameter_id));
  const url = s.doi ? `https://doi.org/${s.doi}` : s.url;
  app.innerHTML = `<section class="detail-header"><div class="shell detail-title"><a class="back-link" href="#sources">${text.back}</a><p class="eyebrow">${esc(s.source_id)} · ${esc(s.year || text.noDate)}</p><h1>${esc(s.title)}</h1><span class="english-name">${esc(s.authors)}</span><div class="detail-chips"><span class="badge">${esc(s.source_type)}</span><span class="badge">${esc(s.language)}</span>${badge(s.access_status)}</div></div></section>
    <div class="shell detail-grid"><div><article class="prose-card"><h2>${text.info}</h2><p>${esc(s.institution_or_journal)}. ${esc(s.notes || "")}</p></article><div class="callout">${text.callout}</div><div class="section-head" style="margin-top:34px"><div><p class="eyebrow">${text.records}</p><h2>${rows.length.toLocaleString(locale())} ${text.observation}</h2></div></div>${estimateTable(rows.map(r => ({ ...r, source_id: "" })))}</div>
    <aside><div class="summary-card"><h2>${text.bibliography}</h2><dl class="summary-list"><div><dt>${text.institution}</dt><dd>${esc(s.institution_or_journal)}</dd></div><div><dt>${text.year}</dt><dd>${esc(s.year || "—")}</dd></div><div><dt>${text.pages}</dt><dd>${esc(s.pdf_pages || "—")}</dd></div><div><dt>${text.parameter}</dt><dd>${s.parameter_count}</dd></div><div><dt>${text.scope}</dt><dd>${esc(humanize(s.scope_status))}</dd></div></dl>${url ? `<p style="margin:18px 0 0"><a class="external-link" href="${esc(url)}" target="_blank" rel="noopener noreferrer">${text.original}</a></p>` : ""}</div></aside></div>`;
}

function renderAbout() {
  const text = c().about;
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">${text.eyebrow}</p><h1>${text.heading}</h1><p>${text.lead}</p></div></section><section class="section"><div class="shell"><div class="method-grid">${text.cards.map(([title, description]) => `<article class="method-card"><h2>${title}</h2><p>${description}</p></article>`).join("")}</div></div></section>`;
}

function renderDownloads() {
  const text = c().downloads;
  const names = ["sources_updated.csv", "parameter_dictionary_updated.csv", "production_technology_estimates.csv", "capital_investment_estimates_updated.csv", "pricing_inflation_firms_estimates.csv", "household_preferences_estimates.csv"];
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">${text.eyebrow}</p><h1>${text.heading}</h1><p>${text.lead}</p></div></section><section class="section"><div class="shell"><div class="download-grid">${names.map((file, index) => `<a class="download-card" href="./downloads/${file}" download><div><strong>${text.files[index]}</strong><span>${file}</span></div><span aria-hidden="true">CSV ↓</span></a>`).join("")}</div></div></section>`;
}

function renderNotFound() {
  const text = c().notFound;
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">404</p><h1>${text.heading}</h1><p>${text.lead}</p><p><a class="primary-button" href="#home">${text.back}</a></p></div></section>`;
}

function render() {
  if (!state.data) return;
  const { route, value } = routeInfo();
  setActiveNav(route); nav.classList.remove("open"); menuButton.setAttribute("aria-expanded", "false");
  if (route === "home") renderHome();
  else if (route === "parameters") renderParameters();
  else if (route === "sources") renderSources();
  else if (route === "parameter") renderParameterDetail(value);
  else if (route === "source") renderSourceDetail(value);
  else if (route === "about") renderAbout();
  else if (route === "downloads") renderDownloads();
  else renderNotFound();
  window.scrollTo({ top: 0, behavior: "instant" });
}

menuButton.addEventListener("click", () => {
  const open = nav.classList.toggle("open"); menuButton.setAttribute("aria-expanded", String(open));
});

languageSwitch.addEventListener("click", () => {
  state.lang = state.lang === "tr" ? "en" : "tr";
  const url = new URL(location.href);
  if (state.lang === "en") url.searchParams.set("lang", "en"); else url.searchParams.delete("lang");
  history.replaceState({}, "", `${url.pathname}${url.search}${url.hash}`);
  applyStaticCopy(); render();
});

window.addEventListener("hashchange", render);
applyStaticCopy();

fetch("./data/catalog.json")
  .then(response => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
  .then(data => { state.data = data; applyStaticCopy(); render(); })
  .catch(error => {
    const text = c().error;
    app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">${text.eyebrow}</p><h1>${text.heading}</h1><p>${esc(error.message)}</p></div></section>`;
  });
