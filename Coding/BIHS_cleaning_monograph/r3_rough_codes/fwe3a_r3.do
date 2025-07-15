**Preparing ownership module

tab we3a07

**#Creating a ownership score variable

gen sc_asset_ownership = .
replace sc_asset_ownership = 0 if we3a07 == 4
replace sc_asset_ownership = 0.5 if we3a07 == 2
replace sc_asset_ownership = 1 if inlist(we3a07, 1, 3)
label var sc_asset_ownership "score of women's asset ownership"
replace sc_asset_ownership=0 if sc_asset_ownership==.

duplicates report a01
duplicates report hhid2
duplicates report a01 we3a


egen u_id = group (a01 we3a)


keep a01 we3a u_id we3a07 hh_type sc_asset_ownership