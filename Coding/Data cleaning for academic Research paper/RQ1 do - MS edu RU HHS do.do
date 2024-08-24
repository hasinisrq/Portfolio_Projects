
keep PSU EAUM HHNO EMP_HRLN EMP_HR03 EMP_HR04 employment Education HR_06 RU HI14

//renaming variables
rename EMP_HR04 Age
rename EMP_HR03 Sex
rename HR_06 Marital_Status
rename HI14 Household_Size

drop if Sex == 1
drop if Sex == 3
replace Marital_Status = 0 if Marital_Status == 1
replace Marital_Status = 1 if Marital_Status == 2
replace Marital_Status = 1 if Marital_Status == 3
replace Marital_Status = 1 if Marital_Status == 5
replace Marital_Status = 1 if Marital_Status == 4
replace Sex = 1 if Sex == 2
label define HR_06_VS1 1 "", modify
label define HR_06_VS1 0 " Never Married", modify

replace Education = 1 if Education == 2
replace Education = 1 if Education == 3
replace Education = 1 if Education == 4
replace Education = 1 if Education == 5
label define label_leducation11 1 "educated", modify

drop if Sex==.
drop if Age==.
drop if Marital_Status==.
drop if Education==.
drop if employment==.
drop if Household_Size==.
drop if RU==.

replace employment = 0 if employment == 3
label define BD_emp_llab 0 "Not in employment", modify

replace RU = 0 if RU == 2
replace RU = 1 if RU == 3
label define RU_VS1 0 "Rural", modify

summarize RU employment employment Education Marital_Status Household_Size

tab RU employment employment Education Marital_Status Household_Size



probit employment Marital_Status 


logit employment Marital_Status


drop if Marital_Status==0

rename employment Married_Employed

global ylist Married_Employed
global Xlist Education RU Household_Size


* Probit model
probit $ylist $Xlist

* Logit model
logit $ylist $Xlist



