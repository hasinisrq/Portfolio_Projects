cd "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\Rough_dos\panel"


**# Loading dataset
use panel_data_fixed_effect.dta

/*___________________________
**# Preparing datasets
use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1_merge.dta", clear
gen round = 1
save "r1_panel.dta", replace

use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2_merge.dta", clear
gen round = 2
save "r2_panel.dta", replace

use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3_merge.dta", clear
drop round
gen round = 3
save "r3_panel.dta", replace



**# Appending
use "r1_panel.dta", clear
append using "r2_panel.dta"
append using "r3_panel.dta"

_____________________________________*/

/*___________________________________________

**# Necessary Adjustments
drop if gender==1
drop if age<15


**# Balancing


bys u_id: egen obs_count = count(round)
keep if obs_count==3
drop obs_count
_____________________________________*/





**# Set as panel
xtset u_id round
xtdescribe
asdoc xtset u_id round, title(Panel Data Balance) replace
asdoc xtdescribe, title(Panel Data Description) append



**# Save final dataset
save "panel_data_fixed_effect.dta", replace

 
*egen Women_Empowerment_overall = rowtotal(Resources_emp Agency_emp Achievements_emp)
 



**#taking regression results to word
asdoc xtreg Resources_emp FI_score, re robust, title(Resources_em RE Result) append
asdoc xtreg Agency_emp FI_score, fe robust, title(Agency_emp FE Result) append
asdoc xtreg Achievements_emp FI_score, fe robust, title(Achievements_emp Hausman Test Result) append


asdoc xtreg Women_Empowerment_overall FI_score mbanking_holder has_credit has_save_account, fe robust, title(Women_Empowerment_overall FE Result) append



asdoc xtreg sc_asset_ownership FI_score, re robust, title(sc_asset_ownership RE Result) append
asdoc xtreg hcap_score FI_score, re robust, title(hcap_score RE Result) append
asdoc xtreg Prod_dec_Cat FI_score, re robust, title(Prod_dec_Cat RE Result) append
asdoc xtreg Input_Income_Cat FI_score, re robust, title(Input_Income_Cat RE Result) append
asdoc xtreg mem_comgrp FI_score, re robust, title(mem_comgrp RE Result) append
asdoc xtreg lead_comgrp FI_score, re robust, title(lead_comgrp RE Result) append
asdoc xtreg ctrl_hh_exp FI_score, re robust, title(ctrl_hh_exp RE Result) append
asdoc xtreg sc_mobility FI_score, re robust, title(sc_mobility RE Result) append
asdoc xtreg ctrl_reproductive_health FI_score, re robust, title(ctrl_reproductive_health RE Result) append
asdoc xtreg neg_dom_violence FI_score, fe robust, title(neg_dom_violence FE Result) append






/*_______________________________________
* Step 1: Run Fixed-effects regression
xtreg Achievements_emp FI_score, fe robust
estimates store FE

* Step 2: Run Random-effects regression
xtreg Achievements_emp FI_score, re robust
estimates store RE

* Step 3: Perform Hausman Test
hausman FE RE, sigmamore

_____________________________________*/


**#Hausman Tests:
xtreg Achievements_emp FI_score, fe
estimates store FE_Ac
xtreg Achievements_emp FI_score, re
estimates store RE_Ac

xtreg Resources_emp FI_score, fe
estimates store FE_R
xtreg Resources_emp FI_score, re
estimates store RE_R

xtreg Agency_emp FI_score, fe
estimates store FE_Ag
xtreg Agency_emp FI_score, re
estimates store RE_Ag

xtreg Women_Empowerment_overall FI_score, fe
estimates store FE_WO
xtreg Women_Empowerment_overall FI_score, re
estimates store RE_WO

xtreg sc_asset_ownership FI_score, fe
estimates store FE_asset
xtreg sc_asset_ownership FI_score, re
estimates store RE_asset


xtreg hcap_score FI_score, fe
estimates store FE_hcap
xtreg hcap_score FI_score, re
estimates store RE_hcap

