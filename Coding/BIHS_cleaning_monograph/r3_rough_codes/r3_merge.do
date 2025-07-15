cd "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3"
use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3m_b1.dta"

**# save hh merge
save r3_merge, replace



**# merging files

merge 1:1 u_id using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3f_z4.dta" , nogen keep(3)

merge 1:1 u_id using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3f__z1.dta" , nogen keep(3)


merge 1:1 u_id using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3m_e.dta" , nogen keep(3)


merge 1:1 u_id using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3m_f.dta" , nogen keep(3)


merge 1:1 u_id using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3_female_weai_ind_mod_we3a.dta" , nogen keep(3)

merge 1:1 u_id using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3f_z3.dta" , nogen keep(3)


merge m:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\hhr3_merge.dta" , nogen keep(3)

**# Creating Resources WE index
order a01 u_id sc_asset_ownership hcap_score mem_comgrp lead_comgrp
egen Resources_emp = rowtotal (sc_asset_ownership hcap_score mem_comgrp lead_comgrp)

label var Resources_emp "Resources Empowerment score"


**# Creating Agency WE index
order a01 u_id sc_asset_ownership hcap_score mem_comgrp lead_comgrp Resources_emp Input_Income_Cat Prod_dec_Cat Productive_dummy inc_dec spending_dec ctrl_hh_exp sc_mobility ctrl_reproductive_health

egen Agency_emp = rowtotal (Input_Income_Cat Prod_dec_Cat Productive_dummy inc_dec spending_dec ctrl_hh_exp sc_mobility ctrl_reproductive_health mem_comgrp lead_comgrp)

**# Creating Achievements WE index
order a01 u_id sc_asset_ownership hcap_score mem_comgrp lead_comgrp Resources_emp Input_Income_Cat Prod_dec_Cat Productive_dummy inc_dec spending_dec ctrl_hh_exp sc_mobility ctrl_reproductive_health Agency_emp neg_dom_violence has_legalK Achievements_emp

gen neg_dom_violence = Dviolence_dummy * -1

egen Achievements_emp = rowtotal (Productive_dummy sc_asset_ownership mem_comgrp lead_comgrp neg_dom_violence has_legalK)


**# Creating Financial Inclusion Index

order a01 u_id sc_asset_ownership hcap_score mem_comgrp lead_comgrp Resources_emp Input_Income_Cat Prod_dec_Cat Productive_dummy inc_dec spending_dec ctrl_hh_exp sc_mobility ctrl_reproductive_health Agency_emp neg_dom_violence has_legalK Achievements_emp has_save_account has_credit mbanking_holder FI_score

egen FI_score = rowtotal (has_save_account has_credit mbanking_holder)


**# Order indexes first
order a01 u_id Resources_emp Agency_emp Achievements_emp FI_score

**# Preparing this dataset cross section 2019
gen Year=2019

order a01 u_id Year Resources_emp Agency_emp Achievements_emp FI_score





