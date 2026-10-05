import tarfile
import os

# Folders for tar process (create it, copy sample files into the first one)
source_dir = "./tar_example_source_data"
destination_dir = "./copy_of_tar_example_source_data"

# Tar filename
newarchive = "newarchive.tar"

# Opens for gzip compressed writing; will auto close
with tarfile.open(newarchive, "w:gz") as tar:
    # Add all files for this folder
    tar.add(source_dir, arcname=os.path.basename(source_dir))

# Open existing tar file for reading; will auto close
with tarfile.open(newarchive, "r") as tar:
    # Iterate through the filenames (including directories)
    for filename in tar.getnames():
        print(filename)

    # Linux "ls"-style listing
    tar.list()

    # Extract everything to a new folder (optional param - files to extract)
    tar.extractall(destination_dir)
