#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# copies an entire folder including its contents into a zip file with incrementing filename


import os, zipfile

# First, let's name the zip file
def nameZipfile(folder):
    # folder should have absolute path
    N = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(N) + '.zip'
        if not os.path.exists(zipFileName):
            break
        N += 1
    return zipFileName


def backupToZip(folder = '.'):
    folder = os.path.abspath(folder)
    zipFileName = nameZipfile(folder)
    print(f'Creating {zipFileName}...')
    backupzip = zipfile.ZipFile(zipFileName, 'w')

    for foldername, subfolders, files in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupzip.write(foldername) # Add current folder to the zip file
        for filename in files:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup zip files
            backupzip.write(os.path.join(foldername, filename))
    backupzip.close()
    print('Done.')



backupToZip()
