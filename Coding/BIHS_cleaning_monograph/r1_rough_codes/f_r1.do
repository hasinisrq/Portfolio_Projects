**preparing credit dataset


sort a01 mid
replace mid = 1 if mid ==.
egen u_id = group (a01 mid)
	
	egen has_credit =total(f03), by (u_id)
	
	replace has_credit = 0 if has_credit ==. | has_credit == 0
	replace has_credit = 1 if has_credit !=0
		
	
	
	duplicates drop u_id, force
	
	
	
	keep a01 mid u_id f04 has_credit
	
	
	
	
	
