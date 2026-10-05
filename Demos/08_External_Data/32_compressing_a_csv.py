# One way of zipping your csv...
import gzip
import shutil

# Tested in Microsoft Windows
with open('accounts2.csv', 'rb') as infile:
    with gzip.open('mynewaccounts2.gz', 'wb') as outfile:
        shutil.copyfileobj(infile, outfile)



# Read and decompress the .gz file
with gzip.open('mynewaccounts2.gz', 'rt', encoding='utf-8') as infile:
    contents = infile.read()

# Print the decompressed contents
print("Contents of compressed file:")
print(contents)