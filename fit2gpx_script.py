from fit2gpx import Converter

import os

# Path to the folder containing files
input_folder = '/home/bram/Documents/Strava data/export_26763577/processed/fit/problem'
output_folder = '/home/bram/Documents/Strava data/export_26763577/processed/fit/gpx'

file_type = '.fit'

conv = Converter()          # create standard converter object

# Loop through all the files in the folder
for filename in os.listdir(input_folder):

    # Check if the file has the specified extension
    if filename.endswith(file_type):
        print(f'Opening: {filename}')

        # Construct the full path to the file
        file_path = os.path.join(input_folder, filename)

        # Define the path for the copied file
        output_file_path = os.path.join(output_folder, filename[:-3] + 'gpx')

        gpx = conv.fit_to_gpx(f_in=file_path,
                              f_out=output_file_path)

        print(f'Copied: {filename} -> {os.path.basename(output_file_path)}')

print('All files copied successfully.')
