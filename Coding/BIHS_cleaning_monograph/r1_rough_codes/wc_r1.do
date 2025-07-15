keep wa01 wc02_a wc02_b wc02_c wc02_d wc02_e wc02_f wc02_g wc02_h wc02_i wc02_j wc02_k wc02_l wc02_m wc02_n

rename wa01 a01

**#Creating a ownership score variable

gen sc_asset_ownership = .

foreach var in wc02_a wc02_b wc02_c wc02_d wc02_e wc02_f wc02_g wc02_h wc02_i wc02_j wc02_k wc02_l wc02_m wc02_n {
    replace sc_asset_ownership = 1 if inlist(`var', 1, 3, 5, 7, 9) 
}
foreach var in wc02_a wc02_b wc02_c wc02_d wc02_e wc02_f wc02_g wc02_h wc02_i wc02_j wc02_k wc02_l wc02_m wc02_n {
    replace sc_asset_ownership = 0 if inlist(`var', 2, 4, 6, 8, 10) 
}

tab sc_asset_ownership



keep a01 sc_asset_ownership



label var sc_asset_ownership "score of women's asset ownership"

