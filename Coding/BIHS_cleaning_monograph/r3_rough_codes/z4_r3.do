**Creating Variable to measure score of Domestic Violence against women using z4 dataset

egen u_id= group (a01 z4_mid)
order a01 z4_mid u_id

keep a01 z4_mid z4_01a z4_01b z4_01c1 z4_01c2 z4_01c3 z4_01d1 z4_01d2 z4_01d3 z4_05 z4_06

**Creating Variable Dviolence_dummy

foreach var in z4_01a z4_01b z4_01c1 z4_01c2 z4_01c3 z4_01d1 z4_01d2 z4_01d3 {
    replace `var' = 0 if inlist(`var', 4, 9)
}
foreach var in z4_01a z4_01b z4_01c1 z4_01c2 z4_01c3 z4_01d1 z4_01d2 z4_01d3 {
    replace `var' = 0 if `var' == .
}
foreach var in z4_01a z4_01b z4_01c1 z4_01c2 z4_01c3 z4_01d1 z4_01d2 z4_01d3 {
    replace `var' = 1 if inlist(`var', 1, 2, 3)
}

egen Dviolence_dummy = rowtotal (z4_01a z4_01b z4_01c1 z4_01c2 z4_01c3 z4_01d1 z4_01d2 z4_01d3)
replace Dviolence_dummy = 1 if Dviolence_dummy > 0
tab Dviolence_dummy


