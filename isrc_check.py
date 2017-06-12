def isrc_check(isrc, strict=False):
	"""Checks whether a string is an ISRC code. 
	
	Returns a tuple containing 1) a string with all non-alphanumeric characters removed and 2) a boolean

	If optional strict parameter is set to True, then the first two characters in the string must match an ISO country code

	Based on the ISRC Handbook --> http://www.ifpi.org/content/library/isrc_handbook.pdf

	Keyword arguments:
	isrc -- the string to be evaluated

	Optional parameters:
	strict -- (default = False)
	"""

	COUNTRIES = ["AD", "AE", "AG", "AI", "AL", "AM", "AO", "AR", "AT", "AU", 
				 "AW", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BM", 
				 "BO", "BR", "BS", "BX", "BY", "BZ", "CA", "CD", "CH", "CI", 
				 "CL", "CM", "CN", "CO", "CP", "CS", "CU", "CW", "CY", "CZ", 
				 "DE", "DG", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ES", 
				 "ET", "FI", "FJ", "FR", "FX", "GB", "GD", "GE", "GG", "GH", 
				 "GI", "GM", "GR", "GT", "GY", "HK", "HN", "HR", "HT", "HU", 
				 "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JE", "JM", 
				 "JO", "JP", "KE", "KN", "KR", "KY", "KZ", "LA", "LB", "LC", 
				 "LI", "LK", "LS", "LT", "LU", "LV", "MA", "MC", "MD", "ME", 
				 "MK", "MO", "MP", "MS", "MT", "MU", "MV", "MW", "MX", "MY", 
				 "MZ", "NA", "NG", "NL", "NO", "NP", "NZ", "PA", "PE", "PF", 
				 "PG", "PH", "PK", "PL", "PR", "PT", "PY", "QA", "QM", "QZ", 
				 "RO", "RS", "RU", "SA", "SB", "SC", "SE", "SG", "SI", "SK", 
				 "SL", "SM", "SN", "SV", "SX", "SZ", "TC", "TH", "TN", "TO", 
				 "TR", "TT", "TW", "TZ", "UA", "UG", "UK", "US", "UY", "UZ", 
				 "VC", "VE", "VG", "VN", "VU", "YU", "ZA", "ZM", "ZW", "ZZ"]

	isrc = ''.join(e for e in str(isrc) if e.isalnum()).upper()

	if len(isrc) != 12: return isrc, False 

	if strict:

			if isrc[0:2] not in COUNTRIES: return isrc, False

	elif isrc[0:2].isalpha() is not True: return isrc, False

	if isrc[2:5].isalnum() is not True: return isrc, False

	if isrc[5:].isdigit() is not True: return isrc, False

	else: return isrc, True
