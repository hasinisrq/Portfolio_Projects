**Preparing q module for mbanking_holder

keep a01 q_20d_1 q_20d_2 q_20d_3

gen mbanking_holder = .
replace mbanking_holder = 1 if inrange(q_20d_1, 1, 5) | inrange(q_20d_2, 1, 5) | inrange(q_20d_3, 1, 5)
replace mbanking_holder = 0 if inlist(q_20d_1, 6, 7) & inlist(q_20d_2, 6, 7) & inlist(q_20d_3, 6, 7)
replace mbanking_holder = 0 if mbanking_holder == .

label var mbanking_holder "mobile_banking_holder"
