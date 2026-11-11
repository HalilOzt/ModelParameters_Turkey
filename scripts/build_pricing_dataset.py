from __future__ import annotations

import csv
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

ESTIMATE_FIELDS = [
    "estimate_id", "source_id", "parameter_id", "value", "lower_bound",
    "upper_bound", "standard_error", "unit", "estimate_status", "model_family",
    "estimation_method", "data_period", "frequency", "sector", "definition_variant",
    "source_pdf_page", "source_locator", "verification_status", "notes",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


source_rows = [
    ("S088", "Does Stock Market Listing Boost or Impede Corporate Investment? Evidence from Türkiye", "İbrahim Yarba; Büşra Yassa", 2021, "Central Bank of the Republic of Türkiye", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2021/21-03", "", "sources/pdfs/S088_yarba_yassa_stock_listing_investment_2021.pdf", 30, "Firm-level listing effects on tangible investment; added to close a previously downloaded-but-uncatalogued source."),
    ("S089", "Turkey Investment Climate Economic Memorandum", "World Bank", 2017, "World Bank", "Institutional report", "English", "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/611101488649316387/turkey-investment-climate-economic-memorandum", "", "sources/pdfs/S089_world_bank_turkey_investment_2017.pdf", 93, "Investment composition and capital-depreciation benchmarks; added to close a previously downloaded-but-uncatalogued source."),
    ("S090", "User Cost of Capital, Investment and Capacity Utilization: The Case of Turkey", "Merter Mert", 2017, "Ankara University SBF Journal", "Journal article", "English", "https://dergipark.org.tr/en/pub/ausbf/issue/30418/328120", "", "sources/pdfs/S090_mert_user_cost_capital_2017.pdf", 25, "User-cost investment model and capital-stock construction; added to close a previously downloaded-but-uncatalogued source."),
    ("S091", "Price Rigidity In Turkey: Evidence From Micro Data", "M. Utku Özmen; Orhun Sevinç", 2011, "Central Bank of the Republic of Türkiye Working Paper 11/25", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2011/11-25", "", "sources/pdfs/S091_ozmen_sevinc_price_rigidity_2011.pdf", 46, "Micro price spells for more than 6,000 items, October 2006-January 2011."),
    ("S092", "State-Dependency in Price Adjustments: Evidence from Large Shocks", "Elif Feyza Özcan Kodaz; Serdar Yürek", 2023, "Central Bank of the Republic of Türkiye Working Paper 23/04", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2023/23-04", "", "sources/pdfs/S092_ozcan_kodaz_yurek_state_dependent_pricing_2023.pdf", 30, "Online daily product-price microdata; posted and regular price changes are separated."),
    ("S093", "Large Exchange Rate Shocks and Nonlinear Effects in Exchange Rate Pass-Through", "Fethi Öğünç; Orhun Özel", 2025, "Central Bank of the Republic of Türkiye Working Paper 25/05", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2025/25-05", "", "sources/pdfs/S093_ogunc_ozel_nonlinear_erpt_2025.pdf", 28, "Quarterly Phillips-curve estimates distinguish normal and large-depreciation regimes."),
    ("S094", "Estimates of Exchange Rate Pass-through with Product-level Data", "Yusuf Emre Akgündüz; Emine Meltem Baştan; Ufuk Demiroğlu; Semih Tümen", 2019, "Central Bank of the Republic of Türkiye Working Paper 19/22", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2019/19-22", "", "sources/pdfs/S094_akgunduz_bastan_demiroglu_tumen_product_erpt_2019.pdf", 31, "Product-country-month customs data; import and export exchange-rate pass-through."),
    ("S095", "Disaggregated Evidence for Exchange Rate and Import Price Pass-through in the Light of Identification Issues, Aggregation Bias and Heterogeneity", "M. Utku Özmen; Meltem Topaloğlu", 2017, "Central Bank of the Republic of Türkiye Working Paper 17/08", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2017/17-08", "", "sources/pdfs/S095_ozmen_topaloglu_disaggregated_erpt_2017.pdf", 29, "Disaggregated consumer-price pass-through with identification and aggregation checks."),
    ("S096", "The Role of Imported Inputs in Pass-through Dynamics", "Dilara Ertuğ; Pınar Özlü; M. Utku Özmen; Çağlar Yüncüler", 2020, "Central Bank of the Republic of Türkiye Working Paper 20/03", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2020/20-03", "", "sources/pdfs/S096_ertug_ozlu_ozmen_yunculer_imported_inputs_2020.pdf", 36, "Sectoral producer-price pass-through and imported-input dependence."),
    ("S097", "Foreign Currency Debt and the Exchange Rate Pass-Through", "Salih Fendoğlu; Mehmet Selman Çolak; Yavuz Selim Hacıhasanoğlu", 2019, "Central Bank of the Republic of Türkiye Working Paper 19/24", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2019/19-24", "", "sources/pdfs/S097_fendoglu_colak_hacihasanoglu_fx_debt_erpt_2019.pdf", 20, "Firm balance sheets matched to sectoral producer prices, 2007-2016."),
    ("S098", "Inflation Dynamics in Turkey from a Bayesian Perspective", "Fethi Öğünç; Mustafa Utku Özmen; Çağrı Sarıkaya", 2018, "Central Bank of the Republic of Türkiye Working Paper 18/10", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2018/18-10", "", "sources/pdfs/S098_ogunc_ozmen_sarikaya_bvar_inflation_2018.pdf", 28, "BVAR impulse responses for exchange rate, import price, growth and nominal wages."),
    ("S099", "Türkiye’de Enflasyonun İş Çevrimlerine Duyarlılığı: Çıktı Açığına Duyarlı TÜFE Alt Gruplarının Saptanması", "Oğuz Atuk; Cem Aysoy; Mustafa Utku Özmen; Çağrı Sarıkaya", 2014, "Central Bank of the Republic of Türkiye Working Paper 14/37", "Working paper", "Turkish", "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Yayinlar/Arastirma+Yayinlari/Calisma+Tebligleri/2014/14-37", "", "sources/pdfs/S099_atuk_aysoy_ozmen_sarikaya_business_cycles_2014.pdf", 27, "Output-gap-sensitive CPI subgroups, 2003-2013."),
    ("S100", "A Model Averaging Approach to Estimate the Exchange Rate Pass-Through", "Ferhat Arslaner; Doğan Karaman; Nuran Arslaner; Süleyman Hilmi Kal", 2014, "Central Bank of the Republic of Türkiye Working Paper 14/16", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2014/14-16", "", "sources/pdfs/S100_arslaner_karaman_arslaner_kal_erpt_2014.pdf", 57, "Model averaging, Markov-switching and VAR exchange-rate pass-through estimates."),
    ("S101", "Invoicing Currency and Exchange Rate Pass-through in Turkish Exports and Imports", "Hülya Saygılı", 2019, "Central Bank of the Republic of Türkiye Working Paper 19/17", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2019/19-17", "", "sources/pdfs/S101_saygili_invoicing_erpt_2019.pdf", 31, "Bilateral trade prices by invoicing currency and broad economic category."),
    ("S102", "Inflation Dynamics in Turkey: In Pursuit of a Domestic Cost Measure", "Selen Başer Andıç; Hande Küçük; Fethi Öğünç", 2014, "Central Bank of the Republic of Türkiye Working Paper 14/20", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2014/14-20", "", "sources/pdfs/S102_andic_kucuk_ogunc_domestic_cost_2014.pdf", 21, "Hybrid New Keynesian Phillips curves with domestic and foreign cost components."),
    ("S103", "The Role of Expectations in the Inflation Process in Turkey: Have the Dynamics Changed Recently?", "Ümit Koç; Fethi Öğünç; Mustafa Utku Özmen", 2021, "Central Bank of the Republic of Türkiye Working Paper 21/02", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2021/21-02", "", "sources/pdfs/S103_koc_ogunc_ozmen_inflation_expectations_2021.pdf", 21, "Fixed and time-varying Phillips curves plus expectation-formation regressions."),
    ("S104", "Inflation Expectations and Firms' Decisions in High Inflation: Evidence from a Randomized Control Trial", "Okan Akarsu; Emrehan Aktuğ; Huzeyfe Torun", 2025, "Central Bank of the Republic of Türkiye Working Paper 25/12", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2025/25-12", "", "sources/pdfs/S104_akarsu_aktug_torun_firm_expectations_rct_2025.pdf", 147, "Randomized information treatment among Turkish firms in May 2024."),
    ("S105", "Market Concentration and Firm Markups: Micro Evidence from an Emerging Market with Inflationary Pressures", "Mehmet Selman Çolak; Abdullah Kazdal; Ünal Seven; Muhammed Hasan Yılmaz", 2025, "Central Bank of the Republic of Türkiye Working Paper 25/01", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2025/25-01", "", "sources/pdfs/S105_colak_kazdal_seven_yilmaz_markups_2025.pdf", 62, "Firm-level markups and concentration with high-inflation interactions."),
    ("S106", "Financial Conditions, Uncertainty and Expectations Errors of Firms", "Petre Caraiani; Nazlı Karamollaoğlu; Cihan Yalçın", 2025, "Central Bank of the Republic of Türkiye Working Paper 25/15", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2025/25-15", "", "sources/pdfs/S106_caraiani_karamollaoglu_yalcin_expectation_errors_2025.pdf", 36, "Firm CPI and PPI forecast errors linked to uncertainty and financial conditions."),
    ("S107", "Estimating Time-Varying Potential Output and NAIRU Using a Multivariate Filter for Turkey", "Mert Gökcü", 2021, "Central Bank of the Republic of Türkiye Working Paper 21/39", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2021/21-39", "", "sources/pdfs/S107_gokcu_multivariate_filter_2021.pdf", 45, "Multivariate-filter Phillips curve jointly estimating output gap and NAIRU."),
    ("S108", "Exchange Rate Pass-Through in Turkey: It is Slow, but is it Really Low?", "Hakan Kara; Fethi Öğünç", 2005, "Central Bank of the Republic of Türkiye Working Paper 05/10", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2005/05-10", "", "sources/pdfs/S108_kara_ogunc_erpt_2005.pdf", 19, "Recursive VAR comparison of pre-float and post-float pass-through speed and extent."),
    ("S109", "Recent Inflation Trend from a Pricing Behavior Perspective", "Central Bank of the Republic of Türkiye", 2025, "Inflation Report 2025-I, Box 2.3", "Report box", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Reports/Inflation+Report/2025/Inflation+Report+2025-I", "", "sources/pdfs/S109_tcmb_ir_2025i_pricing_behavior.pdf", 5, "CPI split by predominantly time-dependent and state-dependent pricing behavior."),
    ("S110", "Pricing Behavior and Expectations of the Real Sector", "Central Bank of the Republic of Türkiye", 2025, "Inflation Report 2025-IV, Box 2.5", "Report box", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Reports/Inflation+Report/2025/Inflation+Report+2025-IV", "", "sources/pdfs/S110_tcmb_ir_2025iv_real_sector_pricing.pdf", 46, "Business Tendency Survey indicators on firms' price-change frequency, implied duration and PPI expectations."),
    ("S111", "How Do Monetary Policy and Inflation Announcements Affect Firm Expectations in High Inflation?", "Okan Akarsu; Emrehan Aktuğ", 2026, "Central Bank of the Republic of Türkiye Working Paper 26/09", "Working paper", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2026/26-09", "", "sources/pdfs/S111_akarsu_aktug_policy_announcements_firm_expectations_2026.pdf", 121, "Event-study estimates for 2015-2024, separating low- and high-inflation regimes."),
    ("S112", "Firmaların Davranış Psikolojisi: Algılardan Eylemlere", "K. Azim Özdemir", 2026, "Central Bank of the Republic of Türkiye Working Paper 26/03", "Working paper", "Turkish", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Working+Paperss/2026/26-03", "", "sources/pdfs/S112_ozdemir_firm_behavioral_psychology_2026.pdf", 27, "PLS-SEM estimates from RESİM firm interviews, January 2019-January 2022."),
    ("S113", "Firms’ Inflation Expectations During the Phases of Inflation", "Okan Akarsu; Huzeyfe Torun", 2025, "Central Bank of the Republic of Türkiye Research Notes in Economics 2025-19", "Research note", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Publications/Research/Research+Notes+in+Economics/2025/25-19", "", "sources/pdfs/S113_tcmb_research_note_firm_expectations_2025.pdf", 16, "Propensity-score-matched effects of firms' price and unit-cost expectations on 12-month inflation expectations."),
]


parameter_rows = [
    ("CI_STOCK_LISTING_INVESTMENT_EFFECT", "Stock-listing effect on investment", "Borsaya kotasyonun yatırıma etkisi", "tau_list", "log_points", "firm_investment", "Estimated treatment effect of becoming publicly listed on firm tangible investment or capital.", "Match gross/net asset outcome, sector and treatment estimator."),
    ("CI_INVESTMENT_TO_GDP_RATIO", "Investment-to-GDP ratio", "Yatırımın GSYH'ye oranı", "I_Y", "percent_of_GDP", "investment_rate", "Gross fixed investment as a share of GDP.", "Match public/private/total investment, nominal/real construction and averaging period."),
    ("CI_CAPITAL_OUTPUT_ELASTICITY", "Capital-output elasticity", "Sermaye-çıktı esnekliği", "epsilon_Y_K", "elasticity", "capital_demand", "Long-run elasticity of output with respect to capital in an investment or production relation.", "Do not equate with the capital income share unless the model justifies it."),
    ("PF_PRICE_CHANGE_FREQUENCY", "Price-change frequency", "Fiyat değiştirme sıklığı", "f_p", "fraction_per_period", "price_setting", "Share or count of price changes within the stated observation period.", "Match observation frequency, posted-versus-regular-price treatment and product coverage."),
    ("PF_PRICE_SPELL_DURATION", "Price-spell duration", "Fiyat değişmeme süresi", "d_p", "periods", "price_setting", "Mean or implied duration for which a price remains unchanged.", "Do not pool biweekly, weekly and monthly durations without conversion; distinguish actual and implied duration."),
    ("PF_PRICE_INCREASE_SIZE", "Average price-increase size", "Ortalama fiyat artışı büyüklüğü", "Delta_p_plus", "percent", "price_setting", "Average non-zero positive price change.", "Match posted/regular prices and product coverage."),
    ("PF_PRICE_DECREASE_SIZE", "Average price-decrease size", "Ortalama fiyat azalışı büyüklüğü", "Delta_p_minus", "percent", "price_setting", "Average non-zero negative price change.", "Negative signs are retained; compare absolute magnitudes only when explicitly intended."),
    ("PF_PRICE_SYNCHRONIZATION", "Price-change synchronization", "Fiyat değişimi eşzamanlılığı", "sync_p", "index_ratio", "price_setting", "Synchronization ratio for price changes within a product group.", "Compare only identical synchronization definitions and time frequencies."),
    ("PF_DURATION_SIZE_SENSITIVITY", "Price-change size sensitivity to spell duration", "Fiyat değişimi büyüklüğünün süreye duyarlılığı", "beta_d", "regression_coefficient", "price_setting", "Coefficient linking price-change size to the duration of the preceding spell.", "Sign and unit depend on the source regression's scaling."),
    ("PF_CALVO_PRICE_STICKINESS", "Calvo price stickiness", "Calvo fiyat yapışkanlığı", "theta_p", "fraction", "nominal_rigidity", "Probability of not reoptimizing a price in one model period.", "A quarterly Calvo probability is not a monthly frequency; distinguish domestic and import prices."),
    ("PF_CALVO_WAGE_STICKINESS", "Calvo wage stickiness", "Calvo ücret yapışkanlığı", "theta_w", "fraction", "nominal_rigidity", "Probability of not reoptimizing a wage in one model period.", "Match model period and wage-setting block."),
    ("PF_PRICE_INDEXATION", "Price indexation", "Fiyat endekslemesi", "gamma_p", "fraction", "nominal_rigidity", "Degree of indexation of non-reoptimized prices to past inflation.", "Distinguish domestic, imported and administered-price indexation."),
    ("PF_WAGE_INDEXATION", "Wage indexation", "Ücret endekslemesi", "gamma_w", "fraction", "nominal_rigidity", "Degree of indexation of non-reoptimized wages to past inflation.", "Match model period and the inflation measure used for indexation."),
    ("PF_EXCHANGE_RATE_PASS_THROUGH", "Exchange-rate pass-through", "Döviz kuru geçişkenliği", "ERPT", "fraction", "pass_through", "Response of domestic or trade prices to an exchange-rate change.", "Always match price index, horizon, shock normalization, exchange-rate sign convention and regime."),
    ("PF_IMPORT_PRICE_PASS_THROUGH", "Import-price pass-through", "İthalat fiyatı geçişkenliği", "IPPT", "fraction", "pass_through", "Response of domestic inflation or prices to foreign-currency import prices.", "Keep import-price and exchange-rate shocks separate and record the cumulative horizon."),
    ("PF_WAGE_PASS_THROUGH", "Wage pass-through to inflation", "Ücretten enflasyona geçişkenlik", "WPT", "fraction", "pass_through", "Cumulative response of inflation to a nominal wage shock.", "Match wage concept, inflation index, shock size and horizon."),
    ("PF_MINIMUM_WAGE_PASS_THROUGH", "Minimum-wage pass-through", "Asgari ücret geçişkenliği", "MWPT", "regression_coefficient", "pass_through", "Phillips-curve response to current or lagged minimum-wage growth.", "Do not add current and lagged coefficients unless the specification and horizon justify it."),
    ("PF_OUTPUT_GAP_INFLATION_SENSITIVITY", "Inflation sensitivity to the output gap", "Enflasyonun çıktı açığına duyarlılığı", "kappa_y", "regression_coefficient", "phillips_curve", "Phillips-curve slope on the output gap.", "Compare only the same inflation transformation, gap definition and frequency."),
    ("PF_GROWTH_INFLATION_SENSITIVITY", "Inflation sensitivity to output growth", "Enflasyonun büyümeye duyarlılığı", "beta_g", "percentage_points", "phillips_curve", "Cumulative inflation response to a one-percentage-point output-growth shock.", "Not interchangeable with an output-gap coefficient."),
    ("PF_INFLATION_PERSISTENCE", "Inflation persistence", "Enflasyon sürekliliği", "rho_pi", "fraction", "phillips_curve", "Lagged-inflation coefficient or backward-looking share in an inflation equation.", "Distinguish a reduced-form lag coefficient from structural indexation."),
    ("PF_FORWARD_LOOKING_SHARE", "Forward-looking inflation share", "İleriye dönük enflasyon payı", "gamma_f", "fraction", "phillips_curve", "Weight on expected future inflation in a hybrid Phillips curve.", "Check whether constrained to complement the backward-looking weight."),
    ("PF_MARGINAL_COST_INFLATION_SLOPE", "Inflation slope on marginal cost", "Enflasyonun marjinal maliyet eğimi", "lambda_mc", "regression_coefficient", "phillips_curve", "Hybrid New Keynesian Phillips-curve coefficient on real marginal cost.", "Marginal-cost proxy and inflation definition must match."),
    ("PF_DOMESTIC_COST_SHARE", "Domestic-cost share", "Yurtiçi maliyet payı", "omega_d", "fraction", "cost_structure", "Estimated domestic component of the marginal-cost composite.", "Compare only within the same cost aggregation and sector."),
    ("PF_FOREIGN_COST_SHARE", "Foreign-cost share", "Yabancı maliyet payı", "omega_f", "fraction", "cost_structure", "Estimated imported/foreign component of the marginal-cost composite.", "May be constrained to one minus the domestic share."),
    ("PF_FX_DEBT_PRICE_SENSITIVITY", "Price sensitivity to foreign-currency debt", "Fiyatların döviz borcuna duyarlılığı", "beta_fxdebt", "regression_coefficient", "firm_pricing", "Interaction of exchange-rate change with firm foreign-currency exposure in a price equation.", "Match exposure denominator and exchange-rate normalization."),
    ("PF_IMPORT_DEPENDENCE", "Imported-input dependence", "İthal girdi bağımlılığı", "m_share", "percent", "cost_structure", "Imported-input share of sectoral production costs.", "The input-output denominator and reference year must match."),
    ("PF_MARKUP", "Firm markup", "Firma kâr marjı", "mu", "ratio", "firm_pricing", "Ratio of output elasticity to the corresponding variable-input cost share.", "Match production-function estimator, trimming and aggregation."),
    ("PF_CONCENTRATION_MARKUP_SENSITIVITY", "Markup sensitivity to market concentration", "Kâr marjının piyasa yoğunlaşmasına duyarlılığı", "beta_CR", "regression_coefficient", "firm_pricing", "Effect of concentration on firm markups, possibly interacted with inflation regimes.", "CR4 and CR20, OLS/CEM/IV, and regime interactions are distinct estimates."),
    ("PF_EXPECTATION_BACKWARD_WEIGHT", "Backward-looking weight in expectations", "Beklentilerde geriye dönük ağırlık", "beta_past", "regression_coefficient", "expectations", "Sensitivity of inflation expectations to past realized inflation.", "Match forecast horizon and survey group."),
    ("PF_EXPECTATION_FX_SENSITIVITY", "Inflation-expectation sensitivity to exchange rates", "Enflasyon beklentisinin döviz kuruna duyarlılığı", "beta_E", "regression_coefficient", "expectations", "Response of inflation expectations to exchange-rate developments.", "Match exchange-rate measure and lag structure."),
    ("PF_EXPECTATION_TARGET_WEIGHT", "Inflation-target weight in expectations", "Beklentilerde enflasyon hedefi ağırlığı", "beta_target", "regression_coefficient", "expectations", "Sensitivity of inflation expectations to the announced inflation target.", "A statistically weak coefficient should remain visible as such."),
    ("PF_EXPECTATION_SURPRISE_SENSITIVITY", "Expectation sensitivity to inflation surprises", "Beklentinin enflasyon sürprizine duyarlılığı", "beta_surprise", "regression_coefficient", "expectations", "Response of expectations to an inflation surprise or forecast error.", "Match event window, surprise orthogonalization and dependent variable."),
    ("PF_FIRM_DECISION_RESPONSE_TO_EXPECTATIONS", "Firm-decision response to inflation expectations", "Firma kararlarının enflasyon beklentisine tepkisi", "beta_decision", "regression_coefficient", "firm_expectations", "Causal response of firms' own wage, cost, price or outlook decisions to shifted inflation expectations.", "Outcome, treatment and survey scale must be filtered separately."),
    ("PF_EXPECTATION_ERROR", "Firm inflation-expectation error", "Firma enflasyon beklentisi hatası", "e_pi", "percentage_points", "expectations", "Absolute or normalized firm forecast error for CPI or PPI inflation.", "Distinguish mean/median, absolute/normalized errors and CPI/PPI targets."),
    ("PF_SALES_PRICE_EXPECTATION_EFFECT", "Sales-price expectation effect on inflation expectations", "Satış fiyatı beklentisinin enflasyon beklentisine etkisi", "tau_price", "percentage_points", "firm_expectations", "Treatment effect of expecting a sales-price change on the firm's 12-month inflation forecast.", "ATE and matched ATT are distinct; compare within inflation regime and direction."),
    ("PF_UNIT_COST_EXPECTATION_EFFECT", "Unit-cost expectation effect on inflation expectations", "Birim maliyet beklentisinin enflasyon beklentisine etkisi", "tau_cost", "percentage_points", "firm_expectations", "Treatment effect of expecting a unit-cost change on the firm's 12-month inflation forecast.", "ATE and matched ATT are distinct; compare within inflation regime and direction."),
    ("PF_MONETARY_POLICY_NEWS_RESPONSE", "Firm expectation response to monetary-policy news", "Firma beklentisinin para politikası haberine tepkisi", "beta_MPS", "regression_coefficient", "firm_expectations", "Event-study response of a firm expectation to a monetary-policy surprise.", "Dependent variable, shock size, inflation regime and firm subgroup must match."),
    ("PF_INFLATION_NEWS_RESPONSE", "Firm expectation response to inflation news", "Firma beklentisinin enflasyon haberine tepkisi", "beta_INFSURP", "regression_coefficient", "firm_expectations", "Event-study response of a firm expectation to an inflation surprise.", "Dependent variable, event window, regime and firm subgroup must match."),
    ("PF_PRICING_PRESSURE_COST_EFFECT", "Effect of cost perceptions on pricing pressure", "Maliyet algısının fiyatlama baskısına etkisi", "beta_cost_to_price", "standardized_coefficient", "firm_behavior", "Standardized structural path from perceived costs to pricing pressure.", "Compare only PLS-SEM models using compatible latent-variable measurement blocks."),
    ("PF_PRICING_PRESSURE_DEMAND_EFFECT", "Effect of demand optimism on pricing pressure", "Talep iyimserliğinin fiyatlama baskısına etkisi", "beta_demand_to_price", "standardized_coefficient", "firm_behavior", "Standardized structural path from domestic-demand optimism to pricing pressure.", "Regime-specific paths may be statistically insignificant."),
    ("PF_PRICING_PRESSURE_PROFIT_EFFECT", "Effect of pricing pressure on perceived profitability", "Fiyatlama baskısının algılanan kârlılığa etkisi", "beta_price_to_profit", "standardized_coefficient", "firm_behavior", "Standardized structural path from pricing pressure to perceived profitability.", "Sign refers to the latent constructs as coded by the source."),
    ("PF_GENERAL_OPTIMISM_VARIANCE", "Variance explained by the general-optimism factor", "Genel iyimserlik faktörünün açıkladığı varyans", "R2_PC1", "percent_of_variance", "firm_behavior", "Share of latent-construct variation explained by the first principal component interpreted as general optimism.", "This is a dimension-reduction statistic, not a pricing or markup coefficient."),
    ("PF_STATE_DEPENDENT_ITEM_SHARE", "Share of state-dependent-price items", "Duruma bağlı fiyatlanan kalemlerin payı", "s_state", "percent", "price_setting", "CPI basket weight classified as predominantly state-dependent pricing.", "Classification threshold and basket weights must match."),
    ("PF_TIME_DEPENDENT_ITEM_SHARE", "Share of time-dependent-price items", "Zamana bağlı fiyatlanan kalemlerin payı", "s_time", "percent", "price_setting", "CPI basket weight classified as predominantly time-dependent pricing.", "Classification threshold and basket weights must match."),
    ("PF_PRICING_GROUP_INFLATION", "Inflation rate by pricing-behavior group", "Fiyatlama davranışı grubuna göre enflasyon", "pi_group", "percent", "price_setting", "Monthly or annual inflation of CPI items grouped by predominantly time- or state-dependent pricing.", "This is an inflation rate, not a frequency; match group, month and annual/monthly transformation."),
    ("PF_PASS_THROUGH_SPEED", "Pass-through speed", "Geçişkenlik hızı", "h_PT", "months", "pass_through", "Months required for a stated share or near-completion of cumulative pass-through.", "Match price index, regime and completion criterion."),
]


def source_dict(row: tuple[object, ...]) -> dict[str, object]:
    sid, title, authors, year, inst, stype, lang, url, doi, local, pages, notes = row
    return {"source_id": sid, "title": title, "authors": authors, "year": year,
            "institution_or_journal": inst, "source_type": stype, "language": lang,
            "url": url, "doi": doi, "local_pdf": local, "pdf_pages": pages,
            "access_status": "archived", "scope_status": "in_scope",
            "accessed_date": "2026-10-17", "notes": notes}


def parameter_dict(row: tuple[str, ...]) -> dict[str, str]:
    return dict(zip(["parameter_id", "name_en", "name_tr", "canonical_symbol", "default_unit",
                     "parameter_class", "definition", "comparison_rule"], row))


rows: list[dict[str, object]] = []


def add(source_id: str, parameter_id: str, value: object, *, lower: object = "", upper: object = "",
        se: object = "", unit: str, status: str = "estimated", family: str,
        method: str, period: str, frequency: str, sector: str, variant: str,
        page: object, locator: str, notes: str = "") -> None:
    rows.append({"source_id": source_id, "parameter_id": parameter_id, "value": value,
                 "lower_bound": lower, "upper_bound": upper, "standard_error": se,
                 "unit": unit, "estimate_status": status, "model_family": family,
                 "estimation_method": method, "data_period": period, "frequency": frequency,
                 "sector": sector, "definition_variant": variant, "source_pdf_page": page,
                 "source_locator": locator, "verification_status": "pdf_verified", "notes": notes})


# S001 — estimated nominal rigidities and steady-state markups from the baseline DSGE model.
for pid, value, lo, hi, variant in [
    ("PF_CALVO_WAGE_STICKINESS", .749, .591, .912, "Quarterly Calvo non-reoptimization probability for wages"),
    ("PF_CALVO_PRICE_STICKINESS", .920, .893, .948, "Quarterly Calvo non-reoptimization probability for domestic prices"),
    ("PF_CALVO_PRICE_STICKINESS", .798, .744, .853, "Quarterly Calvo non-reoptimization probability for import prices"),
    ("PF_WAGE_INDEXATION", .497, .338, .668, "Wage indexation"),
    ("PF_PRICE_INDEXATION", .299, .337, .662, "Domestic-price indexation")]:
    add("S001", pid, value, lower=lo, upper=hi, unit="fraction", family="Small-open-economy DSGE",
        method="Bayesian estimation", period="2002Q1-2012Q2", frequency="quarterly", sector="Whole economy",
        variant=variant, page=38, locator="Table 4.2",
        notes="The source prints a posterior mean of 0.299 for price indexation but a 0.337-0.662 interval; the apparent internal inconsistency is preserved and flagged." if pid == "PF_PRICE_INDEXATION" else "")
for sector in ["Domestically produced goods", "Imports"]:
    add("S001", "PF_MARKUP", 1.15, unit="ratio", status="calibrated", family="Small-open-economy DSGE",
        method="Steady-state calibration", period="2002Q1-2012Q2", frequency="quarterly", sector=sector,
        variant="Steady-state gross price markup", page=37, locator="Table 4.1")


# S091 — micro price rigidity.
for sector, duration in [("Consumer prices", 3.69), ("Food", 3.16), ("Unprocessed food", 2.03),
                         ("Processed food", 4.44), ("Services", 7.22), ("Energy", 4.51),
                         ("Goods excluding food and energy", 5.20)]:
    add("S091", "PF_PRICE_SPELL_DURATION", duration, unit="biweekly_periods", status="descriptive_statistic",
        family="Micro price-spell analysis", method="Item-level spell calculation", period="2006-10 to 2011-01",
        frequency="biweekly", sector=sector, variant="Mean completed-spell duration", page=13, locator="Table 1")
for sector, actual, implied in [("Consumer prices", 7.4, 6.3), ("Food", 6.3, 5.3), ("Energy", 9.0, 8.0),
                                ("Goods excluding food and energy", 10.4, 9.4), ("Services", 14.4, 13.4)]:
    for label, val in [("Actual mean duration", actual), ("Implied duration from frequency", implied)]:
        add("S091", "PF_PRICE_SPELL_DURATION", val, unit="weeks", status="descriptive_statistic",
            family="Micro price-spell analysis", method="Item-level spell calculation", period="2006-10 to 2011-01",
            frequency="biweekly", sector=sector, variant=label, page=15, locator="Table 3")
for sector, up, down in [("Consumer prices", 18.06, -16.78), ("Food", 19.20, -17.75),
                          ("Unprocessed food", 23.12, -20.98), ("Processed food", 15.79, -14.19),
                          ("Services", 12.80, -11.32), ("Energy", 5.09, -2.80),
                          ("Goods excluding food and energy", 14.98, -13.90)]:
    add("S091", "PF_PRICE_INCREASE_SIZE", up, unit="percent", status="descriptive_statistic",
        family="Micro price-spell analysis", method="Item-level mean non-zero change", period="2006-10 to 2011-01",
        frequency="biweekly", sector=sector, variant="Mean positive price change", page=23, locator="Table 6")
    add("S091", "PF_PRICE_DECREASE_SIZE", down, unit="percent", status="descriptive_statistic",
        family="Micro price-spell analysis", method="Item-level mean non-zero change", period="2006-10 to 2011-01",
        frequency="biweekly", sector=sector, variant="Mean negative price change", page=23, locator="Table 6")
for sector, coef, se in [("Consumer prices", -.57, .02), ("Food", -.67, .02),
                         ("Goods excluding food and energy", -.47, .03), ("Energy", .21, .03),
                         ("Services", .22, .03)]:
    add("S091", "PF_DURATION_SIZE_SENSITIVITY", coef, se=se, unit="regression_coefficient",
        family="Price-change size regression", method="OLS", period="2006-10 to 2011-01", frequency="biweekly",
        sector=sector, variant="Coefficient of preceding spell duration", page=24, locator="Table 8")
for sector, value in [("Consumer prices", .14), ("Food", .13), ("Energy", .29),
                      ("Goods excluding food and energy", .20), ("Services", .25)]:
    add("S091", "PF_PRICE_SYNCHRONIZATION", value, unit="index_ratio", status="descriptive_statistic",
        family="Micro price synchronization", method="Synchronization ratio", period="2006-10 to 2011-01",
        frequency="biweekly", sector=sector, variant="Price-change synchronization ratio", page=27, locator="Table 9")
for sector, value in [("Consumer prices", .22), ("Food", .27), ("Non-food", .16)]:
    add("S091", "PF_PRICE_CHANGE_FREQUENCY", value, unit="fraction_per_biweek", status="descriptive_statistic",
        family="Micro price-spell analysis", method="Share of items changing price", period="2006-10 to 2011-01",
        frequency="biweekly", sector=sector, variant="Average non-zero price-change frequency", page=25, locator="Text following Table 8")


# S092 — posted/regular prices and inflation regimes.
base_freq = {
    "Processed food": ((.40, .25, .15), (.26, .19, .08)), "Milk and dairy": ((.53, .31, .22), (.34, .22, .11)),
    "Durables": ((.48, .32, .15), (.42, .31, .11)), "Other core goods": ((.35, .21, .14), (.25, .17, .08)),
    "Fuel": ((1.14, .68, .46), None), "Gold": ((1.86, 1.16, .71), None),
}
for sector, groups in base_freq.items():
    for price_type, values in [("Posted prices", groups[0]), ("Regular prices", groups[1])]:
        if values is None:
            continue
        for direction, value in zip(("All changes", "Increases", "Decreases"), values):
            add("S092", "PF_PRICE_CHANGE_FREQUENCY", value, unit="changes_per_month", status="descriptive_statistic",
                family="Daily online-price analysis", method="Monthly count per product", period="2012Q1-2022Q1",
                frequency="daily prices aggregated monthly", sector=sector, variant=f"{price_type}; {direction}", page=17, locator="Table 4.1.1")
base_size = {
    "Processed food": ((14.71, -12.38), (11.56, -11.15)), "Milk and dairy": ((13.55, -11.30), (10.21, -9.86)),
    "Durables": ((8.23, -7.96), (7.29, -8.57)), "Other core goods": ((18.43, -15.41), (14.28, -14.15)),
    "Fuel": ((3.30, -2.91), None), "Gold": ((3.52, -2.61), None),
}
for sector, groups in base_size.items():
    for price_type, values in [("Posted prices", groups[0]), ("Regular prices", groups[1])]:
        if values is None:
            continue
        add("S092", "PF_PRICE_INCREASE_SIZE", values[0], unit="percent", status="descriptive_statistic",
            family="Daily online-price analysis", method="Mean non-zero price change", period="2012Q1-2022Q1",
            frequency="daily", sector=sector, variant=price_type, page=17, locator="Table 4.1.2")
        add("S092", "PF_PRICE_DECREASE_SIZE", values[1], unit="percent", status="descriptive_statistic",
            family="Daily online-price analysis", method="Mean non-zero price change", period="2012Q1-2022Q1",
            frequency="daily", sector=sector, variant=price_type, page=17, locator="Table 4.1.2")
regime_freq = {
    "Processed food": ((.22, .15, .08), (.32, .24, .08)), "Milk and dairy": ((.32, .21, .11), (.36, .25, .11)),
    "Durables": ((.32, .22, .10), (.55, .42, .13)), "Other core goods": ((.20, .12, .08), (.31, .22, .09)),
    "Fuel": ((1.20, .62, .57), (1.06, .76, .30)), "Gold": ((1.81, 1.07, .75), (1.91, 1.24, .67)),
}
for sector, regimes in regime_freq.items():
    for period, values in [("2012Q1-2017Q4", regimes[0]), ("2018Q1-2022Q1", regimes[1])]:
        for direction, value in zip(("All changes", "Increases", "Decreases"), values):
            add("S092", "PF_PRICE_CHANGE_FREQUENCY", value, unit="changes_per_month", status="descriptive_statistic",
                family="State-dependent pricing comparison", method="Regular-price monthly count per product", period=period,
                frequency="daily prices aggregated monthly", sector=sector, variant=f"Regular prices; {direction}", page=18, locator="Table 4.1.3")
regime_size = {
    "Processed food": ((11.26, -11.56), (11.97, -10.58)), "Milk and dairy": ((9.67, -10.36), (10.90, -9.20)),
    "Durables": ((6.36, -8.27), (8.32, -8.87)), "Other core goods": ((13.46, -14.15), (15.31, -14.16)),
    "Fuel": ((2.63, -2.58), (4.03, -3.89)), "Gold": ((2.53, -2.55), (4.31, -2.67)),
}
for sector, regimes in regime_size.items():
    for period, values in [("2012Q1-2017Q4", regimes[0]), ("2018Q1-2022Q1", regimes[1])]:
        add("S092", "PF_PRICE_INCREASE_SIZE", values[0], unit="percent", status="descriptive_statistic",
            family="State-dependent pricing comparison", method="Regular-price mean change", period=period,
            frequency="daily", sector=sector, variant="Regular-price increase", page=18, locator="Table 4.1.4")
        add("S092", "PF_PRICE_DECREASE_SIZE", values[1], unit="percent", status="descriptive_statistic",
            family="State-dependent pricing comparison", method="Regular-price mean change", period=period,
            frequency="daily", sector=sector, variant="Regular-price decrease", page=18, locator="Table 4.1.4")


# S093 — nonlinear quarterly ERPT and other Phillips-curve drivers.
for regime, horizon, value in [("Normal exchange-rate movement", "Impact quarter", .10),
                               ("Normal exchange-rate movement", "One year", .26),
                               ("Normal exchange-rate movement", "Long run", .39),
                               ("Large depreciation", "Impact quarter", .46),
                               ("Large depreciation", "One year", .60),
                               ("Large depreciation", "Long run", .73)]:
    add("S093", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", status="estimated_derived" if horizon != "Impact quarter" else "estimated",
        family="Nonlinear Phillips curve", method="Quarterly regression with large-shock interaction", period="2006Q2-2024Q2",
        frequency="quarterly", sector="Consumer prices", variant=f"{regime}; cumulative {horizon.lower()}", page=13,
        locator="Table 1 and cumulative calculations", notes="Large-depreciation values combine the baseline and large-shock interaction where applicable.")
specs = [
    ("Output gap", "PF_OUTPUT_GAP_INFLATION_SENSITIVITY", [.13, .10, .07, .07, .11, .10], "regression_coefficient"),
    ("Current exchange rate", "PF_EXCHANGE_RATE_PASS_THROUGH", [.10, .10, .10, .10, .10, .11], "fraction"),
    ("Large-shock interaction", "PF_EXCHANGE_RATE_PASS_THROUGH", [.36, .38, "", "", .36, .35], "fraction"),
    ("Import prices", "PF_IMPORT_PRICE_PASS_THROUGH", [.11, .12, .09, .09, .10, .12], "fraction"),
    ("Current minimum wage", "PF_MINIMUM_WAGE_PASS_THROUGH", [.02, .05, .02, .02, .01, .02], "regression_coefficient"),
    ("Lagged minimum wage", "PF_MINIMUM_WAGE_PASS_THROUGH", [.03, .03, .02, .02, .01, .01], "regression_coefficient"),
]
for label, pid, values, unit in specs:
    for idx, value in enumerate(values, 1):
        if value == "":
            continue
        add("S093", pid, value, unit=unit, family="Nonlinear Phillips curve", method=f"Specification {idx}",
            period="2006Q2-2024Q2", frequency="quarterly", sector="Consumer prices", variant=label,
            page=13 if idx <= 3 else 14, locator="Table 1")
for episode, value in [("2018Q3 depreciation interaction", .24), ("2021Q4 depreciation interaction", .48),
                       ("2022Q1 depreciation interaction", .24), ("2023Q3 depreciation interaction", .44)]:
    add("S093", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", family="Nonlinear Phillips curve",
        method="Episode-specific interaction regression", period="2006Q2-2024Q2", frequency="quarterly",
        sector="Consumer prices", variant=episode, page=14, locator="Table 1, Model 3",
        notes="Incremental pass-through relative to the baseline, not the total response.")


# S094 — product-level trade-price ERPT.
for flow, short_vals, long_vals, short_se, long_se in [
    ("Imports", [.9227, .8947, .8811], [.8688, .8565, .8933], [.0495, .0378, .0322], [.0397, .0306, .0280]),
    ("Exports", [.8083, .8289, .8371], [.8283, .8093, .8160], [.0532, .0417, .0392], [.0464, .0303, .0279]),
]:
    for spec in range(3):
        for horizon, value, se in [("Short run", short_vals[spec], short_se[spec]), ("Long run", long_vals[spec], long_se[spec])]:
            add("S094", "PF_EXCHANGE_RATE_PASS_THROUGH", value, se=se, unit="fraction", family="Product-level trade-price regression",
                method=f"Fixed effects specification {spec+1}", period="2002-2017", frequency="monthly",
                sector=flow, variant=f"{flow.lower()} ERPT; {horizon.lower()}", page=23 if flow == "Imports" else 24,
                locator="Table 2" if flow == "Imports" else "Table 3")
for flow, short, long, se_s, se_l in [("Imports", .98, .90, .073, .050), ("Exports", .90, .82, .060, .044)]:
    for horizon, value, se in [("Short run", short, se_s), ("Long run", long, se_l)]:
        add("S094", "PF_EXCHANGE_RATE_PASS_THROUGH", value, se=se, unit="fraction", family="Aggregate trade-price regression",
            method="Macro time-series benchmark", period="2002-2017", frequency="monthly", sector=flow,
            variant=f"Aggregate {flow.lower()} price ERPT; {horizon.lower()}", page=27, locator="Table 5")
sectoral = {
    "Food and agriculture": ((.6932, .0441, .6220, .0706), (.7119, .5339)),
    "Chemicals and plastics": ((.8921, "", .8519, ""), (.8257, .8280)),
    "Leather and textiles": ((.9425, "", .8398, ""), (.9450, .8074)),
    "Unprocessed materials": ((.8443, "", .8710, ""), (.7738, .9100)),
    "Processed goods": ((.9793, "", .9628, ""), (.9178, .8043)),
}
for sector, (imports, exports) in sectoral.items():
    for flow, values in [("Imports", (imports[0], imports[2])), ("Exports", exports)]:
        for horizon, value in zip(("Short run", "Long run"), values):
            add("S094", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", family="Product-level trade-price regression",
                method="Sector fixed-effects specification", period="2002-2017", frequency="monthly", sector=sector,
                variant=f"{flow.lower()} ERPT; {horizon.lower()}", page=28, locator="Table 6")


# S095 — disaggregated CPI pass-through at an eight-quarter horizon.
for sector, erpt, ippt in [("Headline CPI", 17.4, 14.0), ("Unprocessed food", 23.5, 12.8),
                           ("Processed food", 27.1, 15.4), ("Energy", 7.5, 30.5),
                           ("Core goods", 24.8, 17.0), ("Services", 11.5, 4.2),
                           ("CPIX", 17.5, 14.8), ("CPI excluding selected volatile items", 19.1, 15.3)]:
    add("S095", "PF_EXCHANGE_RATE_PASS_THROUGH", erpt, unit="percent", status="estimated_derived",
        family="Disaggregated Phillips curves", method="Eight-quarter cumulative distributed lag", period="2005Q2-2015Q4",
        frequency="quarterly", sector=sector, variant="Eight-quarter cumulative ERPT", page=18, locator="Table 3")
    add("S095", "PF_IMPORT_PRICE_PASS_THROUGH", ippt, unit="percent", status="estimated_derived",
        family="Disaggregated Phillips curves", method="Eight-quarter cumulative distributed lag", period="2005Q2-2015Q4",
        frequency="quarterly", sector=sector, variant="Eight-quarter cumulative import-price pass-through", page=18, locator="Table 3")
for threshold, erpt, ippt in [(66, 18.5, 14.5), (75, 17.4, 14.0), (80, 15.7, 13.5)]:
    add("S095", "PF_EXCHANGE_RATE_PASS_THROUGH", erpt, unit="percent", status="estimated_derived",
        family="Disaggregated Phillips curves", method="Aggregation-threshold robustness", period="2005Q2-2015Q4",
        frequency="quarterly", sector="Headline CPI", variant=f"Eight-quarter cumulative; inclusion threshold {threshold}%", page=20, locator="Robustness exercise")
    add("S095", "PF_IMPORT_PRICE_PASS_THROUGH", ippt, unit="percent", status="estimated_derived",
        family="Disaggregated Phillips curves", method="Aggregation-threshold robustness", period="2005Q2-2015Q4",
        frequency="quarterly", sector="Headline CPI", variant=f"Eight-quarter cumulative; inclusion threshold {threshold}%", page=20, locator="Robustness exercise")


# S096 — sectoral producer-price pass-through and import dependence.
industry = [
    ("Refined petroleum", 92.7, 70.0, 106.8, 72.1), ("Chemicals", 42.5, 31.8, 49.5, 41.4),
    ("Base metals", 60.4, 44.3, 71.8, 35.3), ("Motor vehicles", 42.4, .7, 45.2, 32.6),
    ("Rubber and plastics", 35.8, 38.2, 33.7, 33.6), ("Paper", 42.2, 33.0, 52.0, 33.9),
    ("Computer and electronics", 42.1, 80.2, 62.8, 34.5), ("Electrical equipment", 36.3, 13.0, 39.1, 26.6),
    ("Electricity", 6.2, 3.5, 12.8, 26.3), ("Pharmaceuticals", 5.9, 2.0, 5.3, 25.5),
    ("Machinery", 35.6, 16.7, 35.6, 25.5), ("Other transport equipment", 5.8, -.4, 6.7, 22.4),
    ("Printing", 4.4, 4.8, 7.9, 22.1), ("Fabricated metals", 39.5, 8.3, 48.4, 18.9),
    ("Wood", 4.5, .7, 8.6, 18.2), ("Furniture", 12.1, 2.8, 4.5, 17.5),
    ("Textiles apparel and leather", 32.2, 40.3, 32.1, 15.2), ("Food beverages and tobacco", 7.6, 2.7, 16.7, 13.3),
    ("Non-metallic minerals", 9.9, 6.1, 14.0, 13.0), ("Mining", 32.7, 34.4, 31.5, 12.1),
]
services = [
    ("Repair services", -2.0, -6.3, -.5, 18.4), ("Other services", -8.6, 8.5, -13.4, 12.7),
    ("Travel services", 28.0, 11.4, 38.0, 10.9), ("Financial services", 18.1, -21.8, 19.0, 2.3),
    ("Education", -1.2, -2.6, .3, 1.2), ("Wholesale retail and repair", 42.9, 8.9, 42.5, 13.1),
    ("Land transport", 4.0, 2.3, -.9, 12.5), ("Legal and accounting", -5.2, -7.8, -3.5, 3.9),
    ("Accommodation and food", 1.5, -2.6, 2.3, 6.6), ("Water transport", -7.0, -3.4, -16.2, 13.6),
    ("Telecommunications", 2.2, -6.8, 9.8, 3.7), ("Air transport", -1.3, .7, -8.7, 17.6),
    ("Health", 3.8, -7.6, 11.9, 6.5), ("Recreation and culture", 16.3, 9.8, 14.2, 3.0),
    ("Postal services", -11.2, 7.8, -66.4, 5.1), ("Sports and amusement", 1.2, -7.9, -.8, 4.8),
    ("Insurance", 4.7, -14.2, 48.4, 12.7),
]
for group, table, page, model in [(industry, "Table 2", 21, "Industrial sector price equation"),
                                  (services, "Table 3", 23, "Service sector price equation")]:
    for sector, tl_ippt, usd_ippt, erpt, dep in group:
        add("S096", "PF_IMPORT_PRICE_PASS_THROUGH", tl_ippt, unit="percent", family=model,
            method="Sectoral distributed-lag regression", period="2010-2017", frequency="monthly", sector=sector,
            variant="Cumulative pass-through of import prices in TRY", page=page, locator=table)
        add("S096", "PF_IMPORT_PRICE_PASS_THROUGH", usd_ippt, unit="percent", family=model,
            method="Sectoral distributed-lag regression", period="2010-2017", frequency="monthly", sector=sector,
            variant="Cumulative pass-through of import prices in USD", page=page, locator=table)
        add("S096", "PF_EXCHANGE_RATE_PASS_THROUGH", erpt, unit="percent", family=model,
            method="Sectoral distributed-lag regression", period="2010-2017", frequency="monthly", sector=sector,
            variant="Cumulative sectoral producer-price ERPT", page=page, locator=table)
        add("S096", "PF_IMPORT_DEPENDENCE", dep, unit="percent", status="calculated",
            family="Input-output cost structure", method="Imported-input share calculation", period="2010-2017",
            frequency="annual benchmark", sector=sector, variant="Imported-input dependence", page=page, locator=table)
for period, erpt_coef, erpt_se, ippt_coef, ippt_se in [
    ("2005-2017", 1.513, .225, 1.064, .227), ("2010-2017", 1.590, .170, 1.038, .208)]:
    add("S096", "PF_EXCHANGE_RATE_PASS_THROUGH", erpt_coef, se=erpt_se, unit="cross_sector_slope",
        family="Cross-sector pass-through regression", method="Weighted cross-section regression", period=period,
        frequency="sectoral", sector="Industry sectors", variant="Slope of ERPT on imported-input dependence", page=26, locator="Table 4")
    add("S096", "PF_IMPORT_PRICE_PASS_THROUGH", ippt_coef, se=ippt_se, unit="cross_sector_slope",
        family="Cross-sector pass-through regression", method="Weighted cross-section regression", period=period,
        frequency="sectoral", sector="Industry sectors", variant="Slope of import-price pass-through on imported-input dependence", page=26, locator="Table 4")


# S097 — foreign-currency debt amplification.
for denom, coefs, ses, implied in [
    ("Equity", [.017, .010, .038, .035], [.005, .005, .010, .010], [2.20, 1.29, 2.19, 2.01]),
    ("Assets", [.042, .028, .080, .087], [.014, .015, .026, .027], [1.77, 1.18, 1.63, 1.77]),
]:
    for spec, (coef, se, effect) in enumerate(zip(coefs, ses, implied), 1):
        add("S097", "PF_FX_DEBT_PRICE_SENSITIVITY", coef, se=se, unit="regression_coefficient",
            family="Firm-balance-sheet augmented price equation", method=f"Panel specification {spec}",
            period="2007-2016", frequency="annual firm balance sheets and monthly prices", sector="Manufacturing firms",
            variant=f"Exchange-rate change × net FX liabilities/{denom.lower()}", page=16 if denom == "Equity" else 17,
            locator="Table 4" if denom == "Equity" else "Table 5")
        add("S097", "PF_FX_DEBT_PRICE_SENSITIVITY", effect, unit="percentage_points", status="estimated_derived",
            family="Firm-balance-sheet augmented price equation", method=f"Panel specification {spec}",
            period="2007-2016", frequency="annual firm balance sheets and monthly prices", sector="Manufacturing firms",
            variant=f"Inflation increase after 10% depreciation for one-SD higher net FX liabilities/{denom.lower()}",
            page=16 if denom == "Equity" else 17, locator="Derived effect reported below table")


# S098 — BVAR cumulative pass-through and transmission speed.
bvar = {
    "Exchange-rate shock": ("PF_EXCHANGE_RATE_PASS_THROUGH", [("2 quarters", 1.1), ("4 quarters", 1.6), ("8 quarters", 1.7)], [(1, 38), (2, 63), (3, 80), (4, 93), (6, 99)]),
    "Import-price shock": ("PF_IMPORT_PRICE_PASS_THROUGH", [("2 quarters", 1.2), ("4 quarters", 1.3), ("8 quarters", 1.3)], [(1, 80), (2, 93), (3, 100), (4, 100), (6, 100)]),
    "GDP-growth shock": ("PF_GROWTH_INFLATION_SENSITIVITY", [("2 quarters", .12), ("4 quarters", .25), ("8 quarters", .29)], [(2, 39), (3, 71), (4, 86), (6, 93)]),
    "Nominal-wage shock": ("PF_WAGE_PASS_THROUGH", [("2 quarters", .07), ("4 quarters", .15), ("8 quarters", .18)], [(2, 37), (3, 64), (4, 80), (6, 94)]),
}
for shock, (pid, magnitudes, speeds) in bvar.items():
    for horizon, value in magnitudes:
        add("S098", pid, value, unit="percentage_points", status="estimated_derived", family="Bayesian VAR",
            method="Sign/zero-restricted BVAR impulse response", period="2005Q2-2016Q2", frequency="quarterly",
            sector="Headline consumer inflation", variant=f"Cumulative response to standardized 10% shock; {horizon}" if "shock" in shock and "GDP" not in shock and "wage" not in shock.lower() else f"Cumulative response; {horizon}",
            page=14, locator="Table 1", notes="For exchange-rate/import-price shocks the source uses a 10% shock; for growth and wages see the source normalization.")
    for quarter, share in speeds:
        add("S098", "PF_PASS_THROUGH_SPEED", share, unit="percent_of_eight_quarter_effect", status="estimated_derived",
            family="Bayesian VAR", method="Share of cumulative eight-quarter response", period="2005Q2-2016Q2",
            frequency="quarterly", sector="Headline consumer inflation", variant=f"{shock}; share completed by quarter {quarter}", page=14, locator="Table 1")


# S099 — output-gap-sensitive CPI coverage.
for value, variant in [(47, "Number of output-gap-sensitive CPI subgroups"), (152, "Total CPI subgroups tested")]:
    add("S099", "PF_OUTPUT_GAP_INFLATION_SENSITIVITY", value, unit="count", status="descriptive_statistic",
        family="Disaggregated output-gap screening", method="Subgroup Phillips-curve significance screen", period="2003-2013",
        frequency="monthly", sector="CPI subgroups", variant=variant, page=15, locator="Results summary")
for value, variant in [(34, "Basket share classified output-gap-sensitive"), (66, "Basket share classified non-sensitive"),
                       (56, "Non-sensitive share excluding fresh produce alcohol and tobacco")]:
    add("S099", "PF_OUTPUT_GAP_INFLATION_SENSITIVITY", value, unit="percent_of_CPI_basket", status="descriptive_statistic",
        family="Disaggregated output-gap screening", method="CPI-weight aggregation", period="2003-2013", frequency="monthly",
        sector="Consumer prices", variant=variant, page=15, locator="Results summary")
add("S099", "PF_OUTPUT_GAP_INFLATION_SENSITIVITY", .11, unit="percentage_points", family="Cross-country Phillips curve",
    method="Panel comparison coefficient for Türkiye", period="2003-2013", frequency="annualized inflation",
    sector="Consumer prices", variant="Annual inflation response to a one-percentage-point output gap", page=18, locator="Cross-country comparison")


# S100 — model-averaged and regime-switching ERPT.
for frequency, cpi, ppi in [("monthly", -.1809, -.2558), ("quarterly", -.1522, -.2138), ("annual", -.1254, -.1855)]:
    for sector, value in [("CPI", cpi), ("PPI", ppi)]:
        add("S100", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="regression_coefficient", family="Model averaging",
            method="Average OLS coefficient across specifications", period="2003-2013", frequency=frequency,
            sector=sector, variant="Average nominal effective exchange-rate coefficient", page=25, locator="Table 2",
            notes="The source's NEER sign convention makes depreciation pass-through appear with a negative coefficient.")
for state, current, lagged in [("State 1", -.29, -.28), ("State 2", -.13, .07)]:
    for lag, value in [("Current", current), ("Lag 1", lagged)]:
        add("S100", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="regression_coefficient", family="Markov-switching regression",
            method="Two-state Markov switching", period="2003-2013", frequency="monthly", sector="CPI",
            variant=f"{state}; {lag.lower()} NEER coefficient", page=27, locator="Table 3")
for sector, value in [("CPI", -.4765), ("PPI", -.5213)]:
    add("S100", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", status="estimated_derived", family="VAR",
        method="Long-run cumulative impulse response", period="2003-2013", frequency="monthly", sector=sector,
        variant="Long-run cumulative NEER pass-through", page=54, locator="VAR horizon table")


# S101 — invoicing currency and trade-price pass-through.
for flow, category, value in [
    ("Imports", "All products", .182), ("Exports", "All products", -.195),
    ("Imports", "Consumption goods", .138), ("Exports", "Consumption goods", -.143),
    ("Imports", "Capital goods", .255), ("Exports", "Capital goods", -.250),
    ("Imports", "Intermediate goods", .194), ("Exports", "Intermediate goods", -.215),
]:
    add("S101", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", family="Bilateral trade-price regression",
        method="Product-country fixed effects", period="2002-2017", frequency="monthly", sector=f"{flow}; {category}",
        variant="Baseline bilateral exchange-rate pass-through", page=20, locator="Table 7")
currency_values = {
    "Imports": {"USD": [.396, .638, 1.155, -.039], "EUR": [.574, .538, .703, .501], "TRY": [-.785, -.745, -.991, -.694]},
    "Exports": {"USD": [-.498, -.513, -.881, -.230], "EUR": [-.595, -.444, -.783, -.558], "TRY": [.793, .650, 1.000, .731]},
}
cats = ["All products", "Consumption goods", "Capital goods", "Intermediate goods"]
for flow, currencies in currency_values.items():
    for currency, values in currencies.items():
        for category, value in zip(cats, values):
            add("S101", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", family="Invoicing-currency trade-price regression",
                method="Product-country fixed effects with currency interactions", period="2002-2017", frequency="monthly",
                sector=f"{flow}; {category}", variant=f"{currency}-invoiced price coefficient", page=21, locator="Table 8",
                notes="Signs follow the source's flow-specific exchange-rate convention; do not compare absolute signs mechanically across imports and exports.")
for gvc, imp, exp in [("Lower GVC participation", .296, -.276), ("Upper GVC participation", .267, -.237)]:
    for flow, value in [("Imports", imp), ("Exports", exp)]:
        add("S101", "PF_EXCHANGE_RATE_PASS_THROUGH", value, unit="fraction", family="GVC-heterogeneous trade-price regression",
            method="Product-country fixed effects", period="2002-2017", frequency="monthly", sector=flow,
            variant=gvc, page=22, locator="Table 9")


# S102 — domestic-cost hybrid Phillips curves.
for period, vals in [
    ("2003Q2-2012Q3", {"back": (.56, .44, .70), "forward": (.44, "", ""), "slope": (.16, .07, .23),
                        "domestic": (.42, .20, .64), "foreign": (.58, "", ""), "foreign_current": (.68, .43, .95),
                        "foreign_lag": (.34, .16, .50), "gap_current": (.48, .14, .82), "gap_lag": (.44, .11, .77)}),
    ("2005Q2-2012Q3", {"back": (.49, .40, .60), "forward": (.51, "", ""), "slope": (.17, .10, .24),
                        "domestic": (.36, .14, .55), "foreign": (.64, "", ""), "foreign_current": (.72, .48, .96),
                        "foreign_lag": (.33, .17, .50), "gap_current": (.51, .17, .84), "gap_lag": (.46, .10, .78)}),
]:
    mapping = [
        ("back", "PF_INFLATION_PERSISTENCE", "Backward-looking inflation weight", "fraction"),
        ("forward", "PF_FORWARD_LOOKING_SHARE", "Forward-looking inflation weight", "fraction"),
        ("slope", "PF_MARGINAL_COST_INFLATION_SLOPE", "Marginal-cost slope", "regression_coefficient"),
        ("domestic", "PF_DOMESTIC_COST_SHARE", "Domestic-cost share", "fraction"),
        ("foreign", "PF_FOREIGN_COST_SHARE", "Foreign-cost share", "fraction"),
        ("foreign_current", "PF_FOREIGN_COST_SHARE", "Current foreign-cost dynamic weight", "fraction"),
        ("foreign_lag", "PF_FOREIGN_COST_SHARE", "Lagged foreign-cost dynamic weight", "fraction"),
        ("gap_current", "PF_OUTPUT_GAP_INFLATION_SENSITIVITY", "Current output-gap dynamic weight", "fraction"),
        ("gap_lag", "PF_OUTPUT_GAP_INFLATION_SENSITIVITY", "Lagged output-gap dynamic weight", "fraction"),
    ]
    for key, pid, variant, unit in mapping:
        value, lo, hi = vals[key]
        add("S102", pid, value, lower=lo, upper=hi, unit=unit, family="Hybrid New Keynesian Phillips curve",
            method="GMM", period=period, frequency="quarterly", sector="Headline CPI", variant=variant, page=12, locator="Table 1")
for spec, back, forward, slope, domestic in [("Services specification 1", .66, .34, .13, .64),
                                             ("Services specification 2", .71, .29, .31, .65)]:
    for pid, value, variant, unit in [
        ("PF_INFLATION_PERSISTENCE", back, "Backward-looking inflation weight", "fraction"),
        ("PF_FORWARD_LOOKING_SHARE", forward, "Forward-looking inflation weight", "fraction"),
        ("PF_MARGINAL_COST_INFLATION_SLOPE", slope, "Marginal-cost slope", "regression_coefficient"),
        ("PF_DOMESTIC_COST_SHARE", domestic, "Domestic-cost share", "fraction")]:
        add("S102", pid, value, unit=unit, family="Services hybrid Phillips curve", method="GMM",
            period="2003Q2-2012Q3", frequency="quarterly", sector="Services CPI", variant=f"{spec}; {variant}", page=16, locator="Table 3")


# S103 — expectations, fixed Phillips curve and expectation formation.
fixed = [
    ("PF_INFLATION_PERSISTENCE", .174, .0591, "Lagged quarterly inflation"),
    ("PF_FORWARD_LOOKING_SHARE", .478, .103, "One-year-ahead inflation expectations"),
    ("PF_OUTPUT_GAP_INFLATION_SENSITIVITY", .362, .0773, "Output gap"),
    ("PF_EXCHANGE_RATE_PASS_THROUGH", .359, .0417, "Current exchange-rate change"),
    ("PF_EXCHANGE_RATE_PASS_THROUGH", .0527, .0426, "Exchange-rate change lag 1"),
    ("PF_EXCHANGE_RATE_PASS_THROUGH", .0947, .0357, "Exchange-rate change lag 2"),
    ("PF_IMPORT_PRICE_PASS_THROUGH", .354, .0461, "Import-price change"),
    ("PF_MARGINAL_COST_INFLATION_SLOPE", .431, .184, "Real unit labor cost"),
]
for pid, value, se, variant in fixed:
    add("S103", pid, value, se=se, unit="regression_coefficient", family="Fixed-coefficient Phillips curve",
        method="System estimator", period="2007Q2-2019Q4", frequency="quarterly", sector="Headline CPI",
        variant=variant, page=11, locator="Table 1, system-estimator column")
expectation = [
    ("PF_EXPECTATION_BACKWARD_WEIGHT", .143, .0344, "Past annual inflation"),
    ("PF_EXPECTATION_FX_SENSITIVITY", .0402, .00899, "Exchange-rate change"),
    ("PF_EXPECTATION_TARGET_WEIGHT", .116, .151, "Inflation target"),
    ("PF_EXPECTATION_SURPRISE_SENSITIVITY", .141, .0440, "Inflation surprise"),
    ("PF_EXPECTATION_TARGET_WEIGHT", -.478, .484, "Inflation-target revision"),
    ("PF_EXPECTATION_SURPRISE_SENSITIVITY", .436, .0826, "CBRT forecast revision"),
]
for pid, value, se, variant in expectation:
    add("S103", pid, value, se=se, unit="regression_coefficient", family="Inflation-expectation formation",
        method="System estimator", period="2007Q2-2019Q4", frequency="quarterly", sector="Survey of Market Participants",
        variant=variant, page=12, locator="Table 2, system-estimator column")
for pid, value, variant in [
    ("PF_FORWARD_LOOKING_SHARE", .46, "Latest time-varying sensitivity to expectations"),
    ("PF_EXCHANGE_RATE_PASS_THROUGH", .20, "Latest current-quarter ERPT"),
    ("PF_IMPORT_PRICE_PASS_THROUGH", .10, "Latest cumulative import-price pass-through"),
    ("PF_OUTPUT_GAP_INFLATION_SENSITIVITY", .47, "Latest long-run output-gap effect"),
    ("PF_MARGINAL_COST_INFLATION_SLOPE", .61, "Latest long-run real unit labor-cost effect")]:
    add("S103", pid, value, unit="fraction", status="descriptive_time_varying_result", family="Time-varying Phillips curve",
        method="TVP regression", period="2007Q2-2020Q3", frequency="quarterly", sector="Headline CPI",
        variant=variant, page=15, locator="Time-varying estimates discussion",
        notes="Approximate endpoint reported in text/figures; not a fixed full-sample structural parameter.")


# S104 — randomized expectation treatment and firms' own decisions.
for outcome, value, se in [("Own wage expectations", .582, .250), ("Own unit-cost expectations", .535, .189),
                           ("Own price expectations", .551, .182), ("Business outlook pessimism", .014, .003),
                           ("Economy-wide outlook pessimism", .024, .002), ("Credit-condition pessimism", .012, .002)]:
    add("S104", "PF_FIRM_DECISION_RESPONSE_TO_EXPECTATIONS", value, se=se, unit="regression_coefficient",
        family="Randomized information experiment", method="Instrumental variables / treatment-induced expectation shift",
        period="2024-05", frequency="one-off firm survey", sector="Surveyed firms", variant=outcome, page=54, locator="Table 5",
        notes="Higher coded outlook values indicate greater pessimism for the outlook outcomes.")


# S105 — markups and concentration under inflationary pressure.
for stat, value in [("Mean", 1.3106), ("Standard deviation", 1.1029), ("Median", 1.0451),
                    ("5th percentile", .5375), ("95th percentile", 2.9452)]:
    add("S105", "PF_MARKUP", value, unit="ratio", status="descriptive_statistic", family="Production-function markup estimation",
        method="Firm-level markup distribution", period="2006-2021", frequency="annual", sector="Non-financial firms",
        variant=stat, page=18, locator="Summary statistics table")
concentration = [
    ("CR4 high-inflation interaction; baseline", .1107, .0471),
    ("CR4 high-inflation interaction; controls 1", .0921, .0465),
    ("CR4 high-inflation interaction; controls 2", .1059, .0518),
    ("CR20 high-inflation interaction; baseline", .0966, .0377),
    ("CR20 high-inflation interaction; controls 1", .0856, .0371),
    ("CR20 high-inflation interaction; controls 2", .1323, .0457),
    ("CR4; coarsened exact matching", .1565, .0551), ("CR20; coarsened exact matching", .1701, .0490),
    ("CR4; instrumental variables", .8558, .2936), ("CR20; instrumental variables", .4656, .1203),
    ("CR4 × small firm", .1234, .0507), ("CR20 × small firm", .0582, .0278),
]
for variant, value, se in concentration:
    page = 25 if "CR4" in variant and "matching" not in variant and "instrumental" not in variant and "small" not in variant else 27
    add("S105", "PF_CONCENTRATION_MARKUP_SENSITIVITY", value, se=se, unit="regression_coefficient",
        family="Firm markup-concentration regression", method=variant.split(";")[-1].strip() if ";" in variant else "Panel fixed effects",
        period="2006-2021", frequency="annual", sector="Non-financial firms", variant=variant, page=page,
        locator="Tables 1-5", notes="High-inflation interactions are incremental effects unless the variant states otherwise.")


# S106 — firm expectation errors.
for target, stats in [("PPI inflation", [("Mean absolute error", 17.70), ("Median absolute error", 6.67),
                                         ("Mean normalized absolute error", .80), ("Median normalized absolute error", .69)]),
                      ("CPI inflation", [("Mean absolute error", 8.97), ("Median absolute error", 3.35),
                                         ("Mean normalized absolute error", .40), ("Median normalized absolute error", .31)])]:
    for variant, value in stats:
        add("S106", "PF_EXPECTATION_ERROR", value, unit="ratio" if "normalized" in variant.lower() else "percentage_points",
            status="descriptive_statistic", family="Firm forecast-error analysis", method="Absolute forecast-error calculation",
            period="2012-2023", frequency="monthly survey matched to realization", sector=target, variant=variant,
            page=15, locator="Summary statistics", notes="Normalized errors divide the absolute error by the realized inflation measure.")


# S107 — multivariate-filter Phillips curve.
for pid, value, lo, hi, variant in [
    ("PF_INFLATION_PERSISTENCE", .5364, .4214, .6593, "Backward-looking inflation coefficient"),
    ("PF_OUTPUT_GAP_INFLATION_SENSITIVITY", .1246, .0377, .1970, "Output-gap coefficient"),
    ("PF_IMPORT_PRICE_PASS_THROUGH", .1029, .0275, .1769, "Real import-price-gap coefficient"),
    ("PF_MARGINAL_COST_INFLATION_SLOPE", .0961, .0226, .1621, "Real unit-labor-cost coefficient"),
    ("PF_EXCHANGE_RATE_PASS_THROUGH", .1118, .0259, .1919, "Nominal exchange-rate-basket gap coefficient")]:
    add("S107", pid, value, lower=lo, upper=hi, unit="regression_coefficient", family="Multivariate filter Phillips curve",
        method="Bayesian state-space multivariate filter", period="2005Q1-2020Q4", frequency="quarterly",
        sector="Headline CPI", variant=variant, page=38, locator="Table C1")


# S108 — pass-through speed and extent before/after floating.
for sector, pre_speed, post_speed, pre_extent, post_extent in [
    ("Private manufacturing prices", "3-4", "8", .74, .51), ("Core CPI", "4-5", "10-11", .46, .30),
    ("Tradable CPI", "4", "12-13", .80, .31), ("Public manufacturing prices", "2-3", "3", .70, .49)]:
    for period, speed, extent in [("1994-02 to 2001-02", pre_speed, pre_extent), ("2001-05 to 2004-12", post_speed, post_extent)]:
        lo, hi = (speed.split("-") + [speed])[:2]
        midpoint = (float(lo) + float(hi)) / 2
        add("S108", "PF_PASS_THROUGH_SPEED", midpoint, lower=lo, upper=hi, unit="months", status="range_reported",
            family="Recursive VAR", method="Impulse-response completion timing", period=period, frequency="monthly",
            sector=sector, variant="Months to near-completion of pass-through", page=13, locator="Table 4")
        add("S108", "PF_EXCHANGE_RATE_PASS_THROUGH", extent, unit="fraction", status="estimated_derived",
            family="Recursive VAR", method="Cumulative impulse response", period=period, frequency="monthly",
            sector=sector, variant="Extent of cumulative pass-through", page=13, locator="Table 4")


# S109 — state- versus time-dependent CPI basket classification.
for year, state, time in [(2024, 83.3, 16.7), (2025, 79.9, 20.1)]:
    add("S109", "PF_STATE_DEPENDENT_ITEM_SHARE", state, unit="percent", status="calculated",
        family="CPI pricing-behavior classification", method="CPI-weighted item classification", period=str(year),
        frequency="annual weights", sector="Consumer prices", variant="Predominantly state-dependent basket share", page=1, locator="Text and footnote")
    add("S109", "PF_TIME_DEPENDENT_ITEM_SHARE", time, unit="percent", status="calculated",
        family="CPI pricing-behavior classification", method="CPI-weighted item classification", period=str(year),
        frequency="annual weights", sector="Consumer prices", variant="Predominantly time-dependent basket share", page=1, locator="Text and footnote")
for group, annual, monthly in [("All CPI", 42.1, ""), ("Time-dependent group", 81.6, 12.8), ("State-dependent group", 33.8, 3.6)]:
    add("S109", "PF_PRICING_GROUP_INFLATION", annual, unit="percent", status="descriptive_statistic",
        family="CPI pricing-behavior classification", method="Annual inflation decomposition", period="2025-01",
        frequency="annual rate", sector=group, variant="Annual price increase", page=4, locator="Chart 4")
    if monthly != "":
        add("S109", "PF_PRICING_GROUP_INFLATION", monthly, unit="percent", status="descriptive_statistic",
            family="CPI pricing-behavior classification", method="Monthly inflation decomposition", period="2025-01",
            frequency="monthly", sector=group, variant="Monthly price increase", page=4, locator="Chart 4")


# S111 — firm responses around policy and inflation announcements.
subgroups = ["All firms", "Large firms", "SMEs", "High leverage", "Low leverage", "Low inflation", "High inflation"]
table2 = {
    "CPI expectations": ([.263, .202, .282, .291, .244, -.062, .329], [.088, .098, .128, .115, .130, .025, .101]),
    "PPI expectations": ([.435, .368, .491, .576, .359, -.094, .492], [.122, .195, .168, .173, .176, .039, .162]),
    "Own price expectations": ([.012, .007, .013, .014, .009, .007, .015], [.006, .004, .006, .007, .005, .009, .005]),
    "Unit-cost expectations": ([.014, .009, .016, .019, .013, .006, .018], [.005, .004, .005, .007, .005, .004, .008]),
}
for outcome, (values, ses) in table2.items():
    for subgroup, value, se in zip(subgroups, values, ses):
        add("S111", "PF_MONETARY_POLICY_NEWS_RESPONSE", value, se=se, unit="regression_coefficient",
            family="Firm-level event study", method="Five-day-window fixed-effects regression", period="2015M1-2024M12",
            frequency="MPC announcements", sector=subgroup, variant=f"Monetary-policy surprise response of {outcome}", page=50, locator="Table 2",
            notes="CPI/PPI outcomes are percentage-point expectations; own-price and unit-cost outcomes use an ordered three-point scale.")
table5 = {
    "CPI expectations": ([.234, .220, .276, .280, .198, .194, .252], [.012, .021, .016, .014, .023, .018, .014]),
    "PPI expectations": ([.344, .336, .371, .374, .329, .204, .379], [.009, .016, .013, .013, .019, .024, .042]),
    "Own price expectations": ([.029, .023, .032, .031, .025, .015, .036], [.014, .007, .008, .006, .006, .006, .019]),
    "Unit-cost expectations": ([.025, .030, .026, .037, .018, .019, .034], [.012, .007, .006, .007, .004, .012, .015]),
}
for outcome, (values, ses) in table5.items():
    for subgroup, value, se in zip(subgroups, values, ses):
        add("S111", "PF_INFLATION_NEWS_RESPONSE", value, se=se, unit="regression_coefficient",
            family="Firm-level event study", method="Five-day-window fixed-effects regression", period="2015M1-2024M12",
            frequency="CPI announcements", sector=subgroup, variant=f"Inflation-surprise response of {outcome}", page=53, locator="Table 5",
            notes="CPI/PPI outcomes are percentage-point expectations; own-price and unit-cost outcomes use an ordered three-point scale.")
for regime, cpi_small, cpi_large, ppi_small, ppi_large in [
    ("All sample", -.197, .311, -.186, .520), ("Low inflation", -.182, .394, -.208, .650),
    ("High inflation", -.129, .498, -.161, .597)]:
    for outcome, size, value in [("CPI expectations", "Small shocks", cpi_small), ("CPI expectations", "Large shocks", cpi_large),
                                 ("PPI expectations", "Small shocks", ppi_small), ("PPI expectations", "Large shocks", ppi_large)]:
        add("S111", "PF_MONETARY_POLICY_NEWS_RESPONSE", value, unit="regression_coefficient",
            family="State-dependent firm event study", method="Median-split shock-size regression", period="2015M1-2024M12",
            frequency="MPC announcements", sector=regime, variant=f"{size}; response of {outcome}", page=52, locator="Table 4")


# S112 — PLS-SEM pricing-pressure paths.
for pid, value, variant in [
    ("PF_PRICING_PRESSURE_DEMAND_EFFECT", .076, "Full sample: domestic-demand optimism → pricing pressure"),
    ("PF_PRICING_PRESSURE_COST_EFFECT", .311, "Full sample: cost perceptions → pricing pressure"),
    ("PF_PRICING_PRESSURE_PROFIT_EFFECT", .010, "Full sample: pricing pressure → perceived profitability")]:
    add("S112", pid, value, unit="standardized_coefficient", family="Partial least squares structural equation model",
        method="PLS-SEM with bootstrap inference", period="2019-01 to 2022-01", frequency="firm interviews",
        sector="RESİM interviewed firms", variant=variant, page=18, locator="Table 4")
periods = [("2019-01 to 2019-06", "Tightening cycle"), ("2019-07 to 2020-09", "Easing cycle"),
           ("2020-10 to 2021-08", "Tightening cycle"), ("2021-09 to 2022-01", "Easing/high-inflation cycle")]
for (period, label), demand, cost in zip(periods, [.047, .090, -.025, .007], [.213, .254, .221, .276]):
    add("S112", "PF_PRICING_PRESSURE_DEMAND_EFFECT", demand, unit="standardized_coefficient",
        family="Partial least squares structural equation model", method="PLS-SEM with bootstrap inference",
        period=period, frequency="firm interviews", sector="RESİM interviewed firms",
        variant=f"{label}: domestic-demand optimism → pricing pressure", page=19, locator="Table 6")
    add("S112", "PF_PRICING_PRESSURE_COST_EFFECT", cost, unit="standardized_coefficient",
        family="Partial least squares structural equation model", method="PLS-SEM with bootstrap inference",
        period=period, frequency="firm interviews", sector="RESİM interviewed firms",
        variant=f"{label}: cost perceptions → pricing pressure", page=19, locator="Table 6")
for (period, label), value in zip(periods, [.008, .011, -.028, -.100]):
    add("S112", "PF_PRICING_PRESSURE_PROFIT_EFFECT", value, unit="standardized_coefficient",
        family="Partial least squares structural equation model", method="PLS-SEM with bootstrap inference",
        period=period, frequency="firm interviews", sector="RESİM interviewed firms",
        variant=f"{label}: pricing pressure → perceived profitability", page=18, locator="Table 5")
add("S112", "PF_GENERAL_OPTIMISM_VARIANCE", 54, unit="percent_of_variance", status="calculated", family="Latent-factor summary",
    method="First principal component", period="2019-01 to 2022-01", frequency="firm interviews",
    sector="RESİM interviewed firms", variant="General optimism first principal component explained variance", page=23, locator="Footnote 7",
    notes="This is not a markup estimate; retained under firm behavior as a documented latent-summary statistic and should be filtered by definition_variant.")


# S113 — matched effects of own price/cost expectations on inflation forecasts.
for pid, treatment, values in [
    ("PF_SALES_PRICE_EXPECTATION_EFFECT", "Expected sales-price increase", [(7.39, .21), (10.35, .26), (3.45, .26), (3.25, .12), (7.12, .21), (3.04, .27)]),
    ("PF_SALES_PRICE_EXPECTATION_EFFECT", "Expected sales-price decrease", [(-.85, .13), (4.51, .55), (-1.02, .47), (-.52, .19), (1.15, .19), (-.85, .29)]),
    ("PF_UNIT_COST_EXPECTATION_EFFECT", "Expected unit-cost increase", [(8.88, .09), (11.25, .21), (4.12, .28), (6.50, .08), (10.01, .21), (4.05, .33)]),
    ("PF_UNIT_COST_EXPECTATION_EFFECT", "Expected unit-cost decrease", [(-1.25, .16), (2.03, .94), (-3.87, .97), (-.19, .09), (1.71, .28), (-2.59, 1.19)]),
]:
    for estimator, offset in [("ATE", 0), ("Propensity-score-matched ATT", 3)]:
        for regime, (value, se) in zip(["Full sample 2009M1-2024M9", "High inflation 2020M1-2024M9", "Disinflation 2023M6-2024M9"], values[offset:offset+3]):
            add("S113", pid, value, se=se, unit="percentage_points", family="Matched firm-expectations design",
                method=estimator, period=regime.split(" ", 2)[-1], frequency="monthly firm survey",
                sector="Manufacturing firms", variant=f"{treatment}; {regime.split(' 20')[0]}; {estimator}",
                page=7 if pid == "PF_SALES_PRICE_EXPECTATION_EFFECT" else 8,
                locator="Table 1" if pid == "PF_SALES_PRICE_EXPECTATION_EFFECT" else "Table 2")


def main() -> None:
    # Update sources and controlled vocabulary idempotently.
    source_fields, sources = read_csv(DATA / "sources.csv")
    new_source_ids = {row[0] for row in source_rows}
    sources = [row for row in sources if row["source_id"] not in new_source_ids]
    sources.extend(source_dict(row) for row in source_rows)
    sources.sort(key=lambda row: int(str(row["source_id"])[1:]))
    write_csv(DATA / "sources_updated.csv", source_fields, sources)

    parameter_fields, parameters = read_csv(DATA / "parameter_dictionary.csv")
    new_parameter_ids = {row[0] for row in parameter_rows}
    parameters = [row for row in parameters if row["parameter_id"] not in new_parameter_ids]
    parameters.extend(parameter_dict(row) for row in parameter_rows)
    write_csv(DATA / "parameter_dictionary_updated.csv", parameter_fields, parameters)

    for idx, row in enumerate(rows, 1):
        row["estimate_id"] = f"PF{idx:04d}"
    write_csv(DATA / "pricing_inflation_firms_estimates.csv", ESTIMATE_FIELDS, rows)

    # Repair S088-S090 integration in the existing capital-investment table.
    capital_path = DATA / "capital_investment_estimates.csv"
    capital_fields, capital = read_csv(capital_path)
    capital = [row for row in capital if row["source_id"] not in {"S088", "S089", "S090"}]
    additions = [
        {"source_id": "S088", "parameter_id": "CI_STOCK_LISTING_INVESTMENT_EFFECT", "value": .283, "standard_error": .124, "unit": "log_points", "estimate_status": "estimated", "model_family": "Firm investment treatment effects", "estimation_method": "Propensity-score matching", "data_period": "2005-2019", "frequency": "annual", "sector": "Manufacturing firms", "definition_variant": "Listing effect on gross tangible assets", "source_pdf_page": 18, "source_locator": "Table 5", "verification_status": "pdf_verified", "notes": "Matched listed-versus-unlisted firms."},
        {"source_id": "S088", "parameter_id": "CI_STOCK_LISTING_INVESTMENT_EFFECT", "value": .441, "standard_error": .151, "unit": "log_points", "estimate_status": "estimated", "model_family": "Firm investment treatment effects", "estimation_method": "Propensity-score matching", "data_period": "2005-2019", "frequency": "annual", "sector": "Manufacturing firms", "definition_variant": "Listing effect on net tangible assets", "source_pdf_page": 18, "source_locator": "Table 5", "verification_status": "pdf_verified", "notes": "Matched listed-versus-unlisted firms."},
        {"source_id": "S088", "parameter_id": "CI_STOCK_LISTING_INVESTMENT_EFFECT", "value": -.551, "unit": "log_points", "estimate_status": "estimated", "model_family": "Firm investment treatment effects", "estimation_method": "Propensity-score matching", "data_period": "2005-2019", "frequency": "annual", "sector": "Non-manufacturing firms", "definition_variant": "Listing effect on gross tangible assets", "source_pdf_page": 18, "source_locator": "Table 5", "verification_status": "pdf_verified", "notes": "Matched listed-versus-unlisted firms; standard error not entered because the extracted table alignment requires visual recheck."},
        {"source_id": "S089", "parameter_id": "CI_INVESTMENT_TO_GDP_RATIO", "value": 20.3, "unit": "percent_of_GDP", "estimate_status": "descriptive_statistic", "model_family": "Investment climate accounting", "estimation_method": "National-accounts average", "data_period": "2012-2014", "frequency": "annual", "sector": "Whole economy", "definition_variant": "Average gross fixed investment to GDP", "source_pdf_page": 17, "source_locator": "Investment overview", "verification_status": "pdf_verified", "notes": "Institutional-report benchmark, not an econometric parameter."},
        {"source_id": "S089", "parameter_id": "CI_DEPRECIATION_RATE", "value": 3.6, "unit": "percent_per_year", "estimate_status": "assumed", "model_family": "Growth-accounting simulation", "estimation_method": "Report assumption", "data_period": "Simulation calibration", "frequency": "annual", "sector": "Aggregate capital", "definition_variant": "Capital depreciation assumption", "source_pdf_page": 75, "source_locator": "Simulation assumptions", "verification_status": "pdf_verified", "notes": "Report calibration rather than a Turkey-data estimate."},
        {"source_id": "S090", "parameter_id": "CI_DEPRECIATION_RATE", "value": .17, "unit": "fraction_per_year", "estimate_status": "assumed", "model_family": "User-cost investment model", "estimation_method": "Perpetual-inventory calibration", "data_period": "1968-2006", "frequency": "annual", "sector": "Private capital stock", "definition_variant": "Annual depreciation rate", "source_pdf_page": 10, "source_locator": "Capital-stock construction", "verification_status": "pdf_verified", "notes": "High annual depreciation assumption used to construct the capital stock."},
        {"source_id": "S090", "parameter_id": "CI_CAPITAL_OUTPUT_ELASTICITY", "value": .78, "standard_error": .00756, "unit": "elasticity", "estimate_status": "estimated", "model_family": "User-cost investment model", "estimation_method": "Cointegrating production relation", "data_period": "1968-2006", "frequency": "annual", "sector": "Private economy", "definition_variant": "Long-run output elasticity with respect to capital", "source_pdf_page": 16, "source_locator": "Estimated production relation", "verification_status": "pdf_verified", "notes": "See source specification before interpreting as a production-function share."},
    ]
    start = max(int(row["estimate_id"][2:]) for row in capital) + 1
    for idx, row in enumerate(additions, start):
        row = {field: row.get(field, "") for field in capital_fields}
        row["estimate_id"] = f"CI{idx:03d}"
        capital.append(row)
    write_csv(DATA / "capital_investment_estimates_updated.csv", capital_fields, capital)

    print(f"sources={len(sources)} parameters={len(parameters)} pricing_rows={len(rows)} capital_rows={len(capital)}")


if __name__ == "__main__":
    main()
