cd "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2"
use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2f_we2.dta"

**# save hh merge
save hhr2_merge, replace


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2f_we4.dta" , nogen keep(3)



merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2f_z1.dta" , nogen keep(3)



merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2f_z2.dta" , nogen keep(3)



merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2f_z3.dta" , nogen keep(3)



merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2f_z4.dta" , nogen keep(3)



merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r2\r2m_q.dta" , nogen keep(3)









