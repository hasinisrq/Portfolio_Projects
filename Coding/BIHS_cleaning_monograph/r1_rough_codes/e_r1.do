**preparing savings dataset

*tab e04

sort a01 mid
replace mid = 1 if mid ==.
egen u_id = group (a01 mid)
	
	egen has_save_account =total(e03), by (u_id)
	
	replace has_save_account = 0 if has_save_account ==. | has_save_account == 0
	replace has_save_account = 1 if has_save_account !=0
		
	
	
	duplicates drop u_id, force
	
	
	
	keep a01 mid u_id e04 has_save_account 
	
	
	
	
	
