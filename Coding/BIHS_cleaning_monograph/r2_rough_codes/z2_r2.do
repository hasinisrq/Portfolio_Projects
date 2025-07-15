**creating index variable to measure freedom of mobility

keep a01 z2_01_1 z2_02_1 z2_03_1 z2_04_1 z2_05_1

**#Creating a variable for Control over Household Expenditures
*drop sc_mobility

foreach var in z2_01_1 z2_02_1 z2_03_1 z2_04_1 z2_05_1 {
    replace `var' = 0 if inlist(`var', 2, 4,5)
}
foreach var in z2_01_1 z2_02_1 z2_03_1 z2_04_1 z2_05_1  {
    replace `var' = 0 if `var' == .
}
foreach var in z2_01_1 z2_02_1 z2_03_1 z2_04_1 z2_05_1 {
    replace `var' = 0.5 if `var'== 3
}
foreach var in z2_01_1 z2_02_1 z2_03_1 z2_04_1 z2_05_1 {
    replace `var' = 1 if `var'==1
}



egen sc_mobility = rowtotal(z2_01_1 z2_02_1 z2_03_1 z2_04_1 z2_05_1)
tab sc_mobility

replace sc_mobility = 0 if sc_mobility == 0
replace sc_mobility = 1 if inrange(sc_mobility, .5, 1.5)
replace sc_mobility = 2 if inrange(sc_mobility, 2, 3.5)
replace sc_mobility = 3 if inrange(sc_mobility, 4, 5)

label define sc_fmobility 0 "No mobility" 1 "Low mobility" 2 "Medium mobility" 3 "High mobility"
label values sc_mobility sc_fmobility

**#Keeping necessary vars
keep a01 sc_mobility

