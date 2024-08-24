cd "E:\Ayon Important\econ a\#Sanem\WGI Indicators Bimstec"
use WGI_I_Bimstec.dta
save WGI_I_Bimstec, replace

//String to non-string
encode countryname, gen(Country_name)

//Adding Value labels
label value country_name "country_name"
label define country_name 2 "Bhutan" 1 "Bangladesh" 5 "Nepal" 3 "India" 4 "Myanmar" 6 "Sri Lanka" 7 "Thailand"

/* Scatter Diagrams
*/
scatter controlofcorruptionpercentileran controlofcorruptionestimateccest, mlabel(country_name)
scatter governmenteffectivenesspercentil governmenteffectivenessestimateg , mlabel(country_name)
scatter politicalstabilityandabsenceofvi var12, mlabel(country_name)
scatter regulatoryqualitypercentilerankr regulatoryqualityestimaterqest, mlabel(country_name)
scatter ruleoflawpercentilerankrlperrnk ruleoflawestimaterlest, mlabel(country_name)
scatter voiceandaccountabilitypercentile voiceandaccountabilityestimateva, mlabel(country_name)










