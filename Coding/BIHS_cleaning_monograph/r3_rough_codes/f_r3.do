**preparing credit dataset

tab 

sort a01 mid_f
replace mid_f = 1 if mid_f ==.
egen u_id = group (a01 mid_f)
	
	egen has_credit =total(f03), by (u_id)
	
	replace has_credit = 0 if has_credit ==. | has_credit == 0
	replace has_credit = 1 if has_credit !=0
		
	
	
	duplicates drop u_id, force
	
	
	
	keep a01 mid_f u_id f04 has_credit
	
	
	
	
	
