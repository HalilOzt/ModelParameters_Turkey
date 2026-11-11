from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PDF = ROOT / "sources" / "pdfs"

SOURCE_FIELDS = [
    "source_id", "title", "authors", "year", "institution_or_journal", "source_type",
    "language", "url", "doi", "local_pdf", "pdf_pages", "access_status", "scope_status",
    "accessed_date", "notes",
]
PARAM_FIELDS = [
    "parameter_id", "name_en", "name_tr", "canonical_symbol", "default_unit",
    "parameter_class", "definition", "comparison_rule",
]
EST_FIELDS = [
    "estimate_id", "source_id", "parameter_id", "value", "lower_bound", "upper_bound",
    "standard_error", "unit", "estimate_status", "model_family", "estimation_method",
    "data_period", "frequency", "sector", "definition_variant", "source_pdf_page",
    "source_locator", "verification_status", "notes",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})
    tmp.replace(path)


new_sources = [
    ("S114", "Household Expectations and Household Consumption Expenditures: The Case of Turkey", "Evren Ceritoğlu", 2013, "Central Bank of the Republic of Turkey", "Working Paper 13/10", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research/Working%2BPaperss/2013/13-10", "", "S114_tcmb_wp1310_household_expectations.pdf", 24, "Quarterly aggregate consumption GMM estimates, 2004Q1-2012Q3."),
    ("S115", "The Impact of Labour Income Risk on Household Saving Decisions in Turkey", "Evren Ceritoğlu", 2011, "Central Bank of the Republic of Turkey", "Working Paper 11/09", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2011/11-09", "", "S115_tcmb_wp1109_labor_income_risk.pdf", 25, "Pooled HBS precautionary-saving regressions, 2003-2009."),
    ("S116", "Do Household Consumption and Saving Preferences Vary Between Birth-Year Cohorts in Turkey?", "Evren Ceritoğlu", 2020, "Central Bank of the Republic of Turkey", "Working Paper 20/15", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2020/20-15", "", "S116_tcmb_wp2015_cohort_mpc.pdf", 34, "Pseudo-panel marginal propensities to consume by birth cohort and age."),
    ("S117", "Self-Insurance and Consumption Risk-Sharing between Birth-Year Cohorts in Turkey", "Evren Ceritoğlu", 2017, "Central Bank of the Republic of Turkey", "Working Paper 17/01", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2017/17-01", "", "S117_tcmb_wp1701_risk_sharing.pdf", 34, "Pseudo-panel risk-sharing coefficients and welfare gains."),
    ("S118", "Health Expenditures Risk, Purchase of Private Health Insurance, and Precautionary Saving in Turkey", "Evren Ceritoğlu", 2012, "Central Bank of the Republic of Turkey", "Working Paper 12/22", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2012/12-22", "", "S118_tcmb_wp1222_health_risk_saving.pdf", 29, "HBS saving regressions and endogenous health-insurance effects."),
    ("S119", "Home-ownership, Housing Demand and Household Wealth Distribution in Turkey", "Evren Ceritoğlu", 2017, "Central Bank of the Republic of Turkey", "Working Paper 17/14", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2017/17-14", "", "S119_tcmb_wp1714_housing_demand.pdf", 37, "Housing tenure, debt and demand elasticities from household surveys."),
    ("S120", "Disentangling Age and Cohorts Effects on Home-Ownership and Housing Wealth in Turkey", "Evren Ceritoğlu", 2017, "Central Bank of the Republic of Turkey", "Working Paper 17/06", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2017/17-06", "", "S120_tcmb_wp1706_homeownership_cohorts.pdf", 32, "Pseudo-panel cohort effects for homeownership, debt, second homes and housing wealth."),
    ("S121", "Türkiye'de Hanehalkı Tasarruflarını Etkileyen Faktörler", "Betül Pektaş Erdem", 2017, "T.C. Kalkınma Bakanlığı", "Uzmanlık Tezi", "Turkish", "https://www.sbb.gov.tr/wp-content/uploads/2022/08/Turkiyede_Hanehalki_Tasarruflarini_Etkileyen_Faktorler-Betul_Pektas_Erdem.pdf", "", "S121_sbb_erdem_household_saving_2017.pdf", 243, "2SLS household saving-rate determinants, 2004-2013."),
    ("S122", "Labor Supply Elasticity of Turkish Labor Market: 2003-2011", "Gökhan Aykaç", 2016, "Ege Academic Review 16(1):13-29", "Journal article", "English_and_Turkish", "https://dergipark.org.tr/en/pub/eab/issue/39985/475253", "", "S122_aykac_labor_supply_elasticity_2016.pdf", 17, "Pseudo-panel intensive-margin wage elasticity estimated by GMM."),
    ("S123", "Frisch Demand Functions and Intertemporal Behaviour in Consumption: The Turkish Case", "Erdinç Telatar; Funda Telatar; Şadiye Türkmen", 2000, "Pakistan Development Review 39(3):235-246", "Journal article", "English", "https://ideas.repec.org/a/pid/journl/v39y2000i3p235-246.html", "", "S123_telatar_frisch_consumption_2000.pdf", 12, "Frisch demand system and intertemporal substitution, 1988Q1-1999Q2."),
    ("S124", "Household Demand in Turkey: An Application of Almost Ideal Demand System with Spatial Cost Index", "Savaş Alpay; Ali Koç", 2002, "Economic Research Forum", "Working Paper 0226", "English", "https://ideas.repec.org/p/erg/wpaper/0226.html", "", "S124_alpay_koc_household_demand_2002.pdf", 8, "Complete AIDS demand system using the 1994 Household Expenditure Survey."),
    ("S125", "Determinants of Household Saving Behaviour in Turkey", "Kübranur Çebi Karaaslan; Erkan Oktay; Ömer Alkan", 2022, "Sosyoekonomi 30(51):71-90", "Journal article", "English_and_Turkish", "https://dergipark.org.tr/tr/pub/sosyoekonomi/article/896694", "10.17233/sosyoekonomi.2022.01.04", "S125_cebi_karaaslan_household_saving_2022.pdf", 20, "Logit and probit elasticities for household saving probability, 2015-2017."),
    ("S126", "The Effects of Demographic and Social Changes on Household Savings in Turkey", "Evren Ceritoğlu; Okan Eren", 2014, "Central Bank Review 14(3):15-33", "Journal article", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Central%2BBank%2BReview/2014/Volume%2B14-3", "", "S126_ceritoglu_eren_demographic_saving_2014.pdf", 19, "Microsimulation projections of household saving through 2050."),
    ("S127", "Structural Determinants of Household Savings in Turkey: 2003-2008", "Arda Aktaş; Duygu Güner; Seyfettin Gürsel; Gökçe Uysal", 2012, "Bahçeşehir University Center for Economic and Social Research", "BETAM Working Paper 007", "English", "https://betam.bahcesehir.edu.tr/wp-content/uploads/2012/05/WorkingPaper0072.pdf", "", "S127_aktas_guner_gursel_uysal_saving_2012.pdf", 52, "Annual 2SLS saving-rate regressions and income-quintile heterogeneity."),
    ("S128", "Turkey - Sustaining High Growth: The Role of Domestic Savings - Synthesis Report", "World Bank", 2011, "World Bank", "Report 66301-TR", "English", "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/663011468318858985", "", "S128_worldbank_domestic_savings_turkey_2011.pdf", 72, "Synthesis source; overlapping micro estimates are attributed to original papers where possible."),
    ("S129", "Yurtiçi Tasarruflar ve Bireysel Emeklilik Sistemi: Türkiye'deki Uygulamaya İlişkin Bir Değerlendirme", "Özgür Özel; Cihan Yalçın", 2013, "Central Bank of the Republic of Turkey", "Working Paper 13/04", "Turkish", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2013/13-04", "", "S129_tcmb_wp1304_private_pension_saving.pdf", 38, "Cross-country pension-reform estimates and Turkish private-pension scenarios."),
    ("S130", "Demografik Gelişmeler ve Makroekonomik Etkileri", "M. Koray Kalafatcılar", 2019, "Central Bank of the Republic of Turkey", "Working Paper 19/11", "Turkish", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research%2Band%2BMonetary%2BPolicy/Working%2BPapers/2019/19-11", "", "S130_tcmb_wp1911_demographic_model.pdf", 52, "Overlapping-generations general-equilibrium calibration and demographic scenarios."),
    ("S131", "Central Bank of the Republic of Turkey Household Finance and Consumption Survey Methodology", "Gianni Betti; Evren Ceritoğlu; Müşerref Küçükbayrak; Özlem Sevinç", 2022, "Central Bank of the Republic of Turkey", "Working Paper 22/01", "English", "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research/Working%2BPaperss/2022/22-01", "", "S131_tcmb_wp2201_household_finance_survey.pdf", 31, "Methodological source; no structural preference estimate entered."),
]

source_rows = read_csv(DATA / "sources_updated.csv")
source_rows = [r for r in source_rows if r["source_id"] not in {s[0] for s in new_sources}]
for sid, title, authors, year, inst, typ, lang, url, doi, filename, pages, notes in new_sources:
    source_rows.append(dict(zip(SOURCE_FIELDS, [sid, title, authors, year, inst, typ, lang, url, doi,
        f"sources/pdfs/{filename}", pages, "archived", "in_scope", "2026-10-17", notes])))
source_rows.sort(key=lambda r: int(r["source_id"][1:]))


new_params = [
    ("HH_DISCOUNT_FACTOR", "Household discount factor", "Hanehalkı iskonto faktörü", "beta", "fraction", "preferences", "Intertemporal utility discount factor per model period.", "Match model frequency and annualization before comparison."),
    ("HH_TIME_PREFERENCE_RATE", "Time preference rate", "Zaman tercihi oranı", "rho", "fraction", "preferences", "Rate of pure time preference or a source-labelled time-preference parameter.", "Do not mix rates with discount factors without the source's conversion."),
    ("HH_RELATIVE_RISK_AVERSION", "Relative risk aversion", "Göreli riskten kaçınma", "sigma", "coefficient", "preferences", "Curvature of utility with respect to consumption.", "Check whether the source reports risk aversion or its inverse as intertemporal elasticity."),
    ("HH_INTERTEMPORAL_SUBSTITUTION_ELASTICITY", "Intertemporal elasticity of substitution", "Dönemler arası ikame esnekliği", "IES", "elasticity", "preferences", "Aggregate willingness to substitute consumption across time.", "Compare only equal aggregation and utility definitions."),
    ("HH_COMMODITY_INTERTEMPORAL_SUBSTITUTION_ELASTICITY", "Commodity-specific intertemporal substitution elasticity", "Mal grubu özelinde dönemler arası ikame esnekliği", "IES_i", "elasticity", "demand", "Intertemporal substitution elasticity for a commodity group.", "Filter by commodity group."),
    ("HH_INTERTEMPORAL_OWN_PRICE_ELASTICITY", "Intertemporal own-price elasticity", "Dönemler arası öz-fiyat esnekliği", "e_ii", "elasticity", "demand", "Frisch-demand own-price response for a commodity group.", "Do not mix with static Marshallian or Hicksian elasticity."),
    ("HH_HABIT_PERSISTENCE", "External habit persistence", "Dışsal alışkanlık sürekliliği", "h", "fraction", "preferences", "Weight of lagged aggregate consumption in utility.", "Match internal/external habit and model frequency."),
    ("HH_LABOR_SUPPLY_ELASTICITY", "Labor supply wage elasticity", "İşgücü arzının ücret esnekliği", "xi", "elasticity", "labor_supply", "Percentage response of labor supply to a wage change.", "Separate estimated intensive-margin elasticities from DSGE calibrations."),
    ("HH_INVERSE_LABOR_SUPPLY_ELASTICITY", "Inverse labor supply elasticity", "İşgücü arz esnekliğinin tersi", "varphi", "coefficient", "labor_supply", "Curvature parameter governing the inverse Frisch elasticity.", "Do not compare directly with the elasticity without inversion and definition checks."),
    ("HH_LABOR_DISUTILITY_WEIGHT", "Labor disutility weight", "Emek faydasızlığı ağırlığı", "psi", "model_units", "preferences", "Utility weight on hours or disutility of work.", "Model normalization-specific."),
    ("HH_MONEY_UTILITY_WEIGHT", "Money-in-utility weight", "Faydada para ağırlığı", "chi", "model_units", "preferences", "Utility weight on real money balances.", "Model normalization-specific."),
    ("HH_CONSUMPTION_HOME_BIAS", "Domestic-goods weight in consumption", "Tüketimde yerli mal ağırlığı", "omega_c", "fraction", "preferences", "CES weight of domestically produced consumption goods.", "Check whether the complement is the import share."),
    ("HH_CONSUMPTION_IMPORT_SHARE", "Imported-goods weight in consumption", "Tüketimde ithal mal ağırlığı", "1-omega_c", "fraction", "preferences", "CES weight or steady-state share assigned to imported consumption goods.", "Weights and observed expenditure shares are not automatically identical."),
    ("HH_CONSUMPTION_INTRATEMPORAL_SUBSTITUTION", "Intratemporal consumption substitution elasticity", "Tüketimde dönem içi ikame esnekliği", "eta_c", "elasticity", "preferences", "Elasticity between domestic and imported consumption bundles.", "Match the exact nested CES block."),
    ("HH_STEADY_STATE_HOURS_SHARE", "Steady-state hours share", "Durağan durum çalışma süresi payı", "N_ss", "fraction", "labor_supply", "Steady-state hours as a share of available time.", "Targets and estimated values must be separated."),
    ("HH_PREFERENCE_SHOCK_PERSISTENCE", "Preference shock persistence", "Tercih şoku sürekliliği", "rho_b", "fraction", "shocks", "Autoregressive persistence of the consumption preference shock.", "Match model frequency."),
    ("HH_PREFERENCE_SHOCK_VOLATILITY", "Preference shock volatility", "Tercih şoku oynaklığı", "sigma_b", "percent", "shocks", "Innovation standard deviation of the preference shock.", "Check shock scaling and percentage convention."),
    ("HH_LABOR_SUPPLY_SHOCK_PERSISTENCE", "Labor supply shock persistence", "İşgücü arzı şoku sürekliliği", "rho_l", "fraction", "shocks", "Autoregressive persistence of the labor-supply preference shock.", "Match model frequency."),
    ("HH_LABOR_SUPPLY_SHOCK_VOLATILITY", "Labor supply shock volatility", "İşgücü arzı şoku oynaklığı", "sigma_l", "percent", "shocks", "Innovation standard deviation of the labor-supply shock.", "Check shock scaling."),
    ("HH_CONSUMPTION_VARIANCE_SHARE_PREFERENCE_SHOCK", "Consumption variance share of preference shock", "Tercih şokunun tüketim varyansı payı", "VD_c,b", "percent", "shocks", "Forecast-error variance share of consumption attributed to the preference shock.", "Match horizon and identification."),
    ("HH_MPC_CURRENT_INCOME", "Marginal propensity to consume from current income", "Cari gelirden marjinal tüketim eğilimi", "MPC_y", "coefficient", "consumption", "Consumption response to current disposable income in the source's scale.", "Match income and consumption transformation and subgroup."),
    ("HH_MPC_PERMANENT_INCOME", "Marginal propensity to consume from permanent income", "Sürekli gelirden marjinal tüketim eğilimi", "MPC_yp", "coefficient", "consumption", "Consumption response to predicted permanent income.", "Generated-regressor design and age/cohort sample must match."),
    ("HH_CONSUMPTION_INCOME_SENSITIVITY", "Consumption sensitivity to income", "Tüketimin gelire duyarlılığı", "b_y", "regression_coefficient", "consumption", "Regression coefficient linking consumption growth to real disposable income growth.", "Filter by consumption aggregate and specification."),
    ("HH_CONSUMPTION_REAL_RATE_SENSITIVITY", "Consumption sensitivity to real interest rate", "Tüketimin reel faize duyarlılığı", "b_r", "regression_coefficient", "consumption", "Regression coefficient of the real interest rate in consumption growth.", "Not a structural IES unless the model supports that interpretation."),
    ("HH_CONSUMPTION_CREDIT_SENSITIVITY", "Consumption sensitivity to credit", "Tüketimin krediye duyarlılığı", "b_cr", "regression_coefficient", "consumption", "Consumption-growth response to household credit growth.", "Match credit definition and consumption aggregate."),
    ("HH_CONSUMPTION_JOB_EXPECTATIONS_SENSITIVITY", "Consumption sensitivity to job expectations", "Tüketimin iş beklentilerine duyarlılığı", "b_job", "regression_coefficient", "consumption", "Consumption-growth response to an employment-expectations index.", "Index scaling is source-specific."),
    ("HH_CONSUMPTION_FINANCIAL_VARIABLE_SENSITIVITY", "Consumption sensitivity to financial conditions", "Tüketimin finansal koşullara duyarlılığı", "b_f", "regression_coefficient", "consumption", "Coefficient on inflation, confidence, exchange rate, or lending/deposit-rate variables.", "Filter by named regressor and specification."),
    ("HH_RISK_SHARING_AGGREGATE_RESOURCE_COEFFICIENT", "Aggregate-resource risk-sharing coefficient", "Risk paylaşımında toplam kaynak katsayısı", "b_A", "regression_coefficient", "risk_sharing", "Consumption-growth loading on aggregate income or aggregate consumption.", "Filter by aggregate-resource definition, region and age sample."),
    ("HH_RISK_SHARING_COHORT_INCOME_COEFFICIENT", "Cohort-income risk-sharing coefficient", "Risk paylaşımında kohort geliri katsayısı", "b_C", "regression_coefficient", "risk_sharing", "Consumption-growth loading on cohort-specific income growth.", "Lower coefficients imply more cohort-specific risk sharing under the paper's setup."),
    ("HH_PRECAUTIONARY_UNCERTAINTY_COEFFICIENT", "Precautionary-saving uncertainty coefficient", "İhtiyati tasarruf belirsizlik katsayısı", "b_U", "regression_coefficient", "saving", "Saving regression coefficient on an income-risk or uncertainty measure.", "Risk measures and scaling differ across specifications."),
    ("HH_WELFARE_GAIN_INSURANCE", "Welfare gain from complete insurance", "Tam sigortadan refah kazancı", "G", "percent", "risk_sharing", "Permanent-consumption-equivalent welfare gain from eliminating idiosyncratic risk.", "Filter by risk-aversion calibration, region and cohort."),
    ("HH_SAVING_RATE_COEFFICIENT", "Household saving-rate coefficient", "Hanehalkı tasarruf oranı katsayısı", "b_s", "regression_coefficient", "saving", "Coefficient in a household saving-rate regression.", "Regressor, saving definition, method, year and income group must match."),
    ("HH_SAVING_RATE_INCOME_ELASTICITY", "Saving-rate income elasticity", "Tasarruf oranının gelir esnekliği", "e_sy", "elasticity", "saving", "Response of the household saving rate to log income.", "Separate annual and pooled 2SLS estimates and income quintiles."),
    ("HH_SAVING_PROBABILITY_ELASTICITY", "Saving-probability elasticity", "Tasarruf yapma olasılığı esnekliği", "e_Pr(s)", "elasticity", "saving", "Elasticity of the probability that a household saves.", "Logit and probit marginal elasticities are separate variants."),
    ("HH_HEALTH_INSURANCE_SAVING_EFFECT", "Health-insurance effect on saving", "Sağlık sigortasının tasarrufa etkisi", "b_ins", "regression_coefficient", "saving", "Saving-level coefficient for health-insurance status.", "Insurance type, saving definition and endogeneity correction must match."),
    ("HH_HOMEOWNERSHIP_PROBIT_COEFFICIENT", "Homeownership probit coefficient", "Konut sahipliği probit katsayısı", "b_home", "regression_coefficient", "housing", "Probit index coefficient for owning the main residence.", "Not a probability change unless converted to a marginal effect."),
    ("HH_SECOND_HOME_PROBIT_COEFFICIENT", "Second-home ownership coefficient", "İkinci konut sahipliği katsayısı", "b_2home", "regression_coefficient", "housing", "Linear-probability or probit-index coefficient for second-home ownership.", "Match estimator and omitted cohort."),
    ("HH_HOUSING_DEBT_PROBIT_COEFFICIENT", "Housing-debt coefficient", "Konut borcu katsayısı", "b_debt", "regression_coefficient", "housing", "Linear-probability or probit-index coefficient for outstanding housing debt.", "Match estimator and omitted cohort."),
    ("HH_HOUSING_INCOME_ELASTICITY", "Housing-demand income elasticity", "Konut talebi gelir esnekliği", "e_hy", "elasticity", "housing", "Elasticity of housing demand with respect to permanent income.", "Compare homeowners and sample restrictions separately."),
    ("HH_HOUSING_PRICE_ELASTICITY", "Housing-demand price elasticity", "Konut talebi fiyat esnekliği", "e_hp", "elasticity", "housing", "Housing demand response to housing prices.", "Source reports imprecise estimates; preserve uncertainty."),
    ("HH_HOUSING_INTEREST_RATE_ELASTICITY", "Housing-demand interest-rate elasticity", "Konut talebi faiz esnekliği", "e_hr", "elasticity", "housing", "Housing demand response to the real mortgage interest rate.", "Match rate scaling and sample."),
    ("HH_HOUSING_VALUE_COHORT_EFFECT", "Housing-value cohort effect", "Konut değeri kohort etkisi", "gamma_b", "log_points", "housing", "Birth-year cohort coefficient in log home value.", "Compare adjusted and unadjusted home values separately."),
    ("HH_MARSHALLIAN_PRICE_ELASTICITY", "Marshallian price elasticity", "Marshallgil fiyat esnekliği", "eM_ij", "elasticity", "demand", "Uncompensated demand elasticity for a commodity pair.", "Filter by demand good and price good; diagonal is own-price."),
    ("HH_HICKSIAN_PRICE_ELASTICITY", "Hicksian price elasticity", "Hicksgil fiyat esnekliği", "eH_ij", "elasticity", "demand", "Compensated demand elasticity for a commodity pair.", "Filter by demand good and price good; do not mix with Marshallian."),
    ("HH_EXPENDITURE_ELASTICITY", "Expenditure elasticity", "Harcama esnekliği", "e_x", "elasticity", "demand", "Demand response to total household expenditure.", "Filter by commodity and demand-system specification."),
    ("HH_SAVING_RATE_PROJECTED_CHANGE", "Projected saving-rate change", "Projeksiyon tasarruf oranı değişimi", "Delta_s", "percentage_points", "saving", "Projected change in aggregate household saving rate relative to baseline year.", "Projection horizon and scenario are mandatory."),
    ("HH_SAVING_RATE_PROJECTED_LEVEL", "Projected saving-rate level", "Projeksiyon tasarruf oranı seviyesi", "s_T", "percent", "saving", "Projected aggregate household saving rate at the horizon.", "Not an observed realization."),
    ("HH_PENSION_REFORM_SAVING_EFFECT", "Private-pension reform effect on saving rate", "Bireysel emeklilik reformunun tasarruf oranına etkisi", "b_PPS", "percentage_points", "saving", "Cumulative panel-regression effect of pension-system adoption on domestic saving rate.", "Cross-country reform estimate is not a Turkey-only causal estimate."),
    ("HH_PENSION_FUND_ELASTICITY", "Pension-fund accumulation elasticity", "Emeklilik fonu birikim esnekliği", "e_F", "elasticity", "saving", "Elasticity of retirement fund value to a policy or fee parameter.", "Scenario-based elasticity, not econometric estimate."),
    ("HH_LABOR_SUPPLY_MODEL_COEFFICIENT", "Labor-supply model coefficient", "İşgücü arzı modeli katsayısı", "b_L", "regression_coefficient", "labor_supply", "Coefficient in the estimated Lucas-Rapping labor-supply equation.", "Regressor and estimator must match."),
    ("HH_UTILITY_CONSUMPTION_WEIGHT", "Utility weight on consumption", "Faydada tüketim ağırlığı", "xi_1", "fraction", "preferences", "Share parameter on consumption in period utility.", "Model-specific normalization."),
    ("HH_UTILITY_LEISURE_WEIGHT", "Utility weight on leisure", "Faydada boş zaman ağırlığı", "xi_2", "fraction", "preferences", "Share parameter on leisure in period utility.", "Model-specific normalization."),
    ("HH_UTILITY_CURVATURE_PARAMETER", "Utility curvature exponent", "Fayda eğrilik üssü", "rho", "coefficient", "preferences", "Power exponent linked to intertemporal substitution by the source utility specification.", "This exponent is not itself relative risk aversion; use the source relation before transforming it."),
]

param_rows = read_csv(DATA / "parameter_dictionary_updated.csv")
param_rows = [r for r in param_rows if not r["parameter_id"].startswith("HH_")]
param_rows.extend(dict(zip(PARAM_FIELDS, p)) for p in new_params)


est: list[dict[str, object]] = []


def add(source: str, param: str, value: object, *, se: object = "", lb: object = "", ub: object = "",
        unit: str, status: str, family: str, method: str, period: str, frequency: str,
        sector: str, variant: str, page: int, locator: str, notes: str = "") -> None:
    est.append({
        "source_id": source, "parameter_id": param, "value": value, "lower_bound": lb,
        "upper_bound": ub, "standard_error": se, "unit": unit, "estimate_status": status,
        "model_family": family, "estimation_method": method, "data_period": period,
        "frequency": frequency, "sector": sector, "definition_variant": variant,
        "source_pdf_page": page, "source_locator": locator, "verification_status": "pdf_verified",
        "notes": notes,
    })


# Structural preference calibrations and estimated household shocks in existing model sources.
for p, v, unit, status, page, variant, lb, ub in [
    ("HH_DISCOUNT_FACTOR", .9928, "fraction", "calibrated", 37, "Quarterly; targets 3% annual real rate", "", ""),
    ("HH_CONSUMPTION_INTRATEMPORAL_SUBSTITUTION", 1, "elasticity", "external_calibration", 37, "Domestic/imported consumption bundle", "", ""),
    ("HH_LABOR_SUPPLY_ELASTICITY", 1, "elasticity", "external_calibration", 37, "Frisch labor-supply elasticity", "", ""),
    ("HH_CONSUMPTION_IMPORT_SHARE", .25, "fraction", "calibrated", 37, "Imported consumption weight", "", ""),
    ("HH_LABOR_DISUTILITY_WEIGHT", 7, "model_units", "calibrated", 24, "Targets steady-state hours share of 0.30", "", ""),
    ("HH_STEADY_STATE_HOURS_SHARE", .30, "fraction", "calibration_target", 24, "Steady-state time worked", "", ""),
    ("HH_PREFERENCE_SHOCK_PERSISTENCE", .868, "fraction", "estimated", 38, "AR(1), posterior mean", .787, .955),
    ("HH_LABOR_SUPPLY_SHOCK_PERSISTENCE", .800, "fraction", "estimated", 38, "AR(1), posterior mean", .648, .957),
    ("HH_PREFERENCE_SHOCK_VOLATILITY", .414, "percent", "estimated", 39, "Innovation standard deviation", .328, .494),
    ("HH_LABOR_SUPPLY_SHOCK_VOLATILITY", .025, "percent", "estimated", 39, "Innovation standard deviation", .007, .050),
    ("HH_CONSUMPTION_VARIANCE_SHARE_PREFERENCE_SHOCK", 82.04, "percent", "estimated_derived", 39, "Consumption FEVD contribution", "", ""),
]:
    add("S001", p, v, lb=lb, ub=ub, unit=unit, status=status, family="Small-open-economy DSGE", method="Bayesian estimation/calibration", period="2002Q1-2012Q2", frequency="quarterly", sector="Whole economy", variant=variant, page=page, locator="Table 4.1, Table 4.2 or variance decomposition", notes="External calibration is explicitly separated from Turkey-data posterior estimates.")

for p, v, unit, variant in [
    ("HH_DISCOUNT_FACTOR", .9821, "fraction", "Quarterly; targets 7.48% annualized real deposit rate"),
    ("HH_RELATIVE_RISK_AVERSION", 2, "coefficient", "CRRA curvature"),
    ("HH_HABIT_PERSISTENCE", .7, "fraction", "External habit"),
    ("HH_LABOR_SUPPLY_ELASTICITY", 5, "coefficient", "Source labels xi as labor supply elasticity; model text implies an inverse-curvature role"),
    ("HH_LABOR_DISUTILITY_WEIGHT", 4000, "model_units", "Targets hours share 0.33"),
    ("HH_MONEY_UTILITY_WEIGHT", .35, "model_units", "Targets M2/GDP"),
    ("HH_CONSUMPTION_HOME_BIAS", .4, "fraction", "Domestic-goods CES weight"),
    ("HH_CONSUMPTION_IMPORT_SHARE", .6, "fraction", "Complementary imported-goods weight"),
    ("HH_CONSUMPTION_INTRATEMPORAL_SUBSTITUTION", 1, "elasticity", "Domestic/imported consumption bundle"),
]:
    add("S067", p, v, unit=unit, status="calibrated", family="Banking DSGE", method="Calibration", period="2002Q1-2013Q4", frequency="quarterly", sector="Whole economy", variant=variant, page=48, locator="Table 2", notes="The value 5 is preserved under the source label; users should inspect the inverse-elasticity convention before comparison.")

for p, v, unit, variant in [
    ("HH_HABIT_PERSISTENCE", .9, "fraction", "Baseline model"),
    ("HH_HABIT_PERSISTENCE", .8, "fraction", "Alternative model"),
    ("HH_RELATIVE_RISK_AVERSION", 1, "coefficient", "Log-utility / unit curvature"),
    ("HH_INVERSE_LABOR_SUPPLY_ELASTICITY", 2, "coefficient", "Inverse elasticity of work effort"),
    ("HH_DISCOUNT_FACTOR", .985, "fraction", "Baseline quarterly time preference"),
    ("HH_DISCOUNT_FACTOR", .990, "fraction", "Alternative quarterly steady-state value"),
]:
    add("S082", p, v, unit=unit, status="calibrated", family="DSGE with housing", method="Calibration", period="Turkey calibration", frequency="quarterly", sector="Whole economy", variant=variant, page=193, locator="Table 5.2", notes="Baseline and alternative variants are separate rows.")

for p, v, unit, variant in [
    ("HH_DISCOUNT_FACTOR", .99, "fraction", "Quarterly"),
    ("HH_RELATIVE_RISK_AVERSION", 1, "coefficient", "CRRA curvature"),
    ("HH_INVERSE_LABOR_SUPPLY_ELASTICITY", 1, "coefficient", "Inverse Frisch elasticity"),
    ("HH_HABIT_PERSISTENCE", .5, "fraction", "External habit"),
]:
    add("S104", p, v, unit=unit, status="external_calibration", family="New Keynesian DSGE", method="Calibration", period="Model calibration", frequency="quarterly", sector="Whole economy", variant=variant, page=145, locator="Appendix K, Table K1", notes="General calibration in a model for Turkey; not estimated from the paper's micro survey.")


# S114: consumption growth equations.
s114 = {
    "total": [
        {"income": .895}, {"rate": -.002, "income": .867}, {"rate": -.004, "income": .726, "credit": .081},
        {"rate": -.003, "income": .461, "job": .177, "credit": .099}, {"income": .326, "job": .264, "credit": .078}, {"income": .267, "job": .338},
    ],
    "nondurable_goods_and_services": [
        {"income": .476}, {"rate": -.003, "income": .555}, {"rate": -.003, "income": .446, "credit": .050},
        {"rate": .001, "income": .039, "job": .117, "credit": .101}, {"income": .070, "job": .101, "credit": .113}, {"income": .157, "job": .119},
    ],
    "durable_goods": [
        {"income": 1.695}, {"rate": -.006, "income": 1.789}, {"rate": -.002, "income": 1.225, "credit": .158},
        {"rate": .002, "income": .353, "job": .499, "credit": .191}, {"income": .455, "job": .455, "credit": .192}, {"income": .633, "job": .446},
    ],
}
param_map = {"income": "HH_CONSUMPTION_INCOME_SENSITIVITY", "rate": "HH_CONSUMPTION_REAL_RATE_SENSITIVITY", "credit": "HH_CONSUMPTION_CREDIT_SENSITIVITY", "job": "HH_CONSUMPTION_JOB_EXPECTATIONS_SENSITIVITY"}
page_map = {"total": 16, "nondurable_goods_and_services": 18, "durable_goods": 20}
table_map = {"total": "Table 4", "nondurable_goods_and_services": "Table 5", "durable_goods": "Table 6"}
for sector, specs in s114.items():
    for i, vals in enumerate(specs, 1):
        for reg, val in vals.items():
            add("S114", param_map[reg], val, unit="regression_coefficient", status="estimated", family="Aggregate consumption Euler equation", method="GMM", period="2004Q1-2012Q3", frequency="quarterly", sector=sector, variant=f"Specification {i}; regressor={reg}", page=page_map[sector], locator=table_map[sector])


# S115: income and uncertainty coefficients in six variants for each saving definition.
for risk_name, page, table, perm, risk, risk_se in [
    ("LIRI", 19, "Table 5", [.220,.211,.212,.264,.254,.253], [133.3e-6,135.4e-6,119.9e-6,192.4e-6,195.3e-6,193.3e-6], [15.1e-6,15.3e-6,17.4e-6,20.0e-6,19.6e-6,21.9e-6]),
    ("LIRII", 21, "Table 6", [.215,.206,.207,.259,.248,.247], [226.3e-6,229.8e-6,215.7e-6,319.2e-6,323.8e-6,337.5e-6], [25.7e-6,25.7e-6,28.8e-6,33.9e-6,33.6e-6,36.1e-6]),
]:
    for i in range(6):
        saving = "SAVI" if i < 3 else "SAVII"
        add("S115", "HH_MPC_PERMANENT_INCOME", perm[i], se=.010 if risk_name == "LIRII" or i != 0 else .009, unit="regression_coefficient", status="estimated", family="Precautionary saving", method="Pooled OLS; bootstrap SE (1,000 replications)", period="2003-2009", frequency="annual microdata", sector="Households", variant=f"{saving}; specification {(i%3)+1}; permanent income", page=page, locator=table)
        add("S115", "HH_PRECAUTIONARY_UNCERTAINTY_COEFFICIENT", risk[i], se=risk_se[i], unit="regression_coefficient", status="estimated", family="Precautionary saving", method="Pooled OLS; bootstrap SE (1,000 replications)", period="2003-2009", frequency="annual microdata", sector="Households", variant=f"{saving}; {risk_name}; specification {(i%3)+1}", page=page, locator=table, notes="Risk-variable scale is source-specific; source also reports that a 10% risk increase raises saving by 2.2%-3.5% depending on measure.")


# S116: MPC estimates.
for i,(v,se) in enumerate(zip([.891,.833,.900,.835],[.0472,.0481,.0502,.0515]),1):
    add("S116", "HH_MPC_CURRENT_INCOME", v, se=se, unit="coefficient", status="estimated", family="Pseudo-panel consumption", method="Weighted least squares", period="2003-2018", frequency="annual pseudo-panel", sector="Households", variant=f"Current income; sample restriction specification {i}", page=18, locator="Table 4")
for name,v,se in [("old",1.014,.0886),("middle",.804,.0786),("young",.617,.0860)]:
    add("S116", "HH_MPC_CURRENT_INCOME", v, se=se, unit="coefficient", status="estimated", family="Pseudo-panel consumption", method="Weighted least squares", period="2003-2018", frequency="annual pseudo-panel", sector=f"{name} age group", variant="Current disposable income", page=21, locator="Table 6")
for i,(v,se) in enumerate(zip([.800,.674,1.001,.876],[.141,.139,.145,.143]),1):
    add("S116", "HH_MPC_PERMANENT_INCOME", v, se=se, unit="coefficient", status="estimated", family="Pseudo-panel consumption", method="Two-stage generated permanent income", period="2003-2018", frequency="annual pseudo-panel", sector="Households", variant=f"Permanent income; specification {i}", page=23, locator="Table 7")
for name,v in [("consumer_loan_rate",-.00154),("inflation",.0345),("consumer_confidence",-.156),("exchange_rate",-.0438),("deposit_loan_rate",.0223)]:
    add("S116", "HH_CONSUMPTION_FINANCIAL_VARIABLE_SENSITIVITY", v, unit="regression_coefficient", status="estimated", family="Pseudo-panel consumption", method="Weighted least squares", period="2003-2018", frequency="annual pseudo-panel", sector="Households", variant=f"Financial regressor={name}", page=20, locator="Table 5")


# S117: risk-sharing coefficients and welfare gains.
risk_tables = [
    (18,"Table 3","aggregate_income",[.212,.159,.293,.283,.243,.232],[.701,.627,.665,.611,.601,.388],[2.126,1.084,3.851]),
    (20,"Table 4","aggregate_consumption",[.495,.415,.496,.460,.599,.438],[.607,.560,.620,.578,.499,.370],[1.700,.959,3.210]),
    (21,"Table 5","aggregate_income_age_groups",[.300,.331,.0278,.0128,.397,.0958],[.756,.720,.702,.341,.549,.455],[.892,5.427,4.883]),
    (22,"Table 6","aggregate_consumption_age_groups",[.718,.703,.291,.169,.694,.401],[.596,.584,.577,.283,.549,.468],[.648,5.192,3.518]),
]
for page, table, aggdef, aggvals, cohortvals, variancevals in risk_tables:
    groups = ["Turkey","Turkey","Rural","Rural","Urban","Urban"] if "age_groups" not in aggdef else ["Old","Old","Middle","Middle","Young","Young"]
    for i,(av,cv) in enumerate(zip(aggvals,cohortvals),1):
        add("S117", "HH_RISK_SHARING_AGGREGATE_RESOURCE_COEFFICIENT", av, unit="regression_coefficient", status="estimated", family="Pseudo-panel risk sharing", method="Weighted least squares", period="2003-2014", frequency="annual pseudo-panel", sector=groups[i-1], variant=f"{aggdef}; specification {i}", page=page, locator=table)
        add("S117", "HH_RISK_SHARING_COHORT_INCOME_COEFFICIENT", cv, unit="regression_coefficient", status="estimated", family="Pseudo-panel risk sharing", method="Weighted least squares", period="2003-2014", frequency="annual pseudo-panel", sector=groups[i-1], variant=f"cohort_income; {aggdef}; specification {i}", page=page, locator=table)
        if i in (2,4,6):
            add("S117", "HH_PRECAUTIONARY_UNCERTAINTY_COEFFICIENT", variancevals[i//2-1], unit="regression_coefficient", status="estimated", family="Pseudo-panel risk sharing", method="Weighted least squares", period="2003-2014", frequency="annual pseudo-panel", sector=groups[i-1], variant=f"cohort_income_variance; {aggdef}; specification {i}", page=page, locator=table)
welfare = {
    "Turkey": [("all",.53,1.32),("1930-35",.66,1.65),("1935-40",.86,.86),("1940-45",.88,2.19),("1945-50",.75,1.89),("1950-55",.56,1.39),("1955-60",.56,1.41),("1960-65",.51,1.27),("1965-70",.36,.90),("1970-75",.28,.71),("1975-80",.36,.89),("1980-85",.50,1.25)],
    "Rural": [("all",1.01,2.53),("1930-35",.77,1.92),("1935-40",2.05,2.05),("1940-45",1.21,3.02),("1945-50",1.50,3.74),("1950-55",.63,1.58),("1955-60",1.00,2.51),("1960-65",.91,2.28),("1965-70",.69,1.71),("1970-75",.56,1.41),("1975-80",1.04,2.59),("1980-85",1.79,4.48)],
    "Urban": [("all",.45,1.12),("1930-35",.53,1.33),("1935-40",.41,.41),("1940-45",.49,1.23),("1945-50",.50,1.26),("1950-55",.51,1.28),("1955-60",.47,1.19),("1960-65",.44,1.11),("1965-70",.46,1.14),("1970-75",.31,.77),("1975-80",.44,1.10),("1980-85",.78,1.96)],
}
for region, rows in welfare.items():
    for cohort,v2,v5 in rows:
        for rho,v in [(2,v2),(5,v5)]:
            add("S117", "HH_WELFARE_GAIN_INSURANCE", v, unit="percent", status="estimated_derived", family="Risk-sharing welfare calculation", method="Permanent-consumption equivalent", period="2003-2014", frequency="annual pseudo-panel", sector=region, variant=f"birth cohort={cohort}; relative risk aversion={rho}", page=24, locator="Table 7", notes="A few source-table pairs are non-monotone in risk aversion; values are transcribed as printed.")


# S118: saving and health-insurance effects.
ols118 = [("permanent_income",.220,.296),("female",-347.874,-163.981),("age",368.343,452.889),("age_squared",-16.019,-21.353),("compulsory_insurance",160.874,318.688),("voluntary_insurance",52.036,183.383),("green_card",-369.854,-558.305),("homeowner",1069.704,1182.968)]
for reg,v1,v2 in ols118:
    param = "HH_MPC_PERMANENT_INCOME" if reg == "permanent_income" else ("HH_HEALTH_INSURANCE_SAVING_EFFECT" if "insurance" in reg or reg == "green_card" else "HH_SAVING_RATE_COEFFICIENT")
    for sav,v in [("SAVI",v1),("SAVII",v2)]:
        add("S118", param, v, unit="regression_coefficient", status="estimated", family="Health risk and precautionary saving", method="Pooled OLS", period="2003-2010", frequency="annual microdata", sector="Households", variant=f"{sav}; regressor={reg}", page=21, locator="Table 5")
for sav, insvals, incvals, page in [
    ("SAVI", [135.237,-507.220,-205.761,-152.041],[.231,.229,.214,.238],23),
    ("SAVII", [188.794,-708.092,-287.248,-212.253],[.305,.301,.281,.315],25),
]:
    for ins,v,inc in zip(["compulsory","voluntary","green_card","no_insurance"],insvals,incvals):
        add("S118", "HH_HEALTH_INSURANCE_SAVING_EFFECT", v, unit="regression_coefficient", status="estimated", family="Health risk and precautionary saving", method="Two-stage predictor substitution", period="2003-2010", frequency="annual microdata", sector="Households", variant=f"{sav}; endogenous insurance={ins}", page=page, locator="Table 6" if sav=="SAVI" else "Table 7")
        add("S118", "HH_MPC_PERMANENT_INCOME", inc, unit="regression_coefficient", status="estimated", family="Health risk and precautionary saving", method="Two-stage predictor substitution", period="2003-2010", frequency="annual microdata", sector="Households", variant=f"{sav}; insurance equation={ins}", page=page, locator="Table 6" if sav=="SAVI" else "Table 7")


# S119: housing-demand elasticities.
for i,(inc,incse) in enumerate(zip([.243,.243,.243],[.0523,.0494,.0492]),1):
    add("S119", "HH_HOUSING_INCOME_ELASTICITY", inc, se=incse, unit="elasticity", status="estimated", family="Housing demand", method="Heckman two-step", period="2003-2014", frequency="annual microdata", sector="Homeowners", variant=f"Permanent income; specification {i}", page=30, locator="Table 5")
for i,(v,se) in enumerate([(-.289,.346),(-.353,.426)],2):
    add("S119", "HH_HOUSING_PRICE_ELASTICITY", v, se=se, unit="elasticity", status="estimated", family="Housing demand", method="Heckman two-step", period="2003-2014", frequency="annual microdata", sector="Homeowners", variant=f"Housing price; specification {i}", page=30, locator="Table 5", notes="Estimate is statistically imprecise in the source table.")
add("S119", "HH_HOUSING_INTEREST_RATE_ELASTICITY", -.0128, se=.0597, unit="elasticity", status="estimated", family="Housing demand", method="Heckman two-step", period="2003-2014", frequency="annual microdata", sector="Homeowners", variant="Real mortgage interest rate; specification 3", page=30, locator="Table 5")
add("S119", "HH_HOUSING_INCOME_ELASTICITY", .25, unit="elasticity", status="estimated_robustness", family="Housing demand", method="Heckman two-step", period="2003-2014", frequency="annual microdata", sector="All homeowners", variant="Robustness sample", page=31, locator="Robustness text")
add("S119", "HH_HOUSING_INTEREST_RATE_ELASTICITY", -.024, unit="elasticity", status="estimated_robustness", family="Housing demand", method="Heckman two-step", period="2003-2014", frequency="annual microdata", sector="All homeowners", variant="Robustness sample", page=31, locator="Robustness text", notes="Reported significant at 5% in text.")


# S120: complete cohort profiles for tenure, debt and housing wealth.
cohort_vals = [
    (1946,-.029,.016,.014,.009,.003,.008),(1947,-.055,.017,.003,.009,-.001,.008),(1948,-.050,.017,.035,.009,.012,.008),(1949,-.065,.017,.035,.009,.009,.008),(1950,-.058,.018,.030,.010,.012,.008),(1951,-.070,.018,.034,.010,.020,.008),(1952,-.080,.018,.035,.010,.032,.009),(1953,-.093,.019,.022,.010,.030,.009),(1954,-.112,.019,.033,.010,.025,.009),(1955,-.100,.020,.041,.011,.038,.009),(1956,-.122,.020,.042,.011,.044,.009),(1957,-.146,.021,.043,.011,.050,.010),(1958,-.161,.021,.056,.012,.047,.010),(1959,-.167,.022,.046,.012,.064,.010),(1960,-.174,.023,.049,.012,.074,.010),(1961,-.204,.023,.050,.012,.086,.011),(1962,-.203,.024,.050,.013,.093,.011),(1963,-.244,.024,.048,.013,.095,.011),(1964,-.237,.025,.050,.013,.105,.012),(1965,-.263,.025,.052,.014,.113,.012),(1966,-.276,.026,.046,.014,.116,.012),(1967,-.284,.027,.050,.014,.144,.012),(1968,-.304,.027,.052,.015,.129,.013),(1969,-.352,.028,.048,.015,.148,.013),(1970,-.360,.028,.058,.015,.146,.013),(1971,-.393,.029,.056,.016,.164,.014),(1972,-.407,.030,.052,.016,.173,.014),(1973,-.424,.030,.050,.016,.184,.014),(1974,-.465,.031,.056,.017,.182,.014),(1975,-.461,.032,.052,.017,.208,.015),
]
for year,h,se_h,s,se_s,d,se_d in cohort_vals:
    for param,v,se,kind in [("HH_HOMEOWNERSHIP_PROBIT_COEFFICIENT",h,se_h,"homeowner"),("HH_SECOND_HOME_PROBIT_COEFFICIENT",s,se_s,"second_home"),("HH_HOUSING_DEBT_PROBIT_COEFFICIENT",d,se_d,"housing_debt")]:
        add("S120", param, v, se=se, unit="regression_coefficient", status="estimated", family="Cohort housing profile", method="Pseudo-panel linear probability regression", period="2003-2014", frequency="annual pseudo-panel", sector="Households", variant=f"birth year={year}; omitted cohort=1945; outcome={kind}", page=13, locator="Table 2")
wealth = [
    (1946,.062,.010),(1947,.028,.039),(1948,.099,.047),(1949,.153,.057),(1950,.181,.086),(1951,.290,.105),(1952,.326,.122),(1953,.357,.143),(1954,.439,.170),(1955,.484,.173),(1956,.519,.206),(1957,.578,.224),(1958,.669,.248),(1959,.742,.269),(1960,.778,.282),(1961,.840,.310),(1962,.875,.347),(1963,.907,.355),(1964,.973,.377),(1965,1.060,.411),(1966,1.113,.437),(1967,1.153,.466),(1968,1.244,.471),(1969,1.256,.510),(1970,1.324,.526),(1971,1.416,.555),(1972,1.458,.601),(1973,1.542,.613),(1974,1.548,.636),(1975,1.688,.670),
]
for year,unadj,adj in wealth:
    for v,kind in [(unadj,"unadjusted home value"),(adj,"quality-adjusted home value")]:
        add("S120", "HH_HOUSING_VALUE_COHORT_EFFECT", v, unit="log_points", status="estimated", family="Cohort housing wealth", method="Random-effects pseudo-panel regression", period="2003-2014", frequency="annual pseudo-panel", sector="Homeowners", variant=f"birth year={year}; omitted cohort=1945; {kind}", page=21, locator="Table 4")
for reg,v,se in [("age",.070,.005),("age_squared",-.0004,0),("female",-.182,.025),("income_q2",.207,.016),("income_q3",.309,.016),("income_q4",.506,.018),("income_q5",.710,.020),("extended_family",.074,.021),("single_parent",-.249,.030)]:
    add("S120", "HH_HOMEOWNERSHIP_PROBIT_COEFFICIENT", v, se=se, unit="regression_coefficient", status="estimated", family="Housing selection and quality", method="Probit", period="2003-2014", frequency="annual microdata", sector="Households", variant=f"regressor={reg}", page=19, locator="Table 3")


# S121: national and quintile-specific 2SLS saving-rate coefficients.
overall121 = {"log_real_income":.159,"consumer_credit_gdp":-.017,"unemployed_head":-.019,"working_women_share":.100,"urban":-.032,"public_health_insurance":-.003,"young_dependency":-.083,"old_dependency":.121,"education_years":-.007,"interest_income":.019,"first_home":.021,"second_home":-.009,"land":-.018,"hot_water_low_income":-.165}
for reg,v in overall121.items():
    param = "HH_SAVING_RATE_INCOME_ELASTICITY" if reg=="log_real_income" else "HH_SAVING_RATE_COEFFICIENT"
    add("S121", param, v, unit="elasticity" if reg=="log_real_income" else "regression_coefficient", status="estimated", family="Household saving rate", method="2SLS", period="2004-2013", frequency="annual microdata", sector="Households", variant=f"pooled; regressor={reg}", page=142, locator="Table 4.2")
qvals121 = {
    "log_real_income":[.425,.260,.291,.295,.239],"consumer_credit_gdp":[-.048,-.019,-.023,-.027,-.013],"unemployed_head":[.027,.029,.040,-.007,.021],"working_women_share":[.023,.090,.135,.102,.081],"urban":[-.039,-.044,-.056,-.074,-.093],"public_health_insurance":[.006,.006,-.005,-.025,-.012],"young_dependency":[-.192,-.067,-.059,-.078,-.097],"old_dependency":[.182,.101,.097,.093,.056],"education_years":[-.033,-.014,-.014,-.012,-.014],"interest_income":[-.051,-.065,-.004,-.018,-.004],"first_home":[.007,-.004,.003,-.004,-.019],"second_home":[-.101,-.040,-.020,-.042,-.037],"land":[-.031,-.042,-.067,-.039,-.022],
}
for reg,vals in qvals121.items():
    for q,v in enumerate(vals,1):
        param = "HH_SAVING_RATE_INCOME_ELASTICITY" if reg=="log_real_income" else "HH_SAVING_RATE_COEFFICIENT"
        add("S121", param, v, unit="elasticity" if reg=="log_real_income" else "regression_coefficient", status="estimated", family="Household saving rate", method="2SLS", period="2004-2013", frequency="annual microdata", sector=f"Income quintile {q}", variant=f"regressor={reg}", page=148 if q<=3 else 149, locator="Table 4.3")


# S122: labor-supply equation.
for method, vals, ses in [
    ("Difference GMM",[.094,.118,.210,.118],["",.008,.041,.030]),
    ("System GMM",[.059,.086,.196,.221],[.012,.014,.069,.022]),
    ("OLS",[.019,-.033,.015,.559],["",.028,.023,.055]),
]:
    for reg,v,se in zip(["current_log_wage_real_income_ratio","lagged_log_wage_real_income_ratio","inflation_proxy","lagged_nonwage_income_ratio"],vals,ses):
        param = "HH_LABOR_SUPPLY_ELASTICITY" if reg=="current_log_wage_real_income_ratio" else "HH_LABOR_SUPPLY_MODEL_COEFFICIENT"
        add("S122", param, v, se=se, unit="elasticity" if param=="HH_LABOR_SUPPLY_ELASTICITY" else "regression_coefficient", status="estimated", family="Lucas-Rapping aggregate labor supply", method=method, period="2003-2011", frequency="annual pseudo-panel", sector="Households; intensive margin", variant=f"regressor={reg}", page=10, locator="Table 4")


# S123: Frisch demand elasticities.
for good,exp,ies,own in zip(["food","semi_and_nondurables","energy_transport_communication","services","dwelling"],[1.256,.525,.360,2.261,.227],[.060,.025,.017,.109,.011],[-.304,-.754,-.086,-.843,-.114]):
    add("S123", "HH_EXPENDITURE_ELASTICITY", exp, unit="elasticity", status="estimated", family="Frisch demand system", method="Full-information maximum likelihood", period="1988Q1-1999Q2", frequency="quarterly", sector=good, variant="Expenditure elasticity", page=8, locator="Elasticity results")
    add("S123", "HH_COMMODITY_INTERTEMPORAL_SUBSTITUTION_ELASTICITY", ies, unit="elasticity", status="estimated", family="Frisch demand system", method="Full-information maximum likelihood", period="1988Q1-1999Q2", frequency="quarterly", sector=good, variant="Commodity-specific IES", page=8, locator="Elasticity results")
    add("S123", "HH_INTERTEMPORAL_OWN_PRICE_ELASTICITY", own, unit="elasticity", status="estimated", family="Frisch demand system", method="Full-information maximum likelihood", period="1988Q1-1999Q2", frequency="quarterly", sector=good, variant="Intertemporal own-price elasticity", page=8, locator="Elasticity results")
add("S123", "HH_INTERTEMPORAL_SUBSTITUTION_ELASTICITY", .048, unit="elasticity", status="estimated", family="Frisch demand system", method="Full-information maximum likelihood", period="1988Q1-1999Q2", frequency="quarterly", sector="Aggregate consumption", variant="Aggregate IES", page=8, locator="Elasticity results")


# S124: complete 10x10 Marshallian and Hicksian demand matrices plus expenditure elasticities.
goods = ["food","clothing","housing","furniture","health","transport","energy","education","tourism","other"]
marshall = [
[-.71,0,.09,-.04,-.01,-.07,.02,.05,-.04,.15],[-.21,-.98,-.12,.02,-.02,.10,.01,-.03,.04,.01],[.02,-.02,-.74,-.04,-.01,-.03,-.01,-.03,.03,-.04],[-.59,-.01,-.32,-.84,-.04,.30,-.03,-.04,-.06,-.01],[-.14,-.03,-.06,-.05,-1.33,.46,-.14,.42,-.24,.37],[-.87,.06,-.35,.31,.11,-.25,-.16,-.20,.15,-.73],[-.16,-.02,-.34,-.12,.03,-.54,-.39,.13,.01,-.30],[.79,-.27,-.79,-.21,.59,-.96,.19,-1.24,.17,-.19],[-.76,.15,.26,-.14,-.24,.47,.02,.11,-1.07,.10],[.63,-.02,-.36,0,.12,-.93,-.11,-.04,.03,-.84],
]
hicks = [
[-.51,.06,.23,0,.01,-.03,.03,.06,-.03,.18],[.23,-.87,.17,.12,0,.19,.03,-.01,.07,.07],[.34,.06,-.53,.03,.01,.04,.01,-.02,.06,0],[.01,.14,.08,-.71,0,.42,0,-.01,-.01,.08],[.11,.02,.10,-.01,-1.33,.49,.07,.41,-.25,.39],[-.17,.24,.13,.47,.15,-.11,-.12,-.17,.20,-.62],[.46,.14,.08,.01,.07,-.41,-.35,.16,.05,-.21],[1.49,-.10,-.31,-.05,.63,-.82,.23,-1.21,.22,-.08],[-.36,.26,.53,-.05,-.21,.55,.04,.13,-1.05,.16],[1.18,.12,.01,.12,.16,-.82,-.08,-.02,.07,-.76],
]
for matrix,param,page,table in [(marshall,"HH_MARSHALLIAN_PRICE_ELASTICITY",6,"Table 3"),(hicks,"HH_HICKSIAN_PRICE_ELASTICITY",7,"Table 4")]:
    for i,demand_good in enumerate(goods):
        for j,price_good in enumerate(goods):
            add("S124", param, matrix[i][j], unit="elasticity", status="estimated", family="Almost Ideal Demand System", method="Iterated seemingly unrelated regression", period="1994", frequency="cross-section", sector=demand_good, variant=f"price good={price_good}; {'own-price' if i==j else 'cross-price'}", page=page, locator=table)
for good,v in zip(goods,[.56,1.20,.87,1.64,.74,1.94,1.70,1.94,1.10,1.52]):
    add("S124", "HH_EXPENDITURE_ELASTICITY", v, unit="elasticity", status="estimated", family="Almost Ideal Demand System", method="Iterated seemingly unrelated regression", period="1994", frequency="cross-section", sector=good, variant="Total expenditure", page=8, locator="Table 5")


# S125: published logit/probit elasticities for selected household characteristics.
s125 = {
    "female":(-.143,-.160),"age_35_44":(-.131,-.130),"age_45_54":(-.250,-.276),"age_55_64":(-.185,-.200),"household_size_1":(.582,.640),"household_size_2":(.227,.257),"household_size_6_plus":(-.377,-.441),"tenant":(-.334,-.378),"second_home":(.209,.246),"private_insurance":(.351,.407),"credit_card":(-.149,-.156),"income_q2":(.671,.737),"income_q3":(1.229,1.321),"income_q4":(1.601,1.705),"income_q5":(2.114,2.231),"car":(.226,.248),"primary_education":(.257,.279),"secondary_education":(.311,.337),"high_school":(.262,.288),"university":(.286,.316),"apartment":(-.078,-.079),"central_heating":(.182,.201),"boiler":(.326,.357),"advanced_heating_fuel":(-.222,-.255),"advanced_hot_water_fuel":(-.194,-.199),"house_size_61_90":(.150,.159),"house_size_91_120":(.231,.253),"house_size_121_150":(.196,.205),"house_size_150_plus":(.257,.279),"smoking":(-.279,-.318),"eating_out":(.136,.149),"cinema":(.143,.170),"market":(.067,.079),"year_2016":(.167,.181),"year_2017":(.267,.296),
}
for reg,(lv,pv) in s125.items():
    page = 15 if reg in list(s125)[:20] else 17
    for method,v in [("Logit",lv),("Probit",pv)]:
        add("S125", "HH_SAVING_PROBABILITY_ELASTICITY", v, unit="elasticity", status="estimated", family="Household saving participation", method=method, period="2015-2017", frequency="annual microdata", sector="Households", variant=f"regressor={reg}", page=page, locator="Table 6" if page==15 else "Table 7")


# S126: demographic and social saving projections.
projections126 = [
    ("HH_SAVING_RATE_PROJECTED_CHANGE",1.17,"percentage_points","demography_only; 2010-2025"),("HH_SAVING_RATE_PROJECTED_CHANGE",2.21,"percentage_points","demography_only; 2010-2050"),("HH_SAVING_RATE_PROJECTED_LEVEL",11.24,"percent","demography_only; 2050 level"),("HH_SAVING_RATE_PROJECTED_CHANGE",.05,"percentage_points","urbanization incremental effect; 2050"),("HH_SAVING_RATE_PROJECTED_CHANGE",3.60,"percentage_points","demography+labor_force_participation+college; 2010-2025"),("HH_SAVING_RATE_PROJECTED_CHANGE",7.61,"percentage_points","demography+labor_force_participation+college; 2010-2050"),("HH_SAVING_RATE_PROJECTED_LEVEL",17.72,"percent","demography+labor_force_participation+college; 2050 level"),("HH_SAVING_RATE_PROJECTED_CHANGE",1.91,"percentage_points","component=demography; 2010-2050"),("HH_SAVING_RATE_PROJECTED_CHANGE",1.45,"percentage_points","component=labor_force_participation; 2010-2050"),("HH_SAVING_RATE_PROJECTED_CHANGE",4.59,"percentage_points","component=college_attainment; 2010-2050"),("HH_SAVING_RATE_PROJECTED_CHANGE",-.35,"percentage_points","component=cross_effect; 2010-2050"),("HH_SAVING_RATE_PROJECTED_CHANGE",.96,"percentage_points","frozen LFP and college; 2010-2025"),("HH_SAVING_RATE_PROJECTED_CHANGE",1.91,"percentage_points","frozen LFP and college; 2010-2050"),("HH_SAVING_RATE_PROJECTED_LEVEL",12.02,"percent","frozen LFP and college; 2050 level"),("HH_SAVING_RATE_PROJECTED_CHANGE",6.60,"percentage_points","robustness using 2003 HBS; 2010-2050"),("HH_SAVING_RATE_PROJECTED_CHANGE",10.32,"percentage_points","robustness using 2010 HBS; 2010-2050"),
]
for param,v,unit,variant in projections126:
    if variant.startswith("demography_only") or variant.startswith("urbanization"):
        source_page = 12
    elif variant.startswith("robustness") or variant.startswith("frozen") or variant.startswith("component=cross"):
        source_page = 16
    else:
        source_page = 15
    add("S126", param, v, unit=unit, status="forecast_contribution", family="Microsimulation saving projection", method="Coefficient-based demographic projection", period="2010-2050", frequency="projection horizon", sector="Households", variant=variant, page=source_page, locator="Projection results", notes="Projection, not an observed realization.")


# S127: annual 2SLS saving-rate results and pooled income-quintile heterogeneity.
annual127 = {
    "log_income":[.026,.116,.147,.031,.061,.065],"dependent_children":[-.020,-.015,-.019,-.011,-.016,-.022],"dependent_elderly":[.036,.043,.010,-.005,.045,.040],"working_female_share":[.051,.026,.005,.035,.026,.045],"homeowner":[.085,.049,.042,.070,.051,.154],"second_home":[.024,.028,.021,.038,.052,.048],"government_employee":[.043,.062,.086,.047,.089,.114],"entrepreneur":[.166,.159,.128,.141,.134,.105],"unemployed_head":[-.128,-.070,.015,-.074,-.088,-.073],"informal_worker":[-.063,-.050,-.044,-.030,-.029,-.054],"pension_income_share":[-.075,-.055,-.065,-.110,-.080,-.112],
}
for reg,vals in annual127.items():
    for year,v in zip(range(2003,2009),vals):
        param = "HH_SAVING_RATE_INCOME_ELASTICITY" if reg=="log_income" else "HH_SAVING_RATE_COEFFICIENT"
        add("S127", param, v, unit="elasticity" if reg=="log_income" else "regression_coefficient", status="estimated", family="Household saving rate", method="2SLS", period=str(year), frequency="annual microdata", sector="Households", variant=f"saving definition S2; regressor={reg}", page=21 if reg in list(annual127)[:4] else 22, locator="Table 4")
for q,v,se in zip(["pooled","Q1","Q2","Q3","Q4","Q5"],[.065,.166,.175,.160,.117,.028],[.010,.038,.030,.025,.020,.026]):
    add("S127", "HH_SAVING_RATE_INCOME_ELASTICITY", v, se=se, unit="elasticity", status="estimated", family="Household saving rate", method="2SLS", period="2003-2008", frequency="annual microdata", sector=f"Income group {q}", variant="saving definition S2; log income", page=33, locator="Table 8")


# S129: dynamic reform effect and pension-fund scenario elasticities.
for method,vals in [("Fixed effects",[.412,.710,.823,.965,.961,1.391,1.450]),("System GMM",[.399,.701,.817,.965,.973,1.423,1.474])]:
    for lag,v in enumerate(vals,1):
        add("S129", "HH_PENSION_REFORM_SAVING_EFFECT", v, unit="percentage_points", status="estimated", family="Cross-country domestic saving panel", method=method, period="1980-2010", frequency="annual panel", sector="16 emerging economies including Turkey", variant=f"Cumulative private-pension reform effect through lag {lag}", page=13 if method=="Fixed effects" else 14, locator="Table 2" if method=="Fixed effects" else "Table 3", notes="Predominantly mandatory reforms; not a Turkey-only causal estimate.")
for reg,v in [("government_contribution_rate",.29),("fund_management_fee",-.31),("administrative_fee",-.03)]:
    add("S129", "HH_PENSION_FUND_ELASTICITY", v, unit="elasticity", status="scenario_calculation", family="Turkish private-pension accumulation scenario", method="Deterministic accumulation simulation", period="2012 reform scenario", frequency="retirement horizon", sector="Representative participant", variant=f"retirement fund with respect to {reg}", page=26, locator="Table 13")


# S130: OLG household calibration and endogenous steady-state MPCs.
for p,v,unit,variant in [
    ("HH_UTILITY_CONSUMPTION_WEIGHT",2/3,"fraction","Consumption preference weight"),("HH_UTILITY_LEISURE_WEIGHT",1/3,"fraction","Leisure preference weight"),("HH_INTERTEMPORAL_SUBSTITUTION_ELASTICITY",.5,"elasticity","Period utility"),("HH_UTILITY_CURVATURE_PARAMETER",-1,"coefficient","Source relation sigma=(1-rho)^-1 implies rho=-1"),("HH_DISCOUNT_FACTOR",.99,"fraction","Quarterly individual discount factor"),
]:
    add("S130", p, v, unit=unit, status="calibrated", family="Overlapping-generations general equilibrium", method="Calibration", period="Initial steady state", frequency="quarterly", sector="Whole economy", variant=variant, page=48, locator="Appendix Table A3")
for group,v in [("retirees",.025),("workers",.018)]:
    add("S130", "HH_MPC_CURRENT_INCOME", v, unit="fraction", status="model_implied", family="Overlapping-generations general equilibrium", method="Steady-state solution", period="Initial steady state", frequency="quarterly", sector=group, variant="Endogenous marginal propensity to consume", page=34, locator="Table 6.1")


for i,row in enumerate(est,1):
    row["estimate_id"] = f"HH{i:04d}"

write_csv(DATA / "sources_updated.csv", SOURCE_FIELDS, source_rows)
write_csv(DATA / "parameter_dictionary_updated.csv", PARAM_FIELDS, param_rows)
write_csv(DATA / "household_preferences_estimates.csv", EST_FIELDS, est)

print(f"sources={len(source_rows)} parameters={len(param_rows)} household_estimates={len(est)}")
