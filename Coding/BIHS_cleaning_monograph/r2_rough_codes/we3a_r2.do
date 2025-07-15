**Preparing ownership module


keep a01 we3a we3a02a we3a02b we3a02c
sort a01 we3a


**#Creating a ownership score variable

gen sc_asset_ownership = .
replace sc_asset_ownership = 1 if we3a02a == 1 | we3a02b == 1 | we3a02c == 1
replace sc_asset_ownership = 0 if we3a02a != 1 & we3a02b != 1 & we3a02c != 1

drop we3a02a we3a02b we3a02c

label var sc_asset_ownership "score of women's asset ownership"

egen u_id = group (a01 we3a)

