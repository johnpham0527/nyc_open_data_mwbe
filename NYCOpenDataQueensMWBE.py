#!/usr/bin/env python

# make sure to install these packages before running:
# pip install sodapy
# pip install xlsxwriter

from sodapy import Socrata
#import xlsxwriter

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", "QoQet97KEDYpMW4x4Manaflkp")

# My (John Pham's) app token: QoQet97KEDYpMW4x4Manaflkp

# First 10000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ci93-uc8s", limit=10000)

QueensZipCodes =    [11001,11004,
                11101,11102,11103,11104,11105,11106,11109,11221,
                11354,11355,11356,11357,11358,11360,11361,11362,
                11363,11364,11365,11366,11367,11368,11369,11370,
                11372,11373,11374,11375,11377,11378,11379,11385,
                11411,11412,11413,11414,11415,11416,11417,11418,
                11419,11420,11421,11422,11423,11426,11427,11428,
                11429,11432,11433,11434,11435,11436,11691,11692,
                11693,11694]
QueensCertifiedMWBE = [] #this array will contain all city-certified Minority- or Women-Owned Business Enterprises (MWBE) located in a Queens ZIP code
QueensLargeCertifiedMWBE = [] #this array will store all certified Queens MWBEs with at least one large contract
QueensLargeCertifiedMWBEAsianOrHispanic = []

largeContractSize = 100000; #we are defining a large contract size as $100,000

#store into the array all certified Queens MWBEs into the QueensMWBE array
for business in results:
    for zipCode in QueensZipCodes:
        if business["zip"] == str(zipCode):
            QueensCertifiedMWBE.append(business) 

#filter business: find any 
for business in QueensCertifiedMWBE: 
    if "job_exp1_value_of_contract" in business: #check if the MWBE has at least one contract listed
        if float(business["job_exp1_value_of_contract"]) > largeContractSize: #check if the contract size is large enough
            QueensLargeCertifiedMWBE.append(business) #if the contract size is large enough, add it to the QueensLargeCertifiedMWBE array
        elif "job_exp2_value_of_contract" in business: #check if the MWBE has a second contract listed
            if float(business["job_exp2_value_of_contract"]) > largeContractSize: #check if the contract size is large enough
                QueensLargeCertifiedMWBE.append(business) #if the contract size is large enough, add it to the QueensLargeCertifiedMWBE array
            elif "job_exp3_value_of_contract" in business: #check if the MWBE has a second contract listed
                if float(business["job_exp3_value_of_contract"]) > largeContractSize: #check if the contract size is large enough
                    QueensLargeCertifiedMWBE.append(business) #if the contract size is large enough, add it to the QueensLargeCertifiedMWBE array
                elif "job_exp4_value_of_contract" in business: #check if the MWBE has a second contract listed
                    if float(business["job_exp4_value_of_contract"]) > largeContractSize: #check if the contract size is large enough
                        QueensLargeCertifiedMWBE.append(business) #if the contract size is large enough, add it to the QueensLargeCertifiedMWBE array

for business in QueensLargeCertifiedMWBE:
    if "ethnicity" in business:
        if business["ethnicity"] == "ASIAN" or business["ethnicity"] == "HISPANIC": #check to see if a business is owned by someone who identifies as Asian or Hispanic
            QueensLargeCertifiedMWBEAsianOrHispanic.append(business) #add the business to the QueensLargeCertifiedMWBEAsianOrHispanic array

#export the data to Excel
#workbook = xlsxwriter.Workbook('Queens_Large_Certified_MWBE_Asian_or_Hispanic.xlsx')
#worksheet = workbook.add_worksheet()
#for row, dataRecord in enumerate(QueensLargeCertifiedMWBEAsianOrHispanic): #iterate through each business in the array.
#    for col, dataRecordTuple in enumerate(dataRecord.items()):   #iterate through each column value
#        print (str(row) + "\t" + str(col) + "\t" + dataRecordTuple[1]) #output the value of the data record tuple. Each tuple contains a key ("zip") and a value ("11432").
#        outputString=dataRecordTuple[0] + " " + dataRecordTuple[1]
#        worksheet.write(row,col,outputString)
#
#workbook.close()

print(len(QueensLargeCertifiedMWBEAsianOrHispanic))

f = open("QueensCertifiedMWBEAsianOrHispanic.txt","w",encoding="utf-8")
try: 
    for numBusiness,business in enumerate(QueensLargeCertifiedMWBEAsianOrHispanic): #iterate through each business in the array.
        for dataRecordTuple in business.items():   #iterate through each column value
            outputString = dataRecordTuple[0] + "\t" + dataRecordTuple[1]
            print(outputString) #output the value of the data record tuple. Each tuple contains a key ("zip") and a value ("11432").
            f.write(outputString)
            f.write("\n")
        f.write("\n\n")
finally:
    f.close()