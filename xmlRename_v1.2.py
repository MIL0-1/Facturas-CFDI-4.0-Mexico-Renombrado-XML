# Copyright 2023 Luis Emilio Sánchez Ramos
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

# Update v1.2 - Works well with minor issue (cannot convert lowecase to upper due to Windows restrictions)

import xml.etree.ElementTree as ET
import os, datetime, shutil
import pandas as pd

# Define the folder path (input) and *report* output path (output)
folder_path = r'C:\User\path'
output_path = r'C:\User\path'

# Create a dictionary to store the count of each UUID found in the XML files
UUID_count = {}

# Create a list to store relevant data for each file
file_data = []

# Get the list of files in the folder and sort them by creation time (oldest to latest, so newest files could be easily noticeable because of the counter)
files = sorted(os.listdir(folder_path), key=lambda f: os.path.getctime(os.path.join(folder_path, f)))
print('Sorting files by latest creation time')
# Iterate through all the sorted list of files in the folder
for filename in files:
    if filename.lower().endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join(folder_path, filename))
        print(f'Parsing {filename}')

        # Get the root element
        root = tree.getroot()

        # Find the element with the 'tfd:TimbreFiscalDigital' tag
        tfd_element = root.find('.//{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital')
        if tfd_element is not None:
            # Get the value of the 'UUID' attribute
            UUID = tfd_element.get('UUID')
            print(f'Found UUID {UUID} in {filename}')

            # Check if the UUID is already in the filename
            if UUID.upper() not in filename.upper():
                # RENAME the file with the UUID in uppercase (only variables)
                new_filename = UUID.upper() + '.xml'
                # Check if the file with the new name already exists
                if os.path.exists(os.path.join(folder_path, new_filename)):
                    # If True, add a counter to the end of the file name until it finds a file name that does not exist in the folder
                    counter = 2
                    while os.path.exists(os.path.join(folder_path, f'{UUID.upper()}_{counter}.xml')):
                        counter += 1
                    new_filename = f'{UUID.upper()}_{counter}.xml'
                try:
                    shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                    print(f'Renaming {filename} to {new_filename}')
                    file_data.append({'filename': filename, 'new_filename': new_filename, 'UUID': UUID})
                except FileNotFoundError:
                    print(f'Error: File not found: {filename}')
                    file_data.append({'filename': filename, 'error': 'File not found'})

                # Check if the UUID already exists in the dictionary
                if UUID in UUID_count:
                    # Increment the count
                    UUID_count[UUID] += 1
                else:
                    # Add the UUID to the dictionary with a count of 1
                    UUID_count[UUID] = 1
            else:
                print(f'{UUID.upper()} already in filename: {filename}')
                file_data.append({'filename': filename, 'error': 'UUID already in filename'})
                new_filename = filename.upper() + '.xml'
        else:
            print(f'UUID not found for file: {filename}')
            file_data.append({'filename': filename, 'error': 'UUID not found'})

    else:
        print(f'Skipping non-XML file: {filename}')
        file_data.append({'filename': filename, 'error': 'Skipping non-XML file'})

# Create the report file name with the current date
date_str = datetime.datetime.now().strftime('%Y%m%d')
report_filename = f'{date_str}_XML renaming report.xlsx'

# Check if the report file already exists
counter = 2
while os.path.exists(os.path.join(output_path, report_filename)):
    report_filename = f'{date_str}_XML renaming report_{counter}.xlsx'
    counter += 1

# Export the dictionary to Excel
report_path = os.path.join(output_path, report_filename)
with pd.ExcelWriter(report_path) as writer:
    df = pd.DataFrame(list(UUID_count.items()), columns=['UUID', 'Count'])
    df.to_excel(writer, sheet_name='UUID Counts', index=False)
    print(f'Exporting to Excel workbook: {report_filename}')

    # Add the file data to a new sheet in the Excel file
    df = pd.DataFrame(file_data)
    df.to_excel(writer, sheet_name='File Data', index=False)
    print(f'Exporting file data to Excel workbook: {report_filename}')

print('Report finished')
