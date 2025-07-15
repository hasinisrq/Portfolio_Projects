cd "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1"
use "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_wb.dta"

**# save hh merge
save hhr1_merge, replace


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_wc.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_we.dta" , nogen keep(3)



merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_z1.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_z2.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_z3.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1f_z4.dta" , nogen keep(3)


merge 1:1 a01 using "E:\econ a\academics\8th Semester\Monograph\Monograph_Codes\M_Datasets\r1\r1m_q.dta" , nogen keep(3)







