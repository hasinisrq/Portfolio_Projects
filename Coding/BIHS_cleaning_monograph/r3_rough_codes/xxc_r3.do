**female_xxc 
** keep xxc_02

keep a01 res_id_xxc xxc_02
gen has_legalK= xxc_02 ==18

label var has_legalK "dummy_for_Legal_knowledge"
label define dummy_for_Legal_knowledge 0 "Unaware" 1 "Aware", modify