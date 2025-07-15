** using we2
** genarating a variable to see who makes decision



drop hh_type wa01 wa03 wa04 wa05

**Genarating Input_Income_Use variable: 
*drop Input_Income_Use 
tab Input_Income_Use

egen Input_Income_Use = rowtotal(we2_03_1 we2_03_2 we2_03_3 we2_03_4 we2_03_5 we2_03_6)

*add label to variables to describe better
label var Input_Income_Use  "Level_of_input_income_use"

*add label to values of a variable
label define Level_of_input_income_use 0 "No input"
forvalues i = 1/6 {
    label define Level_of_input_income_use `i' "Low input", add
}
forvalues i = 7/13 {
    label define Level_of_input_income_use `i' "Medium input", add
}
forvalues i = 14/19 {
    label define Level_of_input_income_use `i' "High input", add
}

gen Input_Income_Cat = .
replace Input_Income_Cat = 0 if Input_Income_Use == 0
replace Input_Income_Cat = 1 if inrange(Input_Income_Use, 1, 6)
replace Input_Income_Cat = 2 if inrange(Input_Income_Use, 7, 13)
replace Input_Income_Cat = 3 if inrange(Input_Income_Use, 14, 19)

label define inputcat 0 "No input" 1 "Low input" 2 "Medium input" 3 "High input"
label values Input_Income_Cat inputcat





**Genarating Input_Prod_Dec variable: 
*drop Input_Prod_Dec 
tab Input_Prod_Dec

egen Input_Prod_Dec = rowtotal(we2_02_1 we2_02_2 we2_02_3 we2_02_4 we2_02_5 we2_02_6)

*add label to variables to describe better
label var Input_Prod_Dec  "Level_of_prod_dec"

*add label to values of a variable
label define Level_of_prod_dec 0 "No input"
forvalues i = 1/6 {
    label define Level_of_prod_dec `i' "Low input", add
}
forvalues i = 7/13 {
    label define Level_of_prod_dec `i' "Medium input", add
}
forvalues i = 14/19 {
    label define Level_of_prod_dec `i' "High input", add
}

gen Prod_dec_Cat = .
replace Prod_dec_Cat = 0 if Input_Prod_Dec == 0
replace Prod_dec_Cat = 1 if inrange(Input_Prod_Dec, 1, 6)
replace Prod_dec_Cat = 2 if inrange(Input_Prod_Dec, 7, 13)
replace Prod_dec_Cat = 3 if inrange(Input_Prod_Dec, 14, 19)

label define productioncat 0 "No input" 1 "Low input" 2 "Medium input" 3 "High input"
label values Prod_dec_Cat productioncat

**keeping necessary variables only 
keep a01 Input_Income_Cat Prod_dec_Cat


