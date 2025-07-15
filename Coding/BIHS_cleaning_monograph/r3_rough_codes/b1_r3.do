**Preparing Roster dataset and gen human capital var

keep a01 mid b1_01 b1_02 b1_03 b1_04 b1_08 b1_10
sort a01 mid 

egen u_id = group (a01 mid)
order a01 mid u_id


**#Renaming Vars
rename b1_01 gender
rename b1_02 age
rename b1_03 rel_hh
rename b1_04 marital_s
rename b1_10 occupation


**#genarating Human Capital Var
rename b1_08 h_cap
tab h_cap

gen hcap_score = .
replace hcap_score = 0 if h_cap == 99
replace hcap_score = 0 if h_cap == .
replace hcap_score = 1 if inlist(h_cap, 0, 1, 2, 3, 4, 5, 66, 67, 76)
replace hcap_score = 2 if inlist(h_cap, 6, 7, 8, 9, 10, 22)
replace hcap_score = 3 if inlist(h_cap, 12, 33, 75)
replace hcap_score = 4 if inlist(h_cap, 72, 74)
replace hcap_score = 5 if inlist(h_cap, 14, 15, 16, 73)


label var hcap_score "Human Captal Score"
label values hcap_score hcscore
label define hcscore 0 "Not Educated" 1 "Primary" 2 "High School" 3 "Colllege" 4 "Diploma" 5 "Undergrad and Beyond"


