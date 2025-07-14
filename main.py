# ZIP

from zipfile import ZipFile
import os

csv_files = [f for f in os.listdir() if f.endswith('.csv')]
with ZipFile('archive.zip', 'w') as myzip:
    for file in csv_files:
        myzip.write(file)
        os.remove(file)

# with ZipFile('archive.zip', 'r') as zip_obj:
#     zip_obj.extractall()