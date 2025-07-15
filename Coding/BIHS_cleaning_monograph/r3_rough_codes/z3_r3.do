
keep a01 z3_mid z3_02

egen u_id = group (a01 z3_mid)

**#creating a variable for Control over Reproductive health for women
rename z3_02 ctrl_reproductive_health
tab ctrl_reproductive_health
levelsof ctrl_reproductive_health

replace ctrl_reproductive_health = 1 if ctrl_reproductive_health == 1
replace ctrl_reproductive_health = 0.5 if ctrl_reproductive_health == 3
replace ctrl_reproductive_health = 0 if inlist(ctrl_reproductive_health, 2, 4)
label var ctrl_reproductive_health "score of women's control over Reproductive Health"
replace ctrl_reproductive_health=0 if ctrl_reproductive_health==.

