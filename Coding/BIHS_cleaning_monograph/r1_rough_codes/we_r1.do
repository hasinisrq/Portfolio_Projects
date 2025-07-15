** using we4
** genarating a variable to see who makes decision



keep wa01 e07_a e07_b e07_c e07_d e07_e e07_f e07_g e07_h e07_i e07_j e07_k e08_a e09_a e08_b e09_b e08_c e09_c e08_d e09_d e08_e e09_e e08_f e09_f e08_g e09_g e08_h e09_h e08_i e09_i e08_j e09_j e08_k e09_k

rename wa01 a01

**#Genarating mem_comgrp variable: 
*drop mem_comgrp 
*tab mem_comgrp

foreach var in e07_a e07_b e07_c e07_d e07_e e07_f e07_g e07_h e07_i e07_j e07_k {
    replace `var' = 0 if missing(`var')
}
foreach var in e07_a e07_b e07_c e07_d e07_e e07_f e07_g e07_h e07_i e07_j e07_k {
    replace `var' = 0 if `var' == 2
}



egen mem_comgrp = rowtotal(e07_a e07_b e07_c e07_d e07_e e07_f e07_g e07_h e07_i e07_j e07_k)
replace mem_comgrp = 1 if mem_comgrp > 0


order a01 e07_a e07_b e07_c e07_d e07_e e07_f e07_g e07_h e07_i e07_j e07_k mem_comgrp 

*add label to variables to describe better
label var mem_comgrp  "member of any Community Group"

label define yn_mem_comgrp 0 "Not a member" 1 "Yes" 
label values mem_comgrp yn_mem_comgrp


**#Genarating lead_comgrp variable: 
*drop lead_comgrp 
*tab lead_comgrp

foreach var in e08_a e09_a e08_b e09_b e08_c e09_c e08_d e09_d e08_e e09_e e08_f e09_f e08_g e09_g e08_h e09_h e08_i e09_i e08_j e09_j e08_k e09_k {
    replace `var' = 0 if missing(`var')
}
foreach var in e08_a e09_a e08_b e09_b e08_c e09_c e08_d e09_d e08_e e09_e e08_f e09_f e08_g e09_g e08_h e09_h e08_i e09_i e08_j e09_j e08_k e09_k{
    replace `var' = 0 if `var' == 2
}



egen lead_comgrp = rowtotal(e08_a e09_a e08_b e09_b e08_c e09_c e08_d e09_d e08_e e09_e e08_f e09_f e08_g e09_g e08_h e09_h e08_i e09_i e08_j e09_j e08_k e09_k)
replace lead_comgrp = 1 if lead_comgrp > 0


*add label to variables to describe better
label var lead_comgrp  "leader of any Community Group"

label define yn_lead_comgrp 0 "Not a member" 1 "Yes" 
label values lead_comgrp yn_lead_comgrp




**#keeping necessary variables only 
keep a01 mem_comgrp lead_comgrp