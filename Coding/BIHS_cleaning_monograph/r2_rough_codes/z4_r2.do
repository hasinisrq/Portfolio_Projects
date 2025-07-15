**Creating Variable to measure score of Domestic Violence against women using z4 dataset


keep a01 z4_01a z4_01b z4_01c z4_01d

**Creating Variable Dviolence_dummy

foreach var in z4_01a z4_01b z4_01c z4_01d {
    replace `var' = 0 if inlist(`var', 4, 9)
}
foreach var in z4_01a z4_01b z4_01c z4_01d {
    replace `var' = 0 if `var' == .
}
foreach var in z4_01a z4_01b z4_01c z4_01d {
    replace `var' = 1 if inlist(`var', 1, 2, 3)
}

egen Dviolence_dummy = rowtotal (z4_01a z4_01b z4_01c z4_01d)
replace Dviolence_dummy = 1 if Dviolence_dummy > 0
tab Dviolence_dummy


