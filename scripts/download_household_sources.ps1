$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$pdfDir = Join-Path $root 'sources\pdfs'
New-Item -ItemType Directory -Force -Path $pdfDir | Out-Null

$downloads = @(
    @{ Name = 'S114_tcmb_wp1310_household_expectations.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/e6438539-025d-4ade-8f84-6a25f27068e9/WP1310.pdf?CACHEID=ROOTWORKSPACE-e6438539-025d-4ade-8f84-6a25f27068e9-m3fw60H&MOD=AJPERES' },
    @{ Name = 'S115_tcmb_wp1109_labor_income_risk.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/57591941-f847-4994-bb3d-b5dc9d30557d/WP1109.pdf?CACHEID=ROOTWORKSPACE-57591941-f847-4994-bb3d-b5dc9d30557d-m3fw5V1&MOD=AJPERES' },
    @{ Name = 'S116_tcmb_wp2015_cohort_mpc.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/02af1d9b-385f-4cd6-b3e4-522b21b01378/wp2015.pdf?MOD=AJPERES' },
    @{ Name = 'S117_tcmb_wp1701_risk_sharing.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/8225af12-8a14-4836-9396-3b4da0be110d/WP1701.pdf?CACHEID=ROOTWORKSPACE-8225af12-8a14-4836-9396-3b4da0be110d-m3fw6jr&MOD=AJPERES' },
    @{ Name = 'S118_tcmb_wp1222_health_risk_saving.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/ad56e85f-1bc0-41fb-97e0-58f3fd031b0e/WP1222.pdf?CACHEID=ROOTWORKSPACE-ad56e85f-1bc0-41fb-97e0-58f3fd031b0e-m3fw5-7&MOD=AJPERES' },
    @{ Name = 'S119_tcmb_wp1714_housing_demand.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/c8b2ed18-9ced-4489-979e-e9bc0e0e4ce4/wp1714.pdf?CACHEID=ROOTWORKSPACE-c8b2ed18-9ced-4489-979e-e9bc0e0e4ce4-m3fw6m5&MOD=AJPERES' },
    @{ Name = 'S120_tcmb_wp1706_homeownership_cohorts.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/1a30c8dc-c938-4258-8025-b239194785b3/wp1706.pdf?CACHEID=ROOTWORKSPACE-1a30c8dc-c938-4258-8025-b239194785b3-m3fw6jq&MOD=AJPERES' },
    @{ Name = 'S121_sbb_erdem_household_saving_2017.pdf'; Url = 'https://www.sbb.gov.tr/wp-content/uploads/2022/08/Turkiyede_Hanehalki_Tasarruflarini_Etkileyen_Faktorler-Betul_Pektas_Erdem.pdf' },
    @{ Name = 'S122_aykac_labor_supply_elasticity_2016.pdf'; Url = 'https://dergipark.org.tr/en/download/article-file/561848' },
    @{ Name = 'S123_telatar_frisch_consumption_2000.pdf'; Url = 'https://file.pide.org.pk/pdf/PDR/2000/Volume3/235-246.pdf' },
    @{ Name = 'S124_alpay_koc_household_demand_2002.pdf'; Url = 'https://erf.org.eg/app/uploads/2017/05/0226.pdf' },
    @{ Name = 'S125_cebi_karaaslan_household_saving_2022.pdf'; Url = 'https://dergipark.org.tr/tr/download/article-file/1637829' },
    @{ Name = 'S126_ceritoglu_eren_demographic_saving_2014.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/fdad7670-1109-4163-b03f-79189672d0dc/Sep14-2.pdf?CACHEID=ROOTWORKSPACE-fdad7670-1109-4163-b03f-79189672d0dc-m3fB70B&MOD=AJPERES' },
    @{ Name = 'S127_aktas_guner_gursel_uysal_saving_2012.pdf'; Url = 'https://betam.bahcesehir.edu.tr/wp-content/uploads/2012/05/WorkingPaper0072.pdf' },
    @{ Name = 'S128_worldbank_domestic_savings_turkey_2011.pdf'; Url = 'https://documents1.worldbank.org/curated/en/367591468172772598/pdf/NonAsciiFileName0.pdf' },
    @{ Name = 'S129_tcmb_wp1304_private_pension_saving.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/b567edab-3ed7-45f0-b1d2-cf4808a7be4d/WP1304.pdf?CACHEID=ROOTWORKSPACE-b567edab-3ed7-45f0-b1d2-cf4808a7be4d-m3fw60I&MOD=AJPERES' },
    @{ Name = 'S130_tcmb_wp1911_demographic_model.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Publications/Research/Working%2BPaperss/2019/19-11' },
    @{ Name = 'S131_tcmb_wp2201_household_finance_survey.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/b404a817-c455-470e-9165-4142fe6f622c/wp2201.pdf?CACHEID=ROOTWORKSPACE-b404a817-c455-470e-9165-4142fe6f622c-o1QgtDP&MOD=AJPERES' }
)

foreach ($download in $downloads) {
    $destination = Join-Path $pdfDir $download.Name
    if (Test-Path -LiteralPath $destination) {
        Write-Host "SKIP $($download.Name)"
        continue
    }
    Write-Host "GET  $($download.Name)"
    Invoke-WebRequest -Uri $download.Url -OutFile $destination -UseBasicParsing
}

