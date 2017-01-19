I have done the technical test in python version 2.7.13

Included are 3 files

part2and3.py - Script to run part 2 and 3 of the assesment

validator.py - Validator module

validator_unittests.py - Unit test for part one of the assesment

The Input and Output file paths are specified in the part2and3.py file these should be update to your local paths

Lines required to update paths below

Import_data.csv

validator_part2 = Validator('/home/pslinux/Downloads/import_data.csv')
validator_part3 = Validator('/home/pslinux/Downloads/import_data.csv')

failed_validation.csv

validator_part2.write_csv('/home/pslinux/Downloads/failed_validation.csv', 'failed')
validator_part3.write_csv('/home/pslinux/Downloads/failed_validation.csv', 'failed')

succeeded_validation.csv

validator_part3.write_csv('/home/pslinux/Downloads/succeeded_validation.csv', 'success')



Part 1.

With two small modifications to the Regex, the regex validates to the basic format of the UK postcode system.
The second part of the regex is missing ^ at the beginning and $ at the end.
This makes sure that the regex is matched to the begining of the string not a component of it, $ ensure that it matches to the end.

E.G

LI10 3QP

I10 3QP

Updated Regex Below

(GIR\s0AA)|^((([A-PR-UWYZ][0-9][0-9]?)|(([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9])|([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9])|x(WC[0-9][A-Z])|(([A-PR-UWYZ][0-9][A-HJKPSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))))\s[0-9][ABD-HJLNP-UW-Z]{2})$

A number of post codes in this file that pass the regex must not be currently valid as there are 2+ Million distinct postcodes which exceeds the number of postcodes in the PAF ("Royal mail UK Postcode Address File"),which is a current publish list of valid postcodes

Part 2 and 3.

How i made my scripts faster

I split the regex into the compile and match sequence so that the compiled regex is reused increasing the efficency of the regex

	compiled_regex = re.compile(pattern, re.X)
	compiled_regex.match(string)

I saved the result of processing the csv into a dictonary list as i found this more efficient than creating a class and adding it to a list or utilising tuples.

I measured the changes using the time module provided and measuring the overall time taken for each step to be completed i have left this in the part2and3.py script for review 

 
