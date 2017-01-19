import ValidatePostcodeCSV
import time

start = time.time()
print("Part 2 - Bulk import - Begin")
validator_part2 = ValidatePostcodeCSV.Validate(input_file='/home/pslinux/Downloads/import_data.csv')
validator_part2.write_csv(path='/home/pslinux/Downloads/failed_validation.csv', csv_type='failed')
print("Part 2 - Bulk import - End")
end = time.time()
print(end - start)

start = time.time()
print("Part 3 - Performance engineering - Begin")
validator = ValidatePostcodeCSV.Validate(input_file='/home/pslinux/Downloads/import_data.csv')
validator.write_csv(path='/home/pslinux/Downloads/failed_validation.csv', csv_type='failed')
validator.write_csv(path='/home/pslinux/Downloads/succeeded_validation.csv', csv_type='success')
print("Part 3 - Performance engineering - End")
end = time.time()
print(end - start)
