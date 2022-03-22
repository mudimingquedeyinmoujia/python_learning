import zipfile

z=zipfile.ZipFile('18_zipfile.zip')
for f in z.namelist():
    print(f)