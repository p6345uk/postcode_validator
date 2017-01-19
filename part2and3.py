import time
from validator import Validator

if __name__ == '__main__':
    start = time.time()
    print("Part 2 - Bulk import - Begin")
    validator_part2 = Validator('/home/pslinux/Downloads/import_data.csv')
    validator_part2.validate()
    validator_part2.write_csv('/home/pslinux/Downloads/failed_validation.csv', 'failed')
    print("Part 2 - Bulk import - End")
    end = time.time()
    print(end - start)

    start = time.time()
    print("Part 3 - Performance engineering - Begin")
    validator_part3 = Validator('/home/pslinux/Downloads/import_data.csv')
    validator_part3.validate()
    validator_part3.write_csv('/home/pslinux/Downloads/failed_validation.csv', 'failed')
    validator_part3.write_csv('/home/pslinux/Downloads/succeeded_validation.csv', 'success')
    print("Part 3 - Performance engineering - End")
    end = time.time()
    print(end - start)
