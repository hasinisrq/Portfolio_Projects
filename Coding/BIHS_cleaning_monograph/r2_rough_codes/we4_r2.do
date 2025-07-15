** using we4
** genarating a variable to see who makes decision



keep a01 we4_08a we4_08b we4_08c we4_08d we4_08e we4_08f we4_08g we4_08h we4_08i we4_08j we4_08k we4_09a we4_09b we4_09c we4_09d we4_09e we4_09f we4_09g we4_09h we4_09i we4_09j we4_09k

**#Genarating mem_comgrp variable: 
*drop mem_comgrp 
tab mem_comgrp

foreach var in we4_08a we4_08b we4_08c we4_08d we4_08e we4_08f we4_08g we4_08h we4_08i we4_08j we4_08k {
    replace `var' = 0 if missing(`var')
}
foreach var in we4_08a we4_08b we4_08c we4_08d we4_08e we4_08f we4_08g we4_08h we4_08i we4_08j we4_08k {
    replace `var' = 0 if `var' == 2
}



egen mem_comgrp = rowtotal(we4_08a we4_08b we4_08c we4_08d we4_08e we4_08f we4_08g we4_08h we4_08i we4_08j we4_08k)
replace mem_comgrp = 1 if mem_comgrp > 0


order a01 we4_08a we4_08b we4_08c we4_08d we4_08e we4_08f we4_08g we4_08h we4_08i we4_08j we4_08k mem_comgrp 

*add label to variables to describe better
label var mem_comgrp  "member of any Community Group"

label define yn_mem_comgrp 0 "Not a member" 1 "Yes" 
label values mem_comgrp yn_mem_comgrp


**#Genarating lead_comgrp variable: 
*drop lead_comgrp 
tab lead_comgrp

foreach var in we4_09a we4_09b we4_09c we4_09d we4_09e we4_09f we4_09g we4_09h we4_09i we4_09j we4_09k {
    replace `var' = 0 if missing(`var')
}
foreach var in we4_09a we4_09b we4_09c we4_09d we4_09e we4_09f we4_09g we4_09h we4_09i we4_09j we4_09k{
    replace `var' = 0 if `var' == 2
}



egen lead_comgrp = rowtotal(we4_09a we4_09b we4_09c we4_09d we4_09e we4_09f we4_09g we4_09h we4_09i we4_09j we4_09k)
replace lead_comgrp = 1 if lead_comgrp > 0


*add label to variables to describe better
label var lead_comgrp  "leader of any Community Group"

label define yn_lead_comgrp 0 "Not a member" 1 "Yes" 
label values lead_comgrp yn_lead_comgrp




**#keeping necessary variables only 
keep a01 mem_comgrp lead_comgrp