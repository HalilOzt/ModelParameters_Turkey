$ErrorActionPreference = 'Stop'

$targets = @(
    @{ File = 'S091_ozmen_sevinc_price_rigidity_2011.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/07c51662-caea-41af-bee9-a9ef60fd7596/WP1125.pdf?CACHEID=ROOTWORKSPACE-07c51662-caea-41af-bee9-a9ef60fd7596-m3fw5XZ&MOD=AJPERES' },
    @{ File = 'S092_ozcan_kodaz_yurek_state_dependent_pricing_2023.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/fb377e85-e195-41e1-8030-b503cd6de850/wp23_04.pdf?CACHEID=ROOTWORKSPACE-fb377e85-e195-41e1-8030-b503cd6de850-oJ2vfaB&MOD=AJPERES' },
    @{ File = 'S093_ogunc_ozel_nonlinear_erpt_2025.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/25d56e1a-e054-4c1f-8ffc-39dbc40cc7e2/wp2505.pdf?CACHEID=ROOTWORKSPACE-25d56e1a-e054-4c1f-8ffc-39dbc40cc7e2-pnS6qBF&MOD=AJPERES' },
    @{ File = 'S094_akgunduz_bastan_demiroglu_tumen_product_erpt_2019.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/2e42fc55-7edd-4935-975f-986bbd0629c0/wp1922.pdf?CACHEID=ROOTWORKSPACE-2e42fc55-7edd-4935-975f-986bbd0629c0-mOP-g59&MOD=AJPERES' },
    @{ File = 'S095_ozmen_topaloglu_disaggregated_erpt_2017.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/27b188b3-6cac-428d-af91-382bbe32b02e/wp1708.pdf?CACHEID=ROOTWORKSPACE-27b188b3-6cac-428d-af91-382bbe32b02e-m3fw6m6&MOD=AJPERES' },
    @{ File = 'S096_ertug_ozlu_ozmen_yunculer_imported_inputs_2020.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/f1f1e78b-9d9b-4bc0-85b9-75ff8b55cbe9/wp2003.pdf?CACHEID=ROOTWORKSPACE-f1f1e78b-9d9b-4bc0-85b9-75ff8b55cbe9-n0pGiEG&MOD=AJPERES' },
    @{ File = 'S097_fendoglu_colak_hacihasanoglu_fx_debt_erpt_2019.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/85ec72ff-4e7b-4243-be6b-cacc9f623dd0/wp1924.pdf?CACHEID=ROOTWORKSPACE-85ec72ff-4e7b-4243-be6b-cacc9f623dd0-mPiXTUS&MOD=AJPERES' },
    @{ File = 'S098_ogunc_ozmen_sarikaya_bvar_inflation_2018.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/16c5f7e9-3797-4ffe-912e-2ee47778082b/wp1810.pdf?CACHEID=ROOTWORKSPACE-16c5f7e9-3797-4ffe-912e-2ee47778082b-mi3kBkU&MOD=AJPERES' },
    @{ File = 'S099_atuk_aysoy_ozmen_sarikaya_business_cycles_2014.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/c4b1a5bf-8d61-4d09-8340-aa476585deb0/1437.pdf?CACHEID=ROOTWORKSPACE-c4b1a5bf-8d61-4d09-8340-aa476585deb0-m3fw6bo&MOD=AJPERES' },
    @{ File = 'S100_arslaner_karaman_arslaner_kal_erpt_2014.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/8107c582-7d02-49d7-be3a-be66ad0677e0/WP1416.pdf?CACHEID=ROOTWORKSPACE-8107c582-7d02-49d7-be3a-be66ad0677e0-m3fw68k&MOD=AJPERES' },
    @{ File = 'S101_saygili_invoicing_erpt_2019.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/f61a971d-f7f7-4ff8-8c26-41d2bffd3fef/wp1917.pdf?CACHEID=ROOTWORKSPACE-f61a971d-f7f7-4ff8-8c26-41d2bffd3fef-mNSIOR3&MOD=AJPERES' },
    @{ File = 'S102_andic_kucuk_ogunc_domestic_cost_2014.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/9ab7f9e4-cfda-4d51-8eca-ba1f28f3dca4/WP1420.pdf?CACHEID=ROOTWORKSPACE-9ab7f9e4-cfda-4d51-8eca-ba1f28f3dca4-m3fw68i&MOD=AJPERES' },
    @{ File = 'S103_koc_ogunc_ozmen_inflation_expectations_2021.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/e36fb1c7-6f8f-4601-9414-15b36f484545/wp2102.pdf?CACHEID=ROOTWORKSPACE-e36fb1c7-6f8f-4601-9414-15b36f484545-nuck12E&MOD=AJPERES' },
    @{ File = 'S104_akarsu_aktug_torun_firm_expectations_rct_2025.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/c286a3bd-1e4c-4074-a148-11695d225319/WP2512.pdf?CACHEID=ROOTWORKSPACE-c286a3bd-1e4c-4074-a148-11695d225319-pz1ggkX&MOD=AJPERES' },
    @{ File = 'S105_colak_kazdal_seven_yilmaz_markups_2025.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/2e5b08f8-e3af-422d-b1f2-061f911f198f/wp_2501.pdf?CACHEID=ROOTWORKSPACE-2e5b08f8-e3af-422d-b1f2-061f911f198f-pgHJpXj&MOD=AJPERES' },
    @{ File = 'S106_caraiani_karamollaoglu_yalcin_expectation_errors_2025.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/8f2cdf37-6aac-49bb-8868-d30a673a18cf/WP2515.pdf?CACHEID=ROOTWORKSPACE-8f2cdf37-6aac-49bb-8868-d30a673a18cf-pBNiibK&MOD=AJPERES' },
    @{ File = 'S107_gokcu_multivariate_filter_2021.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/e4b72c20-f4fc-4a8b-8354-cf27979a53da/wp2139.pdf?CACHEID=ROOTWORKSPACE-e4b72c20-f4fc-4a8b-8354-cf27979a53da-oR4ErgX&MOD=AJPERES' },
    @{ File = 'S108_kara_ogunc_erpt_2005.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/e895eb1e-000f-4235-87a4-1f467faa4f5a/WP0510ENG.pdf?MOD=AJPERES' },
    @{ File = 'S109_tcmb_ir_2025i_pricing_behavior.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/7b5c8ae3-a9d3-411a-be44-ba763c2ad8b5/Box_2.3_25_i.pdf?CACHEID=ROOTWORKSPACE-7b5c8ae3-a9d3-411a-be44-ba763c2ad8b5-pjvvJ7q&MOD=AJPERES' },
    @{ File = 'S110_tcmb_ir_2025iv_real_sector_pricing.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/ecc802b7-19b7-40be-8bbb-b1d717cd79db/2c25iv.pdf?CACHEID=ROOTWORKSPACE-ecc802b7-19b7-40be-8bbb-b1d717cd79db-pOZ9-NN&MOD=AJPERES' },
    @{ File = 'S111_akarsu_aktug_policy_announcements_firm_expectations_2026.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/a38ab625-1d55-43be-b8e3-1aad2e92372a/wp2609.pdf?CACHEID=ROOTWORKSPACE-a38ab625-1d55-43be-b8e3-1aad2e92372a-pUX3y5n&MOD=AJPERES' },
    @{ File = 'S112_ozdemir_firm_behavioral_psychology_2026.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/a9744394-632e-4b28-87b8-57dbc69e6dd0/wp2603.pdf?CACHEID=ROOTWORKSPACE-a9744394-632e-4b28-87b8-57dbc69e6dd0-pLGpeqC&MOD=AJPERES' },
    @{ File = 'S113_tcmb_research_note_firm_expectations_2025.pdf'; Url = 'https://www.tcmb.gov.tr/wps/wcm/connect/cdec8cc7-3596-40b2-9484-d970148e3ced/en202519en.pdf?CACHEID=ROOTWORKSPACE-cdec8cc7-3596-40b2-9484-d970148e3ced-pBr.78e&MOD=AJPERES' }
)

$destination = Join-Path $PSScriptRoot '..\sources\pdfs'
foreach ($target in $targets) {
    $outFile = Join-Path $destination $target.File
    if (-not (Test-Path -LiteralPath $outFile)) {
        Invoke-WebRequest -Uri $target.Url -OutFile $outFile -UseBasicParsing
    }
    $item = Get-Item -LiteralPath $outFile
    [PSCustomObject]@{ File = $item.Name; Bytes = $item.Length }
}
