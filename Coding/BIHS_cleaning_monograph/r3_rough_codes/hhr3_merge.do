cd "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3"
use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3_female_weai_ind_mod_we2.dta"

**# save hh merge
save hhr3_merge, replace

merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3_female_mod_xxc.dta" , nogen keep(3)

merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3m_q.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3f_z2.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3_female_weai_ind_mod_we2.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3_female_weai_ind_mod_we4.dta" , nogen keep(3)

merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r3\r3m_a.dta" , nogen keep(3)








