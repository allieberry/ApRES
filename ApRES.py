
import argparse
import glob
from apres import ApRESFile
import os


def convert_apres_files(input_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in input_dir
    for filename in os.listdir(input_dir):
        if filename.endswith('.DAT'):
            infile = os.path.join(input_dir, filename)
            outfile = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.nc")
            
            print(f"Converting {infile} to {outfile}...")

            try:
                with ApRESFile(infile) as f:
                    f.to_netcdf(outfile)
            except KeyError as e:
                 print(f"KeyError: {e} in file {infile}. Skipping this file.")
    print("Conversion completed.")

if __name__ == '__main__':
    input_dir = '/Users/allison.berry1/Desktop/ApRES_data/'
    output_dir = '/Users/allison.berry1/Desktop/ApRES_data/converted_netCDF/'
    convert_apres_files(input_dir, output_dir)
