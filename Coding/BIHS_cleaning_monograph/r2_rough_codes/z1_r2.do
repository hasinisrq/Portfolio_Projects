** creating necessary variables

keep a01 z1_01 z1_06 z1_15a z1_15b z1_15c z1_15d z1_15e z1_11


**#creating a variable for productive women
rename z1_01 Productive_dummy
tab Productive_dummy
replace Productive_dummy=0 if Productive_dummy==2

**#creating a variable for women's spending decision
gen spending_dec = .
replace spending_dec = 1 if z1_11 == 1
replace spending_dec = 0.5 if z1_11 == 3
replace spending_dec = 0 if inlist(z1_11, 2, 4)
label var spending_dec "score of women's spending decisionmaking"
replace spending_dec=0 if spending_dec==.

**#creating a variable for income decision making of woman
rename z1_06 inc_dec
tab inc_dec
replace inc_dec = 1 if inc_dec == 1
replace inc_dec = 0.5 if inc_dec == 3
replace inc_dec = 0 if inlist(inc_dec, 2, 4)
label var inc_dec "score of women's earning decisionmaking"
replace inc_dec=0 if inc_dec==.

**#Creating a variable for Control over Household Expenditures
*drop ctrl_hh_exp

foreach var in z1_15a z1_15b z1_15c z1_15d z1_15e {
    replace `var' = 0 if inlist(`var', 2, 4)
}
foreach var in z1_15a z1_15b z1_15c z1_15d z1_15e {
    replace `var' = 0 if `var' == .
}
foreach var in z1_15a z1_15b z1_15c z1_15d z1_15e {
    replace `var' = 0.5 if `var'== 3
}
foreach var in z1_15a z1_15b z1_15c z1_15d z1_15e {
    replace `var' = 0 if `var'> 3
}



egen ctrl_hh_exp = rowtotal(z1_15a z1_15b z1_15c z1_15d z1_15e)
tab ctrl_hh_exp

replace ctrl_hh_exp = 0 if ctrl_hh_exp == 0
replace ctrl_hh_exp = 1 if inrange(ctrl_hh_exp, .5, 1.5)
replace ctrl_hh_exp = 2 if inrange(ctrl_hh_exp, 2, 3.5)
replace ctrl_hh_exp = 3 if inrange(ctrl_hh_exp, 4, 5)

label define hhexp_ctrl 0 "No control" 1 "Low control" 2 "Medium control" 3 "High control"
label values ctrl_hh_exp hhexp_ctrl

**#Keeping necessary vars
keep a01 Productive_dummy inc_dec spending_dec ctrl_hh_exp

