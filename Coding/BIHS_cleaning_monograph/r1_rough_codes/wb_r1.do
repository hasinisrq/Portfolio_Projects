** using we2
** genarating a variable to see who makes decision



keep wa01 wb02_1 wb02_2 wb02_3 wb02_4 wb02_5 wb02_6 wb03_1 wb03_2 wb03_3 wb03_4 wb03_5 wb03_6

rename wa01 a01

**Genarating Input_Income_Use variable: 
*drop Input_Income_Use 
tab Input_Income_Use

egen Input_Income_Use = rowtotal(wb03_1 wb03_2 wb03_3 wb03_4 wb03_5 wb03_6)

*add label to variables to describe better
label var Input_Income_Use  "Level_of_input_income_use"

*add label to values of a variable
label define Level_of_input_income_use 0 "No input"
forvalues i = 1/10 {
    label define Level_of_input_income_use `i' "Low input", add
}
forvalues i = 11/20 {
    label define Level_of_input_income_use `i' "Medium input", add
}
forvalues i = 21/30 {
    label define Level_of_input_income_use `i' "High input", add
}

gen Input_Income_Cat = .
replace Input_Income_Cat = 0 if Input_Income_Use == 0
replace Input_Income_Cat = 1 if inrange(Input_Income_Use, 1, 10)
replace Input_Income_Cat = 2 if inrange(Input_Income_Use, 11, 20)
replace Input_Income_Cat = 3 if inrange(Input_Income_Use, 21, 30)

label define inputcat 0 "No input" 1 "Low input" 2 "Medium input" 3 "High input"
label values Input_Income_Cat inputcat





**Genarating Input_Prod_Dec variable: 
*drop Input_Prod_Dec 
tab Input_Prod_Dec


egen Input_Prod_Dec = rowtotal(wb02_1 wb02_2 wb02_3 wb02_4 wb02_5 wb02_6)

*add label to variables to describe better
label var Input_Prod_Dec  "Level_of_prod_dec"

*add label to values of a variable
label define Level_of_prod_dec 0 "No input"
forvalues i = 1/11 {
    label define Level_of_prod_dec `i' "Low input", add
}
forvalues i = 12/22 {
    label define Level_of_prod_dec `i' "Medium input", add
}
forvalues i = 23/33 {
    label define Level_of_prod_dec `i' "High input", add
}

gen Prod_dec_Cat = .
replace Prod_dec_Cat = 0 if Input_Prod_Dec == 0
replace Prod_dec_Cat = 1 if inrange(Input_Prod_Dec, 1, 11)
replace Prod_dec_Cat = 2 if inrange(Input_Prod_Dec, 12, 22)
replace Prod_dec_Cat = 3 if inrange(Input_Prod_Dec, 23, 33)

label define productioncat 0 "No input" 1 "Low input" 2 "Medium input" 3 "High input"
label values Prod_dec_Cat productioncat

**keeping necessary variables only 
keep a01 Input_Income_Cat Prod_dec_Cat


