import csv
import re
import os.path


class RegexHelper(object):
    def __init__(self, pattern):
        self.compiled_regex = re.compile(pattern)

    def match_string(self, string):
        return self.compiled_regex.match(string)


class Validate(object):
    def __init__(self, input_file):
        self.error_occured = bool(0)
        self.is_input_file_found = bool(0)
        try:
            pattern = '(GIR\s0AA)|^((([A-PR-UWYZ][0-9][0-9]?)|(([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9])|([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9])|x(WC[0-9][A-Z])|(([A-PR-UWYZ][0-9][A-HJKPSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))))\s[0-9][ABD-HJLNP-UW-Z]{2})'
            self.validator = RegexHelper(pattern=pattern)
            self.input_file = input_file
            self.is_input_file_found = os.path.isfile(self.input_file)
            if (self.is_input_file_found):
                self.passed_validation = {}
                self.failed_validation = {}
                with open(self.input_file, 'rb') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    next(csvfile, None)
                    for row in reader:
                        if self.validator.match_string(string=row[1]):
                            self.passed_validation[int(row[0])] = row[1]
                        else:
                            self.failed_validation[int(row[0])] = row[1]
            else:
                self.error_occured = bool(1)
                print('Input file not found')
        except IOError as ex:
            self.error_occured = bool(1)
            print "Initialise Validate CSV I/O error({0}): {1}".format(ex.errno, ex.strerror)
        except ValueError:
            self.error_occured = bool(1)
            print "Failed to parse CSV file"

    def write_csv(self, path, csv_type):
        if (not self.error_occured):
            if csv_type == "success":
                self.csv_type_list = self.passed_validation
                self.write_csv_file(path, data_to_export=self.csv_type_list)
            elif csv_type == "failed":
                self.csv_type_list = self.failed_validation
                self.write_csv_file(path, data_to_export=self.csv_type_list)
            else:
                print("CSV type not found")

    def write_csv_file(self, path, data_to_export):
        self.data_to_export = data_to_export
        if (not self.error_occured):
            print("Write CSV")
            try:
                with open(path, 'wb') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for key in sorted(self.data_to_export):
                        writer.writerow([key, self.data_to_export[key]])
            except IOError as ex:
                print "CSV write error - I/O error({0}): {1}".format(ex.errno, ex.strerror)
            print("Write CSV - Complete")
        else:
            if (not self.is_input_file_found):
                print('Input file not found - cannot write file')
            else:
                print('An error occured')
