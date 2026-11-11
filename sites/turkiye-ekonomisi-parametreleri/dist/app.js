const state = {
  data: null,
  paramFilters: { q: "", family: "", className: "", unit: "" },
  sourceFilters: { q: "", year: "", type: "" },
};

const app = document.querySelector("#app");
const nav = document.querySelector("#site-nav");
const menuButton = document.querySelector(".menu-button");

const familyDescriptions = {
  "production-technology": "Üretim fonksiyonları, faktör payları, verimlilik ve teknoloji dinamikleri.",
  "capital-investment": "Sermaye birikimi, yatırım davranışı, finansman koşulları ve kamu yatırımları.",
  "pricing-inflation-firms": "Fiyat ayarlama, enflasyon dinamikleri, geçişkenlik ve firma davranışları.",
  "household-preferences": "Tüketim, tasarruf, emek arzı, konut ve hanehalkı tercihleri.",
};

function esc(value = "") {
  return String(value).replace(/[&<>'"]/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[char]);
}

function normalize(value = "") {
  return String(value).toLocaleLowerCase("tr-TR").normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function formatNumber(value) {
  if (value === null || value === undefined || value === "") return "—";
  if (typeof value !== "number") return esc(value);
  const abs = Math.abs(value);
  const maxDigits = abs !== 0 && abs < 0.001 ? 8 : abs < 1 ? 4 : 3;
  return new Intl.NumberFormat("tr-TR", { maximumFractionDigits: maxDigits }).format(value);
}

function humanize(value = "") {
  const dictionary = {
    estimated: "Tahmin", calibrated: "Kalibrasyon", external_calibration: "Dışsal kalibrasyon",
    estimated_derived: "Türetilmiş tahmin", derived: "Türetilmiş", forecast_contribution: "Projeksiyon",
    model_implied: "Model sonucu", calculated: "Hesaplanan", descriptive_statistic: "Betimsel",
    pdf_verified: "PDF’den doğrulandı", web_fulltext_verified: "Web tam metni",
    archived: "Arşivlendi", in_scope: "Kapsam içi", excluded: "Kapsam dışı",
  };
  return dictionary[value] || String(value).replaceAll("_", " ").replace(/\b\w/g, x => x.toUpperCase());
}

function badge(status) {
  let cls = "";
  if (status.includes("estimated")) cls = "estimated";
  else if (status.includes("calibrat")) cls = status.includes("external") ? "external" : "calibrated";
  else if (status.includes("forecast") || status.includes("scenario")) cls = "forecast";
  return `<span class="badge ${cls}">${esc(humanize(status))}</span>`;
}

function routeInfo() {
  const raw = location.hash.replace(/^#/, "") || "home";
  const [route, value] = raw.split("=");
  return { route, value: value ? decodeURIComponent(value) : "" };
}

function setActiveNav(route) {
  document.querySelectorAll("[data-nav]").forEach(link => {
    const active = link.dataset.nav === route;
    if (active) link.setAttribute("aria-current", "page"); else link.removeAttribute("aria-current");
  });
}

function statsMarkup(meta) {
  return `<div class="stats">
    <div class="stat"><strong>${meta.source_count.toLocaleString("tr-TR")}</strong><span>kaynak kaydı</span></div>
    <div class="stat"><strong>${meta.parameter_count.toLocaleString("tr-TR")}</strong><span>iki dilli parametre</span></div>
    <div class="stat"><strong>${meta.estimate_count.toLocaleString("tr-TR")}</strong><span>sayısal gözlem</span></div>
    <div class="stat"><strong>${meta.archived_pdf_count.toLocaleString("tr-TR")}</strong><span>arşivlenmiş PDF</span></div>
  </div>`;
}

function renderHome() {
  const { meta, families } = state.data;
  app.innerHTML = `
    <section class="hero">
      <div class="shell">
        <p class="eyebrow">Türkiye için karşılaştırmalı araştırma kataloğu</p>
        <h1>İktisadi model parametrelerini tek yerde keşfedin.</h1>
        <p class="hero-lead">Tahminleri, kalibrasyonları ve projeksiyonları; kaynak, yöntem, dönem ve tanım farklılıklarını kaybetmeden inceleyin.</p>
        <form class="hero-search" id="hero-search">
          <input id="hero-query" type="search" autocomplete="off" placeholder="Parametre, yazar, çalışma veya model ara…" aria-label="Katalogda ara" />
          <button class="primary-button" type="submit">Katalogda ara</button>
        </form>
      </div>
    </section>
    <div class="shell">${statsMarkup(meta)}</div>
    <section class="section">
      <div class="shell">
        <div class="section-head"><div><p class="eyebrow">Araştırma alanları</p><h2>Dört ana literatür kümesi</h2><p>Her alan kendi parametre tanımlarıyla tutulur; farklı ekonomik nesneler aynı seri içinde karıştırılmaz.</p></div></div>
        <div class="family-grid">
          ${families.map((family, index) => `<a class="family-card" href="#parameters" data-family-link="${family.id}">
            <div><small>0${index + 1}</small><h3>${esc(family.name)}</h3><p>${esc(familyDescriptions[family.id])}</p></div>
            <div class="family-metrics"><span><strong>${family.parameter_count}</strong> parametre</span><span><strong>${family.estimate_count.toLocaleString("tr-TR")}</strong> gözlem</span><span><strong>${family.source_count}</strong> kaynak</span></div>
          </a>`).join("")}
        </div>
      </div>
    </section>`;
  document.querySelector("#hero-search").addEventListener("submit", event => {
    event.preventDefault();
    state.paramFilters.q = document.querySelector("#hero-query").value.trim();
    location.hash = "#parameters";
  });
  document.querySelectorAll("[data-family-link]").forEach(link => link.addEventListener("click", () => {
    state.paramFilters.family = link.dataset.familyLink;
  }));
}

function optionList(items, selected, label, formatter = humanize) {
  return `<option value="">${label}</option>${items.map(item => `<option value="${esc(item)}" ${item === selected ? "selected" : ""}>${esc(formatter(item))}</option>`).join("")}`;
}

function renderParameters() {
  const families = state.data.families;
  const classes = [...new Set(state.data.parameters.map(x => x.parameter_class).filter(Boolean))].sort();
  const units = [...new Set(state.data.parameters.flatMap(x => x.units).filter(Boolean))].sort();
  const f = state.paramFilters;
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">Kontrollü kavram sözlüğü</p><h1>Parametreler</h1><p>Türkçe ve İngilizce adları, sembolleri, karşılaştırma kuralları ve bunlara bağlı bütün sayısal gözlemleri inceleyin.</p></div></section>
    <section class="section"><div class="shell">
      <div class="filters">
        <div class="field"><label for="param-q">Arama</label><input id="param-q" type="search" value="${esc(f.q)}" placeholder="Örn. iskonto faktörü, TFP, geçişkenlik" /></div>
        <div class="field"><label for="param-family">Araştırma alanı</label><select id="param-family">${optionList(families.map(x => x.id), f.family, "Tüm alanlar", id => families.find(x => x.id === id)?.name || id)}</select></div>
        <div class="field"><label for="param-class">Parametre sınıfı</label><select id="param-class">${optionList(classes, f.className, "Tüm sınıflar")}</select></div>
        <div class="field"><label for="param-unit">Birim</label><select id="param-unit">${optionList(units, f.unit, "Tüm birimler")}</select></div>
      </div>
      <div class="result-bar"><span id="param-count"></span><button class="clear-button" id="clear-params" type="button">Filtreleri temizle</button></div>
      <div class="table-wrap"><table class="data-table"><thead><tr><th>Parametre</th><th>Sembol</th><th>Sınıf</th><th>Gözlem</th><th>Kaynak</th><th>Birim</th></tr></thead><tbody id="parameter-rows"></tbody></table></div>
    </div></section>`;
  const update = () => {
    const q = normalize(f.q);
    const rows = state.data.parameters.filter(p => {
      const hay = normalize(`${p.name_tr} ${p.name_en} ${p.parameter_id} ${p.definition} ${p.canonical_symbol}`);
      return (!q || hay.includes(q)) && (!f.family || p.families.includes(f.family)) && (!f.className || p.parameter_class === f.className) && (!f.unit || p.units.includes(f.unit));
    }).sort((a,b) => b.estimate_count - a.estimate_count || a.name_tr.localeCompare(b.name_tr, "tr"));
    document.querySelector("#param-count").textContent = `${rows.length.toLocaleString("tr-TR")} parametre gösteriliyor`;
    document.querySelector("#parameter-rows").innerHTML = rows.length ? rows.map(p => `<tr>
      <td><a class="table-link" href="#parameter=${encodeURIComponent(p.parameter_id)}">${esc(p.name_tr)}</a><span class="subline">${esc(p.name_en)} · ${esc(p.parameter_id)}</span></td>
      <td class="symbol">${esc(p.canonical_symbol || "—")}</td><td>${esc(humanize(p.parameter_class))}</td><td class="number">${p.estimate_count}</td><td class="number">${p.source_count}</td><td>${esc(p.units.map(humanize).join(", ") || p.default_unit)}</td>
    </tr>`).join("") : `<tr><td colspan="6" class="empty">Bu filtrelerle eşleşen parametre bulunamadı.</td></tr>`;
  };
  ["q","family","className","unit"].forEach(key => {
    const id = { q:"#param-q", family:"#param-family", className:"#param-class", unit:"#param-unit" }[key];
    document.querySelector(id).addEventListener(key === "q" ? "input" : "change", event => { f[key] = event.target.value; update(); });
  });
  document.querySelector("#clear-params").addEventListener("click", () => { state.paramFilters = { q:"", family:"", className:"", unit:"" }; renderParameters(); });
  update();
}

function renderSources() {
  const types = [...new Set(state.data.sources.map(x => x.source_type).filter(Boolean))].sort();
  const years = [...new Set(state.data.sources.map(x => x.year).filter(x => typeof x === "number"))].sort((a,b) => b-a);
  const f = state.sourceFilters;
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">Bibliyografik envanter</p><h1>Kaynaklar</h1><p>Çalışma tebliğleri, makaleler, tezler ve raporlar; erişim ve kapsam durumlarıyla birlikte.</p></div></section>
    <section class="section"><div class="shell">
      <div class="filters">
        <div class="field"><label for="source-q">Arama</label><input id="source-q" type="search" value="${esc(f.q)}" placeholder="Başlık, yazar veya kurum" /></div>
        <div class="field"><label for="source-year">Yıl</label><select id="source-year">${optionList(years.map(String), f.year, "Tüm yıllar", x => x)}</select></div>
        <div class="field"><label for="source-type">Kaynak türü</label><select id="source-type">${optionList(types, f.type, "Tüm türler", x => x)}</select></div>
      </div>
      <div class="result-bar"><span id="source-count"></span><button class="clear-button" id="clear-sources" type="button">Filtreleri temizle</button></div>
      <div class="table-wrap"><table class="data-table"><thead><tr><th>Kaynak</th><th>Yıl</th><th>Tür</th><th>Parametre</th><th>Gözlem</th><th>Durum</th></tr></thead><tbody id="source-rows"></tbody></table></div>
    </div></section>`;
  const update = () => {
    const q = normalize(f.q);
    const rows = state.data.sources.filter(s => {
      const hay = normalize(`${s.title} ${s.authors} ${s.institution_or_journal} ${s.source_id}`);
      return (!q || hay.includes(q)) && (!f.year || String(s.year) === f.year) && (!f.type || s.source_type === f.type);
    }).sort((a,b) => (b.year || 0) - (a.year || 0) || a.title.localeCompare(b.title, "tr"));
    document.querySelector("#source-count").textContent = `${rows.length.toLocaleString("tr-TR")} kaynak gösteriliyor`;
    document.querySelector("#source-rows").innerHTML = rows.length ? rows.map(s => `<tr>
      <td><a class="table-link" href="#source=${encodeURIComponent(s.source_id)}">${esc(s.title)}</a><span class="subline">${esc(s.authors)} · ${esc(s.institution_or_journal)}</span></td>
      <td class="number">${esc(s.year || "—")}</td><td>${esc(s.source_type)}</td><td class="number">${s.parameter_count}</td><td class="number">${s.estimate_count}</td><td>${badge(s.scope_status || s.access_status)}</td>
    </tr>`).join("") : `<tr><td colspan="6" class="empty">Bu filtrelerle eşleşen kaynak bulunamadı.</td></tr>`;
  };
  document.querySelector("#source-q").addEventListener("input", event => { f.q = event.target.value; update(); });
  document.querySelector("#source-year").addEventListener("change", event => { f.year = event.target.value; update(); });
  document.querySelector("#source-type").addEventListener("change", event => { f.type = event.target.value; update(); });
  document.querySelector("#clear-sources").addEventListener("click", () => { state.sourceFilters = { q:"", year:"", type:"" }; renderSources(); });
  update();
}

function estimateTable(rows) {
  if (!rows.length) return `<div class="empty">Bu kayda bağlı sayısal gözlem bulunmuyor.</div>`;
  return `<div class="table-wrap"><table class="data-table"><thead><tr><th>Değer</th><th>Statü</th><th>Kaynak / Parametre</th><th>Model ve yöntem</th><th>Dönem</th><th>Konum</th></tr></thead><tbody>${rows.map(r => {
    const source = state.data.sources.find(x => x.source_id === r.source_id);
    const param = state.data.parameters.find(x => x.parameter_id === r.parameter_id);
    const uncertainty = r.lower_bound !== null || r.upper_bound !== null ? ` [${formatNumber(r.lower_bound)}, ${formatNumber(r.upper_bound)}]` : r.standard_error !== null ? ` (SH ${formatNumber(r.standard_error)})` : "";
    return `<tr><td class="number"><strong>${formatNumber(r.value)}</strong>${esc(uncertainty)}<span class="subline">${esc(humanize(r.unit))}</span></td><td>${badge(r.estimate_status)}</td>
      <td><a class="table-link" href="${source ? `#source=${encodeURIComponent(source.source_id)}` : `#parameter=${encodeURIComponent(param.parameter_id)}`}">${esc(source ? source.title : param?.name_tr || r.parameter_id)}</a><span class="subline">${esc(r.definition_variant || r.sector || "")}</span></td>
      <td>${esc(r.model_family)}<span class="subline">${esc(r.estimation_method)}</span></td><td>${esc(r.data_period || "—")}<span class="subline">${esc(humanize(r.frequency))}</span></td><td>${r.source_pdf_page ? `PDF s. ${r.source_pdf_page}` : "—"}<span class="subline">${esc(r.source_locator || "")}</span></td></tr>`;
  }).join("")}</tbody></table></div>`;
}

function renderParameterDetail(id) {
  const p = state.data.parameters.find(x => x.parameter_id === id);
  if (!p) return renderNotFound();
  const rows = state.data.estimates.filter(x => x.parameter_id === id).sort((a,b) => a.source_id.localeCompare(b.source_id) || Number(a.value) - Number(b.value));
  app.innerHTML = `<section class="detail-header"><div class="shell detail-title"><a class="back-link" href="#parameters">← Parametrelere dön</a><p class="eyebrow">${esc(p.parameter_id)}</p><h1>${esc(p.name_tr)}</h1><span class="english-name">${esc(p.name_en)}</span><div class="detail-chips"><span class="badge">${esc(p.canonical_symbol || "Sembol yok")}</span><span class="badge">${esc(humanize(p.parameter_class))}</span><span class="badge">${esc(humanize(p.default_unit))}</span></div></div></section>
    <div class="shell detail-grid"><div><article class="prose-card"><h2>Tanım</h2><p>${esc(p.definition)}</p></article><article class="prose-card"><h2>Karşılaştırma kuralı</h2><p>${esc(p.comparison_rule)}</p></article>
      <div class="section-head"><div><p class="eyebrow">Sayısal kayıtlar</p><h2>${rows.length.toLocaleString("tr-TR")} gözlem</h2></div></div>${estimateTable(rows)}</div>
      <aside><div class="summary-card"><h2>Kapsam özeti</h2><dl class="summary-list"><div><dt>Kaynak</dt><dd>${new Set(rows.map(x => x.source_id)).size}</dd></div><div><dt>Gözlem</dt><dd>${rows.length}</dd></div><div><dt>Birim</dt><dd>${esc([...new Set(rows.map(x => humanize(x.unit)))].join(", ") || humanize(p.default_unit))}</dd></div><div><dt>Alan</dt><dd>${esc([...new Set(rows.map(x => x.family_name))].join(", ") || "—")}</dd></div></dl></div></aside></div>`;
}

function renderSourceDetail(id) {
  const s = state.data.sources.find(x => x.source_id === id);
  if (!s) return renderNotFound();
  const rows = state.data.estimates.filter(x => x.source_id === id).sort((a,b) => a.parameter_id.localeCompare(b.parameter_id));
  const url = s.doi ? `https://doi.org/${s.doi}` : s.url;
  app.innerHTML = `<section class="detail-header"><div class="shell detail-title"><a class="back-link" href="#sources">← Kaynaklara dön</a><p class="eyebrow">${esc(s.source_id)} · ${esc(s.year || "Tarih yok")}</p><h1>${esc(s.title)}</h1><span class="english-name">${esc(s.authors)}</span><div class="detail-chips"><span class="badge">${esc(s.source_type)}</span><span class="badge">${esc(s.language)}</span>${badge(s.access_status)}</div></div></section>
    <div class="shell detail-grid"><div><article class="prose-card"><h2>Kaynak bilgisi</h2><p>${esc(s.institution_or_journal)}. ${esc(s.notes || "")}</p></article><div class="callout">Yerel PDF araştırma doğrulaması için arşivlenmiştir; kamuya açık sitede yayıncı bağlantısı sunulur.</div>
      <div class="section-head" style="margin-top:34px"><div><p class="eyebrow">Çıkarılan kayıtlar</p><h2>${rows.length.toLocaleString("tr-TR")} gözlem</h2></div></div>${estimateTable(rows.map(r => ({...r, source_id:""})))}</div>
      <aside><div class="summary-card"><h2>Bibliyografya</h2><dl class="summary-list"><div><dt>Kurum / dergi</dt><dd>${esc(s.institution_or_journal)}</dd></div><div><dt>Yıl</dt><dd>${esc(s.year || "—")}</dd></div><div><dt>PDF sayfası</dt><dd>${esc(s.pdf_pages || "—")}</dd></div><div><dt>Parametre</dt><dd>${s.parameter_count}</dd></div><div><dt>Kapsam</dt><dd>${esc(humanize(s.scope_status))}</dd></div></dl>${url ? `<p style="margin:18px 0 0"><a class="external-link" href="${esc(url)}" target="_blank" rel="noopener noreferrer">Orijinal yayına git ↗</a></p>` : ""}</div></aside></div>`;
}

function renderAbout() {
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">Şeffaf ve yeniden üretilebilir</p><h1>Yöntem</h1><p>Bu katalog aynı sayıyı iki kez girmemek, kalibrasyonları tahmin gibi göstermemek ve farklı tanımları birbirine karıştırmamak için kaynak, kavram ve gözlem katmanlarını ayırır.</p></div></section>
    <section class="section"><div class="shell"><div class="method-grid">
      <article class="method-card"><h2>Kaynak katmanı</h2><p>Her çalışma tek kaynak kimliğiyle tutulur. Yazar, yıl, kurum, DOI, yayıncı bağlantısı, erişim ve kapsam durumu ayrı alanlardır.</p></article>
      <article class="method-card"><h2>Kavram katmanı</h2><p>Her parametrenin Türkçe ve İngilizce adı, sembolü, birimi, tanımı ve karşılaştırma kuralı kontrollü sözlükte tanımlanır.</p></article>
      <article class="method-card"><h2>Gözlem katmanı</h2><p>Bir kaynak-parametre-sektör-dönem-yöntem kombinasyonu bir satırdır. Alternatif modeller ve sağlamlık tahminleri ayrı tutulur.</p></article>
      <article class="method-card"><h2>Doğrulama</h2><p>Değerlerin PDF sayfası ve tablo/şekil konumu kaydedilir. Yerel PDF arşivi bütünlük özetiyle korunur.</p></article>
      <article class="method-card"><h2>Tahmin ve kalibrasyon</h2><p>Ekonometrik tahmin, dışsal kalibrasyon, türetilmiş değer, model sonucu ve projeksiyon aynı statüde gösterilmez.</p></article>
      <article class="method-card"><h2>Karşılaştırılabilirlik</h2><p>Birim, model sıklığı, sektör, dönem ve kesin tanım eşleşmeden değerler otomatik olarak ortalanmaz veya tek grafikte birleştirilmez.</p></article>
    </div></div></section>`;
}

function renderDownloads() {
  const files = [
    ["sources_updated.csv","Güncel kaynak kataloğu"], ["parameter_dictionary_updated.csv","İki dilli parametre sözlüğü"],
    ["production_technology_estimates.csv","Üretim ve teknoloji tahminleri"], ["capital_investment_estimates_updated.csv","Sermaye ve yatırım tahminleri"],
    ["pricing_inflation_firms_estimates.csv","Fiyatlama, enflasyon ve firmalar"], ["household_preferences_estimates.csv","Hanehalkı ve tercihler"],
  ];
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">Makinece okunabilir veri</p><h1>Veri dosyaları</h1><p>Kataloğun kaynak, parametre ve gözlem tablolarını UTF-8 CSV biçiminde indirin. Değerleri kullanırken statü, birim ve karşılaştırma kuralını birlikte okuyun.</p></div></section>
    <section class="section"><div class="shell"><div class="download-grid">${files.map(([file,title]) => `<a class="download-card" href="./downloads/${file}" download><div><strong>${esc(title)}</strong><span>${esc(file)}</span></div><span aria-hidden="true">CSV ↓</span></a>`).join("")}</div></div></section>`;
}

function renderNotFound() {
  app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">404</p><h1>Kayıt bulunamadı</h1><p>Aradığınız parametre veya kaynak veri kataloğunda bulunmuyor.</p><p><a class="primary-button" href="#home">Ana sayfaya dön</a></p></div></section>`;
}

function render() {
  if (!state.data) return;
  const { route, value } = routeInfo();
  setActiveNav(route);
  nav.classList.remove("open");
  menuButton.setAttribute("aria-expanded", "false");
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
  const open = nav.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(open));
});
window.addEventListener("hashchange", render);

fetch("./data/catalog.json")
  .then(response => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
  .then(data => {
    state.data = data;
    document.querySelector("#generated-date").textContent = new Intl.DateTimeFormat("tr-TR", { dateStyle: "long" }).format(new Date(`${data.meta.generated_on}T12:00:00`));
    render();
  })
  .catch(error => {
    app.innerHTML = `<section class="page-heading"><div class="shell"><p class="eyebrow">Veri hatası</p><h1>Katalog yüklenemedi</h1><p>${esc(error.message)}</p></div></section>`;
  });