xtreg Prod_dec_Cat FI_score, fe
estimates store FE_prod
xtreg Prod_dec_Cat FI_score, re
estimates store RE_prod

xtreg Input_Income_Cat FI_score, fe
estimates store FE_inc
xtreg Input_Income_Cat FI_score, re
estimates store RE_inc


xtreg mem_comgrp FI_score, fe
estimates store FE_memcom
xtreg mem_comgrp FI_score, re
estimates store RE_memcom

xtreg lead_comgrp FI_score, fe
estimates store FE_leadcom
xtreg lead_comgrp FI_score, re
estimates store RE_leadcom

xtreg ctrl_hh_exp FI_score, fe
estimates store FE_hhexp
xtreg ctrl_hh_exp FI_score, re
estimates store RE_hhexp

xtreg sc_mobility FI_score, fe
estimates store FE_mob
xtreg sc_mobility FI_score, re
estimates store RE_mob

xtreg ctrl_reproductive_health FI_score, fe
estimates store FE_rep
xtreg ctrl_reproductive_health FI_score, re
estimates store RE_rep

xtreg neg_dom_violence FI_score, fe
estimates store FE_domv
xtreg neg_dom_violence FI_score, re
estimates store RE_domv




asdoc hausman FE_Ac RE_Ac, sigmamore, title( Hausman test for Achievements_emp) append
asdoc hausman FE_R RE_R, sigmamore, title( Hausman test for Resources_emp) append
asdoc hausman FE_Ag RE_Ag, sigmamore, title( Hausman test for Agency_emp) append
asdoc hausman FE_WO RE_WO, sigmamore, title( Hausman test for Women_Empowerment_overall) append

asdoc hausman FE_asset RE_asset, sigmamore, title( Hausman test for sc_asset_ownership) append
asdoc hausman FE_hcap RE_hcap, sigmamore, title( Hausman test for hcap_score) append
asdoc hausman FE_prod RE_prod, sigmamore, title( Hausman test for Prod_dec_Cat) append
asdoc hausman FE_inc RE_inc, sigmamore, title( Hausman test for Input_Income_Cat) append
asdoc hausman FE_memcom RE_memcom, sigmamore, title( Hausman test for mem_comgrp) append
asdoc hausman FE_leadcom RE_leadcom, sigmamore, title( Hausman test for lead_comgrp) append
asdoc hausman FE_hhexp RE_hhexp, sigmamore, title( Hausman test for ctrl_hh_exp) append
asdoc hausman FE_mob RE_mob, sigmamore, title( Hausman test for sc_mobility) append
asdoc hausman FE_rep RE_rep, sigmamore, title( Hausman test for ctrl_reproductive_health) append
asdoc hausman FE_domv RE_domv, sigmamore, title( Hausman test for neg_dom_violence) append





xx
**# Making data Tables
asdoc tab Women_Empowerment_overall if round==3, title(Women Empowerment Score, Round 3) replace
asdoc tab Women_Empowerment_overall if round==2, title(Women Empowerment Score, Round 2) append
asdoc tab Women_Empowerment_overall if round==1, title(Women Empowerment Score, Round 1) append

asdoc tab Agency_emp if round==3, title(Agency Empowerment Score, Round 3) append
asdoc tab Agency_emp if round==2, title(Agency Empowerment Score, Round 2) append
asdoc tab Agency_emp if round==1, title(Agency Empowerment Score, Round 1) append

asdoc tab Achievements_emp if round==3, title(Achievement Empowerment Score, Round 3) append
asdoc tab Achievements_emp if round==2, title(Achievement Empowerment Score, Round 2) append
asdoc tab Achievements_emp if round==1, title(Achievement Empowerment Score, Round 1) append

asdoc tab Resources_emp if round==3, title(Resources Empowerment Score, Round 3) append
asdoc tab Resources_emp if round==2, title(Resources Empowerment Score, Round 2) append
asdoc tab Resources_emp if round==1, title(Resources Empowerment Score, Round 1) append

