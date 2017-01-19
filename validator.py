import csv
import re
import os.path


class Regex_helpers(object):
    def __init__(self, pattern):
        self.compiled_regex = re.compile(pattern, re.X)

    def match_string(self, string):
        return self.compiled_regex.match(string)


class Validator(object):
    passed_validation = {}
    failed_validation = {}
    is_input_file_found = False
    error_occurred = False

    def __init__(self, input_file):
        pattern = """(GIR\s0AA) |^
    (
        # A9 or A99 prefix
        ( ([A-PR-UWYZ][0-9][0-9]?) |
             # AA99 prefix with some excluded areas
            (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
             # AA9 prefix with some excluded areas
             ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
             # WC1A prefix
             (WC[0-9][A-Z]) |
             (
                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
             )
            )
          )
          # 9AA suffix
        \s[0-9][ABD-HJLNP-UW-Z]{2}
        )$"""
        self.validator = Regex_helpers(pattern=pattern)
        self.input_file = input_file

    def validate(self):

        self.error_occurred = False
        self.is_input_file_found = os.path.isfile(self.input_file)
        try:
            if self.is_input_file_found:

                with open(self.input_file, 'rb') as csv_file:
                    reader = csv.reader(csv_file, delimiter=',')
                    next(csv_file, None)
                    for row in reader:
                        if self.validator.match_string(string=row[1]):
                            self.passed_validation[int(row[0])] = row[1]
                        else:
                            self.failed_validation[int(row[0])] = row[1]
            else:
                self.error_occurred = True
                print('Input file not found')
        except IOError as ex:
            self.error_occurred = True
            print "Initialise Validate CSV I/O error({0}): {1}".format(ex.errno, ex.strerror)
        except ValueError:
            self.error_occurred = True
            print "Failed to parse CSV file"

    def write_csv(self, path, csv_type):
        if not self.error_occurred:
            if csv_type == "success":
                csv_type_list = self.passed_validation
                self._write_csv_file(path, data_to_export=csv_type_list)
            elif csv_type == "failed":
                csv_type_list = self.failed_validation
                self._write_csv_file(path, data_to_export=csv_type_list)
            else:
                print("CSV type not found")

    def _write_csv_file(self, path, data_to_export):
        if not self.error_occurred:
            print("Write CSV")
            try:
                with open(path, 'wb') as csv_file:
                    writer = csv.writer(csv_file, delimiter=',')
                    for key in sorted(data_to_export):
                        writer.writerow([key, data_to_export[key]])
            except IOError as ex:
                print "CSV write error - I/O error({0}): {1}".format(ex.errno, ex.strerror)
            print("Write CSV - Complete")
        else:
            if not self.is_input_file_found:
                print('Input file not found - cannot write file')
            else:
                print('An error occurred')
