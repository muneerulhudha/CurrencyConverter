#!/usr/bin/env python
import urllib2

#change this to 1 to get a few extra prints
debug = 0 
#This it the app id that you get when you register from opencurrencyexchange

#This id is muneers ID
app_id="app_id=6087de5e654644dd9e61146505439bc8"

base_url = "http://openexchangerates.org/api/latest.json?"

url = base_url+app_id


availabe_rates = {'COP': 1893.658604, 'MYR': 3.07189, 'TMT': 2.8525, 'DZD': 79.354177, 'NAD': 9.882377, 'GHS': 1.994741, 'SZL': 9.923248, 'EGP': 6.98273, 'IDR': 9804.219143, 'HNL': 20.266898, 'BGN': 1.50771, 'FJD': 1.843281, 'ETB': 18.64785, 'XCD': 2.70195, 'PAB': 1, 'BZD': 1.973784, 'USD': 1, 'ILS': 3.683173, 'MGA': 2212.388333, 'BOB': 6.986463, 'DKK': 5.733669, 'BWP': 8.568565, 'LBP': 1504.1236, 'TZS': 1632.401593, 'VND': 20963.420825, 'TWD': 30.027794, 'AOA': 96.152166, 'WST': 2.298734, 'KHR': 3998.61, 'MUR': 31.28085, 'SOS': 1460.421667, 'KYD': 0.819298, 'LYD': 1.282511, 'UAH': 8.14198, 'UGX': 2597.102145, 'JOD': 0.708744, 'XAF': 504.899699, 'AWG': 1.789967, 'SAR': 3.749987, 'EUR': 0.767635, 'SEK': 6.602353, 'TOP': 1.750027, 'HKD': 7.764046, 'ZMK': 5227.108333, 'JEP': 0.658028, 'MDL': 12.538968, 'AUD': 1.033803, 'CHF': 0.958156, 'CUP': 22.687419, 'CLF': 0.02146, 'BBD': 2, 'BYR': 8704.775, 'CDF': 918.173832, 'SCR': 11.812323, 'GMD': 34.057212, 'VEF': 6.291024, 'BSD': 1, 'ARS': 5.276637, 'TND': 1.642594, 'HRK': 5.822914, 'DJF': 177.288499, 'UYU': 19.9859, 'YER': 214.980504, 'SYP': 70.135986, 'CLP': 490.761551, 'THB': 30.14922, 'UZS': 2074.313947, 'BND': 1.263189, 'ISK': 122.872501, 'ALL': 108.19575, 'SRD': 3.275, 'NIO': 24.518243, 'KZT': 151.149063, 'LAK': 7682.185, 'RUB': 31.671018, 'XAG': 0.043747, 'NOK': 5.855992, 'PYG': 4239.522035, 'PEN': 2.693755, 'RON': 3.342941, 'OMR': 0.384972, 'BRL': 2.104911, 'MAD': 8.551935, 'MMK': 943.158125, 'PLN': 3.278745, 'MZN': 29.772166, 'PHP': 42.348837, 'KES': 84.987234, 'SVC': 8.743593, 'NPR': 89.857634, 'XPF': 92.081101, 'STD': 18952.85, 'MKD': 47.981954, 'ZWL': 322.322775, 'GBP': 0.658028, 'AZN': 0.7846, 'NGN': 158.481497, 'MVR': 15.32125, 'VUV': 93.683334, 'CRC': 500.746902, 'GNF': 7062.665, 'AED': 3.672846, 'EEK': 11.760122, 'MWK': 333.420125, 'IQD': 1157.803333, 'TTD': 6.414781, 'BAM': 1.505953, 'LKR': 126.478243, 'DOP': 41.206524, 'CAD': 1.033258, 'PKR': 98.369401, 'MXN': 12.715806, 'HUF': 224.408758, 'CVE': 85.163063, 'KWD': 0.286103, 'BMD': 1, 'BIF': 1555.435, 'LSL': 9.923256, 'GIP': 0.658028, 'MNT': 1436.5, 'AMD': 419.733748, 'LTL': 2.655583, 'SDG': 4.410148, 'QAR': 3.641282, 'XDR': 0.667, 'KRW': 1129.183294, 'SGD': 1.263167, 'JMD': 98.605434, 'GEL': 1.6419, 'SHP': 0.658028, 'AFN': 53.841566, 'SBD': 7.189682, 'KPW': 900, 'IRR': 12291.183333, 'CNY': 6.142649, 'KMF': 381.227515, 'BDT': 77.737726, 'XOF': 505.653503, 'GYD': 203.124999, 'MTL': 0.683602, 'NZD': 1.235322, 'FKP': 0.658028, 'LVL': 0.539434, 'TRY': 1.869915, 'HTG': 42.52545, 'SLL': 4322.78161, 'KGS': 48.188801, 'ANG': 1.78875, 'LRD': 74.541367, 'RWF': 648.591123, 'GTQ': 7.802498, 'RSD': 85.929837, 'ZAR': 9.928585, 'MOP': 7.991484, 'BHD': 0.377004, 'INR': 56.317613, 'JPY': 101.033178, 'CZK': 19.851161, 'TJS': 4.755467, 'MRO': 298.983625, 'PGK': 2.272828, 'BTC': 0.007664, 'ZMW': 5.335583, 'BTN': 56.223483, 'XAU': 0.000709}
json = urllib2.urlopen(url).read()

(true,false,null) = (True,False,None)
rates=eval(json)

#debug message to print the entire json that has been evuluated
if (debug == 1 ):
	print rates

check_h = 1
check_w = 1

# Initilazing the variables to have global scope
amt = None
rate = None
want = None
while(check_h == 1):
	have=raw_input("You have:")
	amt, rate = have.split(" ")
	rate = rate.upper()	
	if ( rate in availabe_rates ):
		check_h = 0
	else:
		print "Error in Input,"
		print "Example input You Have:1 USD"
		print "Trailing spaces result in invalid inputs"

while(check_w == 1):
	want=raw_input("You want:")
	want=want.upper()
	if ( want in availabe_rates ):
		check_w = 0
	else:
		print "Invalid Input"
		print "Example You want:INR"
		print "Trailing spaces result in invalid inputs"

amt=float(amt)
conv=rates['rates'][want]
ratec=rates['rates'][rate]

# A debug section to make sure that the data that is gotten is valid USD should be equal to 1
if (debug == 1):
	usd_str='USD'
	usd=rates['rates'][usd_str]
	print "usd =",usd;

#typecasting to float, don't know if its required
conv=float(conv)
ratec=float(ratec)

#The actual currency conversion is happening in the next two lines
res=amt/ratec
res= res * conv
print res

