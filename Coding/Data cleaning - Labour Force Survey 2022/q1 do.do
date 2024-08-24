*Directing saved files to other folder so that the raw file doesn't get manipulated*

cd "E:\Important\Stata LFS 2022\q1_Files"
use q1_clean2.dta
save q1_clean2, replace

sort EAUM
sort YEAR QUARTER PSU EAUM HHNO EMP_HRLN

*Practicing Histogram
histogram EMP_HR04 if EMP_HR04>0
*adding normal dist trendline
histogram EMP_HR04 if EMP_HR04>0, norm
*this age demographic includes all members, we need only hh's head's age
*'&' means 'and' ; '|' means 'or'
histogram EMP_HR04 if (EMP_HR04>0 & EMP_HRLN==1), freq norm

*checking through loop; ` and ' are different, ` can be found top left of the keyboard, beside number
foreach var of varlist EMP_HR03 EMP_HR04 EMP_HRLN{ 
assert `var'>=0
}

*regressing by enumeration area. Without sorting first, sorting error will show up
sort EAUM
by EAUM: regress MJ_08H MJ_05
by EAUM: regress BBS_job1_ife_nature VT_02
by EAUM: regress BBS_job1_ife_nature VT_02, robust constant


*creating a new variable called age_afterfiveyrs where we will have the workforce 5 years later
generate age_afterfiveyrs=EMP_HR04+5 if (EMP_HR04>12 & EMP_HR04<61)
replace age_afterfiveyrs=0 if (EMP_HR04<13 & EMP_HR04>60 | age_afterfiveyrs==.)


*add label to variables to describe better
label var  age_afterfiveyrs "age after Five Years"
*add label to values of a variable
label define wf 0 "Not_in_Workforce", modify



*table
table EAUM , c(mean MJ_15A sum MJ_15A p50 MJ_15B) row col 
bysort EMP_HR03: table EMP_HR04, c(mean MJ_15A sd MJ_15A)
sort EMP_HR03
by EMP_HR03: tabstat EMP_HR04, stats(mean sd p50 skewness kurtosis chi)
*tabulate
tab EMP_HR03 EMP_HR04, chi


*changing value label
label values age_afterfiveyrs yesno_label
*As we changed value label from wf to yesno_label, we again need to add label to values of the variables
label define yesno_label 0 "Not_in_Workforce", modify


*testing whether a variable is uniquely identified
isid age_afterfiveyrs 
isid EMP_HR04
isid HHNO
isid PSU EAUM HHNO EMP_HRLN

*The first command will report the duplicates in terms of variables mentioned after report
duplicates report EMP_HRLN
duplicates report PSU EAUM HHNO EMP_HRLN
duplicates report PSU EAUM HHNO
//identifying the duplicates in PSU EAUM HHNO, creating a new variable, duplicate2 and assigning to it a value of 0 if it is the first instance of that value in hhid, a 1 if it is the second instance, a 2 if it is the third instance and so on//
duplicates tag PSU EAUM HHNO, gen(duplicate2)
*forces Stata to drop the duplicate entries
duplicates drop PSU EAUM HHNO, force
*Checking if still duplicates are left... 0 indicates no duplicates left
duplicates tag PSU EAUM HHNO, gen(duplicate3)

*creating categories in age group
 recode EMP_HR04 (min/17=0 "kid") (18/65=1 "WF") (66/max= 2 "SC"), gen(age_category)
 *Creating new dummy sex variable where 0=male, 1=female
 recode EMP_HR03 (1=0 "Male") (2=1 "Female"), gen(fsex)
 
*Converting double var into string var- creates a new var gender2 that is string
decode sex_dummy , gen(gender2) 
*Coverting String into no-string - creates a new var gender3 that is non-string
encode gender2, gen (gender3)


//Changing Srting Values 

*in prac2 we see values like abcd1234, we have to change the first abc to cba while creating new var prac4
gen prac4=subinstr(prac2,"abc","cba",1)
*in prac4 we have bbcd1234, we need ahcd1234 in prac5; "1" will replace only one b into h from the right, 2 would have replaced 2 bs from the right
gen prac5=subinstr(prac4,"b","h",1) 
*in prac4 we have bbcd1234, we need hhcd1234 in prac6; . replaces all bs into h
gen prac6=subinstr(prac4,"b","h",.) 
/*we have hhcd1234/wxyz9876 in prac6,
in prac7 we need 23/87 */
gen prac7=substr(prac6,6,2) 
/*we have hhcd1234/wxyz9876 in prac6,
in prac8 we need 876/234
here 876/123 both are 3 digit number therefore we wrote 3 */
generate prac8=substr( prac6,6,3)
**in prac10 we need 87/23, which are 2 digit
**the begining here is from the left
generate prac10=substr( prac6,6,2)


/* we have prac10 as string, converting it into non-string at nonstring_ID*/
destring prac10, gen(nonstring_ID)
*converting back to string
tostring nonstring_ID, gen(string_ID)






 
