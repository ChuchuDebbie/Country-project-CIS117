# CIS-117 Lab3
# Description: Wrtiting CSV files by region
# Group 3: Chujun Zhang, George Kuxin

import csv

def write_files(regions):
    try:
        for region in regions:
            filename = region + ".csv"

            with open(filename, mode = "w", newline = "") as file:
                csv_writer = csv.writer(file)

                csv_writer.writerow(["name", "region"])

                for country in regions[region]:
                    csv_writer.writerow(country)

            print(filename, "created succesfully")

    except PermissionError:
        print("Error: Permission denied.")

    except IOError:
        print("Error: An Input/Output error occurred.")

from lab3 import regions

if regions:
    write_files(regions)