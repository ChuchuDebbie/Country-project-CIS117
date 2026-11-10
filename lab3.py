# CIS-117 Lab3
# Description: This program reads a CSV file containing country names and their corresponding regions, groups the countries by region, and handles potential file errors.And writes one CSV file per region 
# Group 3: Chujun Zhang, George Kuxin
#Collaboration: Chujun works on the reading and grouping parts and George works on the writing part. We discussed the logic and structure of the program together.


import csv

regions={} 

#part 1: read the csv file and group 
try:
      with open('country_full.csv',mode='r',newline='') as file:
            csv_reader= csv.reader(file)
            
            header=next(csv_reader)
            print(header)
            
            name_index=header.index('name')
            region_index=header.index('region')
            
            for row in csv_reader:
                  country_name=row[name_index]
                  region=row[region_index]
                  if region=='':
                        region='Unknown'
                  if region not in regions:
                        regions[region]=[]
                  regions[region].append([country_name,region])
                  
except FileNotFoundError:
      print('country_full.csv not found')
except PermissionError:
      print('Permission denied')
except IOError:
      print('Input/output error')
      
#part 2:  write one csv file per region

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


if regions:
    write_files(regions)

      
      