asdoc tab sc_asset_ownership if round==3, title(sc_asset_ownership Score, Round 3) append
asdoc tab sc_asset_ownership if round==2, title(sc_asset_ownership Score, Round 2) append
asdoc tab sc_asset_ownership if round==1, title(sc_asset_ownership Score, Round 1) append


asdoc tab hcap_score if round==3, title(hcap_score Score, Round 3) append
asdoc tab hcap_score if round==2, title(hcap_score Score, Round 2) append
asdoc tab hcap_score if round==1, title(hcap_score Score, Round 1) append


asdoc tab Prod_dec_Cat if round==3, title(Prod_dec_Cat Score, Round 3) append
asdoc tab Prod_dec_Cat if round==2, title(Prod_dec_Cat Score, Round 2) append
asdoc tab Prod_dec_Cat if round==1, title(Prod_dec_Cat Score, Round 1) append


asdoc tab Input_Income_Cat if round==3, title(Input_Income_Cat Score, Round 3) append
asdoc tab Input_Income_Cat if round==2, title(Input_Income_Cat Score, Round 2) append
asdoc tab Input_Income_Cat if round==1, title(Input_Income_Cat Score, Round 1) append


asdoc tab mem_comgrp if round==3, title(mem_comgrp Score, Round 3) append
asdoc tab mem_comgrp if round==2, title(mem_comgrp Score, Round 2) append
asdoc tab mem_comgrp if round==1, title(mem_comgrp Score, Round 1) append


asdoc tab lead_comgrp if round==3, title(lead_comgrp Score, Round 3) append
asdoc tab lead_comgrp if round==2, title(lead_comgrp Score, Round 2) append
asdoc tab lead_comgrp if round==1, title(lead_comgrp score, Round 1) append


asdoc tab ctrl_hh_exp if round==3, title(ctrl_hh_exp Score, Round 3) append
asdoc tab ctrl_hh_exp if round==2, title(ctrl_hh_exp Score, Round 2) append
asdoc tab ctrl_hh_exp if round==1, title(ctrl_hh_exp Score, Round 1) append


asdoc tab sc_mobility if round==3, title(sc_mobility Score, Round 3) append
asdoc tab sc_mobility if round==2, title(sc_mobility Score, Round 2) append
asdoc tab sc_mobility if round==1, title(sc_mobility Score, Round 1) append


asdoc tab ctrl_reproductive_health if round==3, title(ctrl_reproductive_health Score, Round 3) append
asdoc tab ctrl_reproductive_health if round==2, title(ctrl_reproductive_health Score, Round 2) append
asdoc tab ctrl_reproductive_health if round==1, title(ctrl_reproductive_health Score, Round 1) append


asdoc tab neg_dom_violence if round==3, title(neg_dom_violence Score, Round 3) append
asdoc tab neg_dom_violence if round==2, title(neg_dom_violence Score, Round 2) append
asdoc tab neg_dom_violence if round==1, title(neg_dom_violence Score, Round 1) append


asdoc summarize Women_Empowerment_overall Resources_emp Agency_emp Achievements_emp FI_score, title(Summary Statistics of Composite Indices) append






asdoc tabulate FI_score, title(Distribution of Financial Inclusion Score) append



asdoc tabstat Women_Empowerment_overall Resources_emp Agency_emp Achievements_emp FI_score, by(round) statistics(mean) long, title (Evolution of Key Indicators Over Time) append

label define FI_labels 0 "No formal financial access" 1 "Access to one service" 2 "Access to two services" 3 "Access to all three services", modify
asdoc tabulate FI_score, title(Table 4.2: Distribution of Financial Inclusion Score) c(freq percent) label append 





local myvars "Overall_Empowerment Resources_Dimension Agency_Dimension Achievements_Dimension Financial_Inclusion_Score"


table (var) (wave), statistic(mean `myvars'), title(Evolution of Key Indicators Over Time)
	 
asdoc tabstat Women_Empowerment_overall Resources_emp Agency_emp Achievements_emp FI_score,  by(Year) statistics(mean) format(%6.2f),  title (Mean Scores by Year) append